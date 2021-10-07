#!/usr/bin/env python
# coding: utf-8

import sys, re, string


if len(sys.argv) != 3:
    print("python3 {} <input_file_containing_latin_chars> <output_file_without_latin_chars>".format(sys.argv[0]))
    exit(1)


outfile = open(sys.argv[2], "w", encoding="utf-8")
with open(sys.argv[1], "r", encoding="utf-8") as infile:
    for line in infile:
        line_status= False
        for char in line:
            if char in string.ascii_letters:
                line_status= True
                break
        if not line_status:
            outfile.write(line)
outfile.close()


with open(sys.argv[1], "r", encoding="utf-8") as infile:
    print("Before cleanup: {} lines total".format(len(infile)), file=sys.stderr)
    
with open(sys.argv[2], "r", encoding="utf-8") as infile:
    print("After cleanup: {} lines remain".format(len(infile)), file=sys.stderr)



