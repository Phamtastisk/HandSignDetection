import tkinter as tk
import sys

sys.path.append('/.../FingerSpelling/test')

window = tk.Tk()
window.geometry("1400x800")
window.configure(bg="white")
window.rowconfigure(20,weight=1)
window.columnconfigure(35,weight=1)
window.title("The Hangman Game")
entry_var_server = tk.StringVar(window,"")
entry_var_db = tk.StringVar(window,"")
entry_var_driver = tk.StringVar(window,"")

def window_widgets():
    db_ini_frame_top = tk.Frame(master=window,bg="#57b956",height=120,width=1400,highlightbackground="black",highlightthickness=2)
    db_ini_frame_left = tk.Frame(master=window,bg="light grey",height=800,width=120,colormap="new",highlightbackground="black",highlightthickness=2)
    db_ini_main = tk.Frame(master=window,bg="light grey",height=800,width=120,colormap="new",highlightbackground="black",highlightthickness=2)

    db_ini_frame_top.pack(side="top", fill="x")
    db_ini_frame_left.pack(side="left", fill="y")
    db_ini_main.pack(side="top", fill="both", expand=True)

    db_ini_label_top = tk.Label(master=db_ini_frame_top,text="HangMan",bg="#57b956")
    db_ini_label_top.configure(font=("Calibri",26))
    db_ini_label_top.grid(row=1,column=18,sticky="n")

    db_ini_frame_center_nw = tk.Frame(master=db_ini_main,height=200,width=200,bg="blue")
    db_ini_frame_center_sw = tk.Frame(master=db_ini_main,bg="black")
    db_ini_frame_center_ne = tk.Frame(master=db_ini_main,bg="light blue")
    db_ini_frame_center_se = tk.Frame(master=db_ini_main,bg="blue")

    db_ini_main.grid_rowconfigure((0,1), weight=1)
    db_ini_main.grid_columnconfigure((0,1), weight=1)

    db_ini_frame_center_nw.grid(row=0,column=0, sticky="nsew")
    db_ini_frame_center_sw.grid(row=0,column=1, sticky="nsew")
    db_ini_frame_center_ne.grid(row=1,column=0, sticky="nsew")
    db_ini_frame_center_se.grid(row=1,column=1, sticky="nsew")


window_widgets()
window.tk.mainloop()