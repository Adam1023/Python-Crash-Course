import sys
from random import randint

######################################################################################################################
# Below is the part of the game start.
# I ask the user to input his name and if the name is correct I also ask for a password.
# Then the game starts.
# But if the name or password are incorrect, then the program exits.
# For info the correct name is "Adam" and the password is 1234

# Run the program now to understand what happens. Then check my code below and understand it.
# Try different name and/or passwords.
# Once you understood, change the correct name and password in the code.


name = input("Name: ")

if name == "Adam":
    password = int(input("Password: "))
    if password == 1234:
        input("Welcome to the game ! Are you ready ?? ")
        print("######################################")
        print("     ############################")
        print("          ##################")
        print("               ########")
        money = int(input("What amount do you want to put in the game (in euros)? "))


    else:
        print("Wrong ! héhé")
        sys.exit()  # This line allows the program to exit even if there's still code below

else:
    print("Go away you nasty person !")
    sys.exit()  # This line allows the program to exit even if there's still code below

# So from now on we have 3 variables. The variables "name" and "password" won't be used at this point anymore.
# The only important variable here is "money", that will be used later on.
######################################################################################################################


input("From here, it's your time to code man ! ")  # TODO: Remove this line


##################################
#####  1) THE FUNCTIONS     ######
##################################

def generate_new_list():
    """
    This function returns a new list with 5 random elements.
    This function doesn't need any parameter. That's why we have nothing between the parenthesis.
    We'll just return a new list. You don't need to change anything to this function, we have already implemented it
    for you. Just read the code and the comments and try to understand it.

    :return: A list containing 5 randomly generated numbers between 1 and 30.
    """

    # For generating a new list, we first initialize an empty list.
    lst_of_numbers = []

    # Then I use a while loop for looping exactly 5 times. The for loop makes sure that at every iteration
    # the variable "_" is incremented by 1 starting from 0 till 4 (included).
    # The variable "_" is not important. The only thing it's needed for is looping 5 times. At every new loop
    # we generate a new random number and store that number in the variable "random_nb". Then we add that element
    # to the list. Check the code below and do your best in order to understand it:
    for _ in range(5):
        random_nb = randint(1, 30)

        # The next while is needed for making sure we don't add an already existing element. 
        # It's not a big deal if you don't understand it now:
        while random_nb in lst_of_numbers:
            random_nb = randint(1, 30)

        lst_of_numbers += [random_nb]

    # At the end of the loop the list will contain 5 numbers between 1 and 30. And everytime we call this function
    # in our code, a new list will be generated.

    # Now we just need to return that list (outside the loop of course).
    return lst_of_numbers


# The next functions you'll have to implement their bodies yourself.


def value_is_in_list(number, lst):
    """
    This function checks whether a given number is present in a given list. This is a boolean function !

    This function could be easily implemented using the "in" operation. However it would be stupid to use it.
    The goal is for you to train yourself and understand programming.
    So try to proceed this way:
    You check for every element of the list. If an element is the same as the given number, then return True.
    If instead you passed through all the elements but couldn't find it and you finished with the while loop, you return False

    :param number: The integer to check if it is inside the list lst
    :param lst: A list of numbers.
    :return: True if number is inside lst, False otherwise.
    """
    pass  # TODO: 'pass' just means "pass and ignore that line". So remove it when you'll start coding.


def remove_element_from_lst(element, lst):
    """
    This function returns a *new* list that contains all the elements of the list "lst" except the one that is equal to "element".
    You may assume that element will always be present in lst.
    For this function you need to use indexation.

    :param element: The integer to remove from the list.
    :param lst: The list that contains the to remove element.
    :return: A *new* list just like lst but without element
    """
    pass  # TODO


def is_game_over(money, lst):
    """
    This boolean function has as parameter "money" (which means the money left in this game) and a list "lst" which
    represents the numbers still to guess
    If there's no money left or no number anymore to guess, then this function returns True. Otherwise False.
    """
    pass  # TODO


##################################
#####  2) START THE GAME    ######
##################################

"""
The general idea (just read it):
1) First generate a new list and save it in a variable.
2) Then you make a while loop. The condition for leaving the while is if there's no more money or that the list is empty.
    3) We ask repeatedly in a loop for a number and check if that number is inside the list using the function 
    "value_is_in_lst" that you had to implement earlier.
        *   If it's inside, you remove that number from the list using the function "remove_number__from_lst()"
            and we calculate the number of still to guess numbers (= length of list) and we print what you have to print
            what is needed to be printed in this case.
        *   If it's not present, with divide the score by two and print what is needed to be printed in this case.

4) Out of the while we check if the user has won the game or not.
"""

# TODO: Below you'll find a pseudo-code for the algorithm you need to implement. This means that I've written in English the
# full logic that you have to follow for this code. You just need to translate it to Python. Happy coding !

def start_game():
    global money  # You'll need the variable money from above, so I make it global in order to use it here.
    # 1)
    # Generate a new list and save it in a variable

    # 2)
    # While the game is not over:
        # Ask for a to guess number

        # 3)
        # If the guessed number is inside the list:
            # Remove the element
            # Add 1/10 of the current amount (money)
            # Print what you have to print

        # Otherwise if the number guessed is not inside the list:
            # Remove 15% from the money left
            # Print what you have to print



    # 4)
    # If the reason for leaving the loop is the fact of having no money anymore:
        # Print what you have to print

    # If the reason for leaving the loop is not bcs of having no more money but because everything was guessed:
        # Print what you have to print












# And of course we need to start the game
start_game()
