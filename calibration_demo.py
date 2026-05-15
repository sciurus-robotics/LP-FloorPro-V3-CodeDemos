from pybricks.tools import wait, run_task, multitask
from pybricks.hubs import PrimeHub, InventorHub
from pybricks.parameters import Port, Button
from floor_pro_v3 import FloorProV3

hub = InventorHub()
floor_pro = FloorProV3(Port.A)


async def calibration_demo():
    print("Starting calibration demo...")
    print("Press RIGHT button to start calibration.")
    while Button.RIGHT not in hub.buttons.pressed():
        await wait(10)
    while Button.RIGHT in hub.buttons.pressed():
        await wait(10)
    await floor_pro.calibration_start()

    print("Calibrating, move the sensor over the surface catching your bright and dark areas of interest. Press RIGHT button again when done.")

    while Button.RIGHT not in hub.buttons.pressed():
        await wait(10)
    while Button.RIGHT in hub.buttons.pressed():
        await wait(10)
    await floor_pro.calibration_stop()
    print("Calibration complete. Sensor data will now reflect the new calibration.")

run_task(calibration_demo())
