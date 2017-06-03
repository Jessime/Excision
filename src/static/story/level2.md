OREGON TRAIL
=====

an introduction to arrays
--------

images/banner1.jpg

You walk into the office Monday morning and make an announcement. A team is going to head out to the Theraptrix plant as soon as they can get their bags packed. You'll lead the expedition with Anita, whom you've promoted to coordinate the investigation against Gene Corp.

Within the hour, you've boarded the jet. By the time you're in the air, you and Anita are deep in conversation, trying to play out possible long-term scenarios. You ask Anita about her thoughts on the Konrads. Rumor has it that the current CEO of Gene Corp is nothing more than a figurehead. It's a pair of Polish twins, the Konrads, who are calling the shots as COO and CTO. Anita replies that she's been researching the possibility of playing the twins off of one another in an effort to distract Gene Corp's leadership while the Agency is building their case.  

Your plane touches down in Klamath Falls Airport near Medford, Oregon, and you head straight to a local place called Sherry's Shack where you can grab a sandwich. Sherry, somewhat of a minor celebrity in these parts, serves lunch to you herself. She tries to strike up a bit of a conversation since the restaurant isn’t busy this late in the afternoon. You and Anita are also using the Shack as a base of operations, so you're thankful when Sherry quickly picks up on your need for privacy and moves on to the few other customers currently in the diner.

The goal for today is simple: gain access to Theraptrix's file system, particularly their projects directory. The path to achieving this goal is less simple. After all, while the current plan isn't strictly illegal, it definitely isn't by the books. If you officially issue a warrant for the data, they'll just delete it before you can get to it. Instead, you're going to have a member of your team join each of the factory tours given today. Each team member will sneak an extremely low-power digital thermometer past Theraptrix's device detector. The good news is that the thermometers are inconspicuous enough to not trigger alarms and are capable of creating a 2D map of temperatures in the building. The bad news is that these devices are so low-power that they aren't particularly reliable. That's why you're sending in multiple agents. The consensus of the devices, however, should provide a literal heatmap of the building. This means you'll be able to find the server room by finding which location is hottest.

You and Anita can use the rest of the day for additional planning, as soon as you write this program. Down time is rarely in excess, so you'd better get writing!

---

### Problem

Write a program that takes an empty folder location as input. This folder will have multiple subfolders, each of which has a unknown name and contains two .csv files from one of your agents. Your program should collect all of these .csv files and use them to find the index and temperature of the hottest location in the Theraptrix factory. Write both the index and the average temperature (to the nearest integer) to `results/2.txt`.

There's one additional complication. Occasionally, the thermometers will fail to record a reading. If this is the case, the .csv file will register a 0. In order to deal with this missing data, replace it with **76**, as an imputation of 'room temperature'.


**Note(s):**

While you cannot know the names or the number of the incoming subfolders, you can assume there will be nothing in a folder besides necessary subfolders, and nothing in the subfolders besides two files, `pass1.csv` and `pass2.csv`.

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

---

### Task

Write a function called `rms` that returns the [root mean square](https://en.wikipedia.org/wiki/Root_mean_square) of a given list.

#### Hint

The most fundamental package to the data science ecosystem in Python is `numpy`. Within `numpy`, the `ndarray` class is a very commonly used class to create 1- and 2-dimensional arrays, which are great for replacing Python lists and handling numbers found in .csv files. `ndarray`s are different from Python lists and may take some getting used to. Here's a [quickstart](https://docs.scipy.org/doc/numpy/user/quickstart.html) guide to make sure you have at least some familiarity with `numpy` arrays.

---

### Task

Create a `parent_exists` function that takes a path name (as a string) to a potential file as input. `parent_exists` should return one of two strings. If the file has already been created, the function will return `"There is a file at that location."` Otherwise, it should return the name of the parent directory (the folder in which the file would have resided).

#### Hint

Although it's not used very commonly in bioinformatics scripts, the [`os`](https://docs.python.org/3/library/os.html) module can come in handy in many situations. For this level's problem, try learning more about the `os.walk` function.

This hint was also included in the tutorial, but it's worth mentioning again even if you have seen it:

We'll introduce other ways to read data files, but `numpy` provides some basic help. Read up on  [`np.loadtxt`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html) to get your data into an array.

---

### Task

Write `threshold`, a function which takes an `ndarray` and any real number (call this parameter `limit`). `threshold` returns a modified `ndarray` where all elements in the array which are less than the `limit` parameter are set to 0.

#### Hint

One of the benefits of using `numpy` is that it can make your code orders of magnitude faster than pure Python. This speed benefit is often lost by users who use for loops as a way to iterate over their arrays. If you're looking for speed, avoid combining `numpy` arrays and for loops.

To understand how you can index an array without a for loop, check out the [advanced indexing](https://docs.scipy.org/doc/numpy/user/quickstart.html#fancy-indexing-and-index-tricks) portion of the `numpy` quickstart guide.

As a test to make sure you understand these concepts, make sure you can write `threshold` in a couple of short lines of code (including the return statement).
