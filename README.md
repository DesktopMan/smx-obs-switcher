# Introduction

This script switches OBS scenes based on the current screen of the arcade game StepManiaX. The current screen is detected using OCR in a seperate program.

# Prerequisites

1. Setup [SMX OCR](https://github.com/DesktopMan/smx-ocr/)
2. Install [Python 3](https://www.python.org/downloads/)

# OBS setup

1. Open *Tools -> Websocket Server* and enable it. Copy the password for later

# Script setup

Install dependencies:

```
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

1. Copy *config.example.py* to *config.py*
2. Edit *config.py* with your configuration.

Use the same identifier in the config as you did with SMX OCR.

The example config lists the screens you can use for scene transitions.
Each screen can be configured with a scene to use when the screen becomes active and inactive.

The example below has transitions for the *select song* screen and the *gameplay* screen.
Empty settings will not trigger any transition, so you only need to fill in the ones you need.

```
SCREENS = {
    'SELECT SONG': {'in': 'PlayerStats', 'out': 'General'},
    'CONFIRM DIFFICULTY': {'in': '', 'out': ''},
    'GAMEPLAY': {'in': 'GamePlay', 'out': 'General'},
    'RESULTS': {'in': '', 'out': ''},
}
```

# Run the script

```
.venv\Scripts\activate.bat
python main.py
```
