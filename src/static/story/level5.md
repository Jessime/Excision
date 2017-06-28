T
=====

Image processing and analysis
--------

img

That's when the men in masks walk in.

You have no time to respond in any meaningful way, but you note that the silencers on their pistols likely explain how they got past the guards downstairs. Two of them head straight towards you, while the others fan out to control the rest of your coworkers. In your head, it doesn't seem like their moving that fast. It's more like your body is suddenly stuck in molasses. You do little to resist as one of them grabs your hands and throws you to the ground. The other presses a rag to your face. The last thing you hear before you black out is screaming, as if from another room.

"Why is my right arm so sore?" That's the first thing you ask yourself.  

You get kidnapped. These cells have been injected in your arm. You're investigating on yourself.

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

Create a function that takes in a 3D array of size height x width x 3 representing R, G, B channels as input and returns a 2D array of size height x width containing the grayscale component calculated using the luminosity method formula above.

#### Hint

https://pillow.readthedocs.io/en/4.1.x/reference/Image.html

---

### Task

Write a function called “square_means”. This function should take the following input arguments: a 2D square array of numbers and a single integer value representing the dimension of a square window to tile the input array with. This function will be used to calculating mean values in the input array for each individual block in the array determined by the input window size. For example, if the square array “sq_arr” is passed in and has the dimensions 25x25, and the window size “window” has the value 5, then a mean value must be calculated for each 5x5 block in “sq_arr”. These individual blocks should not have overlap. It can be assumed that the input array’s dimension, N, (for an array of size NxN) is perfectly divisible by the window value, w (i.e. N % w = 0) .The function should return as output a list of the mean values ordered by mean values calculated across the first row of windows, then descending in rows.

#### Hint

https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.median_filter.html#scipy.ndimage.median_filter

---

### Task

Make a function named “zeros_ones” that takes as input a 1D array of integers of any length. The function should find and return two lists where the first output list stores those indices indicating the positions of all elements equal to zero in the input array and the second list indicates the positions of all elements equal to one in the input array. The input array could contain any integer greater than or equal to zero.

#### Hint

https://docs.scipy.org/doc/numpy-1.12.0/reference/generated/numpy.count_nonzero.html
