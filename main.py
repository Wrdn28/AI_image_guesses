import tkinter as tk
import Ai
from PIL import Image, ImageTk, ImageDraw
import numpy as np

model = Ai.load_ai()
window = tk.Tk()

img = Image.new(mode="RGB", size=(500, 500), color=0) 
label = tk.Label(window, textvariable=prediction) 
tkimage = ImageTk.PhotoImage(img)
canvas = tk.Label(window, image=tkimage)
canvas.pack()

draw = ImageDraw.Draw(img)

last_point = (0, 0)
line_color = (0, 0, 255)
prediction = tk.StringVar()
label = tk.Label(window, textvariable=prediction) 

def draw_image(event):
    global last_point, tkimage, prediction
    current_point = (event.x, event.y)
    draw.line([last_point, current_point], fill=line_color, width=30)
    last_point = current_point
    tkimage = ImageTk.PhotoImage(img)
    canvas['image'] = tkimage
    canvas.pack()
    img_temp = img.resize((28, 28))
    img_temp = np.array(img_temp)
    img_temp = img_temp.flatten()
    output = model.predict([img_temp])
    if (output[0] == 0):
        prediction("Ini adalah gambar kotak")
    elif(output[0] == 1):
        prediction("Ini adalah gambar lingkaran")
    elif(output[0] == 2):
        prediction("Ini adalah gambar segitiga")
    else:
        prediction("Ini adalah gambar garislurus")
    label.pack()

def start_draw(event):
    global last_point
    last_point = (event.x, event.y)

def reset_canvas(event):
    global tkimage, img, draw
    img = Image.new(mode="RGB", size=(500, 500), color=0)
    tkimage = ImageTk.PhotoImage(img)
    draw = ImageDraw.Draw(img)
    canvas['image'] = tkimage
    canvas.pack()

kotak = 0
lingkaran = 0
garisluruslurus = 0
segitiga = 0

def save_image(event):
    global kotak, lingkaran, segitiga, garislurus
    img_temp = img.resize((28, 28))
    if(event.char == "k"):
        img_temp.save(f"kotak/{kotak}.png")
        kotak += 1
    elif(event.char == "l"):
        img_temp.save(f"lingkaran/{lingkaran}.png")
        lingkaran += 1
    elif(event.char == "g"):
        img_temp.save(f"garislurus/{garislurus}.png")
        garislurus += 1
    elif(event.char == "s"):
        img_temp.save(f"segitiga/{segitiga}.png")
        segitiga += 1

window.bind("<B1-Motion>", draw_image)
window.bind("<ButtonPress-1>", start_draw)
window.bind("<ButtonPress-3>", reset_canvas)
window.bind("<Key>", save_image)

label.pack

window.mainloop()
