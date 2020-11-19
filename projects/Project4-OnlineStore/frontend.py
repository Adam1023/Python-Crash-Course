from tkinter import *
from functools import partial


def validate_login(username, password, root):
    print("username entered :", username.get())
    print("password entered :", password.get())
    if username.get() == "Adam":
        root.destroy()
        root = Tk()
        root.title("Logged In !")
        root.geometry('400x150')
        Label(root, text="Freaking Awesome !").grid(row=0, column=0)
    return


def display_login(root):
    global validate_login

    # 1) Arrange window
    root.geometry('400x150')
    root.title('Log In')
    # 2) Username & Password (label and textbox)
    usernameLabel = Label(root, text="User Name").grid(row=0, column=0)
    username = StringVar()
    usernameEntry = Entry(root, textvariable=username).grid(row=0, column=1)
    passwordLabel = Label(root, text="Password").grid(row=1, column=0)
    password = StringVar()
    passwordEntry = Entry(root, textvariable=password, show='*').grid(row=1, column=1)
    # login button
    validateLogin = partial(validate_login, username, password, root)
    loginButton = Button(root, text="Login", command=validateLogin).grid(row=4, column=0)




if __name__ == '__main__':
    root = Tk()
    display_login(root)
    root.mainloop()