import tkinter
window=tkinter.Tk()
name_enter=tkinter.Entry(window)
name_enter.pack()
name=name_enter.get()
label=tkinter.Label(window,text=f"Wecome {name}")
label.pack()
window.mainloop()