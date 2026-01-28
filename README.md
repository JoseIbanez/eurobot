# Eurobot 2026 Robotics Platform

This repository supports our Raspberry Pi-based robot for Eurobot competition. It contains Python scripts and hardware setup instructions for reliable motor control, traffic light signaling, LCD output, and gamepad operation.

---
## Hardware Requirements

- Raspberry Pi 3+ (with I2C/SPI enabled)
- PCA9685 I2C motor controller (address 0x40)
- DC motors and drivers
- LEDs / NeoPixel rings (for traffic lights)
- LCD display (compatible with `rplcd`)
- Gamepad controller (usually `/dev/input/event2`)
- Jumper wires, breadboard, power supply

---
## Environment Setup

### Install Python & UV
- Python 3.11+ required
- UV is the package manager ([docs](https://docs.astral.sh/uv/getting-started/installation/#installation-methods))

#### Install UV (Shell or Pip)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
# OR
pip install uv
```

### Clone and Initialize Project
```bash
git clone https://github.com/JoseIbanez/eurobot.git
cd eurobot
uv venv
source .venv/bin/activate
uv sync  # install all requirements from pyproject.toml
```

#### For New Python Packages
```bash
uv add adafruit-circuitpython-servokit rpi-gpio
```

---
## Hardware Connection & Identification

- Connect PCA9685 via I2C (typically pins SCL+SDA)
- To confirm hardware addresses:

```bash
sudo apt-get install i2c-tools
pi@rp3:~ $ i2cdetect -y 1
# Should show lines like:
# 40: 40 -- -- ...  (PCA9685 at 0x40)
# 70: 70 -- -- ...  (Alternative addresses)
```

- Reference LCD setup: [rplcd getting started](https://rplcd.readthedocs.io/en/stable/getting_started.html)

---
## Example Usage

Run demos and tests (one at a time):
```bash
python motor-main.py      # Test motor control
python servo-main.py      # Test servo control
python semaforo-main.py   # Test traffic lights
python lcd-main.py        # Test LCD display
python test_01.py         # Test script 1
python test_02.py         # Test script 2
python test_03.py         # Test script 3
```

#### Expected Output
- motors/spin, LEDs change color, LCD displays text, gamepad prints events

---
## Troubleshooting

- **I2C device not found?** Make sure SCL/SDA connected, I2C enabled in `raspi-config`, hardware powered
- **Permission error on `/dev/input/event2`?** Use `sudo` or adjust group membership
- **No output from motor/main scripts?** Double-check wiring and use print/debug statements
- **LCD doesn’t display?** Verify address and contrast settings; see [rplcd docs](https://rplcd.readthedocs.io/en/stable/getting_started.html)

---
## Contributing

Pull requests are welcome! Please follow code style rules in AGENTS.md.

---
## License

MIT License

---
## References & Useful Links

- [Eurobot Official Site](https://www.eurobot.org/)
- [UV Python Package Manager](https://astral.sh/uv/)
- [Adafruit CircuitPython PCA9685 Docs](https://circuitpython.readthedocs.io/en/latest/shared-bindings/adafruit_pca9685/index.html)
- [RPi LCD Python Docs](https://rplcd.readthedocs.io/en/stable/getting_started.html)

---
