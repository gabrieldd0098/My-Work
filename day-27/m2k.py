from tkinter import *

def m2k():
    mi = float(miles_input.get())
    km = mi * 1.609
    kilometers_result_label.config(text=f"{km:.2f}")

window = Tk()
window.title("Miles 2 Kilometers Converter")
window.config(padx=24, pady=24)

miles_input = Entry(width=12)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_eq_label = Label(text="is equal to")
is_eq_label.grid(column=0, row=1)

kilometers_result_label = Label(text="0")
kilometers_result_label.grid(column=1, row=1)

kilometers_label = Label(text="Kilometers")
kilometers_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=m2k)
calc_button.grid(column=1, row=2)

window.mainloop()
