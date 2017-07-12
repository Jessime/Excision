CAPTURE
=====

image processing and analysis
--------

images/level5.jpg

That's when the men in masks walk in.

You have no time to respond in any meaningful way, but you note that the silencers on their pistols likely explain how they got past the guards downstairs. Two of them head straight toward you, while the others fan out to control the rest of your coworkers. In your head, it doesn't seem like they're moving that fast. It's more like your body is suddenly stuck in molasses. You do little to resist as one of them grabs your hands and throws you to the ground. The other presses a rag to your face. The last thing you hear before you black out is screaming, as if from another room.

"Why is my arm so sore?" That's the first thing you ask yourself when you regain consciousness. You open your eyes and take a look around. You're in a small room that appears to be a combination of a holding cell and a basic laboratory. You're lying on a cot in the corner. You sit up and see a sink and toilet next to the cot and a single door on the opposite wall. On the other side of the room, only a few paces away, is a table with a microscope, a computer, and other basic lab equipment. Separating you from the table is a chain-link fence. You get up and, while rubbing your arm, do a quick tour around the room. There isn't much you missed in your first assessment, so you sit back down on your cot and wait.  

After several hours, you're back up and pacing around. The pain in your arm seems to be spreading. You've just completed another lap when a sliding window in the door opens. A man sticks his face in and looks around, making eye contact with you.

"Would you, uh, mind moving to the back of the cell, please?" he asks.

Wordlessly, you do what he says. He steps in with a tray of food in his hands and a gun on his belt. He is a massive guy, and there's no way you'd be able to escape around him in this tiny space.

"Here's some food," he says, handing you the tray. "I guess I need to see your arm while you eat?" Somehow he makes this comes out as a question. While you're eating, the guy takes a tissue sample from your right arm. You're not sure if it's the guy's shaky hands or the soreness in your arm that makes the biopsy so painful.

"What's your name?" you decide to ask.

"Mmm...Max," he responds.

Max takes your tissue sample to the other side of the room, turns on the computer, and slides the sample under the scope. He's muttering to himself as he does, but you can't make out what he's saying.

You try to get more information out of him: "Where are we?"

"I don't think I'm allowed to say," Max says as a picture of a collection of cells appears on the screen. You remember enough from your Cell Bio lab at the Academy to know that something's wrong with these cells. As far as you can tell, Max seems to tweak some settings, undo his work, pause to mutter to himself, then repeat the cycle.

You say hesitantly, "Do you need some help?"

Max turns around to look at you, then looks at the ground. "This is my, uh, second week on the job...I'm a little, er, out of my element. This isn't the type of place where you get...rewarded for asking questions. So, uh, yea. I could use some help. I guess you'll probably have to stay on that side of the room, though."

"Well, what do you have to do?"

---

### Problem

Write a .py file that takes a string as input. This string is a file path to a directory containing a sequence of .png image files. This program should load the .png images as grayscale and apply several image processing steps to each frame. First, apply a median filter using a 5x5 pixel window to filter out any background noise. Next, mask the image by taking the arithmetic mean of the highest and lowest observed pixel values, then setting pixel values below that mean to zero. Then, calculate the cumulative area (in microns) of the remaining object(s). After these steps have been applied to each frame, print the list of areas to `results/5.txt`.

**Note(s):**

* Unlike in task 2, the windows of the median filter will overlap.
* Assume that the width and height of 1 pixel are each 1.5 microns.
* Truncate each area by converting it to integers.
* Expect this script to take approximately 15 seconds to run once you submit it.

##### Example

Directory structure of `path/to/ims/`:

        /path/to/ims/
        ├── image_0.png
        ├── image_1.png
        ├── image_2.png

[Here](https://github.com/Jessime/Excision/tree/master/src/static/images/level5_ims_md) are the contents of `path/to/ims/`.

**Example Execution:**

`$ ./image_proc.py /path/to/ims/`

**Example Result:**

    [2115, 4371, 10671]

---

### Task

An RGB image in its most basic form is a 3D array of shape (height, width, 3). The height and width are representative of the image size, and the 3 represents the R, G, or B channel values of a pixel at a given coordinate index. A grayscale image only has one channel to indicate color; therefore, it is typically stored in a 2D array. When converting an RGB image to a grayscale image, the 3 color channels must be collapsed into a single channel to indicate the pixel value. There are three common techniques for performing this operation:

1. **Averaging Method:** Average the R, G, and B components. <pre>(R + G + B)/3</pre>

2. **Lightness Method:** Average the highest value of the three channels with the lowest value of the three channels. <pre>(max(R, G, B) + min(R, G, B))/2</pre>

3. **Luminosity Method:** Use a pre-formulated equation to calculate a weighted average accounting for human perceptions of color. Humans are typically more sensitive to light in the green spectrum, so this channel is weighted more in this calculation. (Different weighting values have been disputed over the years.) <pre> 0.3R + 0.59G + 0.11B </pre>

Create a function, `color2gray`, that takes an RGB image as a 3D array of shape (height, width, 3) as input and returns a 2D array of shape (height, width) containing the grayscale value calculated using the luminosity method  above.

#### Hint

While it is possible to just use `numpy` arrays to store image data, packages have been written to provide extra convenience. One of the most popular is called `Pillow`, which provides an [`Image`](https://pillow.readthedocs.io/en/4.1.x/reference/Image.html) class.

---

### Task

Write a function called `square_means`. This function should take the following arguments: a 2D square array of numbers, `sq_arr`, and a single integer value representing both dimensions of a square window, `window`. `square_means` will calculate a mean value for each non-overlapping square window of the indicated dimensions within the array. The function should return a square array which includes each window's mean value arranged to correspond to the locations of the windows on `sq_arr`. (Assume that `sq_arr`'s dimensions are perfectly divisible by `window`.)

For example, if `sq_arr` has a shape (25,25) and `window` is 5, then a mean value would be calculated for each non-overlapping (5,5) window in `sq_arr`. `square means` would return each of these 25 mean values in a (5,5) array. The location of a particular mean value would be analogous to the location of its corresponding window on the (25,25) `sq_arr`.

#### Hint

Another foundational package for scientific computing in Python is [`scipy`](https://docs.scipy.org/doc/scipy-0.19.1/reference/index.html). It provides a lot of functionality that we aren't going to get into now, but [here's a filter function](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.median_filter.html#scipy.ndimage.median_filter) that you can apply here.  

  Also, [this is a fun image](https://qph.ec.quoracdn.net/main-qimg-42e32657dd966f717e7f3c8ee7a151c1-c) demonstrating how all of these packages tie into each other.

---

### Task

Make a function named `compress` that takes a 1D `numpy` array, `full`, as a parameter. Calculate and return a second 1D array, `encoded` that represents the [run-length encoding](https://en.wikipedia.org/wiki/Run-length_encoding) of `full`. In `encoded`, every even element of `encoded` should represent a count, and every odd element should represent a value from `full`.

#### Hint
You can use [`count_nonzero`](https://docs.scipy.org/doc/numpy-1.12.0/reference/generated/numpy.count_nonzero.html) for this problem. In more complicated scenarios, you would need the more general [`where`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.where.html) function.
