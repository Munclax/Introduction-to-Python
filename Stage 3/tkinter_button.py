import tkinter
window=tkinter.Tk()
def greet():
    label=tkinter.Label(window,text="Hello, Bitch!",fg="blue",font=("Arial",15))
    label.pack()
button=tkinter.Button(window,text="Click me BITCH",command=greet) 
#Button() is a method that creates a button widget in the window, which allows users to perform an action when clicked.
button.pack()
window.mainloop()