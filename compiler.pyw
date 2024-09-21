from tkinter import *
from pyautogui import *
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showerror
from os import startfile, path
from keyboard import add_hotkey, wait
from sys import argv, exit

def compile():
    file.seek(0)
    for line in file.readlines():
        if line.strip().startswith("open: "):
            try: startfile(line.strip().removeprefix("open: "))
            except: showerror(file.name, f"Couldn't open {line.strip().removeprefix('open: ')}: File not found!")
        if line.strip().startswith("move_mouse: "):
            args = line.strip().removeprefix("move_mouse: ").split(",")
            x, y, dur = int(args[0].strip()), int(args[1].strip()), float(args[2].strip())
            try: moveTo(x, y, dur)
            except: showerror(file.name, "Couldn't move mouse: Try entering integers! (ints don't apply to duration tho :])")
        if line.strip().startswith("click_mouse: "):
            button = line.strip().removeprefix("click_mouse: ")
            if button == "left": leftClick()
            elif button == "right": rightClick()
            elif button == "middle": middleClick()
            else: showerror(file.name, "Couldn't click mouse: Invalid button name!")
        if line.strip().startswith("keyboard: "):
            hk_bare = line.strip().removeprefix("keyboard: ").split(",")
            hk = []
            for x in hk_bare: hk.append(x.strip())
            try: hotkey(*hk)
            except: showerror(file.name, "Couldn't do hotkeys: Invalid keys!")
        if line.strip().startswith("type: "): typewrite(line.strip().removeprefix("type: "))
        if line.strip().startswith("screenshot: "):
            args = line.strip().removeprefix("screenshot: ").split(",")
            try: screenshot(path.join(args[0].strip(), args[1].strip()))
            except: showerror(file.name, "Couldn't screenshot: Try entering a valid path!")

def choose_file():
        global file
        file = askopenfile()
        if not file.name.endswith(".pauto"): 
            showerror("Error", "Invalid file. File must be a PAutomation file!")
            return
        add_hotkey("ctrl+alt+r", compile)
        compile()
        wait("ctrl+q")

try:
    if argv[1].endswith(".pauto") and path.exists(argv[1]):
        global file
        file = open(argv[1])
        if not file.name.endswith(".pauto"): 
            showerror("Error", "Invalid file. File must be a PAutomation file!")
            exit()
        add_hotkey("ctrl+alt+r", compile)
        compile()
        wait("ctrl+q")
except: choose_file()
