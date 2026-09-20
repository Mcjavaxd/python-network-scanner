import os

NMAP_BANNER = """

==========================================================

 ██████╗ ██╗   ██╗   ███╗   ██╗███╗   ███╗ █████╗ ██████╗ 
 ██╔══██╗╚██╗ ██╔╝   ████╗  ██║████╗ ████║██╔══██╗██╔══██╗
 ██████╔╝ ╚████╔╝ == ██╔██╗ ██║██╔████╔██║███████║██████╔╝
 ██╔═══╝   ╚██╔╝     ██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝ 
 ██║        ██║      ██║ ╚████║██║ ╚═╝ ██║██║  ██║██║     
 ╚═╝        ╚═╝      ╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     
 
==========================================================
     [+]Network Scnanner and Reconnisesnce tool[+]
"""
print(NMAP_BANNER)


a=input('\nEnter an ip address from you network: ')
print('\nScanning for Devices....\n')
b=a.split('.')
subnet=b[0]+'.'+b[1]+'.'+b[2]+'.'
counter=0
for i in range(1,256):
	ip=subnet+str(i)
	status=os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
	if status==0:
		print(f'[+] Active Device: {ip}')
		counter+=1
	else:
		pass
print('\nScan Compeleted')
print('====================')
print(f'No of devices active : {counter}')
