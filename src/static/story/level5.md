T
=====

Sub
--------

img

story

---

### Problem

Write a .py file that takes a folder path name to a sequence of .png image files as input. This function should store the image data as grayscale in the folder path for every frame and apply several image processing steps. First, apply a median filter using a 5x5 pixel window to filter out the background noise. Then, mask the image by setting the lower 50% of pixel values across the image sequence to zero. Using this processed image sequence, calculate the total area (nanometers) of the remaining object(s) in the image sequence for every frame and return it as a list.

**Notes:**

Pixel to nanometer conversion: width/height of 1 pixel = 0.XX nanometers


##### Example

Contents of `/ims/`

        /path/to/ims/
        ├── sim_000.png/
        ├── sim_001.png/
        ├── sim_002.png/

Contents of `sim_000.png`

images/level5_ims_md/sim_000.png

Contents of `sim_001.png`

images/level5_ims_md/sim_001.png

Contents of `sim_002.png`

images/level5_ims_md/sim_002.png


**Execution:**

`$ ./image_proc.py /path/to/ims/`

**Result:**

    []


---

### Task

An RGB image at its most basic form is a 3D array of size height x width x 3. The height and width are representative of the image size, and the 3 represents the R, G, or B channel values of a pixel at a given coordinate index. Alternatively, a grayscale image only has one channel to indicate color, therefore it is typically stored in a 2D array. When converting an RGB image to a grayscale image, the 3 color channels must be collapsed into a single channel to indicate the pixel value. There are three common techniques for performing this operation. For a given pixel in an RGB image, its respective grayscale value can be calculated by one of the following:  

1. Averaging Method:
Average the R, G, and B components.
(R + G + B)/3  2)

2. Lightness Method:
Average only the highest value of the three channels with the lowest value of the three channels.
((max(R, G, B) + min(R, G, B))/2  3)

3. Luminosity Method
Using a pre-formulated equation to calculate a weighted average accounting for human perceptions of color. Humans typically are more sensitive to light in the green spectrum, so this channel is weighted more in this calculation. Different weighting values have been disputed over the years 
0.3*R + 0.59*G + 0.11*B  

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
