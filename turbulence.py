import numpy
import PIL
from PIL import Image
import os


def absolute_file_paths(directory):
    path = os.path.abspath(directory)
    return [entry.path for entry in os.scandir(path) if entry.is_file()]


paths = ["./output/bronco.mp4","./output/lambo.mp4"]
for path in paths:
    print(f"Starting work on png files in {path}")
    file_type = ".png"
    png_files = sorted (absolute_file_paths(path))
    averages = []
    for i in range(len(png_files)-1):
        current_file = png_files[i]
        next_file = png_files[i + 1]
        image1 = Image.open(current_file)
        image2 = Image.open(next_file)
        gray_image1 = image1.convert("L")
        gray_image2 = image2.convert("L")
        grey_array1 = numpy.array(gray_image1)
        grey_array2 = numpy.array(gray_image2)
        abs_dif = numpy.abs(grey_array1 - grey_array2)
        avg_dif = numpy.mean(abs_dif)
        averages.append(avg_dif)
    average = numpy.max(averages)
    print (f"Average pixel varition across consecutive frames for {path} : {average}")