# Mikrotik Configuration Manager

Mikrotik Configuration Manager is a Python utility for better configuration and management. The utility uses SSH to configure the device and is intended as a replacement for quickset. This is an ongoing project that will help ISP/WISP/MSP installers and network administrators speed up their time till installtion. 

## Installation

Download the `mikrotik-auto-config-ssh.py` script and
use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install tkinter
pip install paramiko
```

## Usage

To use the utility, cd to the directory that contains your `mikrotik-auto-config-ssh.py` script and then run the script as shown below:
```bash
python mikrotik-auto-config-ssh.py
```

#### **Notes:**
**You must have layer 3 access to the device that you would like to configure for the utlity to work.** At this time, there is not an option to reboot, update, or upload any scripts or files. This will come at a later time. 

## Pipeline
#### Note: These items are subject to change at any time and are not guaranteed
- Ability to upload baseline configurations and scripts
- Ability to update and reboot devices
- Device detection, think similar to CDP neighbors
- Dynamic interface population

## Contributing
If you would like to become a contributer please open an issue. For changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
MIT License
