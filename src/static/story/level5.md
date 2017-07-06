CAPTURE
=====

image processing and analysis
--------

images/level5.jpg

That's when the men in masks walk in.

You have no time to respond in any meaningful way, but you note that the silencers on their pistols likely explain how they got past the guards downstairs. Two of them head straight towards you, while the others fan out to control the rest of your coworkers. In your head, it doesn't seem like their moving that fast. It's more like your body is suddenly stuck in molasses. You do little to resist as one of them grabs your hands and throws you to the ground. The other presses a rag to your face. The last thing you hear before you black out is screaming, as if from another room.

"Why is my right arm so sore?" That's the first thing you ask yourself. You open your eyes and take a look around. You're in small room that appears to be a combination of a holding cell and a basic laboratory. You're lying on a cot in the corner with a sink in front of you and a toilet to the left. On the other side of the room, only a few paces away, is a table with a microscope, a computer, and other basic lab equipment. Separating you from the table is a chain link fence. You get up and, while rubbing your arm, do a quick tour around the room. There isn't much you missed in your first assessment, so you sit back down on your cot and wait.  

After several hours you're back up and pacing around. The pain in your arm seems to be spreading. You've just completed another lap when the sliding window in the door opens. A man sticks his face in and looks around, making eye contact with you.

"Would you, uh, mind moving to the back of the cell, please?" he asks.

Wordlessly, you do what he says. He steps in with a tray of food in his hands and a gun on his belt. He is a massive guy, and there's no way you'd be able to get it from him in this tiny space.

"Here's some food," he says, handing you the tray. "I guess I need to see your arm while you eat?" Somehow he makes this comes out as a question. While you're eating the guy takes a tissue sample from your right arm. You're not sure if it's the soreness in your arm or the guy's shaky hands that makes the biopsy so painful.

"What's your name," you decide to ask.

"Mmm... Max," he responds.

Max takes your tissue sample to the other side of the room, turns on the computer, and sticks the sample under the scope. He's muttering to himself as he does, but you can't make out what he's saying.

You try to get more information out of him, "Where are we?"

"I don't think I'm allowed to say," Max says as a picture of a collection of cells appear on the screen. You remember enough from your Cell Bio. lab at the academy to know that somethings wrong with these cells. As far as you can tell, Max seems to tweak some settings, undo his work, pause to mutter to himself, then repeat the cycle.

This time, it's your turn to be hesitant, "Do you need some help?"

Max turns around to look at you, then looks at the ground. "This is my, uh, second week on the job... I'm a little, er, out of my element. This isn't the type of place where you get... rewarded for asking questions. So, uh, yea. I could use some help. I guess you'll probably have to stay on that side of the room though."

"Well, what do you have to do?"
---

### Problem

Write a .py file that takes a folder path name to a sequence of .png image files as input. This function should store the image data in the folder path as grayscale for every frame and apply several image processing steps. First, apply a median filter to each frame using a 5x5 pixel window to filter out the background noise. Then, mask the image by setting the lower 50% of pixel values across the image sequence to zero. Using this processed image sequence, calculate the total area (nanometers) of the remaining object(s) in the image sequence for every frame and return it as a list.

**Notes:**

Pixel to nanometer conversion: width/height of 1 pixel = 0.15 nanometers

The path to the images is `Excision/src/static/data/5/ims/`

##### Example

Directory structure of `path/to/ims/`

        /path/to/ims/
        ├── sim_0.png
        ├── sim_1.png
        ├── sim_2.png

Contents of `sim_0.png`

images/level5_ims_md/sim_0.png

Contents of `sim_1.png`

images/level5_ims_md/sim_1.png

Contents of `sim_2.png`

images/level5_ims_md/sim_2.png


**Example Execution:**

`$ ./image_proc.py /path/to/ims/`

**Example Result:**

    [21.15, 43.7175, 106.7175]


---

### Task

An RGB image at its most basic form is a 3D array of size height x width x 3. The height and width are representative of the image size, and the 3 represents the R, G, or B channel values of a pixel at a given coordinate index. Alternatively, a grayscale image only has one channel to indicate color, therefore it is typically stored in a 2D array. When converting an RGB image to a grayscale image, the 3 color channels must be collapsed into a single channel to indicate the pixel value. There are three common techniques for performing this operation. For a given pixel in an RGB image, its respective grayscale value can be calculated by one of the following:  

1. **Averaging Method:** Average the R, G, and B components: <pre>(R + G + B)/3  )</pre>

2. **Lightness Method:** Average only the highest value of the three channels with the lowest value of the three channels: <pre>((max(R, G, B) + min(R, G, B))/2  )</pre>

3. **Luminosity Method:** Using a pre-formulated equation to calculate a weighted average accounting for human perceptions of color. Humans typically are more sensitive to light in the green spectrum, so this channel is weighted more in this calculation. Different weighting values have been disputed over the years : <pre> 0.3R + 0.59G + 0.11B </pre>  

Create a function, `color2grey`, that takes in a 3D array of size height x width x 3 representing R, G, B channels as input and returns a 2D array of size height x width containing the grayscale component calculated using the luminosity method formula above.

#### Hint

While it is possible to just use numpy arrays to store image data, packages have been written to provide extra convienence. One of the most popular is called `Pillow`, which provides an [`Image`](https://pillow.readthedocs.io/en/4.1.x/reference/Image.html) class.

---

### Task

Write a function called `square_means`. This function should take the following input arguments: a 2D square array of numbers and a single integer value representing the dimension of a square window to tile the input array with. This function will be used to calculating mean values in the input array for each individual block in the array determined by the input window size. For example, if the square array `sq_arr` is passed in and has a shape (25,25), and the window size `window` has the value 5, then a mean value must be calculated for each 5x5 block in `sq_arr`. These individual blocks should not have overlap. It can be assumed that the input array’s dimension, N, (for an array of size NxN) is perfectly divisible by the window value, w (i.e. N % w = 0). The function should return as output an array of the mean values ordered by mean values calculated across the first row of windows, then descending in rows.

#### Hint

Another foundational package for scientific computing in Python is [scipy](). It provides a lot of functionality that we aren't going to get into now, but a [here's a filter function](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.median_filter.html#scipy.ndimage.median_filter) that you can apply here.  

Also, [this is a fun image](https://qph.ec.quoracdn.net/main-qimg-42e32657dd966f717e7f3c8ee7a151c1-c) demonstrating how all of these packages tie into each other.

---

### Task

Make a function named `compress` that takes a 1D numpy array, `full`, as a parameter. Calculate a second 1D array that represents the [run-length encoding](https://en.wikipedia.org/wiki/Run-length_encoding) of `full`. `compress` should return a list of two elements. The first element should be the size of the full length array measured in bytes, and the second element should be the size of the compressed array, also in bytes.

#### Hint

https://docs.scipy.org/doc/numpy-1.12.0/reference/generated/numpy.count_nonzero.html
