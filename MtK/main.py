from tkinter import *

def calc():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 2)
    result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometers")
window.config(padx=20, pady=20)

FONT = ("Ariel", 12, "normal")

miles_input = Entry(width=7)
miles_input.insert(END, "0")
miles_input.focus()
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

equal_to = Label(text="is equal to", font=FONT)
equal_to.grid(column=0, row=1)

calc_button = Button(text="Calculate", font=FONT, command=calc)
calc_button.grid(column=1, row=2)

result_label = Label(text="0", font=FONT)
result_label.grid(column=1, row=1)

window.mainloop()
