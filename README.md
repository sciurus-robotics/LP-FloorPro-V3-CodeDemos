# SR LP FloorPro V3 — Code Demos

PyBricks driver and demos for the SR LP FloorPro V3 line sensor.
The sensor provides 15 IR reflectance elements and reports centroid position, overall brightness, and per-sensor readings.

## Files

- `floor_pro_v3.py` — `FloorProV3` driver class (subclasses `PUPDevice`)
- `demo.py` — Interactive demos, cycle through with the left/right hub buttons
- `calibration.py` — Calibrate the sensor via software control (you can also calibrate via the physical button on the sensor)

## Requirements

- [PyBricks](https://pybricks.com) firmware on a compatible LEGO hub
- [`pybricksdev`](https://github.com/pybricks/pybricksdev) for uploading/running scripts
