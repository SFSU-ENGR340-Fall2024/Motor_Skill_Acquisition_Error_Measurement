from tkinter import *
 
def set():
    print("Hello World")
 
root = Tk()
root.geometry("200x150")
 
frame = Frame(root)
frame.pack()
button = Button(frame, text = "Button1", command = set)
button.pack()
 
root.mainloop()