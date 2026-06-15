import tkinter as tk
import time
from PIL import Image , ImageTk

root = tk.Tk()
root.title("Photo Slide Show")
root.geometry("800x600")

image_paths= [
  r"C:\Users\suryank\Desktop\album\img (1).jpg" , 
  r"C:\Users\suryank\Desktop\album\img (2).webp",
  r"C:\Users\suryank\Desktop\album\img (3).webp",
  r"C:\Users\suryank\Desktop\album\img (4).jpg",
]

images=[]
for path in image_paths:
  img=Image.open(path)
  image_size = (800, 600)
  img= img.resize(image_size)
  images.append(img)

final_images=[]
for img in images:
  photo= ImageTk.PhotoImage(img)
  final_images.append(photo)

image_label=tk.Label(root)
image_label.pack(pady=30)

def slideshow():
  for photo in final_images:
    image_label.config(image=photo)
    image_label.image=photo
    root.update()
    time.sleep(2)


play_button = tk.Button(
  root,
  text="Play the Slideshow",
  font=("Arial",16),
  command=slideshow
)
play_button.pack(pady=20)


root.mainloop()