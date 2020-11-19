users = []


def login():
    print("Login!")
    username = input("Username: ")
    password = input("Password: ")

    if (username, password) in users:
        print(f"Welcome {username}!")
    else:
        print("Username or password incorrect!")

    input()


def register():
    print("Make a new login!")
    username = input("Username: ")
    password = input("Password: ")
    password_confirmation = input("Confirm password: ")

    if password == password_confirmation:
        users.append((username, password))
        print(f"New user {username} created")
    else:
        print("The password don't match, try again!")

    input()


print("Welcome to IMSAL's Login system")
print("##############################")
print("        ###########           ")
print("          #####           ")
print("            #           ")

while True:
    choice = int(input("Press 1 for login, 2 for register: "))

    if choice == 1:
        login()
    elif choice == 2:
        register()
