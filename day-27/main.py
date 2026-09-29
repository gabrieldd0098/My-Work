from tkinter import *

TEXT = "NO WAY, ROBOTS!"
FONT = ("Times New Roman", 25, "bold")

def cliked():
    input_text = input_e.get()
    label.config(text=input_text)

windy = Tk()
windy.minsize(width=900, height=300)
windy.title("+++GG--UU--II+++")
windy.config(padx=20, pady=20)

#label
label = Label(text=TEXT, font=FONT)
label.grid(column=0, row=0)
label.config(padx=25, pady=25)

#button
button = Button(text= "CLIK ME!", command=cliked)
button.grid(column=1, row=1)
button.config(padx=10, pady=10)

#false button
f_button = Button(text= "CLIK ME!", command=windy.destroy)
f_button.grid(column=2, row=0)
f_button.config(padx=15, pady=15)

#entry
input_e = Entry()
input_e.grid(column=3, row=2)

windy.mainloop() #always @ very end
