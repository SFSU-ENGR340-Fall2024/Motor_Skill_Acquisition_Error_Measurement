from tkinter import *

class gui:
    def start_menu():
        pass

    def review():
        pass


    home = Tk()
    home.option_add('*Font', '20')
    home.geometry("500x500")

    frame = Frame(home)
    frame.pack()

    left_frame = Frame(home)
    left_frame.pack(side = TOP)

    right_frame = Frame(home)
    right_frame.pack(side = BOTTOM)

    start_button = Button(left_frame, text = "Start New Test", command = start_menu)
    start_button.pack(padx = 10, pady =10)

    review_button = Button(right_frame, text = "Review Data")
    review_button.pack(padx = 10, pady = 10)

    home.title("Error Measurement Tool")
    home.mainloop()
