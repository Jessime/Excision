Decisions
=====

File parsing with a touch of statistics
-----

### Problem

 You have three files, all of which are in FASTA format.
 1. `reference.fa` contains a single sequence. This sequence is what is expected if no mutations are present in a sample.
 2. `control.fa` contains ~50 sequences of the same region of the genome as the reference sequence.
 3. `theraptrix.fa` is the file recovered yesterday. It contains another ~50 sequence from people who may have been exposed to illegally dumped waste.

 Write a program that, using these three files, calculates the p-value of the difference in mutation rates between `control.fa` and `theraptrix.fa`. Output the p-value, to 4 decimal places, to `results/1.txt`.

**Notes:**

To make things easy, you can make the following assumptions:

1. There are only single nucleotide polymorphisms (SNPs) mutations present in the dataset. And all sequences will be the same length. You can compare mutations on a nucleotide by nucleotide basis, without length normalization.

2. The error rates in both files will satisfy all of the necessary assumptions for a Student's t-test.

All of the files mentioned above can be found in the `Excision/src/static/data/1/` directory.

##### Example


Contents of `reference.fa`:

    >reference_sequence  
    CAGGTCACTT

Contents of `control.fa`:

    >c1  
    CAGGTCCCTT  
    >c2  
    CACGCCACTT  
    >c3  
    TAGGTCACTT  

Contents of `theraptrix.fa`:

    >OR1  
    CAAATCACTA  
    >OR2  
    CACGCCACTT  
    >OR3  
    CGGGTCACGT

**Execution:**

`$ ./mutations.py /path/to/reference.fa /path/to/control.fa /path/to/theraprix.fa`

**Result:**

    0.1011
Oregon Trail
=====

An introduction to arrays
-----

### Problem

Write a program that takes an empty folder location as input. This folder will have multiple subfolders, each of which have a unknown name and contain two csv files from one of your agents. Your program should collect all of these csv files, and use them to find the index and temperature of the hottest location in the Theraptrix factory. Write both the index and the average temperature (to the nearest integer) to `results/2.txt`.

There's one additional complication. Occasionally, the thermometers will fail to record a reading. If this is the case, the csv file will register a 0. In order to deal with this missing data, replace it with **76**, as an imputation of "room temperature".


**Notes:**

While you cannot know the names, or the number, of the incoming subfolders, you can assume there will be nothing in the folder besides necessary subfolders, and nothing in the subfolders besides two files, `pass1.csv` and `pass2.csv`.

##### Example


Directory structure of `/path/to/level2/`:

    /path/to/level2/
    ├── Kevin-temp-data/
        ├── pass1.csv
        ├── pass2.csv
    ├── temperatures-casey/
        ├── pass1.csv
        ├── pass2.csv

Contents of `Kevin-temp-data/pass1.csv`:

    74,59
    81,0

Contents of `Kevin-temp-data/pass2.csv`:

    79,60  
    77,71

Contents of `temperatures-casey/pass1.csv`

    0,56  
    86,67

Contents of `temperatures-casey/pass2.csv`:

    73,61
    73,72

**Execution:**

`$ ./temp_map.py /path/to/level2/`

**Result:**

    (1, 0)
    79
T
=====

Analyzing structured data (Part I)
-----

### Problem

Parse `ENCFF239FSU.bed` to find potential genomic locations of the Colossus protein. To do this, you are going to create `results3.bed`, which is a filtered version of individual lines from `ENCFF239FSU.bed`. Specifically, you are to find the five largest intervals from each chromosome, if and only if the interval is found on the positive strand.

**Notes:**

The path to the bed file is `Excision/src/static/data/3/ENCFF239FSU.bed`

##### Example


Contents of `ENCFF239FSU.bed`:


    chr1	230125030	230174106	ENST00000454058.2	0	+  
    chr1	29913143	29915337	ENST00000623731.1	0	+  
    chr1	61801712	61803634	ENST00000624542.1	0	+  
    chr1	23567063	23573122	ENST00000454863.3	0	-  
    chr1	82587312	82588411	ENST00000575085.1	0	+  
    chr1	127401725	127470569	ENST00000509671.1	0	+  
    chr3	86481942	86496996	ENST00000460586.1	0	+  
    chr1	53947623	53974950	ENST00000558866.4	0	+  

**Warning:**

While this example is space separated, the real `ENCFF239FSU.bed` file will be separated with tab characters (i.e. \t).

**Execution:**

`$ ./f.py a1`

**Result:**

    chr1  230125030  230174106  ENST00000454058.2  0  +  49076  
    chr1   29913143   29915337  ENST00000623731.1  0  +   2194  
    chr1   61801712   61803634  ENST00000624542.1  0  +   1922  
    chr1  127401725  127470569  ENST00000509671.1  0  +  68844  
    chr3   86481942   86496996  ENST00000460586.1  0  +  15054  
    chr1   53947623   53974950  ENST00000558866.4  0  +  27327
