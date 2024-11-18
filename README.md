# MAC Address Changer

This script allows you to change the MAC address of a network interface on Linux systems. It's a simple tool that uses Python's `optparse` module to handle user inputs and the `subprocess` module to execute system commands.

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
git clone <repository_url>
cd <repository_folder>
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

## Notes
- Always run the script with `sudo` or as root since changing network configurations requires elevated privileges.
- Be cautious when changing MAC addresses, especially on systems where networking is critical.

## Disclaimer
This tool is for educational purposes only. The author is not responsible for any misuse or damages caused by this script.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
