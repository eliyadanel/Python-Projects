import datetime as dt
import smtplib
import random
import pandas as pd

today = (dt.datetime.now().month, dt.datetime.now().day)  # today's month and day

my_email = "ddeliya2@gmail.com"  # source email
password = "pvvnfutgttrmsimu"  # app password for gmail account

data = pd.read_csv('birthdays.csv')
bd_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in bd_dict:  # if the one of birthday dates match today's date...
    birthday_person = bd_dict[today]  # singling out the bday person from the file to access all of their info
    file_path = f"letter{random.randint(1,3)}.txt"  # randomizing the letter file out of the 3 options
    with open(file_path) as letter:
        contents = letter.read()
        replaced_letter = contents.replace('[NAME]', f'{birthday_person["name"]}')  # replacing the general NAME with the bday person's name

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # oppening the connection with the gmail smtp server and port 587
        connection.starttls()  # securing the connection with TL: transport layer security.
        connection.login(user=my_email, password=password)  # loggin into the gmail account with the email and pass
        connection.sendmail(
            from_addr=my_email,
            to_addrs=f"{birthday_person['email']}",
            msg=f"Subject:Happy Birthday Wishes\n\n{replaced_letter}"
        )
