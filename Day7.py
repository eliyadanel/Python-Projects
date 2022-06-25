import random

rival_choice = ["rock", "paper", "scissors"]
pick = random.choice(rival_choice)
print(pick)

print(opponent())

if opponent() == "rock":
        print("Your opponent used 'rock'")
        print('''\r
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        ''')
elif opponent() == "paper":
        print("Your opponent used 'paper'")
        print('''\r
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
        ''')
elif opponent() == "scissors":
        print("Your opponent used 'scissors'")
        print('''\r
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
        ''')        
        
        