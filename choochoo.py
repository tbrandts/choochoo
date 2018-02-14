import socket
import sys
import os
import subprocess
import time

tcp = socket.socket()
tcp.bind(('',55555))

addresses = ['146.163.48.128', '146.163.115.139']
me = '146.163.48.128'

index = addresses.index(me)
num = len(addresses)
nextaddr = addresses[(index + 1) % num]


def send(start = False):
	c = socket.socket()
	c.connect((nextaddr, 55555))
	c.send('choochoo')
	data = c.recv(1024)
	if start == True:
		print 'started'
	print data
	c.close()


print 'Listening'
tcp.listen(1000)

if len(sys.argv) == 2 and sys.argv[1] == 'start':
	send(True)


while True:
	connection, address = tcp.accept()
	data = connection.recv(1024)
	if data == 'choochoo' :
		rows, columns = os.popen('stty size').read().split(' ')
		# status = subprocess.call('sl -e', shell=True)
		status = subprocess.Popen('sl -e', shell=True)
		time.sleep(float(columns) * .02125) #I measured this number as 80 columns / 1.7 sec => .02125
		connection.send('oochooch')
		connection.close()
		send()
