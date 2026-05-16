# SR LP FloorPro V3 — Code Demos

PyBricks driver and demos for the SR LP FloorPro V3 line sensor.
The sensor provides 15 IR reflectance elements and reports centroid position, overall brightness, and per-sensor readings.

**The sensor is known to work with the latest stable version 3.6.1 of Pybricks.** We
are testing it occasionally with the **development version of Pybricks
4.0.0 and we belive that we have identified an issue**:
https://github.com/pybricks/support/issues/2698.



## Files

- `floor_pro_v3.py` — `FloorProV3` driver class (subclasses `PUPDevice`)
- `demo.py` — Interactive demos, cycle through with the left/right hub buttons
- `calibration.py` — Calibrate the sensor via software control (you can also calibrate via the physical button on the sensor)

## Requirements

- [PyBricks](https://pybricks.com) firmware on a compatible LEGO hub
- [`pybricksdev`](https://github.com/pybricks/pybricksdev) for uploading/running scripts
