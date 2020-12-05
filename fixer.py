#This will take input csv from SecApps and prepare a txt for wappalyzer-script.py
#choose the flag accordingly
#download subdomains csv and place the data.csv file in this folder
#or
#download uri csv and place the data.csv file in this folder (useful when there are a lot of domains)

import argparse

#help
parser=argparse.ArgumentParser(description='''Fixer script to lauch before wappalyzer''')
parser.add_argument('--domains', '-d', default=True, required=False, action='store_true', help='Use a list of domains. Output in "domains.txt" file (Default=True)')
parser.add_argument('--uri', '-u', default=False, required=False, action='store_true', help='Use a list of URI instead of domains. Output in "uri.txt" file')
args=parser.parse_args()

def fixer():
	file_in = "data.csv"
	file_out = "temp.txt"
	l=0

	with open  (file_out,"w") as o:
		with open (file_in,"r") as f:
			for line in f:
				if l==0:
					l+=1
					continue
				string = line.replace('"','').replace("\n","")
				o.write(string)
				o.write("\n")

def resolver():
	import socket
	import os
	inputfile = "temp.txt"
	outputfile = "domains.txt"

	with open (outputfile,"w") as o:
	    with open (inputfile,"r") as f:
	        for domain in f:
	            try:
	                ip = socket.gethostbyname(domain.strip())
	                o.write(domain)
	            except:
	                ip = None
	try:
	    os.remove(inputfile)
	except OSError:
	    pass

def fixer_uri():
	import csv
	file_in = "data.csv"
	file_out = "uri.txt"
	l=0
	with open  (file_out,"w") as o:
		with open (file_in,"r") as f:
			reader = csv.reader(f,delimiter=",")
			for line in reader:
				if l == 0:
					l+=1
					continue
				a = is_ip(line[0])	#check if uri contains ip address
				if a == True:
					continue	#skip if is an ip
				else:
					o.write(line[0])
					o.write("\n")

def is_ip(line):
	import re
	match = re.match("https?://(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})", line)
	if not match:
		return False
	else:
		return True

if args.uri:
	print ("Creating Wappalyzer input file")
	fixer_uri()

else:
	print ("Adjusting SecApps input-data")
	fixer()
	print ("Creating Wappalyzer input file")
	resolver()
