#!/usr/bin/env python3

import sys
usage = "Usage: input_data_file <space> source_input_file_language <space> target_output_file\n" \
        "\tPossible language codes:\n" \
        "\t\tCZ: Czech\n" \
        "\t\tEN: English\n" \
        "\t\tLA: Latin\n" \
        "\t\tTA: Tamil\n"

if len(sys.argv) < 4:
	print(usage)
	exit(0)

en_dict = {
	'ADD': 'PROPN',         # contains fields of form web address or mail ID, stored as ADD. changed to PROPN
	'CC': 'CCONJ',
	'CD': 'NUM',
	'DT': 'DET',
	'EX': 'ADV',
	'FW': 'X',
	'IN': 'SCONJ',          # In between a choice for SCONJ and CCONJ, SCONJ is chosen
	'JJ': 'ADJ',
	'JJR': 'ADJ',
	'JJS': 'ADJ',
	'LS': 'PUNCT',
	'MD': 'AUX',
	'NN': 'NOUN',
	'NFP': 'X',             # unknown tag, marked as X
	'NNS': 'NOUN',
	'NNP': 'PROPN',
	'NNPS': 'PROPN',
	'PDT': 'DET',
	'POS': 'PART',
	'PRP': 'PRON',
	'PRP$': 'PRON',
	'RB': 'ADV',
	'RBR': 'ADV',
	'RBS': 'ADV',
	'RP': 'PART',
	'SYM': 'SYM',
	'TO': 'ADP',
	'UH': 'INTJ',
	'VB': 'VERB',
	'VBD': 'VERB',
	'VBG': 'VERB',
	'VBP': 'VERB',
	'VBN': 'VERB',
	'VBZ': 'VERB',
	'WDT': 'DET',
	'WP': 'PRON',
	'WP$': 'PRON',
	'WRB': 'ADV'
	}

la_dict = {
	'n':	'NOUN',
	'v':	'VERB',
	'a':	'ADJ',
	'd':	'ADV',
	# 'c':	'SCONJ',            # chosen if the 7th field is advmod, cc, obj
	# 'c':  'CCONJ',            # chosen otherwise - mark, conj, appos, conj, case,
	'r':	'ADP',
	'p':	'PRON',
	'm':	'NUM',
	'e':    'INTJ',
	'i':	'INTJ',
	'u':	'PUNCT',            # between PUNCT and SYM for u tag, PUNCT is chosen because
	# 'u':    'SYM'             # the text is likely to contain symbols, and more likely to contain PUNCT
	}

ta_dict = {
	'A':	'ADV',
	'C':	'CCONJ',        # for 'C' tags, the tags are mapped to CCONJ and SCONJ once in each iteration, the higher score of LAS and UAS values are kept
	# 'C':    'SCONJ',      # CCONJ UAS: 51.07 LAS: 42.20      SCONJ UAS: 50.12 LAS: 41.25
	'D':	'DET',
	'I':	'INTJ',
	'J':	'ADJ',
	'N':	'NOUN',
	'P':	'ADP',
	'R':	'PRON',
	'T':	'PART',
	'U':	'NUM',
	'V':	'VERB',
	'X':	'X',
	'Z':	'PUNCT',
	'NE':	'PROPN'
	}

cs_dict = {
	'A':    'ADJ',
	'C':    'NUM',
	'D':    'ADV',
	'I':    'INTJ',
	'N':    'NOUN',
	'P':    'PRON',
	'V':    'VERB',
	'R':    'ADP',
	'T':    'PART',
	'X':    'X',
	'Z':    'PUNCT'
	}

string = ''
dic = {}

if sys.argv[2] == "CZ":
	dic = cs_dict
elif sys.argv[2] == 'EN':
	dic = en_dict
elif sys.argv[2] == 'LA':
	dic = la_dict
elif sys.argv[2] == 'TA':
	dic = ta_dict
else:
	print("Invalid Language Code entered.")
	print(usage)
	exit(0)
	
with open(sys.argv[1], "r") as filed:
	for lines in filed:
		if lines[0] == "#":         # lines as commments
			string += lines
		elif lines == '\n':         # empty lines
			string += lines
		else:
			lines = lines.split("\t")
			
			if sys.argv[2] == 'EN':             # if Penn Tree Bank codes are to be changed
				if lines[3] in dic.keys():      # if present in dic, simply modify the values as per dict
					lines[3] = lines[4] = dic[lines[3]]
				elif lines[3] not in dic.keys():        # else, we have 2 cases
					if lines[7] == "punct":             # case 1: if it's a punct
						lines[3] = lines[4] = "PUNCT"
					else:                               # case 2: unidentified symbol or parse
						lines[3] = lines[4] = "X"
				string2 = ""
				for a in range(len(lines) - 1):
					string2 += lines[a] + "\t"
				string2 += lines[-1]
				string += string2
				
			elif sys.argv[2] == 'LA':                           # if latin parse tags are to be changed
				if lines[3][0] in dic.keys():                   # if present in dic, modify as per dict
					lines[3] = lines[4] = dic[lines[3][0]]
				elif lines[3][0] not in dic.keys():             # else, check if it's the case with tag 'c' and handle accordingly
					if lines[3][0] == 'c' and lines[7] in {"advmod", "cc", "obj"}:
						lines[3] = lines[4] = 'SCONJ'
					elif lines[3][0] == 'c' and lines[7] not in {"advmod", "cc", "obj"}:
						lines[3] = lines[4] = 'CCONJ'
					else:                                       # last case is to handle any other as X or alternatively as Foreign word
						lines[3] = lines[4] = 'X'
				string2 = ""
				for a in range(len(lines) - 1):
					string2 += lines[a] + "\t"
				string2 += lines[-1]
				string += string2
				
			elif sys.argv[2] == 'CZ':                           # if czech parse tags are to be handled
				if lines[3][0] in dic.keys():                   # if present in dic, use as such
					lines[3] = lines[4] = dic[lines[3][0]]
				elif lines[3][0] not in dic.keys():
					if lines[3][0] == 'J' and lines[3][1] == ',':
						lines[3] = lines[4] = 'SCONJ'
					elif lines[3][0] == 'J' and lines[3][1] == '^':
						lines[3] = lines[4] = 'CCONJ'
					elif lines[3][0] == 'J' and lines[3][1] == '*':
						lines[3] = lines[4] = 'NUM'
					else:
						if lines[3] == '_':
							pass
						else:
							lines[3] = lines[4] = 'X'
				string2 = ""
				for a in range(len(lines) - 1):
					string2 += lines[a] + "\t"
				string2 += lines[-1]
				string += string2
				
			elif sys.argv[2] == 'TA':                           # if tamil tags are to be handled
				if lines[3][0] == 'N' and lines[3][1] == 'E':   # needs to handle NE and so need to check 2 characters first
					lines[3] = lines[4] = 'PROPN'
				elif lines[3][0] in dic.keys():                 # if present in dic, evaluate as such
					lines[3] = lines[4] = dic[lines[3][0]]
				elif lines[3][0] not in dic.keys():         # contains a compound word usually, as word 2-3 which are then decomposed into word id = 2 and 3 respectively
					if lines[3] == '_':
						pass
					else:
						lines[3] = lines[4] = 'X'
				string2 = ""
				for a in range(len(lines) - 1):
					string2 += lines[a] + "\t"
				string2 += lines[-1]
				string += string2
	print(string, file=open(sys.argv[3], "w"))
