Decisions
=====

File parsing with a touch of statistics
--------

images/pic03.jpg

It's Sunday evening and you're sitting in your house staring at the computer. You can't figure out what to do. You've got work in the morning, so you really shouldn't stay up much later. But you feel like if you just sit quietly for a little bit longer you might get the inspiration you've been looking for. It should be so simple; all you have to do is put yourself in their shoes. What would you need if you were in their position? But the words on the screen are doing nothing to make you think like them. Maybe if you were just a little more… what's the word? Sociopathic.

Despite having a thousand things on your plate, the weekend hasn't been productive as a whole. Sure, you have taken care of a few technical details, getting some operational systems up and running, but you have bigger fish to fry. It can be difficult ramping up a large undertaking like this, true, but that really isn't a good enough excuse when you have people depending on you. Come Monday, how are you going to explain to your team that they'll be waiting even longer for their assignments because your constant indecision forced you to marathon two seasons of House of Cards this weekend instead of doing your job? It isn't acceptable. You take a deep breath and mentally gear up to go over the facts one more time.

The past year of your life has catapulted you from a Novice at the Academy to the head director of the Agency, making you far and away the youngest director in the storied history of the institution. The circumstances which lead to your rise were decidedly unpleasant and have left you with a laundry list of equally unpleasant tasks to resolve. Namely, the full weight of the Agency has found itself pitted against Gene Corporation, which is currently one of the largest organizations on the planet. Gene Corp has a wonderful public image known for quite literally ‘healing the sick and curing the blind'. While the technologies they have created have revolutionized several areas of life, you've seen their dark underbelly first hand. Just last week your team found some decently solid evidence that one of Gene Corp's subsidiaries, Theraptrix has been bribing the environmental officers in Oregon for years. They have been using the freedom they bought to pump waste chemicals directly into the air instead of following waste treatment and filtering protocol.

Bribery and industrial waste may or may not seem like fact-of-life issues when dealing with large corporations, but there's also the evidence that Life/Better, LLC (another child company of Gene Corp) has been illegally testing neurotropic drugs on pregnant women. Oh, and there was the incident when Gene Corp used an artificial intelligence system system to assassinate your mentor and attempted to take over the world. Besides Theraptrix and Life/Better, LLC, Gene Corp has another 47 companies under its name.

The problem is that this giant is in full armor and ready for a fight. You don't have the resources to take it down all at once. Your only option is to divide and conquer, taking out the subsidiaries one at a time. But where should you strike first? That question is the heart of your indecision. Where is Gene Corp investing most of their defenses? What do they expect you to do? You know that if you lose this initial battle, your chances of winning the war decrease dramatically. You currently have the best cases against Theraptrix and Life/Better, LLC, but at which of the two should you direct your focus?

With a sigh, you decide to let the numbers make the choice. Yesterday, your team recovered a DNA sequencing data set performed by Theraptrix on a sample population of people near their main factory. The informant who aided you in acquiring the data says that Theraptrix suspects they may be causing genetic mutations in Oregon residents. If, on top of the bribery, you can prove a statistically significant difference between mutation rates of people in the Oregon data and a control population, you'll concentrate your investigation on Theraptrix. Otherwise, you'll go after Life/Better, LLC.

---

### Problem

 You have three files, all of which are in FASTA format.
 1. `data/1/reference.fa` contains a single sequence. This sequence is what is expected if no mutations are present in a sample.
 2. `data/1/control.fa` contains ~50 sequences of the same region of the genome as the reference sequence.
 3. `data/1/theraptrix.fa` is the file recovered yesterday. It contains another ~50 sequence from people who may have been exposed to illegally dumped waste.

 Write a program that, using these three files, calculates the p-value of the difference in mutation rates between `control.fa` and `theraptrix.fa`. Output the p-value, to 4 decimal places, to `results/1.txt`.

**Notes:**

To make things easy, you can make the following assumptions:

1. There are only single nucleotide polymorphisms (SNPs) mutations present in the dataset. And all sequences will be the same length. You can compare mutations on a nucleotide by nucleotide basis, without length normalization.

2. The error rates in both files will satisfy all of the necessary assumptions for a Student's t-test.

##### Example


Contents of `reference.fa`:

```
\>reference_sequence  
CAGGTCACTT
```

Contents of `control.fa`:

```
\>c1  
CAGGTCCCTT  
\>c2  
CACGCCACTT  
\>c3  
TAGGTCACTT  
```

Contents of `theraptrix.fa`:

```
\>OR1  
CAAATCACTA  
\>OR2  
CACGCCACTT  
\>OR3  
CGGGTCACGT
```

**Execution:**

`$ ./mutations.py /path/to/reference.fa /path/to/control.fa /path/to/theraprix.fa`

**Result:**

```
0.1011
```

---

### Task

Create a new .py file that contains a single function. Call that function `evens_mean`. `evens_mean` should accept a single parameter. You can call the parameter anything you want, but `num_list` is a decent choice, since the parameter will be a list of numbers (floats, ints, or both). `evens_mean` should iterate over `num_list` and calculate the mean of all the even elements. `even_means` should then return the calculated mean value.

#### Hint

H1

---

### Task

Write a function `headers`, which takes the contents of a FASTA file as a string and returns a list of all of the sequence headers in the file, without the initial '>' included.

As a side note, it's fine if you want to write `headers` in the same file as `evens_mean`. Or you can have it in its own file. Whatever makes you feel more organized.

#### Hint

H2

---

### Task

Make function called `make_lookup`. `make_lookup` should take two lists `names` and `seqs` as parameters, and return a dictionary where each element of `names` is a key and each element of `seqs` is a corresponding value.

Here's a small example:

`names = ['seq1', 'seq2']`
`seqs = ['AGTC', 'AAAA']`

The dictionary that should be returned by `make_lookup` would look like:

`lookup = {'seq1':'AGTC', 'seq2':'AAAA'}`

#### Hint

You don't need a dictionary for this problem. Instead, this task is to make sure you're aware of the built-in [zip](https://docs.python.org/3.6/library/functions.html#zip) function. Here's a nice [example](http://stackoverflow.com/questions/13704860/zip-lists-in-python/13704903#13704903) of how zip works.

Bonus hint! Here's some documentation on how to do a [t-test](https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.stats.ttest_ind.html#scipy.stats.ttest_ind).
