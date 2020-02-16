from time import sleep
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
root.title("Alpha")
root.geometry("{}x{}".format(WIDTH, HEIGHT))

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

# set track lines
track_kwargs = {
    'width': 5,
}

tr_2v = canvas.create_line(45, 80,
                           100, 80,
                           fill='gray',
                           **track_kwargs)

tr_2b = canvas.create_line(100, 80,
                           195, 80,
                           fill='gray',
                           **track_kwargs)

tr_2a = canvas.create_line(195, 80,
                           448, 80,
                           fill='gray',
                           **track_kwargs)

tr_2c = canvas.create_line(448, 80,
                           663, 80,
                           fill='gray',
                           **track_kwargs)

tr_4 = canvas.create_line(663, 80,
                          1185, 80,
                          fill='gray',
                          **track_kwargs)

tr_1v = canvas.create_line(44, 134,
                           100, 134,
                           fill='gray',
                           **track_kwargs)

tr_1b = canvas.create_line(100, 134,
                           164, 134,
                           fill='gray',
                           **track_kwargs)

tr_1a = canvas.create_line(164, 134,
                           292, 134,
                           fill='gray',
                           **track_kwargs)

tr_1as = canvas.create_line(292, 134,
                            460, 134,
                            fill='gray',
                            **track_kwargs)

tr_1s = canvas.create_line(460, 134,
                           664, 134,
                           fill='gray',
                           **track_kwargs)

tr_1d = canvas.create_line(664, 134,
                           1068, 134,
                           fill='gray',
                           **track_kwargs)

tr_2d = canvas.create_line(1068, 134,
                           1185, 134,
                           fill='gray',
                           **track_kwargs)

track_sections = {
    'tr_2v':  tr_2v,
    'tr_2b':  tr_2b,
    'tr_2a':  tr_2a,
    'tr_2c':  tr_2c,
    'tr_4':   tr_4,
    'tr_1v':  tr_1v,
    'tr_1b':  tr_1b,
    'tr_1a':  tr_1a,
    'tr_1as': tr_1as,
    'tr_1s':  tr_1s,
    'tr_1d':  tr_1d,
    'tr_2d':  tr_2d
}

# set signals
sg_A2_red_c = (225, 102)
sg_A2_red = canvas.create_oval(sg_A2_red_c[0] - 9,
                               sg_A2_red_c[1] - 9,
                               sg_A2_red_c[0] + 9,
                               sg_A2_red_c[1] + 9,
                               fill='red')

sg_A2_green_c = (243, 102)
sg_A2_green = canvas.create_oval(sg_A2_green_c[0] - 9,
                                 sg_A2_green_c[1] - 9,
                                 sg_A2_green_c[0] + 9,
                                 sg_A2_green_c[1] + 9,
                                 fill='light gray')

sg_E2_red_c = (414, 61)
sg_E2_red = canvas.create_oval(sg_E2_red_c[0] - 9,
                               sg_E2_red_c[1] - 9,
                               sg_E2_red_c[0] + 9,
                               sg_E2_red_c[1] + 9,
                               fill='red')

sg_E2_green_c = (396, 61)
sg_E2_green = canvas.create_oval(sg_E2_green_c[0] - 9,
                                 sg_E2_green_c[1] - 9,
                                 sg_E2_green_c[0] + 9,
                                 sg_E2_green_c[1] + 9,
                                 fill='light gray')

sg_A4_red_c = (479, 98)
sg_A4_red = canvas.create_oval(sg_A4_red_c[0] - 9,
                               sg_A4_red_c[1] - 9,
                               sg_A4_red_c[0] + 9,
                               sg_A4_red_c[1] + 9,
                               fill='red')

sg_A4_green_c = (497, 98)
sg_A4_green = canvas.create_oval(sg_A4_green_c[0] - 9,
                                 sg_A4_green_c[1] - 9,
                                 sg_A4_green_c[0] + 9,
                                 sg_A4_green_c[1] + 9,
                                 fill='light gray')

sg_E1_red_c = (631, 116)
sg_E1_red = canvas.create_oval(sg_E1_red_c[0] - 9,
                               sg_E1_red_c[1] - 9,
                               sg_E1_red_c[0] + 9,
                               sg_E1_red_c[1] + 9,
                               fill='red')

sg_E1_green_c = (613, 116)
sg_E1_green = canvas.create_oval(sg_E1_green_c[0] - 9,
                                 sg_E1_green_c[1] - 9,
                                 sg_E1_green_c[0] + 9,
                                 sg_E1_green_c[1] + 9,
                                 fill='light gray')

sg_A1_red_c = (195, 152)
sg_A1_red = canvas.create_oval(sg_A1_red_c[0] - 9,
                               sg_A1_red_c[1] - 9,
                               sg_A1_red_c[0] + 9,
                               sg_A1_red_c[1] + 9,
                               fill='red')

sg_A1_green_c = (213, 152)
sg_A1_green = canvas.create_oval(sg_A1_green_c[0] - 9,
                                 sg_A1_green_c[1] - 9,
                                 sg_A1_green_c[0] + 9,
                                 sg_A1_green_c[1] + 9,
                                 fill='light gray')

sg_A3_red_c = (491, 152)
sg_A3_red = canvas.create_oval(sg_A3_red_c[0] - 9,
                               sg_A3_red_c[1] - 9,
                               sg_A3_red_c[0] + 9,
                               sg_A3_red_c[1] + 9,
                               fill='red')

sg_A3_green_c = (509, 152)
sg_A3_green = canvas.create_oval(sg_A3_green_c[0] - 9,
                                 sg_A3_green_c[1] - 9,
                                 sg_A3_green_c[0] + 9,
                                 sg_A3_green_c[1] + 9,
                                 fill='light gray')

track_signals = {
    'sg_A2_red':   sg_A2_red,
    'sg_A2_green': sg_A2_green,
    'sg_E2_red':   sg_E2_red,
    'sg_E2_green': sg_E2_green,
    'sg_A4_red':   sg_A4_red,
    'sg_A4_green': sg_A4_green,
    'sg_E1_red':   sg_E1_red,
    'sg_E1_green': sg_E1_green,
    'sg_A1_red':   sg_A1_red,
    'sg_A1_green': sg_A1_green,
    'sg_A3_red':   sg_A3_red,
    'sg_A3_green': sg_A3_green
}

def simulate_route(route, can, sections, signals):
    """
    Simulate train movement on given route.
    Assuming route is safe and valid.

    """

    section_time_coef = 10
    route_sects = []
    route_signals_red = []
    route_signals_green = []

    if route == 'A1 A3':
        route_sects = ['tr_1a',
                      'tr_1as']
        route_signals_red = ['sg_A1_red',]
        route_signals_green = ['sg_A1_green',]

    elif route == 'A2 A3':
        route_sects = ['tr_2a',
                      'tr_1as']
        route_signals_red = ['sg_A2_red',]
        route_signals_green = ['sg_A2_green',]

    elif route == 'A2 A4':
        route_sects = ['tr_2a']
        route_signals_red = ['sg_A2_red',]
        route_signals_green = ['sg_A2_green',]

    elif route == 'E1 z2':
        route_sects = ['tr_1s',
                      'tr_1as',
                      'tr_2a',
                      'tr_2b',
                      'tr_2v']
        route_signals_red = ['sg_E1_red',]
        route_signals_green = ['sg_E1_green',]

    elif route == 'E1 z1':
        route_sects = ['tr_1s',
                      'tr_1as',
                      'tr_1a',
                      'tr_1b',
                      'tr_1v']
        route_signals_red = ['sg_E1_red',]
        route_signals_green = ['sg_E1_green',]

    elif route == 'E2 z2':
        route_sects = ['tr_2a',
                      'tr_2b',
                      'tr_2v']
        route_signals_red = ['sg_E2_red',]
        route_signals_green = ['sg_E2_green',]

    for rs in route_sects:
        can.itemconfig(sections[rs], fill='green')
    
    for sgg in route_signals_green:
        can.itemconfig(signals[sgg], fill='green')
    for sgr in route_signals_red:
        can.itemconfig(signals[sgr], fill='light gray')
    
    for rs in route_sects:
        print("Currently in section: {}".format(rs))
        bounds = can.bbox(sections[rs])
        section_length = bounds[2] - bounds[0]
        can.itemconfig(sections[rs], fill='red')
        print("length: {}".format(section_length))

        wvar = tk.IntVar()
        can.after(int(section_length * section_time_coef + 250),
                  wvar.set, 1)
        can.wait_variable(wvar)
        
        can.itemconfig(sections[rs], fill='green')

    for rs in route_sects:
        can.itemconfig(sections[rs], fill='gray')
    
    for sgg in route_signals_green:
        can.itemconfig(signals[sgg], fill='light gray')
    for sgr in route_signals_red:
        can.itemconfig(signals[sgr], fill='red')
        

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
    print("set route <{}>".format(route))
    if not route:
        return
    if len(route.split()) != 2 or route not in proc.elements[ROUTE]:
        messagebox.showerror("Failure", "Invalid route <{}>".format(route))
    else:
        safe = proc.check_safety(ROUTE, route, SET)
        print(route, "is safe:", safe)
        if not safe:
            messagebox.showerror("Failure", "Route <{}> failed safety check".format(route))
        else:
            proc.recv_message(message(ROUTE, route, SET))
            cur_route_l.config(text="Current route: {}".format(proc.current_route))
            simulate_route(route, canvas, track_sections, track_signals)
            clear_route_clicked()

set_route_b = tk.Button(root, text="Set Route", command=set_route_clicked, width=22, height=1)
set_route_w = canvas.create_window(WIDTH-20, HEIGHT-70, anchor=tk.NE, window=set_route_b)

def clear_route_clicked():
    route_entry.delete(0, tk.END)
    proc.recv_message(message(ROUTE, proc.current_route, UNSET))
    cur_route_l.config(text="Current route: NONE")

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
        messagebox.showerror("Failure", "Invalid checkbox state for switchpoint 1")
        return

    if sp_2_plus.get() == 1 and sp_2_minus.get() == 0:
        sp_2_state = PLUS
        sp_2_indicator = sp_2_close
    elif sp_2_plus.get() == 0 and sp_2_minus.get() == 1:
        sp_2_state = MINUS
        sp_2_indicator = sp_2_open
    else:
        messagebox.showerror("Failure", "Invalid checkbox state for switchpoint 2")
        return

    if sp_1a_plus.get() == 1 and sp_1a_minus.get() == 0:
        sp_1a_state = PLUS
        sp_1a_indicator = sp_1a_close
    elif sp_1a_plus.get() == 0 and sp_1a_minus.get() == 1:
        sp_1a_state = MINUS
        sp_1a_indicator = sp_1a_open
    else:
        messagebox.showerror("Failure", "Invalid checkbox state for switchpoint 1a")
        return

    if sp_2a_plus.get() == 1 and sp_2a_minus.get() == 0:
        sp_2a_state = PLUS
        sp_2a_indicator = sp_2a_close
    elif sp_2a_plus.get() == 0 and sp_2a_minus.get() == 1:
        sp_2a_state = MINUS
        sp_2a_indicator = sp_2a_open
    else:
        messagebox.showerror("Failure", "Invalid checkbox state for switchpoint 2a")
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