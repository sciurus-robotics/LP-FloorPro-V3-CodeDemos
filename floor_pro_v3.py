from pybricks.tools import wait
from pybricks.iodevices import PUPDevice


class FloorProV3(PUPDevice):

    def __init__(self, port):
        super().__init__(port)
        self.current_mode = 0
        self.dev_info = self.info()

    # almost concurrent wite (and read?) requests can throw OSErrors in the
    # pupdevice; retry a few times before giving up.
    async def safe_write(self, mode, data):
        for _ in range(10):
            try:
                await self.write(mode, data)
                return
            except OSError:
                await wait(10)
        raise OSError(f"Failed to write to mode {mode} after 10 attempts")

    async def safe_read(self, mode):
        for _ in range(10):
            try:
                data = await self.read(mode)
                self.current_mode = mode
                return data
            except OSError:
                await wait(10)
        raise OSError(f"Failed to read from mode {mode} after 10 attempts")

    async def send_cmd(self, msg: str):
        data = [ord(c) for c in msg]
        len_data = self.dev_info['modes'][self.current_mode][1]
        if len(data) > len_data:
            raise ValueError(
                f"Message too long for current mode {self.current_mode}. Max length is {len_data}.")
        padded = data + [0x00] * (len_data - len(data))
        await self.safe_write(self.current_mode, padded)

    # main sensor data methods ###################################################

    async def dark_centroid(self):
        """
        Returns the centroid position of detected dark regions as an 8-bit signed integer (-127 to 127) from mode 0.

        This value represents the 'center of mass' of the detected dark regions,
        indicating where the dark area is located relative to the sensor's center.

        Returns:
            int: The centroid position, where negative values indicate left of center,
                 positive values indicate right of center, and zero is centered.
        """
        data = await self.safe_read(0)
        return data[1]

    async def bright_centroid(self):
        """ Returns the centroid position of detected bright regions as an 8-bit signed integer (-127 to 127) from mode 0. """
        data = await self.safe_read(0)
        return data[2]

    async def brightness(self):
        """ Returns the overall brightness as an 8-bit signed integer (-127 to 127) from mode 0. """
        data = await self.safe_read(0)
        return data[3]

    async def line_sensors_binary(self):
        """ Returns a tuple of 15 booleans indicating whether each IR sensor is above the reflectance threshold, from mode 0. """
        data = await self.safe_read(0)
        sens_0_7 = data[4]
        sens_8_14 = data[5]
        return tuple(
            bool((sens_0_7 >> i) & 1) if i < 8 else bool(
                (sens_8_14 >> (i - 8)) & 1)
            for i in range(15)
        )

    async def all_sensor_data(self):
        """ Returns a tuple of all basic sensor data: (dark_centroid, bright_centroid, brightness, raw_sensor_byte, line_sensors_binary) from mode 0. """
        data = await self.safe_read(0)
        sens_0_7 = data[4]
        sens_8_14 = data[5]
        return (data[1], data[2], data[3], data[4], tuple(
            bool((sens_0_7 >> i) & 1) if i < 8 else bool(
                (sens_8_14 >> (i - 8)) & 1)
            for i in range(15)
        ))

    async def line_sensors_analog(self):
        """ Returns a tuple of the reflectance values of all 15 IR line sensors as 8-bit signed integers (-127 to 127) from mode 1. """
        data = await self.safe_read(1)
        return tuple(data[i + 1] for i in range(15))

    ### setter and auxiliary methods ###################################################

    async def device_id(self):
        """ Returns the device identification string from mode 2. """
        data = await self.safe_read(2)
        return ''.join(chr(b) for b in data if b != 0)

    async def calibration_start(self):
        """ Start the sensor calibration process. """
        await self.send_cmd("CALIBSTART")

    async def calibration_stop(self):
        """ Stop the sensor calibration process and persist the calibration data to non-volatile memory. """
        await self.send_cmd("CALIBSTOP")

    async def set_display_brightness(self, brightness: int):
        """ Set the display brightness. Brightness must be an integer between 0 and 100.

        The display brightneess will be persistently stored in the sensor's non-volatile memory, so it will remain at the set level even after power cycles.
        """
        if brightness < 0 or brightness > 100 or not isinstance(brightness, int):
            raise ValueError("Brightness must be an integer between 0 and 100")
        await self.send_cmd(f"DISP={brightness}")

    async def set_rate(self, rate):
        """ Set the sensor sampling rate (target frequency). Accepted values: 'SYNC', '100', '200', 'MAX', 100, or 200. 

        Use with caution. High values could potentially cause heigher loads on the hub. 

        The rate setting will not be persistently stored, so it will reset to the default value after power cycles.
        """
        if rate not in ("SYNC", "100", "200", "MAX", 100, 200):
            raise ValueError(
                "Rate must be one of 'SYNC', '100', '200', 'MAX', 100, or 200")
        await self.send_cmd(f"RATE={rate}")
