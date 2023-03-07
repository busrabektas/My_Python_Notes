from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk() # instantiate an instance of a window
window.geometry("420x420")  # width,height
window.title("Büşra's first GUI program") # title
window.config(background="#5cfcff")

window.mainloop() # place window on computer screen, listen for events
