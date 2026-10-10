import tkinter
window=tkinter.Tk()
user="Prem"
label=tkinter.Label(window,text=f"Wecome {user}")
#here f is used to format the string and insert the value of the variable user into the text of the label.
label.pack()
window.mainloop()