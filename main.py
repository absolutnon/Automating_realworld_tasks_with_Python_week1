
#!/usr/bin/python3

from PIL import Image
import os

def convert_files():
        dir1 = "images"
        dir2 = "/opt/icons/"

        for filename in os.listdir(dir1):
                if not filename.startswith('.'):
                        f = os.path.join(dir1, filename)
                        im = Image.open(f)
                        rgb_im = im.convert("RGB").rotate(270).resize((128, 128)).save(dir2 + filename + ".jpeg")

if __name__ == '__main__':
        convert_files()
