### Parallel Data

    Contains the following tools to work with the parallel-data files:

#### Program Files
1.  <details><summary>accuracy.py</summary>

    File for testing the accuracy of a generated alignment.
    
    List of Arguments (all compulsory):  
        * `-p` or `--parallel`:	Parallel Data File  
        * `-d` or `--delimiter`:	Delimiter seperating target and source side in parallel data file  
        * `-a` or `--alignment`:	Alignment file  
        * `-at` or `--alignment_type`:	The alignment counts index from this value
    
    Usage:    ```python3 accuracy.py -p ./lit-el -d \t -a ./el_final -at 1```
    </details>

2.  <details><summary>parallel_data_accuracy.py</summary>

    File for testing the accuracy of the parallel data (sentence-level).
    
    List of Arguments (all compulsory):  
        * `--parallel`:	Compute accuracy for Parallel Data Files. Multiple files will all be calculated separately, and their scores reported.
    
    Usage:    ```python3 parallel_data_accuracy.py --parallel ./lit-el```
    </details>

#### Data Files
1. <details><summary>el_final</summary>

    Test Alignment file for `accuracy.py`
    </details>
    
2. <details><summary>lit-el</summary>

    Test Parallel Data File for `accuracy.py` and `parallel_data_accuracy.py`
    </details>