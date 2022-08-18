import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text
import os

executable = None
apps = []
root = tk.Tk()
root.geometry('683x384')
root.title('App Automation')
root.iconbitmap('icon.ico')


def addapp():
    executable = filedialog.askopenfilename(initialdir="/", title="Select Files", filetypes=(("executable", "*.exe"), ("All Files", "*.*")))
    if executable != '':
        apps.append(executable)
        list = tk.Label(canvas, text=executable, fg='white', bg='SlateBlue1')
        list.pack()


def startapp():
    for app in apps:
        os.startfile(app)


filename = PhotoImage(file='freeman-zhou-oV9hp8wXkPE-unsplash.png')
canvas = Canvas(root, height=768, width=1366, bg='Blue')
canvas.create_image(0, 0, anchor=NW, image=filename, state='disabled')
canvas.pack(expand=1, fill='both')

openfile = tk.Button(canvas, text="Open File", padx=20, pady=10, fg='black', bg='white', command=addapp, relief='ridge')
openfile.pack()

runapps = tk.Button(canvas, text="Run Apps", padx=30, pady=10, fg='black', bg='white', relief='ridge', command=startapp)
runapps.pack(side='bottom')

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        apps = f.read().split(',')
    for app in apps:
        oldlist = tk.Label(canvas, text=app, fg='white', bg='SlateBlue1')
        oldlist.pack()


root.mainloop()

i = 0

with open('save.txt', 'w')as f:
    for app in apps:
        i += 1
        if app != '':
            if len(apps) != i:
                f.write(app + ',')
            else:
                f.write(app)
    f.close()

with open('save.txt', 'r') as fr:
    if fr.read() == '':
        fr.close()
        os.remove('save.txt')