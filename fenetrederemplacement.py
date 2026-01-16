import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title("Replace")
win.resizable(False,False)

frame=ttk.Frame(win)
frame.pack()
frame.columnconfigure(0,weight=1)
frame.rowconfigure(0,weight=3)

framel=ttk.Frame(frame)
framel.grid(column=0,row=0)
framel.columnconfigure(0,weight=1)
framel.rowconfigure(0,weight=3)
label1=tk.Label(framel,text="Find what: ")
label1.grid(column=0,row=0,sticky=tk.W)
text1=tk.StringVar()
entry1=ttk.Entry(framel,textvariable=text1, width=30)
entry1.grid(column=1,row=0,pady=5,padx=5,ipadx=5)
entry1.focus()

label2=tk.Label(framel,text="Replace with: ")
label2.grid(column=0,row=1,sticky=tk.W)
text2=tk.StringVar()
entry2=ttk.Entry(framel,textvariable=text2, width=30)
entry2.grid(column=1,row=1,pady=5,padx=5,ipadx=5)

check1=tk.StringVar()
cb=ttk.Checkbutton(framel,variable=check1,text="Match Case",command=lambda:print(check1.get()))
cb.grid(column=0,row=2,pady=5,padx=5,sticky=tk.W)

check2=tk.StringVar()
cb=ttk.Checkbutton(framel,variable=check2,text="Wrap Around",command=lambda:print(check2.get()))
cb.grid(column=0,row=3,pady=5,padx=5,sticky=tk.W)


framer=ttk.Frame(frame)
framer.grid(column=1,row=0)
framer.columnconfigure(0,weight=0)
framer.rowconfigure(0,weight=3)
button1=ttk.Button(framer,text="Find Next")
button1.grid(column=0,row=0,pady=5,padx=5)
button2=ttk.Button(framer,text="Replace")
button2.grid(column=0,row=1,pady=5,padx=5)
button3=ttk.Button(framer,text="Replace All")
button3.grid(column=0,row=2,pady=5,padx=5)
button4=ttk.Button(framer,text="Cancel")
button4.grid(column=0,row=3,pady=5,padx=5)


win.mainloop()

'''
import tkinter as tk
from tkinter import TclError, ttk


def create_input_frame(container):

    frame = ttk.Frame(container)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)

    # Find what
    ttk.Label(frame, text='Find what:').grid(column=0, row=0, sticky=tk.W)
    keyword = ttk.Entry(frame, width=30)
    keyword.focus()
    keyword.grid(column=1, row=0, sticky=tk.W)

    # Replace with:
    ttk.Label(frame, text='Replace with:').grid(column=0, row=1, sticky=tk.W)
    replacement = ttk.Entry(frame, width=30)
    replacement.grid(column=1, row=1, sticky=tk.W)

    # Match Case checkbox
    match_case = tk.StringVar()
    match_case_check = ttk.Checkbutton(
        frame,
        text='Match case',
        variable=match_case,
        command=lambda: print(match_case.get()))
    match_case_check.grid(column=0, row=2, sticky=tk.W)

    # Wrap Around checkbox
    wrap_around = tk.StringVar()
    wrap_around_check = ttk.Checkbutton(
        frame,
        variable=wrap_around,
        text='Wrap around',
        command=lambda: print(wrap_around.get()))
    wrap_around_check.grid(column=0, row=3, sticky=tk.W)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame


def create_button_frame(container):
    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=1)

    ttk.Button(frame, text='Find Next').grid(column=0, row=0)
    ttk.Button(frame, text='Replace').grid(column=0, row=1)
    ttk.Button(frame, text='Replace All').grid(column=0, row=2)
    ttk.Button(frame, text='Cancel').grid(column=0, row=3)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame


def create_main_window():
    root = tk.Tk()
    root.title('Replace')
    root.resizable(0, 0)
    try:
        # windows only (remove the minimize/maximize button)
        root.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    # layout on the root window
    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=1)

    input_frame = create_input_frame(root)
    input_frame.grid(column=0, row=0)

    button_frame = create_button_frame(root)
    button_frame.grid(column=1, row=0)

    root.mainloop()


if __name__ == "__main__":
    create_main_window()
'''