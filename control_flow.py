# # Control flow
# # Conditional statements are used to control the flow of our program
#
# # age = 15
# # # if the user is above the age of 15 allow them to buy a ticket
# # if age >= 15: #If this condition is met/true the print statment will execute
# #     print("Thank you, please proceed to your purchase")
# #     #if the user is under the age of 15 do not allow to buy a ticket
# # elif age < 15:
# #     print("You are too young to purchase this ticket")
# # # else block getes executed if non of the above conditions are met
# # else:
# #     print("Oops something went wrong, please try later")
#
# #Syntax to create a loop
# # for is python keyword variable then data_collection
#
# shopping_list = ["bread", "eggs", "milk", "orange"]
#
#
# print(shopping_list)
# print(shopping_list[0])
# print(shopping_list[1])
# print(shopping_list[2])
# print(shopping_list[3])
#
#
# for items in shopping_list:
#     print(items)
#
# # Let's iterate through letter in a word
# # for letter in "fruits":
# #     print(letter)
# # shopping_list = ["bread", "eggs", "milk", "orange"]
# #
# # for items in shopping_list:
# #     print(items)
# #     if items == "milk": # when the condition is true the loop ends
# #         # break is a key word
# #         break # at this point when milk is found in items iterating through the shopping list the loop will stop
# # Lets create a dict of a food bill so we can iterate using loops
food_bill = {1: {"name": "James", "bill": "£1"}, 2: {"name": "Bond", "bill": "£2"},
             3: {"name": "shah", "bill": "£3"}
                              }

# for items in food_bill.keys():
#     print(items)

for items in food_bill.values():
    print(f"{items['name']}'s total is: {items['bill']}")











