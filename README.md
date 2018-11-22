# cross-lingual-tools

Contains the files needed for working with cross-lingual data.

## Files Included

1. <details><summary>accuracy.py</summary>

    File for testing the accuracy of a generated alignment.
    
    List of Arguments (all compulsory):  
        * `-p` or `--parallel`:	Parallel Data File  
        * `-d` or `--delimiter`:	Delimiter seperating target and source side in parallel data file  
        * `-a` or `--alignment`:	Alignment file  
        * `-at` or `--alignment_type`:	The alignment counts index from this value
    
    Usage:    ```python3 accuracy.py -p ./lit-el -d \t -a ./el_final -at 1```
    </details>

2. <details><summary>el_final</summary>

    Test Alignment file for `accuracy.py`
    </details>
    
3. <details><summary>langCodes.tsv</summary>

    TSV File containing the language codes for 134 languages, arranged in alphabetical order of their name, with their codes in 4 major standards. The columns are named as `Language` and `Standard Code` out of which the second is a CSV Value arranged as `ISO 639-1 Code, ISO 639-2 Code, ISO 639-3 Code, WALS Code`.
    
    The following notations hold in CSV values:  
    * `XXX`: List big enough to not fit here  
    * `abc [A, B, C]`: `abc` as inclusive code, along with the ones in braces  
    * `[A, B, C]`: all the codes mentioned are used, each for different dialects/variations of the language  
    * `-`: the language is not coded as per this standard  
    
    Information on WALS can be found [here](WALS).
    </details>

4. <details><summary>lit-el</summary>

    Test Parallel Data File for `accuracy.py` and `parallel_data_accuracy.py`
    </details>
   
5.  <details><summary>parallel_data_accuracy.py</summary>

    File for testing the accuracy of the parallel data (sentence-level).
    
    List of Arguments (all compulsory):  
        * `--parallel`:	Compute accuracy for Parallel Data Files. Multiple files will all be calculated separately, and their scores reported.
    
    Usage:    ```python3 parallel_data_accuracy.py --parallel ./lit-el```
    </details>
    
[WALS]: https://wals.info/
