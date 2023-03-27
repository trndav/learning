# Script rotate, resize, convert images to JPEG and save to output directory.

#!/usr/bin/env python3
from PIL import Image
import os

# Images input directory.
input_dir = "images/"

# Images output directory.
output_dir = "opt/icons/"

# Rotate, resize, convert images from input directory.
for filename in os.listdir(input_dir) :
    with Image.open(os.path.join(input_dir, filename)) as img:
        img = img.rotate(-90)
        img = img.resize((128, 128))
        img = img.convert("RGB")
    print(filename)

# Save rotated/resized/converted image in output directory.
    output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".jpeg")
    img.save(output_path, format="JPEG")