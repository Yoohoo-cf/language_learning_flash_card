from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFFFFF"

data = pandas.read_csv("data/japanese_words.csv")
data_frame = data.to_dict(orient="records")
current_card = {}


def generate_word():
    global current_card

    current_card = choice(data_frame)
    word = current_card["Japanese"]
    canvas.itemconfig(title_text, text="Japanese")
    canvas.itemconfig(word_text, text=word, fill="black")
    canvas.itemconfig(canvas_img, image=card_front_img)


def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill=WHITE)
    canvas.itemconfig(word_text, text=current_card["English"], fill=WHITE)

    window.after_cancel()



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=generate_word)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=generate_word)
known_button.grid(row=1, column=1)

generate_word()

window.mainloop()