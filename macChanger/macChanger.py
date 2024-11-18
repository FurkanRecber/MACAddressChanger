import subprocess
import optparse
import re


def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="interface to change!")
    parse_object.add_option("-m", "--mac", dest="macAddress", help="new mac address!")
    return parse_object.parse_args()


def change_mac(interface, macAddress):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", macAddress])
    subprocess.call(["ifconfig", interface, "up"])


def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
    if new_mac:
        return new_mac.group(0)
    else:
        return None


(user_input, args) = get_user_input()
change_mac(user_input.interface, user_input.macAddress)
final_mac = control_new_mac(str(user_input.interface))

if final_mac == user_input.macAddress:
    print("Successfully changed mac!")
else:
    print("Failed to change mac!")
