import subprocess
import pyfiglet
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="NEW MAC address")
    (value, arguments) =  parser.parse_args()
    if not value.interface:
        parser.error("[-] please specify an interface , use --help for more info")
    elif not value.new_mac:
        parser.error("[-] please specify an new mac , use --help for more info")
    return value


def mac_changer(interface, new_mac):
    print("[+] Changing mac address for  " + interface + "  to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


ascii_banner = pyfiglet.figlet_format("Coded  by  Mirror!!")
print(ascii_banner)

value = get_arguments()
mac_changer(value.interface, value.new_mac)
