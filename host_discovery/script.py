# Import Modules
import sys
import datetime
from ping3 import ping

# main Function
def main(ip):
	try:
		ip=str(ip)
		timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		print(f"Started network discovery. time: ({timestamp}) - ip: ({ip}) ....")

		count=0
		for i in range(1,255):
			num=str(i)
			curr_ip=(ip+"."+num)
			response=ping(curr_ip, timeout=1)
			if response is not None and response is not False:
				count = count + 1
				print(f"{curr_ip} exists!")
		print(f"255 hosts scanned. ({count} are up).")
	except:
		print("Error.....")
		print("Exiting Program....")
		exit()

# Set ip Address
try:
	if (sys.argv[1]=="-h"):
		print("Python program that scans your LAN for active devices.")
		print("usage: python3 script.py -ip <ip-address>")
		print("display this message: python3 script.py -h")
		print("NOTE: you must only enter the first 3 parts of your ip address.")
		exit()
	elif (sys.argv[1]=="-ip"):
		main(sys.argv[2])
		exit()
	else:
		print("Invalid command.")
		print("help: python3 script.py -h")
		exit()
except IndexError:
	print("help: python3 script.py -h")
	exit()
