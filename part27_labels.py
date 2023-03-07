from tkinter import *

# label = an area widget that hold text and/or an image within a window

window = Tk()



label = Label(window,
              text="Hello",
              font=("Arial",40,"bold"),
              fg="green",
              bg="pink",
              relief=RAISED,  # border
              bd = 10,
              padx=20,  # 20px between text and border
              pady = 20)
label.pack()
#label.place(x=0,y=0)

window.mainloop()