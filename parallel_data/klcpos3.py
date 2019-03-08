#! /usr/bin/env python3

import argparse
import math
import operator

parser = argparse.ArgumentParser("Program to calculate klcpos3 measure for single, and multi-sourced delexicalised parsing algorithms")
parser.add_argument("-t", "--target", type=str, required=True, help= "Target candidate file, in CONLLU format")
parser.add_argument("-s", "--source", nargs="+", type=str, required=True, help="Source candidate file(s), in CONLLU format")
group = parser.add_mutually_exclusive_group(required=False)
group.add_argument("--single_source", action='store_true', help="Used for selection of single source, the values would be displayed in decreasing order of similarity measure")
group.add_argument("--multi_source", action='store_true', help="Used for computing klcpos3 ^ -4 as a similarity measure for weighted multiple source parsing")
args = parser.parse_args()


def klcpos3(tgt_dict, src_dict, tgt_total):
	final_result = 0
	for trigram in tgt_dict:
		tgt_val = 0
		src_val = 0
		if trigram not in src_dict:
			src_val = 1
		else:
			src_val = src_dict[trigram]
		tgt_val = tgt_dict[trigram]/tgt_total
		result = tgt_val * (math.log(tgt_val) / math.log(src_val))
		final_result += result
	return final_result


def get_pos_list(file_contents):
	out_list = ["_"]
	for lines in file_contents:
		if lines != "\n":
			if lines[0] != "#":
				Id, form, lemma, upos, xpos, feats, head, deprel, deps, misc = lines.split("\t")
				if upos != "_": # multi word tokens
					out_list.append(upos)
		else:
			out_list.append("_")
	return out_list


def trigram_from_list(pos_list):
	string = pos_list[0] + "+"
	a = dict()
	total = 0
	for i in range(1, len(pos_list)):
		if i % 3 != 0:
			if (i+1) % 3 != 0:
				string += pos_list[i] + "+"
			else:
				string += pos_list[i]
		else:
			if "+_+" not in string:
				if string in a:
					a[string] += 1
					total += 1
				else:
					a[string] = 1
					total += 1
			string = pos_list[i] + "+"
	
	return a, total


def mod_source_list(orig_source, orig_tgt, orig_source_count):
	div_by = orig_source_count
	new_copy = orig_source
	for i in orig_tgt:
		if i not in new_copy:
			new_copy[i] = 1
			div_by += 1
	for i in new_copy:
		new_copy[i] /= div_by
	
	return new_copy
	

if __name__ == "__main__":
	source = dict()
	target = dict()
	tgt_total = 0
	
	with open(args.target, "r", encoding="utf-8") as tgt_file:
		target_data = tgt_file.readlines()
		tgt_list = get_pos_list(target_data)
		target, tgt_total = trigram_from_list(tgt_list)
	
	values_list = dict()
	for i in args.source:
		with open(i, "r", encoding="utf-8") as source_file:
			source.clear()
			src_total = 0
			source_data = source_file.readlines()
			src_list = get_pos_list(source_data)
			source, src_total = trigram_from_list(src_list)
			source = mod_source_list(source, target, src_total)
			values_list[i] = klcpos3(target, source, tgt_total)
			
	if args.single_source:
		values_list_2 = sorted(values_list.items(), key=operator.itemgetter(1), reverse=True)
		for i, j in values_list_2:
			print(i + "\t" + str(j))
	else:
		for i in values_list:
			values_list[i] = math.pow(values_list[i], -4)
		
		values_list_2 = sorted(values_list.items(), key=operator.itemgetter(1), reverse=True)
		for i, j in values_list_2:
			print(i + "\t" + str(j))
		print("\n\nNote that the above weights are not normalised.")
