import tkinter

def button_clicked():
    print("I got clicked")
    my_label["text"] = user_input.get()


window = tkinter.Tk()  # Creating the window object.
window.title("My 1st GUI Program")  # Defining the title of the window object.
window.minsize(width=300, height=200)  # Defining the size of the window object.

FONT = ("Ariel", 18, "bold")

label_1 = tkinter.Label(text="test", font=FONT)
label_1.grid(column=0, row=0)

# Labels:
my_label = tkinter.Label(text="Label", font=FONT)  # Creating and defining the label and its properties.
my_label.grid(column=2, row=0)  # This command makes the label show on screen. Default location is top center.

label_2 = tkinter.Label(text="Label 2", font=FONT)
label_2.grid(column=2, row=3)

# Buttons:

user_input = tkinter.Entry(width=15)
user_input.grid(column=2, row=2)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=1)


"""Arguments with Default values solve the issue of having to define values that obvious most of the time, or just not normally changed.
These arguments can still be changed. They will be shown in the documentation (when hovering over the function) 
with 3 dots to signify that there is already a default value."""

window.mainloop()  # This method insures the window will only close when the user clicks X.

"""The '*' symbol followed by a collective name for the arguments (args) creates an option for an unlimited amount of arguments. """
def add(*args):
    sums = 0
    for n in args:
        sums += n
    print(sums)


# add(3, 2, 6, 9)

"""To refer to a argument by name rather than by position use 2 '*' symbols followed by the key-word arguments collective name (kwargs).
The kwargs are addressed by name in the for of a dictionary, with the key being the name of the kwarg."""
def calc(n, **kwargs):
    print(type(kwargs))  # class is dict
    n *= kwargs["multiply"]
    n += kwargs["add"]
    print(n)


# calc(2, add=3, multiply=5)

"""Kwargs and args stem from classes; if the class your object is created from has kwargs and/or args defined within it
it is possible to redefine them as seen below:"""

"""It's important to notice that when defining kwargs you must use the .get() function and not this kw["name].
When using get() with an undefined kwarg it will return 'none', otherwise it will return an error. 
This is important so users wont be forced to define every kwarg in the class."""
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")  # Correct method
        self.model = kw["model"]  # incorrect method
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R", seats=4)
# print(my_car.model)  # Output will be "GT-R"



