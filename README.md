# Mikrotik Configuration Utility

Mikrotik Configuration Manager is a Python utility for better configuration and management. The utility uses SSH to configure the device and is intended as a replacement for quickset. This is an ongoing project that will help ISP/WISP/MSP installers and network administrators speed up their time till installtion. 


![MikrotikAutoConfigUtilityFinal](https://user-images.githubusercontent.com/87310427/126878739-ee7b9924-74db-4762-ba4c-ffef9a3640bc.png)

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
**Required Fields:**
- Management IP Address
- Management Port
- Username
- Password

**Step 1:** Configuration upload
- Once layer 3 access to device is verified, use the `Upload Configuration File` `select` button to choose your baseline config file. **See notes for requirements.**
- Click the upload button to transer the config file to the Routerboard
- Click the `Run` button to initiate defaulting the device and running the config file. This will take a couple minutes so be patient.

**Step 2:** Configuration of install related fields
- Proceed with entering the install related data fields. **All fields must be data filled for configuration to work.**
- **WAN IP must be entered in CIDR format i.e. 10.1.1.1/24**
- Choose your WAN interface from the drop down menu. 
- Enter Identity, WPA passphrase, and SSIDs to continue. **WPA passphrase must be at lease 8 characters long with at least one number or one capitol. This is a Mikrotik requirement.**
- Once all of the fields are filled, click the ```Submit``` button. This will initiate a SSH connection to the device and will send the remaining programing to the device. 

**Firmware Uploading:**
- Use the ```Select``` button under ```Upload Firmware File``` to chose the package file you would like to upload. 
- Once selected, use the ```Upload``` button to push the firmware file to the Routerboard. 
- Finally, click the ```Reboot``` button to send the reboot command to the Routerboard. Upon rebooting, the device will upgrade the firmware.

#### **Notes:**
This tool uses SSH and SFTP for connection to the device. You must have layer 3 access to the device to use this tool.

**You will need to add the following line to the top of any configuration files that you intend to use:**
```/delay delay-time=15s```

If you do not add the above line, the configuration utility of the program will fail and your device will be reset with no default configuration.

## Pipeline
#### Note: These items are subject to change at any time and are not guaranteed

- Ability to upload baseline configurations and scripts - **Complete**
- Ability to update and reboot devices - **Complete**
- Reformat of the GUI for easier navigation and usage
- Debugging and checks/balances
- Check connection - ICMP check to device
- Making tool executable
- Device detection, think similar to CDP neighbors
- Dynamic interface population

## Contributing
If you would like to become a contributer please open an issue. For changes, please open an issue first to discuss what you would like to change.

If a you would like to commit a change, please open a pull request for review. Please make sure to update tests as appropriate.

## License
MIT License
