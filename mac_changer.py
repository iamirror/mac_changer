#!/sharan/bin/env python
# pip install pyfiglet

import subprocess
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Coded  by  Mirror!!")
print(ascii_banner)

print("")
interface = input("enter interface type : ")
new_mac = input("enter new ip in format of 00:aa:bb:cc:dd: ")

print("Your mac address before changing")
print("/n")
subprocess.call("ifconfig " + interface, shell=True)
print("/n")
subprocess.call("ifconfig " + interface + "down", shell=True)
print("/n")
print("/n")
subprocess.call("ifconfig " + interface + " hw ether "+new_mac, shell=True)
print("/n")
print("/n")
subprocess.call("ifconfig " + interface + "up", shell=True)
print("/n")
print("/n")
print("Your mac address after changing")
print("/n")
subprocess.call("ifconfig " + interface, shell=True)
print("/n")
print("Thank you for using this")