from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Ariel", 20, "italic")


class UserInterface:

    def __init__(self, quizz_brain: QuizBrain):
        self.quiz = quizz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # canvas object for the questions to appear on:
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="Some question",
                                                     fill=THEME_COLOR,
                                                     font=FONT,
                                                     width=280,
                                                     )
        self.canvas.config(bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # buttons:
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_img, highlightthickness=0, bg=THEME_COLOR, command=self.true_click)
        self.false_button = Button(image=false_img, highlightthickness=0, bg=THEME_COLOR, command=self.false_click)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)
        # lable:
        self.score_label = Label(bg=THEME_COLOR, text="score: 0", fg="white")
        self.score_label.grid(row=0, column=1)
        # activating the next_question method
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, fill="black")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You finished the quiz!\nYour final score is: {self.quiz.score}/10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_click(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_click(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="#245953")
            self.canvas.itemconfig(self.question_text, fill="white")
        else:
            self.canvas.config(bg="#FF0303")
            self.canvas.itemconfig(self.question_text, fill="white")

        self.window.after(1000, self.get_next_question)
