#! /usr/bin/env python3

import re
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("-p", "--parallel", type=str, help="Parallel data file", required=True)
parser.add_argument("-d", "--delimiter", type=str, help="Delimiter seperating target and source side in parallel data file", required=True)
parser.add_argument("-a", "--alignment", type=str, help="Alignment file", required=True)
parser.add_argument("-at", "--alignment_type", type=int, help="The alignment counts index from this value", required=True)

args = parser.parse_args()


def replace_by_words(num_list, word_list):
	new_num_list = []
	for i in num_list:
		new_num_list.append(int(i)-args.alignment_type)
	return_list = []
	for i in new_num_list:
		return_list.append(word_list[i])
	return return_list


def isnumber(s):
	try:
		float(s.strip())
		return True
	except ValueError:
		pass
	try:
		import unicodedata
		unicodedata.numeric(s.strip())
		return True
	except (TypeError, ValueError):
		pass
	return False


if __name__ == "__main__":
	data = dict()
	# TODO: Fix issues with the args.delimiter thingy
	# args.delimiter = re.escape(args.delimiter)
	if args.delimiter == "\\t":
		args.delimiter = "\t"
	# store the data in a parallel format in a dictionary
	with open(args.parallel, "r") as parallel_data:
		parallel_contents = parallel_data.readlines()
		for line in parallel_contents:
			source, target = line.split(args.delimiter)
			data[source] = target.strip("\n")
			
	with open(args.alignment, "r") as alignment_file:
		alignment_data = alignment_file.readlines()
		total = 0
		right = 0
		for i in range(len(alignment_data)):
			source = ""
			target = ""
			if i%3 == 1:
				target = alignment_data[i].strip(" \n")
				for x in data:
					if data[x] == target:
						source = x.split()
				target = target.split()
				# start processing the alignment line
				alignment = alignment_data[i+1].strip("\n")
				data2 = dict()
				tgt_list = alignment.strip("\n").split("})")
				tgt_list = tgt_list[1:-1]
				for z in tgt_list:
					src, align = z.split(" ({ ")
					align = align.split()
					if len(align) == 0:
						data2[src] = align
					else:
						align = replace_by_words(align, target)
						data2[src] = align
				
				for z in source:
					if z != "౦" and isnumber(z):
						if z not in data2:
							data2[z] = []
				
				for z in data2:
					numbers_src = []
					numbers_tgt = []
					check = False
					
					if z != "౦" and isnumber(z):
						numbers_src.append(z)
						check = True
					
					for k in data2[z]:
						if k != "౦" and isnumber(k):
							numbers_tgt.append(k)
							check = True
						
					if check is True:
						total += 1
					
					if check:
						if len(numbers_tgt) == len(numbers_src):
							if numbers_src.sort() == numbers_tgt.sort():
								right += 1

	if total != 0:
		print("Accuracy percentage for " + args.alignment + ":\t" + str(round(right*100/total, 3)))
	else:
		print("Not enough numerical data in the alignment")
	
	
