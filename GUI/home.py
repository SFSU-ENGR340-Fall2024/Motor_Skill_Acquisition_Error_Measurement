from tkinter import *
 
def start_menu():
    pass

def review():
    pass


home = Tk()
home.geometry("1000x500")

frame = Frame(home)
frame.pack()

left_frame = Frame(home)
left_frame.pack(side = TOP)

right_frame = Frame(home)
right_frame.pack(side = BOTTOM)

select_folder_button = Button(left_frame, text = "Start New Test", width = 100, height = 10, command = start_menu)
select_folder_button.pack(padx = 10, pady =10)

review_button = Button(right_frame, text = "Review Data", width = 100, height = 10)
review_button.pack(padx = 10, pady = 10)

home.title("Error Measurement Tool")
home.mainloop()
