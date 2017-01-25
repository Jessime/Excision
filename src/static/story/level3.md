T
=====

Analyzing structured data (Part I)
--------

images/pic03.jpg

Great, you've got the location of the servers.
You gain access to the folders. 
There are only two files left; you must have trigger an alarm.
five_prime_colossus.pdb (which is empty).
ENCFF239FSU.bed

---

**Task:** Write `is_nucleic_acid`, which given a string, returns a bool indicating whether the string is a valid representation of a [nucleic acid](https://en.wikipedia.org/wiki/Nucleic_acid_notation).

A1

---

**Task:** Also write `has_digit`, which given a list of strings, returns a filtered list of strings. The filtered list should only contain the strings from the original list that have at least one number in the string. 

A2

---

**Task:** `intersects` should take two lists as parameters and return a bool. The lists, `region1` and `region2`, will each contain two positive integers representing start and stop positions. The bool, then, will indicate whether the `region1` and `region2` intersect (i.e. overlap) in any capacity.

A3

---

>**Problem:**
>
> Parse `ENCFF239FSU.bed` to find potential genomic locations of the Colossus protein. To do this, you are going to create `results3.bed`, which is a filtered version of specific lines from `ENCFF239FSU.bed`. Specifically, you are to find the five largest intervals from each chromosome, if and only if the interval is found on the positive strand. 
>
>**Notes:**
>
> The path to the bed file is `static/data/ENCFF239FSU.bed`
>
>**Example:**
>
>
>Contents of `f.txt`:
>
>>chr1	230125030	230174106	ENST00000454058.2	0	+  
>>chr1	29913143	29915337	ENST00000623731.1	0	+  
>>chr1	61801712	61803634	ENST00000624542.1	0	+  
>>chr1	23567063	23573122	ENST00000454863.3	0	-  
>>chr1	82587312	82588411	ENST00000575085.1	0	+  
>>chr1	127401725	127470569	ENST00000509671.1	0	+  
>>chr3	86481942	86496996	ENST00000460586.1	0	+  
>>chr1	53947623	53974950	ENST00000558866.4	0	+  
>
> **Warning:** While this example is space separated, the real `ENCFF239FSU.bed` file will be separated with tab characters (i.e. \t). 
>
>**Execution:**
>
>`$ ./f.py a1`
>
>**Result:**
>
>> chr1  230125030  230174106  ENST00000454058.2  0  +  49076  
>> chr1   29913143   29915337  ENST00000623731.1  0  +   2194  
>> chr1   61801712   61803634  ENST00000624542.1  0  +   1922  
>> chr1  127401725  127470569  ENST00000509671.1  0  +  68844  
>> chr3   86481942   86496996  ENST00000460586.1  0  +  15054  
>> chr1   53947623   53974950  ENST00000558866.4  0  +  27327