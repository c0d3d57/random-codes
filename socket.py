#Playing with socket and urllib modules
import sys
import re
import socket
import urllib
from time import sleep

#This section defines the url handler and reads the headers.
def urll(url):
	url = "http://www." + url
	url = str(url)
	print url
	conn = urllib.urlopen(url)
	if (conn):
		print("Printing Headers...\n")
		res = conn.info()
		data = conn.read()
		print "URL: ", conn.geturl()
		print "DATE: ", res['date']
		print "SERVER: ", res['server']
		print "TYPE: ", res['content-type']
		print "LENGTH: ", len(data)
	else:
		print("\nUnable to fetch URL!")

#This section checks the ip address against the assigned port.
def d_test(host, port):
	host = host
	port = port
	try:
		print("Testing IP Address: "), host
		s = socket.socket(
    		socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))
	except socket.error as msg:
		print "Connection Failed: " + str(msg[0]) + " Message " + msg[1]
		sys.exit()
	else:
		print "Connection Success: "
		sys.exit()

#This section checks the domain againsts the assigned port and sends it to the url handler for further inspection.
def s_test(host, port):
	host = host
	port = port
	try:
		print("Testing domain: ")
		s = socket.socket(
    		socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))
	except socket.error as msg:
		print "Connection Failed: " + str(msg[0]) + " Message " + msg[1]
		sys.exit()
	else:
		print "Connection Success: "
		urll(host)


#Get input from keyboard
HOST = raw_input("Enter Host Name: ")
PORT = raw_input("Enter Port: ")

print "You have entered", HOST, PORT
sleep(1)
print "Now Checking", HOST, "on port", PORT

#Here we code to differentiate between a domain and ip.
for ip in HOST:
	if re.match(r'[a-zA-Z]+', ip, re.M|re.I): #Here we check to make sure we are not sending an ip address for http inspection :-)
		host = str(HOST)
		port = int(PORT)
		s_test(host, port)
		sys.exit()
	else:
		host = str(HOST)
		port = int(PORT)
		d_test(host, port)
		sys.exit()
