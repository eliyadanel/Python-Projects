import turtle
import pandas

screen = turtle.Screen()  # Creating screen object
screen.title("U.S. States Game")  # Defining screen title
image = "blank_states_img.gif"  # The image variable contains the relative path of the states image
screen.addshape(image)
turtle.shape(image)  # Defining the image as the background of the game

data = pandas.read_csv("50_states.csv")
all_states = data['state'].tolist()  # Creating a list of all the state's names
x_list = data.x.tolist()  # Creating a list of all the state's coordinates
y_list = data.y.tolist()

cor_list = []  # Creating a list of tuples from the x and y coordinates lists.
for x, y in zip(x_list, y_list):
    cor_list.append((x, y))

correct_answers = []  # Correct answers, to keep score.
score = 0

while score < 50:  # While the user has guessed less than 50 correct states, the game loop continues
    # The user inputs the answer in the text box, and it is saved in the variable.
    answer_state = (screen.textinput(title=f"{score}/50 States Guessed", prompt="What's this state's name?")).capitalize()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in correct_answers]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")
        break
    if answer_state in all_states:
        state_index = all_states.index(answer_state)  # Checking the index number of the state in the state list
        t = turtle.Turtle()  # Creating turtle object to write the names of the state on the screen
        t.hideturtle()
        t.penup()
        t.goto(cor_list[state_index])  # The t object goes to the x and y positions of the same index number as the state's
        t.write(arg=answer_state, align="center", move=False, font=("Verdana", 8, "normal"))  # Defining the writing settings
        if answer_state not in correct_answers:  # Appending the correct answer to the correct answers list unless it is already in there
            correct_answers.append(answer_state)
            score = len(correct_answers)
    else:
        print('wrong')

turtle.mainloop()
