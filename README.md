# SR LP FloorPro V3 — Code Demos

PyBricks driver and demos for the SR LP FloorPro V3 line sensor.
The sensor provides 15 IR reflectance elements and reports centroid position, overall brightness, and per-sensor readings.

## Pybricks Compatibility

**The sensor is known to work with the latest stable version 3.6.1 of Pybricks.** When you turn off the hub, we observed that the sensor can remain powered if the hub is connected and charging. That is a shortcoming of the hardware and could be fixed in the firmware, but that seems not to be the case in 3.6.x.

In the development version of Pybricks 4.x there is an issue with occasional disconnects. The issue will be resolved with versions 4.0.0-b11 and later, see https://github.com/pybricks/support/issues/2698. See also the folder `hub-firmware` of this repository for a patched firmware.

## Sensor Firmware

The folder `sensor-firmware` contains the latest firmware binary for the FloorPro V3 sensor itself, along with instructions for flashing it via `dfu-util`. See [`sensor-firmware/README.md`](sensor-firmware/README.md).


## Files

- `floor_pro_v3.py` — `FloorProV3` driver class (subclasses `PUPDevice`)
- `demo.py` — Interactive demos, cycle through with the left/right hub buttons
- `calibration_demo.py` — Calibrate the sensor via software control (you can also calibrate via the physical button on the sensor)
- `qc.py` — Check the range/resolution of the sensor with respect to calibrated values. This can be used to validate operation of the current setup,
    in particular with respect to mounting distance and surface properties. It can also be used for quality control with a standardized setup.


## Requirements

- [PyBricks](https://pybricks.com) firmware on a compatible LEGO hub
- [`pybricksdev`](https://github.com/pybricks/pybricksdev) for uploading/running scripts
