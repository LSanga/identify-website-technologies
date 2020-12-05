#install jq
#install wappalizer

import argparse
import subprocess

#help
parser=argparse.ArgumentParser(description='''Find techlogies on website''')
parser.add_argument('--version', '-v', default=False, required=False, action='store_true', help='Save only components with a version')
parser.add_argument('--full', '-f', default=True, required=False, action='store_true', help='Save full output (Default=True)')
parser.add_argument('--uri', '-u', default=False, required=False, action='store_true', help='Use a list of URI instead of domains')
#parser.add_argument('--input-file', '-i'. default=False, required=False, dest="filename", help='Specify input file')
#add I/O files by cli
args=parser.parse_args()

file_in = "domains.txt"	#list of domains, one per line
prefix = "wappalyzer http://"

#URI already have http schema in front - probably no need to run twice for website that have both
if args.uri:
	file_in = "uri.txt"
	prefix = "wappalyzer "

#bash command full and with versions only
#wappalyzer https://example.com | jq -c ".technologies[] | [.name,.version]"
#wappalyzer https://example.com | jq -c ".technologies[] | select (.version!=null) | [.name,.version]"
#if args.filename:
#	file_in = read(args.filename)

if args.version:
	file_out = "technologies.txt"	#output file
	suffix = ' | jq -c ".technologies[] | select (.version!=null) | [.name,.version]"'
if args.full:
	suffix = ' | jq -c ".technologies[] | [.name,.version]"'
	file_out = "technologies_full.txt"

#it will check appending http:// in front of domains. If they doesn't have a redirect, it will not visit the https version
#TODO add HTTPS if HTTP fails
with open (file_out,"w") as o:
	with open(file_in,"r") as d:
		for domain in d:
			print "Checking "+str(domain)
			command = prefix+str(domain)+suffix	#concatenate full command
			command = command.replace("\n","")
			try:
				result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
				o.write(str(domain))
				o.write(result)
				o.write("\n")
			except:
				print "Error"