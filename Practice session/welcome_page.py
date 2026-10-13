import tkinter
window=tkinter.Tk()
label=tkinter.Label(window,text="Enter your name:",bg="skyblue",fg="black")
label.pack()
entry=tkinter.Entry(window)
entry.pack()
def greet():
  name_unmasked=entry.get()
  name=name_unmasked.strip()
  if name=="":
    label.config(text="Please enter your name")
  else:
    label.config(text=f"Hello {name}")
button=tkinter.Button(window,text="Sign in",command=greet,bg="skyblue",fg="black")
button.pack()
window.mainloop()