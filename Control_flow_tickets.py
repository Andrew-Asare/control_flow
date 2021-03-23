
ticket = int(input("What ticket would you like to buy?\n Enter 1 for the age 15 movie\n Enter 2 for the age 12 movie\n Enter 3 for the PG movie\n Enter 4 for the 18 movie"))
age = int(input("what is your age?"))
print("You are", age, "years old")
if 0 < ticket < 5 :

# if the user is above the age of 15 allow them to buy a ticket
    if ticket == 1:
        if age >= 15:  # If this condition is met/true the print statement will execute
            print("Thank you, please proceed to your purchase")
            # if the user is under the age of 15 do not allow to buy a ticket
        elif age < 15:
            print("You are too young to purchase this ticket")
        # else block gets executed if non of the above conditions are met
        else:
            print("Oops something went wrong, please try later")

    elif ticket == 2:
        if age >= 12:  # If this condition is met/true the print statment will execute
            print("Thank you, please proceed to your purchase")
            # if the user is under the age of 15 do not allow to buy a ticket
        elif age < 12:
            print("You are too young to purchase this ticket")
        # else block gets executed if non of the above conditions are met
        else:
            print("Oops something went wrong, please try later")

    elif ticket == 3:
        if age >= 10:  # If this condition is met/true the print statment will execute
            print("Thank you, please proceed to your purchase")
            # if the user is under the age of 15 do not allow to buy a ticket
        elif age < 10:
            print("You are too young to purchase this ticket")
        # else block gets executed if non of the above conditions are met
        else:
            print("Oops something went wrong, please try later")
    elif ticket == 4:
        if age >= 18:  # If this condition is met/true the print statment will execute
            print("Thank you, please proceed to your purchase")
            # if the user is under the age of 15 do not allow to buy a ticket
        elif age < 18:
            print("You are too young to purchase this ticket")
        # else block gets executed if non of the above conditions are met
        else:
            print("Oops something went wrong, please try later")
    else:
        print("Oops something went wrong, please try later")
else:
    print("oops you need to enter a number that is 1,2,3 or 4")