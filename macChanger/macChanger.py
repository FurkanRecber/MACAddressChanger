import subprocess
import optparse

parse_object = optparse.OptionParser()
parse_object.add_option("-i", "--interface", dest="interface", help="interface to change!")
parse_object.add_option("-m", "--mac", dest="macAddress", help="new mac address!")

(userInputs, arguments) = parse_object.parse_args()
interface = userInputs.interface
macAddress = userInputs.macAddress

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", macAddress])
subprocess.call(["ifconfig", interface, "up"])
