import os
from PIL import Image

src = 'static/originals'
dest = 'static/compressed'

def compress_originals():
    originals = os.listdir(src)
    for original in originals:
        filename = os.path.join(src, original)
        full = os.path.join(dest, original)
        with Image.open(filename) as img:
            img.save(
                full,
                "JPEG",
                optimize=True,
                quality=70,
                progressive=True 
            )
        print(f"✅ File compressed successfully: {full}")

if __name__=='__main__':
    compress_originals()