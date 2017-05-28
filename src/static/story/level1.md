Decisions
=====

File parsing with a touch of statistics
--------

images/banner.jpg

It's Sunday evening, and you're sitting in your house staring at your computer. You can't figure out what to do. You've got work in the morning, so you really shouldn't stay up much later. But you feel like if you just sit quietly for a little bit longer you might get the inspiration you've been looking for. It should be so simple; all you have to do is put yourself in their shoes. What would you need if you were in their position? But the words on the screen are doing nothing to make you think like them. Maybe if you were just a little more…what's the word? Sociopathic.

Despite having a thousand things on your plate, you haven’t had a productive weekend. Sure, you have taken care of a few technical details, getting some operational systems up and running, but you have bigger fish to fry. It can be difficult generating momentum for a large undertaking like this, true, but that really isn't a good enough excuse when you have people depending on you. On Monday, how are you going to explain to your team that they'll be waiting even longer for their assignments because your constant indecision forced you to marathon two seasons of House of Cards this weekend instead of doing your job? It isn't acceptable. You take a deep breath and mentally gear up to go over the facts one more time.

The past year of your life has catapulted you from a Novice at the Academy to the Director of the Agency, making you far and away the youngest director in the storied history of the institution. The circumstances which led to your rise were decidedly unpleasant and have left you with a laundry list of equally unpleasant tasks to resolve. Namely, the Agency, with all of its resources, has found itself pitted against Gene Corporation, which is one of the largest business conglomerates on the planet. Gene Corp has a wonderful public image; it’s known for quite literally ”healing the sick and curing the blind”. While the technologies they have created have revolutionized several aspects of life, you've seen their dark underbelly first hand. Just last week your team found some decently solid evidence that one of Gene Corp's subsidiaries, Theraptrix, has been bribing environmental officers in Oregon for years. They have been using the freedom they bought to pump waste chemicals directly into the air instead of following waste treatment and filtering protocol.

Bribery and industrial waste may seem commonplace when dealing with large corporations, but there's also evidence that Life/Better, LLC (another child company of Gene Corp) has been illegally testing neurotropic drugs on pregnant women. Oh, and there was the incident when Gene Corp used an artificial intelligence system to assassinate your mentor and attempted to take over the world. Besides Theraptrix and Life/Better, LLC, Gene Corp has another 47 companies under its name.

The problem is that this corporate giant is geared up and ready for a fight. You don't have the resources to take it down all at once. Your only option is to divide and conquer, taking out the subsidiaries one at a time. But where should you strike first? That question is at the heart of your indecision. Where is Gene Corp investing most of their defenses? What do they expect you to do? You know that if you lose this initial battle your chances of winning the war decrease dramatically. You currently have the best cases against Theraptrix and Life/Better, LLC, but at which of the two should you direct your energies?

With a sigh, you decide to let the numbers make the choice. Yesterday, your team recovered a DNA sequencing data set collected by Theraptrix from a sample population of people near their main factory. The informant who aided you in acquiring the data says that Theraptrix suspects they may be causing genetic mutations in Oregon residents. If, on top of the bribery, you can demonstrate a statistically significant difference between mutation rates of people in the Oregon data and in a control population, you'll concentrate your investigation on Theraptrix. Otherwise, you'll go after Life/Better, LLC.

---

### Problem

 You have three files, all of which are in FASTA format.
 1. `reference.fa` contains a single sequence. This sequence is what is expected if no mutations are present in a sample.
 2. `control.fa` contains ~50 sequences of the same region of the genome as the reference sequence.
 3. `theraptrix.fa` is the file recovered yesterday. It contains another ~50 sequences from people who may have been exposed to illegally dumped waste.

 Write a program that, using these three files, calculates the p-value of the difference in mutation rates between `control.fa` and `theraptrix.fa`. Output the p-value, rounded to 4 decimal places, to `results/1.txt`.

**Note(s):**

To make things straightforward, you can make the following assumptions:

1. There are only single nucleotide polymorphism mutations (SNPs) present in the dataset. Also, all sequences will be the same length. Therefore, you can compare mutations on a nucleotide-by-nucleotide basis without length normalization.

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

    0.1012

---

### Task

Make a function called `make_lookup`. `make_lookup` should take two lists `names` and `seqs` as parameters, and return a dictionary where each element of `names` is a key and each element of `seqs` is a corresponding value.

Here's a small example:

`names = ['seq1', 'seq2']`

`seqs = ['AGTC', 'AAAA']`

The dictionary that should be returned by `make_lookup` would look like this:

`lookup = {'seq1':'AGTC', 'seq2':'AAAA'}`

#### Hint

You don't need a dictionary for this problem. Instead, this task's goal is to make sure you understand the built-in [`zip`](https://docs.python.org/3.6/library/functions.html#zip) function. Here's a nice [example](http://stackoverflow.com/questions/13704860/zip-lists-in-python/13704903#13704903) of how `zip` works.

Bonus hint! Here's some documentation on how to do a [t-test](https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.stats.ttest_ind.html#scipy.stats.ttest_ind) in Python.

---

### Task

Write a function `headers`, which takes the contents of a FASTA file as a string and returns a list of all of the sequence headers in the file, without the initial '>' included.

As a side note, it's fine if you want to write `headers` in the same file as `evens_mean`. Or you can have it in its own file. Whatever makes you feel more organized.

#### Hint

There are many ways to measure how similar or different two strings are. The way described in the problem is known as [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance). You need to find the hamming distances between the samples and the reference.

---

### Task

Create a new .py file that contains a single function. Call that function `evens_mean`. `evens_mean` should accept a single parameter. You can call the parameter anything you want, but `num_list` is a decent choice, since the parameter will be a list of numbers (floats, ints, or both). `evens_mean` should iterate over `num_list` and calculate the mean of all the even elements. `evens_mean` should then return the calculated mean value.

#### Hint

There are a couple 'best practices' in python that will make your code easier to write and reason about:

1. List comprehensions are a cleaner way to write for loops. [This tutorial](http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/) uses colors to explain the relationship between the two structures.
2. Use the `with` statement to open and read files. [This example](https://docs.quantifiedcode.com/python-anti-patterns/maintainability/not_using_with_to_open_files.html) shows what you're *not* supposed to do, and then how to correct it.
