import ffmpeg
import os

# this tool uses ffmpeg utility
# to create image files from input videos


# Create the ./output dir if it doesn't exist
output_dir = './output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir, exist_ok=True)

# Define video filenames
filenames = ["lambo.mp4", "bronco.mp4"]

# we loop over two input mp4 files
# and rum ffmpeg on each file
for filename in filenames:
    # first create the path so we can see if there are
    # already files in it
    dir_path = f"{output_dir}/{filename}"
    if os.path.exists(dir_path):
        # delete all existing images in case they were updated
        for img_name in os.listdir(dir_path):
            os.remove(f"{dir_path}/{img_name}")

    # Create the directories for each video
    # this is necessary when running the first time
    # or if someone deleted everything
    os.makedirs(dir_path, exist_ok=True)

    # Run ffmpeg for each video
    # this ffmpeg utility will provide us with images 
    # of video frames at 10 fps.
    ffmpeg.input(filename).filter("fps", fps=10).output(f'{dir_path}/frame_%04d.png').run()

# we end on a happy note!
print("Processing completed for all videos!")
