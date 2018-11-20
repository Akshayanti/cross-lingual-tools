# cross-lingual-tools

Contains the files needed for working with cross-lingual data.

## Files Included
1. <b>accuracy.py</b>:	File for testing the accuracy of a generated alignment. Run as:  
	```python3 accuracy.py -p ./lit-el -d \t -a ./el_final -at 1```  
	
	List of Arguments (all compulsory):  
	`-p` or `--parallel`:	Parallel Data File  
	`-d` or `--delimiter`:	Delimiter seperating target and source side in parallel data file  
	`-a` or `--alignment`:	Alignment file  
	`-at` or `--alignment_type`:	The alignment counts index from this value

2. <b>el_final</b>:	Test Alignment file for `accuracy.py`

3. <b>lit-el</b>:	Test Parallel Data File for `accuracy.py` and `parallel_data_accuracy.py`

4. <b>parallel_data_accuracy.py</b>:	File for testing the accuracy of the parallel data (sentence-level). Run as:
	```python3 parallel_data_accuracy.py --parallel ./lit-el```  
	
	List of Arguments (all compulsory):  
	`--parallel`:	Compute accuracy for Parallel Data Files. Multiple files will all be calculated separately, and their scores reported.
