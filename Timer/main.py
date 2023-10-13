from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
window_timer = None
marks = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(window_timer)
    top_label.config(text="Timer")
    check_marks.config(text="")
    canvas.itemconfig(timer, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        top_label.config(text="Break", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW, highlightthickness=0)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        top_label.config(text="Break", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW, highlightthickness=0)
    else:
        countdown(work_sec)
        top_label.config(text="Timer", font=(FONT_NAME, 50), fg=RED, bg=YELLOW, highlightthickness=0)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    minute_sec = f"{count_min}:{count_sec}"
    canvas.itemconfig(timer, text=minute_sec)
    if count > 0:
        global window_timer
        window_timer = window.after(1000, countdown, count -1)
    else:
        start_timer()
        global marks
        for i in range(math.floor(reps/2)):
            marks += "✅"
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

# Setting up the window
window = Tk()
window.title("Timer")
window.config(padx=100, pady=50, bg=YELLOW)


# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Top Label
top_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW, highlightthickness=0)
top_label.grid(column=1, row=0)

# Start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.config(padx=0, pady=0)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Check Marks
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)



window.mainloop()