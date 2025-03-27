import ffmpeg
import numpy
import PIL
import os

filename = "lambo.mp4"

os.mkdir(f"./output/{filename}")

ffmpeg.input(filename).filter("fps",fps=10).output(f'./output/{filename}/frame_%04d.png').run()

