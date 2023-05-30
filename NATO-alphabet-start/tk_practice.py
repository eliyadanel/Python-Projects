import tkinter as tk

window = tk.Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

entry = tk.Entry(width=30)
entry.insert(tk.END, "Some text to begin with.")  # puts the text in the entry
print(entry.get())
entry.pack()

text = tk.Text(height=5, width=30, font=("Ariel", 24, "bold"))
text.focus()  # Puts curser in textbox
text.insert(tk.END, "Example of multi-line text entry.")
print(text.get("1.0", tk.END))
text.pack()

def spinbox_used():
    # gets the current value in spinbox
    print(spinbox.get())


spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

def scale_used(value):
    # prints the value that the scale lands on
    print(value)


scale = tk.Scale(from_=0, to=100, command=scale_used)
scale.pack()

def checkbutton_used():
    # prints 1 if on button checked, otherwise 0.
    print(checked_state.get())


# variable to hold onto checked state, 0  is off 1 is on.
checked_state = tk.IntVar()
checkbutton = tk.Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

def radio_used():
    print(radio_state.get())


# variable to hold on to which radio button value is checked.
radio_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

def listbox_used(event):
    # gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = tk.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()

"""3 methods of arranging items on screen:
pack: simple, no persice position. Options are : left, right, bottom, top.
place: percise positioning with x and y values. (0,0) would be top left corner.
grid: devides the program into rows and columns. Specify a row and a column (0, 1, 2) for a percise but not dificult to manage location.
"""
