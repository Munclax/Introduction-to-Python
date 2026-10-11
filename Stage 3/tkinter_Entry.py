import tkinter
window=tkinter.Tk()
name_enter=tkinter.Entry(window)
#Entry() is a method that creates an entry widget in the window, which allows users to input text.
name_enter.pack()
name=name_enter.get() #get() is a method that retrieves the text entered in the entry widget.
window.mainloop()