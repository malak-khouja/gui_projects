import tkinter as tk
from tkinter import ttk

def clear_button():
    entry.delete(0,tk.END)
    
def display_button(value):
    entry.insert(0,value)
    
def calculate_button():
    res=eval(entry.get())
    entry.delete(0,tk.END)
    entry.insert(0, res)
    
win = tk.Tk()
win.resizable(0,0)
win.title("Calculator")
win.columnconfigure(0,weight=5)
win.rowconfigure(0,weight=5)
entry=ttk.Entry(win)
entry.grid(row=0,ipadx=125,ipady=40,columnspan=5,padx=5,pady=5)


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]    

for (text, row, col) in buttons:
    if text =='C':
        style = ttk.Style()
        style.configure("Custom.TButton", background="red")
        btn=ttk.Button(win,text=text,command=clear_button)
        btn.grid(row=row,column=col,padx=5,pady=5,ipadx=5 ,ipady=5,style="Custom.TButton")
    elif text =='=':
        btn=ttk.Button(win,text=text,command=calculate_button)
        btn.grid(row=row,column=col,padx=5,pady=5,ipadx=5 ,ipady=5)
    else :
        ttk.Button(win,text=text,command=lambda t=text: display_button(t)).grid(row=row,column=col,padx=5,pady=5,ipadx=5 ,ipady=5)

win.mainloop()






















'''
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def sum():
    s=int(x.get())+int(y.get())
    showinfo(title="somme",message=f"the sum of {x.get()} + {y.get()} is : {s}")
    
win=tk.Tk()
win.geometry("400x200")
win.title("calculator")
ttk.Label(win,text="calculate sum of two numbers" ).pack(pady=10)

frame = ttk.Frame(win)
frame.pack(pady=10)

win_l=ttk.Frame(frame)
win_l.pack(side=tk.LEFT, padx=20)
label1=ttk.Label(win_l,text="enter first numbers" )
label1.pack()
x=tk.StringVar()
textbox1=ttk.Entry(win_l,textvariable=x)
textbox1.pack()
textbox1.focus()

win_r=ttk.Frame(frame)
win_r.pack(side=tk.RIGHT, padx=20)
label2=ttk.Label(win_r,text="enter second numbers" )
label2.pack()
y=tk.StringVar()
textbox2=ttk.Entry(win_r,textvariable=y)
textbox2.pack()

ttk.Button(win,text="click",command=sum).pack(pady=10)
win.mainloop()
'''