###########################################################################
##                     Roller coaster tickets                            ##
###########################################################################

#adults = 12
#youth = 7
#child = 5
#mid-life crisis = free

height = round(int(input("What is you hight in cm?\n")))
age = round(int(input("What is your age?\n")))
photos = input("Do you want your photos taken? 'y' or 'n'\n")
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    
    if age <= 12:
        print("Child tickets are 5$")
        bill += 5
    elif age >= 12 and age <= 18:
        print("Youth tickets are 7$")
        bill += 7
    elif age >= 45 and age <= 55:
        print("Tickets for adults going through a mid-life crisis are FREE!")
    else:
        print("Adult tickets are 12$")
        bill += 12

    if photos == 'y':
        print("An additional 3$ charge has been added to your bill.")
        bill += 3
        print(f"Your final bill is {bill}")
        exit()
    else:
        print(f"Your final bill is {bill}")
        exit()

else:
    print("You need to be at least 120cm to ride this rollercoaster! Come back when you're not a midget :)")
    exit()
