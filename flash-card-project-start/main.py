from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Arial", 40, "italic")
FONT2 = ("Arial", 60, "italic")
curr_card = {}
to_learn = {}

try:
    data = pandas.read_csv(filepath_or_buffer="data/french_words_to_learn.csv")
except FileNotFoundError:
    orig_data = pandas.read_csv(filepath_or_buffer="data/french_words.csv")
    to_learn = orig_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

#commands
def next_card():
    global curr_card, flip_t
    window.after_cancel(flip_t)
    curr_card = random.choice(to_learn)
    canvas.itemconfig(c_title, text="French", fill="black")
    canvas.itemconfig(c_word, text=curr_card["French"], fill="black")
    canvas.itemconfig(c_bg, image=card_front_img)
    flip_t = window.after(ms=3000, func=flip_card)

def flip_card():
    canvas.itemconfig(c_title, text="English", fill="white")
    canvas.itemconfig(c_word, text=curr_card["English"], fill="white")
    canvas.itemconfig(c_bg, image=card_back_img)

def is_known():
    to_learn.remove(curr_card)
    data2 = pandas.DataFrame(to_learn)
    data2.to_csv(path_or_buf="data/french_words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("FLASHLY")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_t = window.after(ms=3000, func=flip_card)

#canvas
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
c_bg = canvas.create_image(400, 263, image=card_front_img)
c_title = canvas.create_text(400, 150, text="TITLE", font=FONT)
c_word = canvas.create_text(400, 263, text="word", font=FONT2)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

#wrong btn
cross_image = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_btn.grid(row=1, column=0)

#right btn
check_image = PhotoImage(file="images/right.png")
known_btn = Button(image=check_image, highlightthickness=0, command=is_known)
known_btn.grid(row=1, column=1)

next_card()
window.mainloop()
