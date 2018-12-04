#!/usr/bin/env python3

import argparse
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument('-i', "--input", type=str, help="Input file containing the WALS data, in a tsv format", required=True)
subparsers = parser.add_subparsers(dest="mode")
group1 = subparsers.add_parser("similar", help="Returns the WALS Code of languages with their similarity scores")
group1.add_argument('-c', "--code", type=str, help="Input wals code", required=True)
group1.add_argument('-n', "--number", type=int, help="Number of similar languages to show", required=True)
group2 = subparsers.add_parser('centroid', help="Return the WALS Code of centroid language as per given input genus")
group2.add_argument('-g', '--genus', type=str, help="Input genus for searching the centroid language", required=True)
group3 = subparsers.add_parser('dissimilar', help="Return the WALS Code of most dissimilar languages as per given input genus")
group3.add_argument('-g', '--genus', type=str, help="Input genus for searching the most dissimilar language", required=True)
group3.add_argument('-n', "--number", type=int, help="Number of dissimilar languages to show")
args = parser.parse_args()


def find_orig(param1, name):
    for i in range(1, len(contents)):
        line = contents[i].split("\t")
        if param1 == "wals_code":
            if line[0] == name:
                return i
        elif param1 == "genus":
            if line[6] == name:
                return i
    print("WALS CODE NOT FOUND!")
    exit(0)


def calc_sim(src, sink):
    if sink == src:
        return
    sink_tab = sink.split("\t")
    source_tab = src.split("\t")
    return calc_sim2(source_tab, sink_tab)


def calc_sim2(src, sink):
    features = 0
    total = 0
    
    # genus
    if src[6] != "" and sink[6] != "":
        total += 0.5
        if src[6] == sink[6]:
            features += 0.5
            
    # family
    if src[7] != "" and sink[7] != "":
        total += 0.5
        if src[7] == sink[7]:
            features += 0.5
    
    # Other features
    for i in range(10, len(src)):
        total += 1
        if src[i] != "" and sink[i] != "":
            if src[i] == sink[i]:
                features += 1
    
    return features / total


def get_all_field(fieldname, field_value):
    op = []
    fields = contents[0].split('\t')
    param = 0
    for j in range(len(fields)):
        if fields[j] == fieldname:
            param = j
    for i in range(1, len(contents)):
        line = contents[i].split("\t")
        if line[param] == field_value:
            op.append(line)
    if len(op) != 0:
        return op
    else:
        print("No such " + fieldname + "found")
        exit(0)


def calc_overall(simi):
    sim2 = defaultdict(float)
    for i in simi:
        total = 0
        for j in simi[i]:
            total += simi[i][j]
        sim2[i] = total/len(simi[i])
    return sim2


if __name__ == '__main__':

    with open(args.input, "r") as file:
        global contents
        contents = file.readlines()

        if args.mode == "similar":
            source = find_orig("wals_code", args.code)
            sim = defaultdict(float)
            for i in range(1, len(contents)):
                if source != i:
                    sim[contents[i].split("\t")[0]] = calc_sim(contents[source], contents[i])
            print("Top " + str(args.number) + " most similiar languages-\n\n"
                  "Wals_Code\tSimilarity Score")
            for k1,v1 in sorted(sim.items(), key=lambda k_v: k_v[1], reverse=True)[0:args.number]:
                print(k1, v1, sep="\t")
            exit(0)

        elif args.mode == "centroid":
            new_content = get_all_field("genus", args.genus)
            sim = defaultdict(lambda: defaultdict(float))
            for source in range(0, len(new_content)):
                for i in range(0, len(new_content)):
                    if source != i:
                        sim[new_content[source][0]][new_content[i][0]] = calc_sim2(new_content[source], new_content[i])
            sim2 = calc_overall(sim)
            print("Centroid language (with similarity factor on new line)-")
            for k1 in sorted(sim2.items(), key=lambda k_v: k_v[1], reverse=True)[0]:
                print(k1)
            exit(0)

        elif args.mode == "dissimilar":
            new_content = get_all_field("genus", args.genus)
            sim = defaultdict(lambda: defaultdict(float))
            for source in range(0, len(new_content)):
                for i in range(0, len(new_content)):
                    if source != i:
                        sim[new_content[source][0]][new_content[i][0]] = calc_sim2(new_content[source], new_content[i])
            sim2 = calc_overall(sim)
            print("Most dissimilar languages -\n\n"
                  "WALS Code\tSimilarity Score (with other languages)")
            for k1,v1 in sorted(sim2.items(), key=lambda k_v: k_v[1])[:args.number]:
                print(k1, v1, sep="\t")
            exit(0)
            
        else:
            parser.print_usage()
