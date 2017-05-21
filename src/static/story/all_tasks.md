Decisions
=====

File parsing with a touch of statistics
-----


### Task

Create a new .py file that contains a single function. Call that function `evens_mean`. `evens_mean` should accept a single parameter. You can call the parameter anything you want, but `num_list` is a decent choice, since the parameter will be a list of numbers (floats, ints, or both). `evens_mean` should iterate over `num_list` and calculate the mean of all the even elements. `even_means` should then return the calculated mean value.



### Task

Write a function `headers`, which takes the contents of a FASTA file as a string and returns a list of all of the sequence headers in the file, without the initial '>' included.

As a side note, it's fine if you want to write `headers` in the same file as `evens_mean`. Or you can have it in its own file. Whatever makes you feel more organized.



### Task

Make function called `make_lookup`. `make_lookup` should take two lists `names` and `seqs` as parameters, and return a dictionary where each element of `names` is a key and each element of `seqs` is a corresponding value.

Here's a small example:

`names = ['seq1', 'seq2']`

`seqs = ['AGTC', 'AAAA']`

The dictionary that should be returned by `make_lookup` would look like:

`lookup = {'seq1':'AGTC', 'seq2':'AAAA'}`


Oregon Trail
=====

An introduction to arrays
-----


### Task

Write a function called `rms` that returns the [root mean square](https://en.wikipedia.org/wiki/Root_mean_square) of a given list.



### Task

Write `csv2tab` which, as the name implies, takes a csv file and converts it to a tab file.



### Task

Write `threshold`, a function which takes an `ndarray` and any real number (call this parameter `limit`). `threshold` returns a modified `ndarray` where all elements in the array which are less than the `limit` parameter are set to 0.


T
=====

Analyzing structured data (Part I)
-----


### Task

Write `is_nucleic_acid`, which given a string, returns a bool indicating whether the string is a valid representation of a case insensitive [nucleic acid](https://en.wikipedia.org/wiki/Nucleic_acid_notation) sequence.



### Task

Also write `has_digit`, which given a list of strings, returns a filtered list of strings. The filtered list should only contain the strings from the original list that have at least one number in the string.



### Task

`intersects` should take two lists as parameters and return a bool. The lists, `region1` and `region2`, will each contain two positive integers representing start and stop positions. The bool, then, will indicate whether the `region1` and `region2` intersect (i.e. overlap) in any capacity.


