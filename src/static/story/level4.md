T
=====

analyzing structured data (part II)
--------

img

"Colossus isn't the name of any protein in any database. Unless you count this supplement powder I found online," Anita tells you. The two of you, along with the rest of the team, have spent the last week analyzing the genomic regions in the .bed file you retrieved from Oregon. Day after day you've crossed regions off your list. For the most part, the regions denoted locations near known protein coding genes, none of which appear to have any real relationship to each other.

"Figures," you respond. You didn't expect the name to match anything, which is why Anita hadn't checked before now. You also note to yourself that you're being a little curt, probably because it's been an exasperating week, so ask Joe to make a coffee run for the team. Joe laughs and says he'll be back soon. You're about to look one of the last regions, when your laptop shuts off on you. Of course; that's what you get for not charging the battery.  

"Would you mind looking up 'chr2' 12345-678900? My computer just died," you ask Anita. She says she's on it, so you make a quick lap around the office. A couple days ago, you decided to assign a few people to start investigating the Konrad brothers full time. You ask them how their doing and they tell you that their systems should be fully functional by the end of the day. But they don't have anything to report at the moment. The pair of agents you have working on Life/Better, LLC have a similar amount of material to report. And you know the rest of the team doesn't have anything, so you circle back to Anita.

"This is just a gene desert. As far as I can tell, it doesn't do anything and isn't tied to any functions, diseases or cancers," she informs you. Given the contents of the rest of the file, that doesn't make much sense. But then again, maybe you've been looking at this all backwards. You've spent this whole time looking at what's in or around the regions in this file. What if you should be more interested in what *isn't* there?

"What if they were looking for a gene insertion site", you hypothesize aloud. The total lack of connections between the contents of the sites would then make sense: just the fact that the site had contents was the connection.

"Hmm... How about this theory, then," starts Anita. "What if they're looking for a site to add this Colossus protein, whatever it is? If that were the case, then I bet we could use Theraptrix's protein order forms for the past year and cross-reference those with the database we have of proteins which other researchers have inserted into this site. 

"Sounds like a stretch to me." That's what you want to say. But you don't have any better ideas. So, you sit down and get to work.

---

### Problem


read file. filter for significance. filter for being in other file (list of names). Report the count of HepG2 and K562 cells left.

**Notes:**

N

##### Example


Contents of `f.txt`:


    Contents


**Execution:**

`$ ./f.py a1`

**Result:**

    Result


---

### Task

Before you get started on this task, here is the documentation for [pandas](http://pandas.pydata.org/pandas-docs/stable/index.html), one of the most popular data analysis tools in Python. Use this documentation to write a function called `abc_df`. `abc_df` will take a numpy array as a parameter. The array will have a size of no greater than (26, 26). `abc_df` should return a `DataFrame` where the data of the `DataFrame` is the numpy array, and both the indices and the columns are labeled with letters. The result for a numpy array of shape (4,3) can be imagined as something like:

|a|b|c|
--- | --- | --- | ---
a | 9|2|4
b | 8|1|0
c | 1|9|7
d | 4|2|1


#### Hint

H1

---

### Task

Write `most_common_index`, a function which, when applied to a `DataFrame`, returns the count (i.e. the number of times the element occurs) of the index element which occurs most often.

#### Hint

H2

---

### Task

Create a function called `last_col_median`. Given a `DataFrame` as a parameter, `last_col_median` should attempt to find the median of the last column of the `DataFrame`. If the median cannot be found because the last column does not have a numeric data type, `last_col_median` should simply return `None`.

#### Hint

H3
