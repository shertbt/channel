#!/usr/bin/env python3 

import sys
import time
import string
import random
from scapy.all import *

def client():
	dest=raw_input('Enter the destination IP: ')
	while True:
		message=raw_input('Enter your message: ')
		message+="\n"
		print "Sending data: "+ message
		bitmessage=' '.join(format(ord(x),'b').zfill(8) for x in message)

		for bit in bitmessage:
			if(bit == '0'):
				pkt=(IP(dst=dest,ttl=64)/ICMP(type=8))
				send(pkt)
			elif(bit == '1'):
				pkt=(IP(dst=dest,ttl=128)/ICMP(type=8))
				send(pkt)
			#time.sleep(RandNum(0,1))

		pkt=(IP(dst=dest,ttl=254)/ICMP(type=8))
		send(pkt)
		print "Transmission complete"
client()
