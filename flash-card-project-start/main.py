from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
# Making a kist of dictionaries from the csv file in the following format: [{French: word, English: word}...]
try:
    # If this file exists with the unknown words, the program will use the words from there
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    # If the file does not exist the program will use the original list of words
    original_data = pd.read_csv("data/french_words.csv")
    fr_2_en = original_data.to_dict(orient="records")
else:
    fr_2_en = data.to_dict(orient="records")

current_card = {}
# ---------------------------- Functionality ------------------------------- #
# Called on when the buttons are pressed to show the next card
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(fr_2_en)
    # Configuring the canvas items so that the text contains the language and the word from the current_card variable.
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def known_words():
    fr_2_en.remove(current_card)
    new_data = pd.DataFrame(fr_2_en)
    new_data.to_csv("data/words_to_learn", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
# Creating window object
window = Tk()
window.title("Flashcards Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# The after() method in tkinter waits for a specified amount of time (in ms) after the defined function is called
flip_timer = window.after(3000, func=flip_card)
# Defining the canvas area:
canvas = Canvas(width=800, height=526)
# Creating card front and back images:
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
# The card_background variable will be configured with the front or back image throught the game:
card_background = canvas.create_image(400, 263, image=card_front_img)
# Creating 2 variables that contain the language and the word on the flash card: (later to be configured)
card_title = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons:
x_img = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_img, highlightthickness=0, command=next_card)
x_button.grid(row=1, column=0)

v_img = PhotoImage(file="images/right.png")
v_button = Button(image=v_img, highlightthickness=0, command=known_words)
v_button.grid(row=1, column=1)

next_card()  # Calling on this function so that the 1st card appears immediatly when the program is run.

window.mainloop()
