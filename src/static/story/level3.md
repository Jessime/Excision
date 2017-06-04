COLOSSUS
=====

analyzing structured data (part I)
--------

images/level3.jpg

All aspects of the mission were going exactly as planned. What went wrong?

You'd learned the location of the servers. Joe, the last field agent to go on a tour of the Theraptrix plant, had stolen an employee access card on his way to the 'restroom'. Within minutes, he'd ducked inside the server room, inserted a flash drive he'd hidden in his shoe, and copied the contents of one of the server disks. While returning to the tour, he'd 'informed' the employee that they must have dropped their badge on the ground at some point. It would have been ideal to access to more data, of course, but the flash drive should have been enough.

It wasn't. Joe was lucky to have gotten out of there at all, because he must have triggered an alarm. Your security team's best guess is that the Theraptrix security system doesn't allow unauthorized USBs. Upon looking at the contents of the USB and realizing that you've gained approximately 512 GB of what appears to be corrupted files, you do three things. First, you make backup copies of the only two files which appear to be of any consequence. Second, you disconnect from Sherry's free Wi-Fi and wipe your own system. Some of those seemingly corrupted files were likely spyware. Third, you pack up your team and leave Oregon.


All this work for two files. And not even that. The first file, entitled five_prime_colossus.pdb, now only contains a single line:

HEADER    TRANSPORT PROTEIN                       22-JUL-15   5A

The second file, ENCFF239FSU.bed, appears to contain genomic coordinates. Given that this is your only lead for the moment, you'd better find a way to connect ENCFF239FSU.bed with the .pdb file you found.

---

### Problem

Parse `ENCFF239FSU.bed` to find potential genomic locations of the Colossus protein. To do this, you are going to filter individual lines from `ENCFF239FSU.bed`. Specifically, you are to find the five largest intervals located on the positive strand of each chromosome.

To validate that you have selected the proper rows, calculate the total length of all intervals you have selected. Write this integer to `results/3.txt`.

**Note(s):**

* The path to the .bed file is `Excision/src/static/data/3/ENCFF239FSU.bed`. This script does not need to accept any arguments.
* [Here's a link](https://genome.ucsc.edu/FAQ/FAQformat.html#format1) to a description of the .bed format.

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

While this example is space-separated, the real `ENCFF239FSU.bed` file will be separated with tab characters (i.e., \t).

**Execution:**

`$ ./longest_per_chr.py`

**Result:**

    171575

---

### Task

Write `is_nucleic_acid`, which, given a string, returns a bool indicating whether the string is a valid representation of a case-insensitive [nucleic acid](https://en.wikipedia.org/wiki/Nucleic_acid_notation) sequence.

#### Hint

There are many ways to go about calculating the answer to this problem, and in a fairly straightforward case like this, one isn't necessarily better than another. So, it's difficult to say, "You should use this function for this problem".

In general, data science occupies a unique subset of the programming realm. A majority of programmers are software developers. They write code that is going to be used on a website that will get tens of thousands of views a day, or in an app that's being built by a team of a dozen people, or will be used in a device that will literally put lives at stake if a bug occurs. Over the last few decades, software developers have created many bests practices concerning how to write high quality code. And there are many online resources that will say, "This is the _right_ way to do this."

Biologists are in a very different scenario. They will write code that may very likely only be run once, ever. They may never need to work on a code base with millions of lines, or even work with another person on the same script. Fundamentally, biologists are using programming simply as a means to an end. It's a tool to let them address a biological question of interest. This is a very different goal than that of a software developer, who's code is their product and livelihood.

That said, I urge you to learn and use as many of these best practices as possible. There are reasons that they exist, and they may be beneficial in the long run, even if they don't seem necessary in the present. A simple example is documenting your code. It's easy to say to yourself, "I only need this once, and I'm too rushed to document this code right now." But when you come back to the code a year from now because you're trying to write a manuscript, you are absolutely going to want documentation to exist.

Another example is knowing about and using already existing libraries. You benefit no one (with the small exception of yourself if it happens to be a learning opportunity) by rewriting something that already exists in Python's standard library or as a package you can get with `pip`. As a small aside, a module that I used to solve this level's problem was the [collections module](https://docs.python.org/3.6/library/collections.html#module-collections).  

It is equally important, however, not to obsess over *the right way*. Do not let perfection be the enemy of good. Does it matter if your code is running in polynomial time and taking twice as much memory as it should? It almost certainly couldn't matter less. And, if it does matter in the future, you'll know it. If, a month from when you wrote your original polynomial-time script, you realize you want to put it in a for loop and run it a million times, then it becomes appropriate to rewrite the algorithm in linear time. But it almost certainly is not appropriate to rewrite a working script just in case you need to run it a million time at some indeterminate time in the far future.

---

### Task

Write `has_digit`, which, given a list of strings, returns a filtered list of strings. The filtered list should only contain the strings from the original list that have at least one number in the string.

#### Hint

H2

---

### Task

`intersects` should take two lists as parameters and return a bool. The lists, `region1` and `region2`, will each contain only two positive integers representing start and stop positions. The bool should indicate whether the intervals between the integer pairs in `region1` and `region2` intersect (i.e., overlap) in any capacity.

#### Hint

Even though the prompt implies that you want to keep track of certain rows, it isn't necessary to solve this problem. The task is simplified by only storing the proper intervals.  
