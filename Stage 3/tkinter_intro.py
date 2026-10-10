import tkinter #tkinter is a built-in module in Python for creating GUI applications.
window= tkinter.Tk() #Tk() is a method that creates a new window.
label=tkinter.Label(window, text="Hello World!") #Label() is a method that creates a label widget in the window.
label.pack() #pack() is a method that adds the label to the window and displays it
#a widget is a GUI element that allows users to interact with the application, such as buttons, labels, text boxes, etc.
window.mainloop() #mainloop() is a method that keeps the window open and waits for user interaction.