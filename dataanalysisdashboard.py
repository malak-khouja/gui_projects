import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import pandas as pd

def load_data():
    df=pd.read_csv("Titanic-Dataset.csv")
    df.info()


def showinfo():
    showinfo(title='Information', message='csv file loaded successfully')

win=tk.Tk()
win.geometry("250x100")
win.title("data analysis dashboard")
label1=tk.Label(win,text="enter csv file url : ")
label1.pack()
text1=tk.StringVar()
label1=ttk.Entry(win,textvariable=text1)
label1.pack()
button1=ttk.Button(win,text="load csv file",command=showinfo)
button1.pack()
win.mainloop()

