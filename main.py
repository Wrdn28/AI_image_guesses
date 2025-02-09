import tkinter as tk
import os
import Ai
from PIL import Image, ImageTk, ImageDraw
import numpy as np

model = Ai.load_ai()

window = tk.Tk()
window.title("Image Drawing AI")

canvas_color = (173, 216, 230)
line_color = (0, 0, 255)
img_size = (500, 500)
img = Image.new(mode="RGB", size=img_size, color=canvas_color)

tkimage = ImageTk.PhotoImage(img)
canvas = tk.Label(window, image=tkimage)
canvas.pack()

draw = ImageDraw.Draw(img)
prediction = tk.StringVar()
label = tk.Label(window, textvariable=prediction)
label.pack()

last_point = (0, 0)
def draw_image(event):
    global last_point, tkimage
    current_point = (event.x, event.y)
    draw.line([last_point, current_point], fill=line_color, width=30)
    last_point = current_point
    update_canvas()
    predict_image()

def start_draw(event):
    global last_point
    last_point = (event.x, event.y)

def update_canvas():
    global tkimage
    tkimage = ImageTk.PhotoImage(img)
    canvas['image'] = tkimage
    canvas.pack()

def predict_image():
    img_temp = img.convert("L") 
    img_temp = img.resize((28, 28))
    img_temp = np.array(img_temp).flatten()
    output = model.predict([img_temp])
    
    predictions = {
        0: "Ini adalah gambar kotak",
        1: "Ini adalah gambar lingkaran",
        2: "Ini adalah gambar segitiga",
        3: "Ini adalah gambar garis lurus"
    }
    
    prediction.set(predictions.get(output[0], "Gambar tidak dikenali"))

def reset_canvas(event):
    global img, draw
    img = Image.new(mode="RGB", size=img_size, color=canvas_color)
    draw = ImageDraw.Draw(img)
    update_canvas()

def save_image(event):
    img_temp = img.resize((28, 28))

    folder_map = {
        "k": "kotak",
        "l": "lingkaran",
        "g": "garislurus",
        "s": "segitiga"
    }

    if event.char in folder_map:
        folder = folder_map[event.char]

        if not os.path.exists(folder):
            os.makedirs(folder)

        existing_files = len([name for name in os.listdir(folder) if name.endswith(".png")])

        img_temp.save(f"{folder}/{existing_files}.png")

window.bind("<B1-Motion>", draw_image)
window.bind("<ButtonPress-1>", start_draw)
window.bind("<ButtonPress-3>", reset_canvas)
window.bind("<Key>", save_image)


window.mainloop()
