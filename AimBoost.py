import tkinter as tk
from tkinter import ttk
import time
import os
import tkinter.messagebox

root = tk.Tk()
root.title("Aim Boost")

progress = ttk.Progressbar(root, orient = "horizontal", length = 100, mode = 'determinate') 
progress.place(x=30, y=60, width=200)

w = tk.Label(root, text="")
w.place(x=30, y=90)

def install():
    w.config(text="Locating...")
    progress['value'] = 20
    root.update_idletasks() 
    time.sleep(1) 
    
    w.config(text="Making Folders...")
    progress['value'] = 40
    root.update_idletasks() 
    time.sleep(2) 
    
    w.config(text="Patching Data...")
    progress['value'] = 50
    root.update_idletasks() 
    time.sleep(1.5) 
    
    w.config(text="Dowloading Config Data...")
    progress['value'] = 60
    root.update_idletasks() 
    time.sleep(3) 
    filename = "readme.txt"

    path = "C:/AimBoost"
    if not os.path.exists(path):
            os.makedirs(path)
    else:
        print("already is made")
    filepath = os.path.join(path, filename)

    with open(filepath, "w") as f:
        f.write("This cheat is for educational purposes only and any illegal action used with this cheat is the responsibility of the buyer.\nAim Boosts grants 40 percent more aim. This makes it undetectable and op. This cheat works on the following games:\n\nFortnite\nValorant\n\nI am currently working on adding more game capability.")

    filenam = "INSTRUCTIONS.txt"

    pat = "C:/AimBoost"
    if not os.path.exists(pat):
            os.makedirs(pat)
    else:
        print("already is made")
    filepat = os.path.join(pat, filenam)

    with open(filepat, "w") as f:
         f.write("Open your game and then run AimBoost.exe")
    filena = "AimBoost.bat"

    pa = "C:/AimBoost"
    if not os.path.exists(pa):
            os.makedirs(pa)
    else:
        print("already is made")
    filepa = os.path.join(pa, filena)

    with open(filepa, "w") as f:
         f.write('echo "AimBoost has started, run game to continue"')

    progress['value'] = 80
    root.update_idletasks() 
    time.sleep(1) 
    progress['value'] = 100
    w.config(text="Done!")
    tkinter.messagebox.showinfo("Installed",  "Installed at C:/AimBoost")

e = ttk.Button(text="Install", command=install)

e.place(x=90, y=20)

root.geometry("260x150")
root.mainloop()