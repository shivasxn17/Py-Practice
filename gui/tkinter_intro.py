from tkinter import *
import json
import re


email_regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"


is_email_valid = lambda email: re.search(email_regex, email)

data = {}

# everything is a widget
# need to create root_window widget first
root_window = Tk()
root_window.title("First GUI App")
root_window.geometry("450x250")

# understanding grid
# myLabel.grid(row=0, column=0)

# myLabel.pack()

email_entry = Entry(root_window, width=50, borderwidth=5)
email_entry.grid(row=0, column=2)


def on_generate_click():
    myLabel = Label(root_window, text=prepare_json_contract())
    myLabel.grid(row=2, column=0, columnspan=3)


def prepare_json_contract():
    entered_email = email_entry.get()
    if is_email_valid(entered_email):
        data['email'] = entered_email
    else:
        return "Invalid Email Entered"
    return json.dumps(data)


# creating label widget
myLabel = Label(root_window, text="Enter Email").grid(row=0, column=0)
myButton = Button(	root_window,
                   text="Generate",
                   padx=30,
                   pady=5,
                   command=on_generate_click,
                   fg='white',
                   bg='green').grid(row=1, column=1, columnspan=2)
# myButton = Button(root_window, text="Generate", state=DISABLED).grid(row=0, column=0)
# create event loop
root_window.mainloop()
