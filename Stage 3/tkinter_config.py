import tkinter
window=tkinter.Tk()
label=tkinter.Label(window,text="Hello, Bitch!",fg="blue",font=("Arial",15))
label.pack()
def greet():
    label.config(fg="red",font=("Roman",20))
    #config() is a method that allows you to change the properties of a widget, such as its text, color, font, etc.
    label.config(text="Sayonara Bitch")
    label.pack()
button=tkinter.Button(window,text="Click me BITCH",command=greet) 
#Button() is a method that creates a button widget in the window, which allows users to perform an action when clicked.
button.pack()
window.mainloop()