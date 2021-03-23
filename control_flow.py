# Control flow
# Conditional statements are used to control the flow of our program

age = 15
# if the user is above the age of 15 allow them to buy a ticket
if age >= 15: #If this condition is met/true the print statment will execute
    print("Thank you, please proceed to your purchase")
    #if the user is under the age of 15 do not allow to buy a ticket
elif age < 15:
    print("You are too young to purchase this ticket")
# else block getes executed if non of the above conditions are met
else:
    print("Oops something went wrong, please try later")
