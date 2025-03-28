import ffmpeg
import os
import shutil

# Create the ./output dir if it doesn't exist
output_dir = './output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir, exist_ok=True)

# Define video filenames
filenames = ["lambo.mp4", "bronco.mp4"]

for filename in filenames:
    dir_path = f"{output_dir}/{filename}"
    if os.path.exists(dir_path):
        for img_name in os.listdir(dir_path):
            os.remove(f"{dir_path}/{img_name}")

    # Create the directories for each video
    os.makedirs(dir_path, exist_ok=True)

    # Run ffmpeg for each video
    ffmpeg.input(filename).filter("fps", fps=10).output(f'{dir_path}/frame_%04d.png').run()

print("Processing completed for all videos!")
