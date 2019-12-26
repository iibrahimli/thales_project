import tkinter as tk
from PIL import Image, ImageTk

import message
import cpu


WIDTH = 1200
HEIGHT = 400
BG_IMG_PATH = "bg.png"


# set up CPU

proc = cpu()


# set up GUI

root = tk.Tk()
root.title("Alpha")
root.geometry(f"{WIDTH}x{HEIGHT}")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

bg_img = ImageTk.PhotoImage(Image.open(BG_IMG_PATH).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
canvas.background = bg_img
bg = canvas.create_image(0, 0, anchor=tk.NW, image=bg_img)

route_entry = tk.Entry(root, width=28)
route_entry_w = canvas.create_window(WIDTH-250, HEIGHT-90, anchor=tk.NW, window=route_entry)

def set_route_clicked():
    print(f"set route <{route_entry.get()}>")

set_route_b = tk.Button(root, text="Set Route", command=set_route_clicked, width=10, height=1)
set_route_w = canvas.create_window(WIDTH-130, HEIGHT-50, anchor=tk.NW, window=set_route_b)

def clear_route_clicked():
    route_entry.delete(0, tk.END)

clear_route_b = tk.Button(root, text="Clear Route", command=clear_route_clicked, width=10, height=1)
clear_route_w = canvas.create_window(WIDTH-250, HEIGHT-50, anchor=tk.NW, window=clear_route_b)

root.mainloop()

