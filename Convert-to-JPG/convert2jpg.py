import os
import sys
from PIL import Image

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        im = Image.open(sys.argv[1])
        target_name = f"{sys.argv[1]}.jpg"
        rgb_im = im.convert('RGB')
        rgb_im.save(target_name)
        print(f"Saved as {target_name}")
    else:
        print(f"{sys.argv[1]} not found")
else:
    print("Usage: convert2jpg.py <file>")
