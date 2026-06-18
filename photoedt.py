from string.templatelib import convert
from PIL import Image, ImageEnhance, ImageFilter
import os

path = r'C:/Users/suryank/Desktop/album'
pathout = r'C:/Users/suryank/Desktop/editedimgs'

for filename in os.listdir(path):
  img = Image.open(f"{path}/{filename}")

  edit =img.filter(ImageFilter.SHARPEN).convert('L')
  clean_name= os.path.splitext(filename)[0]
  edit.save(f"{pathout}/{clean_name}_edited.jpg")
   