from tkinter import *
import csv
import random
BACKGROUND_COLOR = "#B1DDC6"

# Adding the French words into a list and dict
french_word_dict = {}
known_words = {}
random_french_word = []

try:
    with open("data/words_to_learn.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            french_word_dict[row[0]] = row[1]
except FileNotFoundError:
    with open("data/french_words.csv", "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)
        for row in csv_reader:
            french_word_dict[row[0]] = row[1]




def show_word_in_french():
    global flip_timer, random_french_word
    random_french_word = random.choice(list(french_word_dict.keys()))
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_word, text=random_french_word, fill="black")
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)
    known_words[random_french_word] = french_word_dict[random_french_word]

def flip_card():
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=f"{french_word_dict[random_french_word]}", fill="white")
    canvas.itemconfig(card_background, image=card_back_image)

def known_button_func():
    del french_word_dict[random_french_word]
    show_word_in_french()

def on_closing():
    with open("data/words_to_learn.csv", "w", newline="") as words_to_learn:
        csv_writer = csv.writer(words_to_learn)
        for key, value in french_word_dict.items():
            csv_writer.writerow([key, value])
    window.destroy()

# UI ---
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_image)
canvas_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
canvas_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=show_word_in_french)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=known_button_func)
known_button.grid(row=1, column=1)

show_word_in_french()
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
