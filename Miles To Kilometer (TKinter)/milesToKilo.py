from tkinter import *

# Setting up the window
window = Tk()
window.title("Miles to Kilometer")
window.minsize(width=100, height=100)
window.config(padx=60, pady=60)

#Entry box
entry = Entry(width=5)
entry.grid(column=1, row=0)

# Miles Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Is equal to label
is_equal_label = Label(text="Is equal to")
is_equal_label.grid(column=0, row=1)

# Result label
result_label = Label(text=0)
result_label.grid(column=1, row=1)

# Kilometer Label
kilometer_label = Label(text="Kilometer")
kilometer_label.grid(column=2, row=1)

def miles_to_kilo():
    miles = int(entry.get())
    kilometers = miles * 1.6
    result_label.config(text=round(kilometers))

# Calculate Button
calculate_button = Button(text="Calculate", command=miles_to_kilo)
calculate_button.grid(column=1, row=3)














window.mainloop()