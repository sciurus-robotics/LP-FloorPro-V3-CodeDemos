# SR LP FloorPro V3 — Code Demos

PyBricks driver and demos for the SR LP FloorPro V3 line sensor.
The sensor provides 15 IR reflectance elements and reports centroid position, overall brightness, and per-sensor readings.

## Pybricks Compatibility 

**The sensor is known to work with the latest stable version 3.6.1 of Pybricks.** When you turn off the hub, we observed that the sensor can remain powered if the hub is connected and charging. That is a shortcoming of the hardware and could be fixed in the firmare but that seems not to be the case in 3.6.x.  

In the development version of Pybricks 4.x there is an issue with occasional disconnects. This seems not to be limited to our device and we are trying to resolve this issue with the Pybricks developers, see https://github.com/pybricks/support/issues/2698. If you want to use a beta of version 4 consider the files in the folder hub-firmware of this repository. It contains a premilary patch that seems to fix or at least significantly mitigate the problem.


## Files

- `floor_pro_v3.py` — `FloorProV3` driver class (subclasses `PUPDevice`)
- `demo.py` — Interactive demos, cycle through with the left/right hub buttons
- `calibration.py` — Calibrate the sensor via software control (you can also calibrate via the physical button on the sensor)

## Requirements

- [PyBricks](https://pybricks.com) firmware on a compatible LEGO hub
- [`pybricksdev`](https://github.com/pybricks/pybricksdev) for uploading/running scripts
