### Tagset Converter

Converts the following tagsets into the [UD](http://universaldependencies.org/u/pos/all.html) tagset:

    - [PDT](http://ufal.mff.cuni.cz/pdt/Morphology_and_Tagging/Doc/hmptagqr.html)
    - [Penn Treebank](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html)
    - [Perseus](https://github.com/PerseusDL/treebank_data/blob/master/v2.1/Latin/TAGSET.txt) 
    - [PDT-based Tamil tagset](http://ufal.mff.cuni.cz/~ramasamy/tamiltb/0.1/morph_annotation.html#2.4.Positional_Tagset_for_Tamil)

#### Program Files

1. converter.py

    Python3 File to convert source tagset to the target tagset.

    Usage:  `python3 converter.py input_data_file source_input_file_language target_output_file`

    Possible values for source_input_file_language:

    - `CZ`: Czech
    - `EN`: English
    - `LA`: Latin
    - `TA`: Tamil

    Note: The `input_data_file` should be in [CONLL-U format](http://universaldependencies.org/format.html).

#### Data Files

1. <details><summary>*orig.conllu</summary>

    Files from dev set of [UD Treebanks](http://universaldependencies.org/) tagged according to the source tagsets.
    
    Files Included:

    - cs-ud-dev-orig.conllu
    - la-ud-dev-orig.conllu
    - en-ud-dev-orig.conllu
    - ta-ud-dev-orig.conllu
    </details>

2. <details><summary>*created.conllu</summary>

    Files after conversion to UD Tagset.
    
    Files Included:

    - tagset_converter/cs-ud-created.conllu
    - tagset_converter/la-ud-created.conllu
    - tagset_converter/en-ud-created.conllu
    - tagset_converter/ta-ud-created.conllu
    </details>
    
#### Statistics

All the accuracies (UAS, LAS) were reported by running the data over [UDPipe](http://ufal.mff.cuni.cz/udpipe).

Tested Sample Results:

|Language Code (with tagset)| UAS, LAS <sup>* </sup> | UAS, LAS <sup>+ </sup>|
|:-------------------------:|:----------------------:|:--------------------:|
|CS (PDT) | 5.13, 0.43 | 60.00, 49.88 |
|EN (Penn) | 15.21, 04.37 | 58.88, 50.16 |
|LA (Perseus) | 14.51, 5.12 | 45.10, 29.07 |
|TA (Tamil) | 17.26, 8.47 | 51.07, 42.20 |

<sup>* </sup>: Before tagset conversion  
<sup>+ </sup>: After tagset conversion

#### Future Work

- Compare and test the harmonisation with Interset
- Try and resolve inconsistencies with LAS<sup>+ </sup> scores