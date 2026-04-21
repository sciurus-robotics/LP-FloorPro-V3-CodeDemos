from pybricks.tools import wait, run_task, multitask
from pybricks.hubs import PrimeHub, InventorHub
from pybricks.parameters import Port
from floor_pro_v3 import FloorProV3

hub = InventorHub()

floor_pro = FloorProV3(Port.A)

RAW = 0
MIN = 1
MAX = 2


async def switch_qc_value(val):
    for attempt in range(10):
        try:
            await floor_pro.send_cmd(f"QC={val}")
            return
        except OSError:
            if attempt == 9:
                raise
            await wait(10)


async def qc():

    print("Device DATA")

    print("Device info:", floor_pro.info())
    print("Device ID:", (await floor_pro.device_id()))

    # switch to mode3
    print(await floor_pro.safe_read(3))

    await switch_qc_value(MIN)
    mins = (await floor_pro.safe_read(3))[1:]
    print("mins readings:", mins)

    await switch_qc_value(MAX)
    maxs = (await floor_pro.safe_read(3))[1:]
    print("maxs readings:", maxs)

    ranges = tuple(maxs[i] - mins[i] for i in range(15))
    print("ranges readings:", ranges)

    return


run_task(qc())
