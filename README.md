


## Install uv (with shell)
https://docs.astral.sh/uv/getting-started/installation/#installation-methods

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Install uv (with pip)

```bash
pip install uv
```

## Create environment 
When the repo was created

```bash
uv init eurobot
cd  eurobot
uv venv

source .venv/bin/activate
uv add adafruit-circuitpython-servokit rpi-gpio
```

## Clone repo
```bash
git clone https://github.com/JoseIbanez/eurobot.git
```


## Update after clone
If you clone this repo, then create the venv, and install python pkgs

```bash
uv venv
source .venv/bin/activate
uv sync
```




## Tools: Identify PCA position

```bash

sudo apt-get install i2c-tools

pi@rp3:~ $ i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- 27 -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: 40 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: 70 -- -- -- -- -- -- --    
```

#LCD
https://rplcd.readthedocs.io/en/stable/getting_started.html

