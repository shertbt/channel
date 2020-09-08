#!/usr/bin/env python3 

import sys
from scapy.all import *

bitmessage=""
message=""

def readmessage(pkt):
		flag=pkt['ICMP'].type
		ttl=pkt['IP'].ttl
		
		global bitmessage
		global message
		if flag==8:
			if ttl==64:
				bitmessage+="0"
			elif ttl==128:
				bitmessage+="1"
			elif ttl==254:
				messageArr=[bitmessage[i:i+8] for i in range(0,len(bitmessage),8)]
				for char in messageArr:
					message+=str(chr(int(char,2)))
				print message
				bitmessage=""
				message=""

sniff(filter="icmp",prn=readmessage)



