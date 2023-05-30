from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0  # Keeps track of how many times the 'start_timer' function has been called.
timer = None  # A variable for the countdown 'after' method.
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():  # A function to completely reset the clock.
    window.after_cancel(timer)  # Canceling the countdown method to stop the clock from counting down.
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)  # Settig the title to go back to its original text.
    v_label.config(text="")  # Deleting the session marks from the screen.
    global reps
    reps = 0  # Resetting the reps to 0 so the sessions won't go out of order


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():  # Calls upon the countdown, and contains the UI settings for each CT session. This function is called when the user clicks the start button (line 79)
    global reps
    reps += 1
    # Calculating how many seconds in each session:
    work_sec = WORK_MIN * 60
    short_br = SHORT_BREAK_MIN * 60
    long_br = LONG_BREAK_MIN * 60
    # Using the 'reps' variable (see line 12) I calculate which session the user is entering (work, short break or long break):
    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)  # Changing the text and color of the title accordingly.
        countdown_mech(long_br)  # Setting the time for the countdowen according to the correct session.
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        countdown_mech(short_br)
    else:
        timer_label.config(text="Work", fg=GREEN)
        countdown_mech(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown_mech(count):  # This funtion contains the functionality of the timer.
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # Changing the type and layout of the clock to avoid bugs when there is a singular seconds digit:
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # Displaying the countdown clock in the proper format.
    if count > 0:  # If the countdown has not yet reached 0 the timer continues counting down. This is to avoid going into the negatives.
        global timer
        timer = window.after(1000, countdown_mech, count - 1)  # The 'after' method from the Window class allows the program to check a condition every set ampunt of ms.
        # The method has 3 main arguments: ms, check, what to do (*args)
    else:  # When the countdown hits 0 the timer will immediately move onto the next session without pausing.
        global reps
        if reps % 2 == 0:  # Counting every 2 sessions when user completes a work session and qa break session which awwrds them with a V
            v_label["text"] += "✔"
        start_timer()  # Calling on the start_timer function to move onto the next session once the current one reaches 00:00


# ---------------------------- UI SETUP ------------------------------- #
# Creating window object:
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)
# Inserting the tomato image into a varrable to be defined as the backgrounf pic:
tomato_img = PhotoImage(file="tomato.png")
# Creating and definign canvas object with the attributes of the GUI program:
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)  # Creating the tomato pic as a background
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))  # defining the clock's attributes with canvas
canvas.grid(column=1, row=1)
# Creating the title:
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)
# Creating the label for the Vs:
v_label = Label(fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 15, "normal"))
v_label.grid(column=1, row=3)
# Creating the buttons and assigning the methods they use:
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
