#! /usr/bin/env python3

import argparse

parser=argparse.ArgumentParser()
parser.add_argument("--parallel", type=str, nargs='+', help="Get the alignment quality of the parallel corpus", required=True)
args = parser.parse_args()

def isnumber(s):
	try:
		float(s)
		return True
	except ValueError:
		pass
	
	try:
		import unicodedata
		unicodedata.numeric(s)
		return True
	except (TypeError, ValueError):
		pass
	return False

if args.parallel:
	for z in args.parallel:
		with open(z, "r") as infile:
			contents = infile.readlines()
			total = 0
			loss = 0
			for line in contents:
				check = False
				numbers = []
				source, target = line.strip("\n").split("\t")
				for i in source:
					if i != "౦" and isnumber(i):
						numbers.append(i)
						check = True
				if check == True:
					total += 1
				
				check = False
				for i in target:
					if i != "౦" and isnumber(i):
						if i in numbers:
							numbers.remove(i)
						else:
							check = True
				if len(numbers) !=0 or check == True:
					loss += 1
		
			print(z + ":\t" + str(round(loss*100/total, 3)))
