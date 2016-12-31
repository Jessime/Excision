<header class="major special">
	<h2>Title</h2>
    <p> Subtitle </p>
</header>

![Image](/path/to/img.jpg "Title")

This is where the main storyline goes.

You can use as many paragraphs as necessary.

---

**Task:** A description of the task for hint#1

<form action="" method="post">
    <input type="submit" value="Hint #1" class="button" name="tutorial_hint1">
</form>

{% if hint_solved1 %}
Answer#1 A clue for solving the problem.
{% endif %}

---

**Task:** A description of the task for hint#2

<form action="" method="post">
    <input type="submit" value="Hint #2" class="button" name="tutorial_hint1">
</form>

{% if hint_solved1 %}
Answer#3 A clue for solving the problem.
{% endif %}

---

**Task:** A description of the task for hint#3

<form action="" method="post">
    <input type="submit" value="Hint #3" class="button" name="tutorial_hint1">
</form>

{% if hint_solved1 %}
Answer#3 A clue for solving the problem.
{% endif %}

---

>**Problem:**
>
>A description of the bioinformatics problem to solve for this page. 
>
>**Notes:**
>
>Here are additional things to know about the problem. Can be "N/A".
>
>**Example:**
>
>This field may contain several parts. If your task involves reading a text file, you'll see:
>
>Contents of file.txt:
>
>"Hello from file.txt"
>
>**Execution:**
>
>`$ /path/to/python_script.py arg1 arg2`
>
>**Result:**
>
>The resulting output of the program you just wrote and executed when using the example data.

<form action="" method="post">
    <input type="submit" value="Submit" class="special" name="tutorial_sum">
</form>
