from tkinter import *
import requests as rq

def get_quote():
    response = rq.get("https://api.kanye.rest/")  # getting the data from the api using request module
    if response.raise_for_status() is not None:  # if the status is equal to None it means there were no errors.
        canvas.itemconfig(quote_text, text="Sorry. Looks like there's a problem")
        print(response.raise_for_status())
    else:
        data = response.json()  # creating the data variale with the json content as a dictionary.
        quote = data["quote"]  # extracting the relevant value from data using the key 'quote'.
        canvas.itemconfig(quote_text, text=quote)  # changing the default text in the canvas item (l. 21) to contain the quote we generated.


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, background='pale turquoise')

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Click on kanye for a Kanye quote", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.config(bg='pale turquoise', highlightthickness=0)
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote, background='pale turquoise', activebackground='pale turquoise')
kanye_button.grid(row=1, column=0)

window.mainloop()
