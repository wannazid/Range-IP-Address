import ipaddress
import threading
import os
import time
from colorama import Fore, Back, Style

linux = 'clear'
windows = 'cls'
os.system([linux,windows][os.name == 'nt'])

hijau = Fore.GREEN
merah = Fore.RED
cyan = Fore.CYAN
tai = Fore.YELLOW
biru = Fore.BLUE
batas = Style.RESET_ALL

banner = '''

      +-+-+-+-+-+ +-+-+
      |R|a|n|g|e| |I|P|
      +-+-+-+-+-+ +-+-+
       By : Wan5550
       Github : github.com/wannazid
       IP Version : 4
'''
print(hijau)
print(banner)
print(batas)
def RangeIP():
	input_ip = input('[#] List IP > ')
	input_save = input('[#] Save Name > ')
	open_ip = open(input_ip,'r').read().splitlines()
	print('\n')
	text = '[!] Procces Range IP'
	for huruf in text:
		print(huruf,end='',flush=True)
		time.sleep(0.5)
	for list in open_ip:
		for ip in ipaddress.IPv4Network(list+'/24', False):
			savefile = open(input_save,'a').write(str(ip)+'\n')
	print('\n')
	print('[!] Done...')
t = threading.Thread(target=RangeIP)
t.start()