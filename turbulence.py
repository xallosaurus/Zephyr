# numpy is for array math
import numpy
# we need Pillow to load images and convert to grayscale
from PIL import Image
# os for file lists
import os


# something did not work with relative paths
# so Claude AI helped create this function to get 
# absolute file paths
def absolute_file_paths(directory):
    path = os.path.abspath(directory)
    return [entry.path for entry in os.scandir(path) if entry.is_file()]


# we will run the analysis for lambo and bronco separately
paths = ["./output/bronco.mp4","./output/lambo.mp4"]

#in this loop we open two dirs so this loop will run two times
for path in paths:
    print(f"Starting work on png files in {path}")
    file_type = ".png"
    # get a list of png files in order because they are consecutive
    png_files = sorted (absolute_file_paths(path))
    # we will put averages between files in this list
    averages = []
    # we will compare first with second, second with third and so on
    for i in range(len(png_files)-1):
        # this is the curent file
        current_file = png_files[i]
        # this is the file right after the current file
        next_file = png_files[i + 1]
        # load the first file as a PIL image
        image1 = Image.open(current_file)
        # load the second file as a PIL IMAge
        image2 = Image.open(next_file)
        #convert them both to grayscale using Pillow
        gray_image1 = image1.convert("L")
        gray_image2 = image2.convert("L")
        # use numpy to turn them into very long arrays of pixels
        grey_array1 = numpy.array(gray_image1)
        grey_array2 = numpy.array(gray_image2)
        # subtract the two pixels arrays to obtain the differences in shade
        # but we also must use absolute numbers 
        # because negative numbers cancel out positives and averages get too small
        abs_dif = numpy.abs(grey_array1 - grey_array2)
        # calculate the average brightness change between image1 and image2
        avg_dif = numpy.mean(abs_dif)
        # now append the value to the list of averages
        averages.append(avg_dif)
    # take the max value which indicates the most turbulent image pair
    biggest_average = numpy.max(averages)
    print (f"Average pixel varition across consecutive frames for {path} : {biggest_average}")