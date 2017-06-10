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

Parse `ENCFF239FSU.bed` to find potential genomic locations of the Colossus protein. To do this, you are going to filter individual lines from `ENCFF239FSU.bed`. Specifically, you should find the five largest intervals located on the positive strand of each chromosome.

To validate that you have selected the proper lines, calculate the sum of the original indices (line numbers) of all lines you have selected. Write this integer to `results/3.txt`.

**Note(s):**

* The path to the .bed file is `Excision/src/static/data/3/ENCFF239FSU.bed`. This script does not need to accept any arguments.
* [Here's a link](https://genome.ucsc.edu/FAQ/FAQformat.html#format1) to a description of the .bed format.
* Don't forget to use a 0-based index for the line numbers.

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
    chr3	61801712	61803634	ENST00000465586.1	0	+
    chr3	87881990	87883995	ENST00000466786.1	0	+
    chr3	91488742	91876543	ENST00000460876.1	0	+
    chr3	94876501	94888501	ENST00000460599.2	0	+

**Warning:**

While this example is space-separated, the real `ENCFF239FSU.bed` file will be separated with tab characters (i.e., \t).

**Execution:**

`$ ./longest_per_chr.py`

**Result:**

    59

---

### Task

Write `is_nucleic_acid`, which, given a string, returns a bool indicating whether the string is a valid representation of a case-insensitive [nucleic acid](https://en.wikipedia.org/wiki/Nucleic_acid_notation) sequence.

#### Hint

There are many ways to go about calculating the answer to this problem, and, in a fairly straightforward case like this, one method isn't necessarily better than another. Therefore, it's difficult to say, "You should use this function for this problem."

In general, data science occupies a unique subset of the programming realm. The majority of programmers are software developers. They write code that is going to be used on a website that will get thousands of views a day, in an app being built by a team of a dozen people, or in a device that will literally endanger lives if a bug occurs. Over the last few decades, software developers have created many best practices for writing high-quality code. There are many online resources that will say, "This is the _right_ way to do this."

Biologists are in a very different situation. They will write code that may only be run once, ever. They may never need to work on a code base with millions of lines or even work with another person on the same script. Essentially, biologists are using programming simply as a means to an end. It's a tool to let them address a biological question of interest. This is a very different goal from that of software developers, whose code is their product and livelihood.

That said, I urge you to learn and use as many of these best practices as possible. There are reasons that they exist, and they may be beneficial in the long run, even if they don't seem necessary in the present. A simple example is documenting your code. It's easy to say to yourself, "I only need this once, and I'm too rushed to comment this code right now." But when you come back to the code a year from now because you're trying to write a manuscript, you are absolutely going to want documentation to exist.

Another example is knowing about and using already existing libraries. You benefit no one (with the possible exception of yourself if there happens to be a learning opportunity) by rewriting something that already exists in Python's standard library or as a package you can get with `pip`. As a small aside, a module that I used to solve this level's problem was the [collections module](https://docs.python.org/3.6/library/collections.html#module-collections).  

It is equally important, however, not to obsess over *the right way*. Do not let perfection be the enemy of good. Does it matter if your code is running in polynomial time and taking twice as much memory as it should? It almost certainly couldn't matter less. If it does matter later, you'll know it later. A month from when you wrote your original polynomial-time script, you may realize you want to put it in a for loop and run it a million times. THEN, it becomes appropriate to rewrite the algorithm in linear time. It almost certainly is NOT appropriate to rewrite a working script *just in case* you need the speed at some indeterminate time.

---

### Task

Write `has_digit`, which, given a list of strings, returns a filtered list of strings. The filtered list should only contain the strings from the original list that have at least one number in the string.

#### Hint

A good way to increase your programming efficiency, especially long-term, is to figure out how to write a function. Or, more specifically, how to write a good function. If you're not comfortable with the technical details of function definitions, they are covered extensively in the [Python documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions).

But even if you know *how* to write a function, when should you? How much should go in a single function? At what point are you making your function definitions too small? These are difficult questions and have been asked [many](https://softwareengineering.stackexchange.com/questions/133404/what-is-the-ideal-length-of-a-method-for-you), [many](https://stackoverflow.com/questions/1170215/how-long-should-functions-methods-should-be-in-average), [many](https://stackoverflow.com/questions/475675/when-is-a-function-too-long) times. Even people who have been programming for decades vary in their suggestions.

My personal approach is to think of a function as a paragraph, and each of the lines as a sentence. The name of the function acts almost as a topic sentence. The paragraph should be about one and only one thing. Just like in writing, that means that some functions are short, and some are long. It depends on how many sentences/lines it takes to convey your message.

The [requests](https://github.com/requests/requests) package is one of the most popular Python modules out there. It's often cited as the first module a beginner programmer should read to understand "Pythonic code". If you browse around, you can see that the function lengths differ. The [api.py file](https://github.com/requests/requests/blob/master/requests/api.py) has no functions that are more than two lines long. But the [build_digest_headers](https://github.com/requests/requests/blob/master/requests/auth.py#L127) function is more than a page. A majority of functions are in between these lengths, and are a [handful of lines](https://github.com/requests/requests/blob/master/requests/models.py#L939).

Again, you should write functions that do a single thing. When you come back to the function in three weeks, you'll have a pretty good idea what it does by the function name. And in six weeks, when you need it for another part of your project, you can just import it instead of rewriting.

---

### Task

`intersects` should take two lists as parameters and return a bool. The lists, `region1` and `region2`, will each contain only two positive integers representing start and stop positions. The bool should indicate whether the intervals between the integer pairs in `region1` and `region2` intersect (i.e., overlap) in any capacity.

#### Hint

One of the most important choices you have to make in this problem is what data structure to use. In other words, how do you store the information as you go along? One option is to use:

    dict(str : list(tuple(int, int)))

This hint isn't going to reveal exactly what information should be stored where, but here's an example piece of data to clarify the notation used above.

    my_data = {'key1': [(12, 2), (90, 99)],
               'key2': [(8, 16), (55, 55)]
              }
