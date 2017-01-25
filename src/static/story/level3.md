T
=====

Analyzing structured data (Part I)
--------

images/pic03.jpg

All portions of the mission have been going exactly as planned. You've got the location of the servers. Joe, the last field agent to go on a tour of the Theraptrix plant, swipes an employee access card on his way to the "restroom". Within four minutes, he's ducked inside the server room, inserted the 512 GB micro flashdrive he'd hidden in his shoe, copied the contents of one of the server disks, and returned to politely inform the employee that they must have dropped their badge on the ground at some point. It would have been ideal to access to more data, of course, but this flashdrive will have to do.

It doesn't do. Joe was lucky to have gotten out of there at all, because you must have triggered some sort of alarm. Your best guess is that the Theraptrix security system doesn't allow unauthorized USBs. Upon looking at the contents of the USB and realizing that you've gained approximately 512 GB of pure garbage, you do three things. First, you make backup copies of the only two files which appear to be of any consequence. Second, you disconnect from Sherry's free WiFi and wipe your own system. Third, you pack up your team and leave Oregon. 


All this work for two files. And not even that. The first file, entitled five_prime_colossus.pdb, now only contains a single line:

HEADER    TRANSPORT PROTEIN                       22-JUL-15   5A

The second file, ENCFF239FSU.bed, appears to contain genomic coordinates. Given that this is your only lead for the moment, you'd better find a way to connect ENCFF239FSU.bed with the pdb file you found. 

---

**Task:** Write `is_nucleic_acid`, which given a string, returns a bool indicating whether the string is a valid representation of a case insensitive [nucleic acid](https://en.wikipedia.org/wiki/Nucleic_acid_notation) sequence.

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