# MAC Address Changer

This script allows you to change the MAC address of a network interface on Linux systems. It uses Python's `optparse` module to handle user inputs, `subprocess` for executing system commands, and `re` for validating the new MAC address.

## Features
- Change the MAC address of a specified network interface.
- Simple and easy-to-use command-line interface.

## Requirements
- Python 3.x
- Root privileges (required to modify network settings)
- A Linux-based operating system

## Installation
Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/FurkanRecber/MACAddressChanger.git
cd MACAddressChanger
```

Make sure Python is installed on your system.

## Usage
Run the script with the following arguments:

- `-i` or `--interface`: Specify the network interface (e.g., `eth0`, `wlan0`).
- `-m` or `--mac`: Provide the new MAC address.

## Example
```bash
sudo python3 mac_changer.py -i wlan0 -m 00:11:22:33:44:55
```

## Explanation
- `ifconfig wlan0 down`: Disables the network interface.
- `ifconfig wlan0 hw ether 00:11:22:33:44:55`: Sets the new MAC address.
- `ifconfig wlan0 up`: Re-enables the network interface.

## Outputs
#### On successful change:
```bash
Successfully changed mac!
```
#### On failure:
```bash
Failed to change mac!
```

## Notes
- Always run the script with `sudo` or as root since changing network configurations requires elevated privileges.
- Be cautious when changing MAC addresses, especially on systems where networking is critical.
- Ensure the MAC address format (e.g., 00:11:22:33:44:55) is correct.

## Disclaimer
This tool is for educational purposes only. The author is not responsible for any misuse or damages caused by this script.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
