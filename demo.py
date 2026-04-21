from pybricks.tools import wait, run_task, multitask
from pybricks.hubs import PrimeHub, InventorHub
from pybricks.parameters import Port, Button
from floor_pro_v3 import FloorProV3

hub = InventorHub()

hub.display.number(100)

floor_pro = FloorProV3(Port.A)


async def demo_dark_centroid():
    print("Method:      dark_centroid()")
    print("Description: Centroid position of dark regions (-127 to 127), displayed as a number.")
    while True:
        value = await floor_pro.dark_centroid()
        hub.display.number(value)
        await wait(10)


async def demo_bright_centroid():
    print("Method:      bright_centroid()")
    print("Description: Centroid position of bright regions (-127 to 127), displayed as a number.")
    while True:
        value = await floor_pro.bright_centroid()
        hub.display.number(value)
        await wait(10)


async def demo_brightness():
    print("Method:      brightness()")
    print("Description: Overall brightness of the sensor (-127 to 127), displayed as a number.")
    while True:
        value = await floor_pro.brightness()
        hub.display.number(value)
        await wait(10)


async def demo_line_sensors_analog():
    print("Method:      line_sensors_analog()")
    print("Description: Analog reflectance of each of the 15 IR line sensors, shown as a grayscale pattern on the 5x5 display.")
    while True:
        await wait(10)
        signed_values = await floor_pro.line_sensors_analog()
        unsigned_values = tuple(b + 127 for b in signed_values)

        # Display on 5x5 grid
        for row in range(5):
            for col in range(5):
                index = row * 5 + col
                if index < 15:
                    # Convert [0, 255] to [0, 100]
                    brightness = unsigned_values[index] * 100 // 255
                    hub.display.pixel(row, col, brightness)
                else:
                    # Turn off remaining LEDs
                    hub.display.pixel(row, col, 0)


async def demo_line_sensors_binary():
    print("Method:      line_sensors_binary()")
    print("Description: On/off state of each of the 15 IR line sensors, shown as a binary pattern on the 5x5 display.")
    while True:
        await wait(10)
        data = await floor_pro.line_sensors_binary()

        # Display on 5x5 grid
        for row in range(5):
            for col in range(5):
                index = row * 5 + col
                brightness = 100 if index < 15 and data[index] else 0
                hub.display.pixel(row, col, brightness)


async def demo():
    print("Device info:", floor_pro.info())
    print("Device ID:", (await floor_pro.device_id()))

    print("Dark centroid:", await floor_pro.dark_centroid())
    print("Bright centroid:", await floor_pro.bright_centroid())
    print("Brightness:", await floor_pro.brightness())
    print("Raw sensor byte:", await floor_pro.line_sensors_analog())

    await wait(1000)

    demos = [
        demo_dark_centroid,
        demo_bright_centroid,
        demo_brightness,
        demo_line_sensors_binary,
        demo_line_sensors_analog,
    ]

    index = 0
    direction = [1]  # +1 = right/next, -1 = left/previous

    async def wait_for_button():
        # Wait for button release first to avoid immediately re-triggering
        while hub.buttons.pressed():
            await wait(50)
        while True:
            pressed = hub.buttons.pressed()
            if Button.RIGHT in pressed:
                direction[0] = 1
                return
            if Button.LEFT in pressed:
                direction[0] = -1
                return
            await wait(50)

    while True:
        print(f"\n--- Demo {index + 1}/{len(demos)} ---")
        hub.display.number(index + 1)
        await wait(500)
        await multitask(demos[index](), wait_for_button(), race=True)
        index = (index + direction[0]) % len(demos)


run_task(demo())
