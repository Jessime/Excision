T
=====

Sub
--------


You walk into the office Monday morning and make an announcement. A team is going to head out to the Theraptrix plant as soon as they can get their bags packed. You'll head the expedition with Anita, who you've promoted to lead the investigation against Gene Corp.

Your plane touches down in Klamath Falls Airport near Medford Oregon, and an hour later you’re grabbing a sandwich with Anita at a local place called Sherry’s Shack. Sherry, somewhat of a minor celebrity in these parts, serves lunch to you herself. She tries to strike up a bit of a conversation since the restaurant isn’t busy this late in the afternoon. You and Anita are also using the Shack as an operations base, so you're thankful when Sherry quickly picks up on the tension and moves on to the few other customers currently in the diner. 

The goal for today is simple: gain access to Theraptrix's file system, particularly their projects directory. The path to achieving this goal is less simple. After all, while the current plan isn't strictly illegal, it definitely isn't by the books. If you offically issue a warrant for the data, they'll just delete it before you can get to it. Instead, you're going to have a member of your team join each of the factory tours given today. Each team member will sneak in an extremely low power digital thermometer past Theraptrix's device detector. The good news is that the thermometers are inconspicuous enough to not trigger alarms, and are capable of creating a 2D map of temperatures in the building. The bad news is, these devices are so low power that they aren't particularly reliable. That's why you're sending in multiple agents (that and the fact that agents now have the option to abort if necessary, without ruining the mission). The consensus of the devices, however, should provide a literal heatmap of the building.This means you'll be able to find the server room by finding which location is hottest. 

Anita and you can use the rest of the day for planning your next move **Edit: plan on the plane ride!**, as soon as you write this program. Down time is rarely in excess, so you'd better get writing!

---

**Task:** Write a function called `rms` that returns the [root mean square](https://en.wikipedia.org/wiki/Root_mean_square) of a given list. 


The most fundamental packages to the data science ecosystem in Python is numpy. Within numpy, the `ndarray` class is a very commonly used class to create 1 and 2 dimensional arrays, which are great for replacing python lists and handling numbers found in csv files. `ndarray`s are different than Python lists, and may take some getting used to. Here's a [quickstart](https://docs.scipy.org/doc/numpy/user/quickstart.html) guide to make sure you have at least some familiarity with numpy arrays.  

---

**Task:** Write `csv2tab` which, as the name implies, takes a csv file and converts it to a tab file.

If you've completed the tutorial, apologies. You've already seen this hint:

We'll introduce other ways to read data files, but numpy provides some basic help. Read up on  [np.loadtxt](https://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html) to get your data into an array. 

---

**Task:** T3

A3

---

>**Problem:**
>
> Write a program that takes an empty folder location as input. This folder will have multiple subfolders, each of which have a unknown name and contain two csv files from one of your agents. Your program should collect all of these csv files, and use them to find the index and temperature of the hottest location in the Theraptrix factory. Write both the index and the average temperature (to the nearest integer) to `results/2.txt`.
>
> There's one additional complication. Occasionally, the thermometers will fail to record a reading. If this is the case, the csv file will register a 0. In order to deal with this missing data, replace it with **76**, as an imputation of "room temperature".
> 
>**Notes:**
>
>While you cannot know the names, or the number, of the incoming subfolders, you can assume there will be nothing in the folder besides necessary subfolders, and nothing in the subfolders besides two files, `pass1.csv` and `pass2.csv`. 
>
>**Example:**
>
>
>Directory structure of `/path/to/level2/`:
>
>>```
>>/path/to/level2/
>>├── Kevin-temp-data/
>>    ├── pass1.csv
>>    ├── pass2.csv
>>├── temperatures-casey/
>>    ├── pass1.csv
>>    ├── pass2.csv
>>
>>```
>
>Contents of `Kevin-temp-data/pass1.csv`:
>
>>74,59  
>>81,0
>
>Contents of `Kevin-temp-data/pass2.csv`:
>
>>79,60  
>>77,71
>
>Contents of `temperatures-casey/pass1.csv`:
>
>>0,56  
>>86,67
>
>Contents of `temperatures-casey/pass2.csv`:
>
>>73,61  
>>73,72
>
>**Execution:**
>
>`$ ./temp_map.py /path/to/level2/`
>
> **Result:**
>
> (1, 0)  
> 79

