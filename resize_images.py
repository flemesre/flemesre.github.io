# Script to automatically create smaller versions of blog post images.
__author__ = "François-Guillaume Lemesre"

import argparse
from pathlib import Path
from tqdm import tqdm
from PIL import Image


def parse_config():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", type=str, default="static/images/",
                        help="Path to directory containing image files to resize.")
    parser.add_argument("--scale_factor", type=float, default=0.3,
                        help="Decimal scale factor to resize images by.")
    return parser.parse_args()


config = parse_config()
input_dir = Path(config.i)
image_files = [f for f in input_dir.glob("**/*") if f.is_file()]

for im_f in tqdm(image_files, colour="green"):
    img_extension = im_f.suffix
    img = Image.open(im_f)
    w, h = img.width, img.height
    img_resized = img.resize((int(w * config.scale_factor), int(h * config.scale_factor)))
    img_resized.save((input_dir / Path(im_f.stem + "_small" + img_extension)))

print("Done.")
