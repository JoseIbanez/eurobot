# AGENTS.md - Agent Guidelines for Eurobot Project

This file contains comprehensive guidelines for agentic coding agents working on the Eurobot Raspberry Pi robotics project.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Environment Setup](#environment-setup)
- [Build/Lint/Test Commands](#buildlinttest-commands)
- [Code Style Guidelines](#code-style-guidelines)
- [Hardware Configuration](#hardware-configuration)
- [Development Workflow](#development-workflow)
- [Safety Guidelines](#safety-guidelines)
- [Testing Approach](#testing-approach)
- [Common Patterns](#common-patterns)
- [Troubleshooting](#troubleshooting)
- [Quick Reference](#quick-reference)

## Project Overview

- **Type**: Raspberry Pi robotics project for Eurobot competition
- **Language**: Python 3.11+
- **Package Manager**: UV (modern Python package manager)
- **Target Platform**: Raspberry Pi 3+ with hardware peripherals
- **Competition**: Eurobot - European robotics competition

### Key Technologies

| Technology | Purpose | Version |
|------------|---------|---------|
| Python | Main language | 3.11+ |
| UV | Package manager | Latest |
| Adafruit CircuitPython | Hardware libraries | Various |
| evdev | Gamepad input | 1.9.2+ |
| RPLCD | LCD display | 1.4.0+ |

## Project Structure

```
eurobot/
├── .venv/                      # Virtual environment (created by UV)
├── gamepad-raspberry/          # Gamepad integration code
├── mylib_gamepad.py           # Gamepad library
├── mylib_ledring.py           # LED ring control library
├── mylib_semaforo.py          # Traffic light (semaforo) library
├── motor-main.py              # Motor control demo
├── motor2-main.py             # Alternative motor demo
├── servo-main.py              # Servo control demo
├── semaforo-main.py           # Traffic light demo
├── lcd-main.py                # LCD display demo
├── led-ring.py                # LED ring basic demo
├── led-ring-kb2.py            # LED ring keyboard control v2
├── led-ring-kp.py             # LED ring keypad control
├── test_01.py                 # Test script 1
├── test_02.py                 # Test script 2
├── test_03.py                 # Test script 3
├── pyproject.toml             # Project dependencies
├── uv.lock                    # Dependency lock file
├── README.md                  # Project documentation
├── AGENTS.md                  # This file
└── LICENSE                    # License file
```

### File Naming Conventions

- **Library files**: `mylib_*.py` - Reusable hardware abstractions
- **Main scripts**: `*-main.py` - Component demonstration scripts
- **Test scripts**: `test_*.py` - Simple hardware validation tests
- **LED scripts**: `led-ring*.py` - LED control variations

## Environment Setup

> [!IMPORTANT]
> Always use UV for package management. Do not use pip directly unless absolutely necessary.

```bash
# Create and activate virtual environment
uv venv
source .venv/bin/activate

# Install dependencies
uv sync

# Add new packages
uv add <package-name>

# Add development dependencies
uv add --dev <package-name>

# Update all dependencies
uv sync --upgrade
```

### First-Time Setup on Raspberry Pi

```bash
# 1. Clone the repository
git clone <repository-url>
cd eurobot

# 2. Install UV if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# 3. Create virtual environment and install dependencies
uv venv
source .venv/bin/activate
uv sync

# 4. Enable I2C and SPI interfaces
sudo raspi-config
# Navigate to: Interface Options -> I2C -> Enable
# Navigate to: Interface Options -> SPI -> Enable

# 5. Verify I2C devices
i2cdetect -y 1

# 6. Test basic functionality
python test_01.py
```

## Build/Lint/Test Commands

### Environment Management

```bash
# Create virtual environment
uv venv

# Install dependencies from pyproject.toml
uv sync

# Activate environment
source .venv/bin/activate

# Deactivate environment
deactivate
```

### Running Scripts

```bash
# Component demos
python motor-main.py       # Test motor control
python motor2-main.py      # Alternative motor control
python servo-main.py       # Test servo control
python semaforo-main.py    # Test traffic light system
python lcd-main.py         # Test LCD display
python led-ring.py         # Basic LED ring
python led-ring-kb2.py     # LED ring with keyboard control
python led-ring-kp.py      # LED ring with keypad control

# Test scripts
python test_01.py          # Run test script 1
python test_02.py          # Run test script 2
python test_03.py          # Run test script 3
```

### Testing

> [!NOTE]
> This project uses simple test scripts without a formal testing framework. Tests are designed for hardware validation.

```bash
# Run individual test scripts
python test_01.py
python test_02.py  
python test_03.py

# Run all tests sequentially
for test in test_*.py; do python "$test"; done
```

### Hardware Validation

```bash
# Check I2C devices (should show PCA9685 at 0x40)
i2cdetect -y 1

# Check SPI devices
ls -l /dev/spidev*

# Check gamepad connection
ls -l /dev/input/event*

# Monitor gamepad events
evtest /dev/input/event2
```

## Code Style Guidelines

### Import Style

> [!TIP]
> Organize imports in three groups: standard library, third-party, and local imports.

```python
# Standard library
import time
import sys
from typing import Optional, List

# Third-party hardware libraries
import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import motor
import evdev

# Local imports
from mylib_semaforo import set_semaforo, set_motor
from mylib_gamepad import Gamepad
```

### Formatting Conventions

| Convention | Rule | Example |
|------------|------|---------|
| Indentation | 4 spaces (no tabs) | `    motor1.throttle = 0.5` |
| Line Length | Maximum 100 characters | Break long lines logically |
| Blank Lines | 2 between functions, 1 within | See examples below |
| Trailing Whitespace | Avoid | Use editor auto-trim |
| String Quotes | Prefer double quotes | `"hello"` over `'hello'` |

### Naming Conventions

```python
# Variables: snake_case
motor1 = motor.DCMotor(pca.channels[0], pca.channels[1])
base_address = 0x40
throttle_value = 0.5

# Functions: snake_case
def set_semaforo(pos: int, color: str) -> None:
    pass

def get_events() -> list:
    pass

# Classes: PascalCase
class Gamepad:
    pass

class MotorController:
    pass

# Constants: UPPER_SNAKE_CASE
MAX_THROTTLE = 1.0
MIN_THROTTLE = -1.0
I2C_ADDRESS = 0x40
DEFAULT_FREQUENCY = 1000

# Hardware references: Descriptive names
pca = PCA9685(i2c, address=64)
motor_left = motor.DCMotor(pca.channels[0], pca.channels[1])
motor_right = motor.DCMotor(pca.channels[2], pca.channels[3])
```

### Type Hints

Use type hints for function parameters and return values, especially for hardware interface functions.

```python
from typing import Optional, List, Tuple

def set_semaforo(pos: int, color: str) -> None:
    """Set traffic light color at specific position."""
    pass

def get_events(self) -> List[evdev.InputEvent]:
    """Get list of gamepad events."""
    pass

def read_sensor(timeout: Optional[float] = None) -> Tuple[bool, float]:
    """Read sensor with optional timeout."""
    pass

def initialize_motor(channel: int, decay_mode: int = motor.SLOW_DECAY) -> motor.DCMotor:
    """Initialize motor with specified channel and decay mode."""
    pass
```

### Error Handling Patterns

> [!WARNING]
> Always handle hardware communication errors gracefully. Hardware can disconnect or fail.

```python
# Pattern 1: Hardware initialization with error handling
try:
    self.device = evdev.InputDevice('/dev/input/event2')
    print(f"Gamepad initialized: {self.device.name}")
except FileNotFoundError:
    print("Error: Gamepad not found at /dev/input/event2")
    print("Available devices:")
    for device in evdev.list_devices():
        print(f"  {device}")
    raise
except Exception as e:
    print(f"Error initializing gamepad: {e}")
    raise

# Pattern 2: I2C communication with retry
def read_i2c_with_retry(address: int, retries: int = 3) -> Optional[bytes]:
    """Read from I2C device with retry logic."""
    for attempt in range(retries):
        try:
            return i2c.readfrom(address, 1)
        except OSError as e:
            if attempt == retries - 1:
                print(f"I2C read failed after {retries} attempts: {e}")
                return None
            time.sleep(0.1)
    return None

# Pattern 3: Graceful shutdown on KeyboardInterrupt
try:
    while True:
        # Main loop
        process_gamepad_input()
        time.sleep(0.01)
except KeyboardInterrupt:
    print("\nShutting down gracefully...")
finally:
    # Cleanup
    motor1.throttle = 0.0
    motor2.throttle = 0.0
    set_semaforo(1, "red")
    print("Cleanup complete")
```

### Documentation Standards

```python
def set_motor(pos: int, throttle: int) -> None:
    """Set motor throttle for specific motor position.
    
    Args:
        pos: Motor position (1 or 2)
        throttle: Throttle value (-100 to 100)
        
    Raises:
        ValueError: If pos is not 1 or 2
        ValueError: If throttle is outside valid range
        
    Example:
        >>> set_motor(1, 50)  # Motor 1 at 50% forward
        >>> set_motor(2, -30)  # Motor 2 at 30% reverse
    """
    if pos not in (1, 2):
        raise ValueError(f"Invalid motor position: {pos}")
    if not -100 <= throttle <= 100:
        raise ValueError(f"Throttle must be between -100 and 100, got {throttle}")
    
    # Implementation here
    pass


class MotorController:
    """Controller for DC motors using PCA9685.
    
    This class provides a high-level interface for controlling DC motors
    through the PCA9685 PWM controller. It handles throttle mapping,
    decay modes, and safety features.
    
    Attributes:
        pca: PCA9685 instance for PWM control
        motors: Dictionary of motor instances
        
    Example:
        >>> controller = MotorController(pca)
        >>> controller.set_speed("left", 0.5)
        >>> controller.stop_all()
    """
    
    def __init__(self, pca: PCA9685):
        """Initialize motor controller.
        
        Args:
            pca: Initialized PCA9685 instance
        """
        self.pca = pca
        self.motors = {}
```

## Hardware Configuration

### I2C Devices

| Device | Address | Purpose | Channels |
|--------|---------|---------|----------|
| PCA9685 | 0x40 (64) | Motor/Servo PWM Controller | 16 channels |
| LCD Display | 0x27 (varies) | Text display | I2C |

### PCA9685 Channel Mapping

```python
# Motor channels (using pairs for H-bridge control)
MOTOR_LEFT_FWD = 0
MOTOR_LEFT_REV = 1
MOTOR_RIGHT_FWD = 2
MOTOR_RIGHT_REV = 3

# Servo channels
SERVO_ARM = 4
SERVO_GRIPPER = 5

# LED/Semaforo channels
SEMAFORO_1_RED = 6
SEMAFORO_1_GREEN = 7
SEMAFORO_1_BLUE = 8
SEMAFORO_2_RED = 9
SEMAFORO_2_GREEN = 10
SEMAFORO_2_BLUE = 11
```

### GPIO Pin Configuration

```python
# SPI for NeoPixel LED rings
SPI_MOSI = GPIO 10
SPI_SCLK = GPIO 11

# I2C for PCA9685 and LCD
I2C_SDA = GPIO 2
I2C_SCL = GPIO 3
```

### Gamepad Configuration

```python
# Default gamepad device
GAMEPAD_DEVICE = '/dev/input/event2'  # May vary, check with ls /dev/input/

# Common gamepad event codes (varies by controller)
BTN_A = 304
BTN_B = 305
BTN_X = 307
BTN_Y = 308
ABS_X = 0  # Left stick X
ABS_Y = 1  # Left stick Y
```

## Development Workflow

### 1. Planning Phase
- Review hardware requirements
- Check existing library functions in `mylib_*.py` files
- Plan component integration

### 2. Implementation Phase
- Create or modify library files (`mylib_*.py`) for reusable code
- Create demo scripts (`*-main.py`) to test components
- Test incrementally on actual hardware

### 3. Testing Phase
- Create test scripts (`test_*.py`) for validation
- Test individual components before integration
- Verify with hardware validation commands

### 4. Integration Phase
- Combine components into main robot control script
- Test full system integration
- Optimize performance for Raspberry Pi

### 5. Deployment Phase
- Ensure all dependencies are in `pyproject.toml`
- Test on target Raspberry Pi hardware
- Document any hardware-specific configurations

## Safety Guidelines

> [!CAUTION]
> Robotics projects involve motors and moving parts. Always prioritize safety.

### Motor Safety

```python
# Always initialize motors to stopped state
motor1.throttle = 0.0
motor2.throttle = 0.0

# Always include cleanup in finally block
try:
    # Motor control code
    pass
finally:
    motor1.throttle = 0.0
    motor2.throttle = 0.0

# Limit maximum speed during testing
MAX_SAFE_THROTTLE = 0.5  # 50% during development
motor1.throttle = min(desired_throttle, MAX_SAFE_THROTTLE)

# Add emergency stop functionality
def emergency_stop():
    """Immediately stop all motors."""
    motor1.throttle = 0.0
    motor2.throttle = 0.0
    print("EMERGENCY STOP ACTIVATED")
```

### Power Management

- Monitor battery voltage if using battery power
- Implement low-battery warnings
- Gracefully shut down on power loss
- Avoid sudden high-current draws

### Hardware Protection

```python
# Limit PWM duty cycles to safe ranges
def safe_duty_cycle(value: int) -> int:
    """Clamp duty cycle to safe range."""
    return max(0x0000, min(0xFFFF, value))

# Add timeouts to prevent infinite loops
import signal

def timeout_handler(signum, frame):
    raise TimeoutError("Operation timed out")

signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(5)  # 5 second timeout
```

## Testing Approach

### Test Script Structure

```python
#!/usr/bin/env python3
"""
Test Script: Motor Control Validation
Tests basic motor functionality and safety features.
"""

import time
import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import motor


def test_motor_initialization():
    """Test motor initialization."""
    print("Test 1: Motor Initialization")
    try:
        i2c = busio.I2C(SCL, SDA)
        pca = PCA9685(i2c, address=64)
        pca.frequency = 1000
        motor1 = motor.DCMotor(pca.channels[0], pca.channels[1])
        print("✓ Motor initialized successfully")
        return True
    except Exception as e:
        print(f"✗ Motor initialization failed: {e}")
        return False


def test_motor_movement():
    """Test motor movement."""
    print("\nTest 2: Motor Movement")
    try:
        i2c = busio.I2C(SCL, SDA)
        pca = PCA9685(i2c, address=64)
        pca.frequency = 1000
        motor1 = motor.DCMotor(pca.channels[0], pca.channels[1])
        motor1.decay_mode = motor.SLOW_DECAY
        
        # Test forward
        motor1.throttle = 0.3
        time.sleep(1)
        
        # Test stop
        motor1.throttle = 0.0
        time.sleep(0.5)
        
        # Test reverse
        motor1.throttle = -0.3
        time.sleep(1)
        
        # Final stop
        motor1.throttle = 0.0
        
        print("✓ Motor movement test passed")
        return True
    except Exception as e:
        print(f"✗ Motor movement test failed: {e}")
        return False
    finally:
        motor1.throttle = 0.0


def main():
    """Run all tests."""
    print("=" * 50)
    print("Motor Control Test Suite")
    print("=" * 50)
    
    results = []
    results.append(test_motor_initialization())
    results.append(test_motor_movement())
    
    print("\n" + "=" * 50)
    print(f"Results: {sum(results)}/{len(results)} tests passed")
    print("=" * 50)


if __name__ == "__main__":
    main()
```

### Hardware Validation Checklist

- [ ] I2C devices detected with `i2cdetect -y 1`
- [ ] SPI devices available at `/dev/spidev*`
- [ ] Gamepad detected at `/dev/input/event*`
- [ ] Motors respond to throttle commands
- [ ] Servos move to commanded positions
- [ ] LEDs display correct colors
- [ ] LCD displays text correctly
- [ ] Emergency stop works
- [ ] Cleanup functions execute properly

## Common Patterns

### Pattern 1: Hardware Initialization

```python
import time
import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import motor

# Initialize I2C bus
i2c = busio.I2C(SCL, SDA)

# Initialize PCA9685 PWM controller
pca = PCA9685(i2c, address=64)
pca.frequency = 1000

# Initialize motors
motor_left = motor.DCMotor(pca.channels[0], pca.channels[1])
motor_left.decay_mode = motor.SLOW_DECAY
motor_left.throttle = 0.0

motor_right = motor.DCMotor(pca.channels[2], pca.channels[3])
motor_right.decay_mode = motor.SLOW_DECAY
motor_right.throttle = 0.0
```

### Pattern 2: Main Loop with Cleanup

```python
def main():
    """Main control loop."""
    # Initialize hardware
    i2c = busio.I2C(SCL, SDA)
    pca = PCA9685(i2c, address=64)
    pca.frequency = 1000
    
    motor1 = motor.DCMotor(pca.channels[0], pca.channels[1])
    motor1.decay_mode = motor.SLOW_DECAY
    motor1.throttle = 0.0
    
    try:
        print("Starting main loop (Ctrl+C to exit)")
        while True:
            # Main logic here
            motor1.throttle = 0.5
            time.sleep(1)
            motor1.throttle = 0.0
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        # Cleanup
        motor1.throttle = 0.0
        print("Motors stopped")


if __name__ == "__main__":
    main()
```

### Pattern 3: LED/RGB Control

```python
def set_rgb_color(channel_r: int, channel_g: int, channel_b: int, 
                  color: str, pca: PCA9685) -> None:
    """Set RGB LED color.
    
    Args:
        channel_r: Red channel number
        channel_g: Green channel number
        channel_b: Blue channel number
        color: Color name (red, green, blue, yellow, cyan, magenta, white, off)
        pca: PCA9685 instance
    """
    colors = {
        "red": (0xFFFF, 0x0000, 0x0000),
        "rojo": (0xFFFF, 0x0000, 0x0000),
        "green": (0x0000, 0xFFFF, 0x0000),
        "verde": (0x0000, 0xFFFF, 0x0000),
        "blue": (0x0000, 0x0000, 0xFFFF),
        "azul": (0x0000, 0x0000, 0xFFFF),
        "yellow": (0xFFFF, 0xFFFF, 0x0000),
        "amarillo": (0xFFFF, 0xFFFF, 0x0000),
        "cyan": (0x0000, 0xFFFF, 0xFFFF),
        "magenta": (0xFFFF, 0x0000, 0xFFFF),
        "white": (0xFFFF, 0xFFFF, 0xFFFF),
        "blanco": (0xFFFF, 0xFFFF, 0xFFFF),
        "off": (0x0000, 0x0000, 0x0000),
        "apagado": (0x0000, 0x0000, 0x0000),
    }
    
    r, g, b = colors.get(color.lower(), (0x0000, 0x0000, 0x0000))
    pca.channels[channel_r].duty_cycle = r
    pca.channels[channel_g].duty_cycle = g
    pca.channels[channel_b].duty_cycle = b
```

### Pattern 4: Gamepad Integration

```python
import evdev
from typing import Optional

class GamepadController:
    """Gamepad input controller."""
    
    def __init__(self, device_path: str = '/dev/input/event2'):
        """Initialize gamepad controller."""
        try:
            self.device = evdev.InputDevice(device_path)
            print(f"Gamepad connected: {self.device.name}")
        except Exception as e:
            print(f"Error: Could not connect to gamepad at {device_path}")
            print("Available devices:")
            for dev in evdev.list_devices():
                device = evdev.InputDevice(dev)
                print(f"  {dev}: {device.name}")
            raise e
    
    def read_events(self) -> list:
        """Read all pending events."""
        events = []
        try:
            for event in self.device.read():
                events.append(event)
        except BlockingIOError:
            pass  # No events available
        return events
    
    def get_axis_value(self, axis_code: int) -> Optional[int]:
        """Get current value of an axis."""
        try:
            return self.device.absinfo(axis_code).value
        except Exception:
            return None
```

## Troubleshooting

### Common Issues and Solutions

#### Issue: I2C Device Not Detected

```bash
# Check if I2C is enabled
sudo raspi-config
# Interface Options -> I2C -> Enable

# Check for I2C devices
i2cdetect -y 1

# If no devices found, check wiring:
# - SDA to GPIO 2
# - SCL to GPIO 3
# - VCC to 3.3V or 5V (check device specs)
# - GND to GND
```

#### Issue: Gamepad Not Found

```bash
# List all input devices
ls -l /dev/input/event*

# Test each device to find gamepad
evtest /dev/input/event0
evtest /dev/input/event1
evtest /dev/input/event2

# Update device path in code
GAMEPAD_DEVICE = '/dev/input/eventX'  # Use correct number
```

#### Issue: Permission Denied for GPIO/I2C

```bash
# Add user to required groups
sudo usermod -a -G i2c,spi,gpio $USER

# Reboot for changes to take effect
sudo reboot

# Or use sudo for testing (not recommended for production)
sudo python motor-main.py
```

#### Issue: Motors Not Responding

```python
# Debug checklist:
# 1. Check PCA9685 is detected
i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c, address=64)
print(f"PCA9685 frequency: {pca.frequency}")

# 2. Check motor channels are correct
print(f"Channel 0 duty cycle: {pca.channels[0].duty_cycle}")

# 3. Verify power supply to motors
# - Check battery voltage
# - Ensure motor driver has power
# - Check motor connections

# 4. Test with simple throttle
motor1.throttle = 0.5
time.sleep(2)
motor1.throttle = 0.0
```

#### Issue: Import Errors

```bash
# Ensure virtual environment is activated
source .venv/bin/activate

# Reinstall dependencies
uv sync

# Check installed packages
uv pip list

# Install missing package
uv add <package-name>
```

#### Issue: Performance/Lag

```python
# Optimize loop timing
import time

# Bad: Busy waiting
while True:
    process_input()
    # CPU at 100%

# Good: Sleep between iterations
while True:
    process_input()
    time.sleep(0.01)  # 100Hz update rate

# Better: Event-driven
for event in gamepad.read_loop():
    process_event(event)
```

### Debug Logging

```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Use in code
logger.debug("Motor initialized")
logger.info("Starting main loop")
logger.warning("Battery voltage low")
logger.error("I2C communication failed")
```

## Quick Reference

### Essential Commands

```bash
# Environment
uv venv && source .venv/bin/activate
uv sync

# Hardware validation
i2cdetect -y 1
ls -l /dev/input/event*

# Run tests
python test_01.py

# Monitor gamepad
evtest /dev/input/event2
```

### Key Dependencies

```python
# Hardware control
import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import motor
from adafruit_servokit import ServoKit

# Input
import evdev

# Display
from RPLCD.i2c import CharLCD

# LED control
from adafruit_circuitpython_neopixel_spi import NeoPixel_SPI
```

### Motor Control Cheat Sheet

```python
# Initialize
motor1 = motor.DCMotor(pca.channels[0], pca.channels[1])
motor1.decay_mode = motor.SLOW_DECAY

# Control
motor1.throttle = 1.0   # Full forward
motor1.throttle = 0.5   # Half forward
motor1.throttle = 0.0   # Stop
motor1.throttle = -0.5  # Half reverse
motor1.throttle = -1.0  # Full reverse
```

### Servo Control Cheat Sheet

```python
# Initialize
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

# Control
kit.servo[0].angle = 0    # Minimum position
kit.servo[0].angle = 90   # Center position
kit.servo[0].angle = 180  # Maximum position
```

### Color Reference

| Color (English) | Color (Spanish) | RGB Values |
|----------------|-----------------|------------|
| red | rojo | (255, 0, 0) |
| green | verde | (0, 255, 0) |
| blue | azul | (0, 0, 255) |
| yellow | amarillo | (255, 255, 0) |
| cyan | cian | (0, 255, 255) |
| magenta | magenta | (255, 0, 255) |
| white | blanco | (255, 255, 255) |
| off | apagado | (0, 0, 0) |

---

## Notes for AI Agents

> [!IMPORTANT]
> Key principles when working on this project:

1. **Hardware First**: This is a hardware-focused project - prioritize reliability over performance
2. **Test on Hardware**: Always test on actual Raspberry Pi hardware when possible
3. **Safety**: Always include cleanup code and emergency stop functionality
4. **Debug Output**: Use print statements liberally for debugging hardware issues
5. **Conservative Values**: Be conservative with motor speeds and LED brightness during development
6. **Error Handling**: Handle hardware disconnection gracefully
7. **Power Awareness**: Consider power management for battery operation
8. **Documentation**: Document hardware-specific configurations and pin mappings
9. **Incremental Testing**: Test components individually before integration
10. **Version Control**: Commit working code frequently with descriptive messages

### Commit Message Guidelines

Use conventional commits format:

```
feat: Add gamepad control for motors
fix: Correct I2C address for LCD display
docs: Update hardware configuration in AGENTS.md
test: Add motor safety validation tests
refactor: Extract LED control into mylib_ledring
chore: Update dependencies in pyproject.toml
```

---

**Last Updated**: 2026-01-28  
**Version**: 2.0  
**Maintained by**: Eurobot Team