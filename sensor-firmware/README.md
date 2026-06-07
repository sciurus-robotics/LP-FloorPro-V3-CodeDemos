# Sensor Firmware

Firmware binaries for the SR LP FloorPro V3 line sensor. Files are named
`sensor-firmware_[ISO8601-date].bin`; the most recent build is the recommended
one.

## Entering boot mode

The sensor exposes a USB DFU bootloader that must be active for flashing.
There are two ways to bring the sensor into boot mode:

- **Cold start**: with the sensor unpowered, hold the `BOOT` button and then
  plug in the USB cable (keep `BOOT` held for a moment after power is
  applied, then release).
- **Warm reset**: with the sensor already powered, hold the `BOOT` button,
  briefly press and release `RST` while still holding `BOOT`, then release
  `BOOT`.

In either case the sensor should now enumerate as a DFU-capable USB device.

## Flashing with `dfu-util`

1. Install `dfu-util` (e.g. `brew install dfu-util` on macOS, or
   `apt install dfu-util` on Debian/Ubuntu).

2. Verify the sensor is detected in DFU mode:

   ```sh
   dfu-util -l
   ```

   You should see an entry with an `alt=0` interface for the internal flash
   (typically `@Internal Flash  /0x08000000/...`).

3. Flash the firmware:

   ```sh
   dfu-util -a 0 -s 0x08000000:leave -D sensor-firmware_2026-06-06.bin
   ```

   The `:leave` suffix instructs the bootloader to jump to the application
   after a successful download. Replace the filename with the build you want
   to flash.

4. Unplug and reconnect (or reset) the sensor. The new firmware is now
   running.

### Troubleshooting

- If `dfu-util -l` shows nothing, re-enter DFU mode (hold the button while
  connecting USB) and check that the cable supports data, not just power.
- On Linux you may need udev rules or `sudo` for USB access.
