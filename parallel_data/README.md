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

3.  <details><summary>klcpos3.py</summary>

	File for calculating klcpos3 measure of source and target treebanks for single-source and multi-source-weighted delexicalised parsing.

	List of Arguments (all compulsory):
		* `--source`: The source file(s) that are to be used for the parsing task, in CONLLU format
		* `--target`: The target file that is to be used for the parsing task, in CONLLU format
		* One of the two:
			* `--single_source`: List the source files in the decreasing order of the klcpos3 similarity measure.
			* `--multi_source`: List the source files in the decreasing order of the klcpos3<sup>-4</sup> measure. The output values are not normalised.

	Usage:	```python3 klcpos3.py --source <sourcefiles> --target <targetfile> --single_source/--multi_source```
	</details>
	
#### Data Files
1. <details><summary>el_final</summary>

    Test Alignment file for `accuracy.py`
    </details>
    
2. <details><summary>lit-el</summary>

    Test Parallel Data File for `accuracy.py` and `parallel_data_accuracy.py`
    </details>