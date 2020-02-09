import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

from util import *
from message import message
import cpu


WIDTH = 1200
HEIGHT = 400
BG_IMG_PATH = "bg.png"


# set up CPU

proc = cpu.cpu()


# set up GUI

root = tk.Tk()
root.title("Demo")
root.geometry(f"{WIDTH}x{HEIGHT}")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

bg_img = ImageTk.PhotoImage(Image.open(BG_IMG_PATH).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
canvas.background = bg_img
bg = canvas.create_image(0, 0, anchor=tk.NW, image=bg_img)

routes_desc_l = tk.Label(root, text="Enter a route to set:")
routes_desc_w = canvas.create_window(900, HEIGHT-160, anchor=tk.NE, window=routes_desc_l)

route_entry = tk.Entry(root, width=51)
route_entry_w = canvas.create_window(WIDTH-20, HEIGHT-120, anchor=tk.NE, window=route_entry)

cur_route_l = tk.Label(root, text="Current route: NONE")
cur_route_w = canvas.create_window(1100, HEIGHT-160, anchor=tk.NE, window=cur_route_l)

# set switchpoint indicators
sp_1_open = ImageTk.PhotoImage(Image.open("sp_open.png").resize((40, 10), Image.ANTIALIAS).transpose(Image.FLIP_LEFT_RIGHT))
sp_1_close = ImageTk.PhotoImage(Image.open("sp_close.png").resize((40, 10), Image.ANTIALIAS).transpose(Image.FLIP_LEFT_RIGHT))

sp_1a_open = ImageTk.PhotoImage(Image.open("sp_open.png").resize((40, 10), Image.ANTIALIAS))
sp_1a_close = ImageTk.PhotoImage(Image.open("sp_close.png").resize((40, 10), Image.ANTIALIAS))

sp_2_open = ImageTk.PhotoImage(Image.open("sp_open.png").resize((40, 10), Image.ANTIALIAS).transpose(Image.FLIP_TOP_BOTTOM))
sp_2_close = ImageTk.PhotoImage(Image.open("sp_close.png").resize((40, 10), Image.ANTIALIAS).transpose(Image.FLIP_TOP_BOTTOM))

sp_2a_open = ImageTk.PhotoImage(Image.open("sp_open.png").resize((40, 10), Image.ANTIALIAS).transpose(Image.FLIP_TOP_BOTTOM).transpose(Image.FLIP_LEFT_RIGHT))
sp_2a_close = ImageTk.PhotoImage(Image.open("sp_close.png").resize((40, 10), Image.ANTIALIAS).transpose(Image.FLIP_TOP_BOTTOM).transpose(Image.FLIP_LEFT_RIGHT))

sp_1_i_l = tk.Label(root, image=sp_1_open)
sp_1_i_w = canvas.create_window(485, 128, anchor=tk.NW, window=sp_1_i_l)

sp_1a_i_l = tk.Label(root, image=sp_1a_open)
sp_1a_i_w = canvas.create_window(375, 128, anchor=tk.NW, window=sp_1a_i_l)

sp_2_i_l = tk.Label(root, image=sp_2_open)
sp_2_i_w = canvas.create_window(566, 76, anchor=tk.NW, window=sp_2_i_l)

sp_2a_i_l = tk.Label(root, image=sp_2a_open)
sp_2a_i_w = canvas.create_window(286, 76, anchor=tk.NW, window=sp_2a_i_l)

def set_route_clicked():
    route = route_entry.get()
    print(f"set route <{route}>")
    if not route:
        return
    if len(route.split()) != 2 or route not in proc.elements[ROUTE]:
        messagebox.showerror("Failure", f"Invalid route <{route}>")
    else:
        safe = proc.check_safety(ROUTE, route, SET)
        print(route, "is safe:", safe)
        if not safe:
            messagebox.showerror("Failure", f"Route <{route}> failed safety check")
        else:
            proc.recv_message(message(ROUTE, route, SET))
            cur_route_l.config(text=f"Current route: {proc.current_route}")

set_route_b = tk.Button(root, text="Set Route", command=set_route_clicked, width=22, height=1)
set_route_w = canvas.create_window(WIDTH-20, HEIGHT-70, anchor=tk.NE, window=set_route_b)

def clear_route_clicked():
    route_entry.delete(0, tk.END)
    proc.recv_message(message(ROUTE, proc.current_route, UNSET))
    cur_route_l.config(text=f"Current route: NONE")

clear_route_b = tk.Button(root, text="Clear Route", command=clear_route_clicked, width=22, height=1)
clear_route_w = canvas.create_window(WIDTH-234, HEIGHT-70, anchor=tk.NE, window=clear_route_b)


# "simulator"

sim_desc_l = tk.Label(root, text="Simulator module")
sim_desc_w = canvas.create_window(20, 200, anchor=tk.NW, window=sim_desc_l)

sp_1_plus  = tk.IntVar()
sp_1_minus = tk.IntVar()

sp_2_plus  = tk.IntVar()
sp_2_minus = tk.IntVar()

sp_1a_plus  = tk.IntVar()
sp_1a_minus = tk.IntVar()

sp_2a_plus  = tk.IntVar()
sp_2a_minus = tk.IntVar()

def set_sp_states():
    if sp_1_plus.get() == 1 and sp_1_minus.get() == 0:
        sp_1_state = PLUS
        sp_1_indicator = sp_1_close
    elif sp_1_plus.get() == 0 and sp_1_minus.get() == 1:
        sp_1_state = MINUS
        sp_1_indicator = sp_1_open
    else:
        messagebox.showerror("Failure", f"Invalid checkbox state for switchpoint 1")
        return

    if sp_2_plus.get() == 1 and sp_2_minus.get() == 0:
        sp_2_state = PLUS
        sp_2_indicator = sp_2_close
    elif sp_2_plus.get() == 0 and sp_2_minus.get() == 1:
        sp_2_state = MINUS
        sp_2_indicator = sp_2_open
    else:
        messagebox.showerror("Failure", f"Invalid checkbox state for switchpoint 2")
        return

    if sp_1a_plus.get() == 1 and sp_1a_minus.get() == 0:
        sp_1a_state = PLUS
        sp_1a_indicator = sp_1a_close
    elif sp_1a_plus.get() == 0 and sp_1a_minus.get() == 1:
        sp_1a_state = MINUS
        sp_1a_indicator = sp_1a_open
    else:
        messagebox.showerror("Failure", f"Invalid checkbox state for switchpoint 1a")
        return

    if sp_2a_plus.get() == 1 and sp_2a_minus.get() == 0:
        sp_2a_state = PLUS
        sp_2a_indicator = sp_2a_close
    elif sp_2a_plus.get() == 0 and sp_2a_minus.get() == 1:
        sp_2a_state = MINUS
        sp_2a_indicator = sp_2a_open
    else:
        messagebox.showerror("Failure", f"Invalid checkbox state for switchpoint 2a")
        return

    # update switchpoint indicators
    sp_1_i_l.configure(image=sp_1_indicator)
    sp_2_i_l.configure(image=sp_2_indicator)
    sp_1a_i_l.configure(image=sp_1a_indicator)
    sp_2a_i_l.configure(image=sp_2a_indicator)

    proc.set_elem_state(SWITCHPOINT, "1", sp_1_state)
    proc.set_elem_state(SWITCHPOINT, "2", sp_2_state)
    proc.set_elem_state(SWITCHPOINT, "1a", sp_1a_state)
    proc.set_elem_state(SWITCHPOINT, "2a", sp_2a_state)


sp_1_l = tk.Label(root, text="Switchpoint 1")
sp_1_l_w = canvas.create_window(20, 240, anchor=tk.NW, window=sp_1_l)
sp_1_m = tk.Checkbutton(root, text=' -  ', variable=sp_1_minus, onvalue=1, offvalue=0, width=4, anchor=tk.W)
sp_1_m_w = canvas.create_window(180, 240, anchor=tk.NW, window=sp_1_m)
sp_1_p = tk.Checkbutton(root, text=' +  ', variable=sp_1_plus, onvalue=1, offvalue=0, width=4, anchor=tk.W)
sp_1_p_w = canvas.create_window(240, 240, anchor=tk.NW, window=sp_1_p)

sp_2_l = tk.Label(root, text="Switchpoint 2")
sp_2_l_w = canvas.create_window(20, 280, anchor=tk.NW, window=sp_2_l)
sp_2_m = tk.Checkbutton(root, text=' -  ', variable=sp_2_minus, onvalue=1, offvalue=0, width=4, anchor=tk.W)
sp_2_m_w = canvas.create_window(180, 280, anchor=tk.NW, window=sp_2_m)
sp_2_p = tk.Checkbutton(root, text=' +  ', variable=sp_2_plus, onvalue=1, offvalue=0, width=4, anchor=tk.W)
sp_2_p_w = canvas.create_window(240, 280, anchor=tk.NW, window=sp_2_p)

sp_1a_l = tk.Label(root, text="Switchpoint 1a")
sp_1a_l_w = canvas.create_window(400, 240, anchor=tk.NW, window=sp_1a_l)
sp_1a_m = tk.Checkbutton(root, text=' -  ', variable=sp_1a_minus, onvalue=1, offvalue=0, width=4, anchor=tk.W)
sp_1a_m_w = canvas.create_window(560, 240, anchor=tk.NW, window=sp_1a_m)
sp_1a_p = tk.Checkbutton(root, text=' +  ', variable=sp_1a_plus, onvalue=1, offvalue=0, width=4, anchor=tk.W)
sp_1a_p_w = canvas.create_window(620, 240, anchor=tk.NW, window=sp_1a_p)

sp_2a_l = tk.Label(root, text="Switchpoint 2a")
sp_2a_l_w = canvas.create_window(400, 280, anchor=tk.NW, window=sp_2a_l)
sp_2a_m = tk.Checkbutton(root, text=' -  ', variable=sp_2a_minus, onvalue=1, offvalue=0, width=4, anchor=tk.W)
sp_2a_m_w = canvas.create_window(560, 280, anchor=tk.NW, window=sp_2a_m)
sp_2a_p = tk.Checkbutton(root, text=' +  ', variable=sp_2a_plus, onvalue=1, offvalue=0, width=4, anchor=tk.W)
sp_2a_p_w = canvas.create_window(620, 280, anchor=tk.NW, window=sp_2a_p)

set_sp_b = tk.Button(root, text="Set switchpoint states", command=set_sp_states, width=86, height=1)
set_sp_w = canvas.create_window(20, HEIGHT-70, anchor=tk.NW, window=set_sp_b)

root.mainloop()