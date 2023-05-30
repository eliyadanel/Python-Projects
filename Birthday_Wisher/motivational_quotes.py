import datetime as dt
import smtplib
import random

my_email = "ddeliya2@gmail.com"
password = "pvvnfutgttrmsimu"  # app password for gmail account

now = dt.datetime.now()
week_day = now.weekday()  # the day of the week

if week_day == 2:  # if the day is wednesday
    with open("quotes.txt") as lines:
        quotes_list = lines.read().splitlines()  # creating a list of quotes from the txt file, split by the end of the line
        chosen_line = random.choice(quotes_list)  # randomly choosing a quote to send in the email

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # oppening the connection with the gmail smtp server and port 587
        connection.starttls()  # securing the connection with TL: transport layer security.
        connection.login(user=my_email, password=password)  # loggin into the gmail account with the email and pass
        connection.sendmail(  # sending the email with a title to the recipient. the email contains the motivational quote
            from_addr=my_email,
            to_addrs="eliyadanel@gmail.com",
            msg=f"Subject:Motivational Monday Email\n\n{}"
        )

else:
    pass



