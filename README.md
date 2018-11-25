# cross-lingual-tools

Contains the files needed for working with cross-lingual data, all developed in-house. The following are the folders present in the directory. Click on the link to see the contents of the folder.

1. [Root Directory](#Root-Directory)

    Files not included in any project, but can be used all by themselves as stand-only files.

2. [Parallel Data](parallel_data/README.md)

    Tools that can be used to check the accuracy of alignments, quality of parallel data.

3. [Tagset Converter](tagset_converter/README.md)

    Convert [PDT](http://ufal.mff.cuni.cz/pdt/Morphology_and_Tagging/Doc/hmptagqr.html), [Penn Treebank](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html), [Perseus](https://github.com/PerseusDL/treebank_data/blob/master/v2.1/Latin/TAGSET.txt) and PDT based [PDT-based Tamil](http://ufal.mff.cuni.cz/~ramasamy/tamiltb/0.1/morph_annotation.html#2.4.Positional_Tagset_for_Tamil) tagsets into [UD](http://universaldependencies.org/u/pos/all.html) tagset. 

### Root Directory

1. <details><summary>langCodes.tsv</summary>

    TSV File containing the language codes for 134 languages, arranged in alphabetical order of their name, with their codes in 4 major standards. The columns are named as `Language` and `Standard Code` out of which the second is a CSV Value arranged as `ISO 639-1 Code, ISO 639-2 Code, ISO 639-3 Code, WALS Code`.
    
    The following notations hold in CSV values:  
    
    |Notation|Implication|
    |:------:|:----------|
    | `XXX` | List big enough to not fit here |
    | `abc [A, B, C]` | `abc` as inclusive code, along with the ones in braces |
    | `[A, B, C]` | all the codes mentioned are used, each for different dialects/variations of the language|
    | `-` | the language is not coded as per this standard|
    
    Information on WALS can be found [here](WALS).
    </details>
    
2.  <details><summary>wals.py</summary>

    Python3 File to  
    
    - Find the most similar languages to given language.
    - Find the centroid language of a given genus, i.e.  a language most similar to other languages of the genus.
    - Find languages that are most dissimilar to any other language in the given genus.

    List of Arguments (all compulsory):
    
    * `-i` or `--input`:	Input file containing the WALS data in a tsv-format  


    List of Positional Arguments, and the sub-arguments (Mutually-exclusive):
    
    * `similarity`: Display the WALS code and similarity scores for most similar languages to given input language's WALS code.

        |Sub-Arguments|Function|
        |:------------|:-------|
        |`-c` or `--code`|	Input WALS code for the source language |
        |`-n` or `--number`| Number of languages to be displayed in the output|  


    * `centroid`:   Display the WALS code and similarity scores for the centroid language of an input genus, i.e.  a language most similar to other languages of the genus.

        |Sub-Arguments|Function|
        |:------------|:-------|
        |`-g` or `--genus`|	Input genus to find the centroid for|  
    

    * `dissimilarity`: Display the WALS Code and similarity scores of the languages that are most dissimilar to any other language in the given genus.
    
        |Sub-Arguments|Function|
        |:------------|:-------|
        |`-g` or `--genus`|	Input genus to find the centroid for|
        |`-n` or `--number`| Number of languages to be displayed in the output|  


        The input file for the task can be downloaded from [here](https://wals.info/languoid).
    
    Usage:

    - ```python3 wals.py -i input_file similar -c <wals_code> -n <output_count>```
    - ```python3 wals.py -i input_file centroid -g <genus_name>```
    - ```python3 wals.py -i input_file dissimilar -g <genus_name> -n <output_count>```
