# cross-lingual-tools

Contains the files needed for working with cross-lingual data.

## Files Included

1. <b>accuracy.py</b>

    File for testing the accuracy of a generated alignment.
    
    List of Arguments (all compulsory):  
        * `-p` or `--parallel`:	Parallel Data File  
        * `-d` or `--delimiter`:	Delimiter seperating target and source side in parallel data file  
        * `-a` or `--alignment`:	Alignment file  
        * `-at` or `--alignment_type`:	The alignment counts index from this value
    
    Usage:    ```python3 accuracy.py -p ./lit-el -d \t -a ./el_final -at 1```
    
2. <b>el_final</b>

    Test Alignment file for `accuracy.py`

3. <b>lit-el</b>

    Test Parallel Data File for `accuracy.py` and `parallel_data_accuracy.py`

4. <b>parallel_data_accuracy.py</b>

    File for testing the accuracy of the parallel data (sentence-level).
    
    List of Arguments (all compulsory):  
        * `--parallel`:	Compute accuracy for Parallel Data Files. Multiple files will all be calculated separately, and their scores reported.
    
    Usage:    ```python3 parallel_data_accuracy.py --parallel ./lit-el```
    
5. <b>langCodes.tsv</b>

    TSV File containing the language codes for 134 languages, arranged in alphabetical order of their name, with their codes in following formats:  
        * [WALS](WALS)  
        * ISO 639-1  
        * ISO 639-2  
        * ISO 639-3  

    The column headers are:  
        * Language Name  
        * Standard Code
    
    The column `Standard Code` has following properties:  
        * It is a CSV list  
        * The CSV values are arranged as follows:  
          * ISO 639-1 Code  
          * ISO 639-2 Code  
          * ISO 639-3 Code  
          * WALS Code  
        * The following notations hold in CSV values:  
          * `XXX`: List big enough to not fit here  
          * `abc [A, B, C]`: `abc` as inclusive code, along with the ones in braces  
          * `[A, B, C]`: all the codes mentioned are used, each for different dialects/variations of the language  
          * `-`: the language is not coded as per this standard
    
[WALS]: https://wals.info/