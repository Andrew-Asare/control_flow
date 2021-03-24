# Control flow
##If, elf, if-elif and else
##For loops
##While loops
##Loops help iterate through the data 
- For loops
- While loops
- Data collections dict lists tuples strings
###What are if statements?
If statements are statements that utilize boolean conditional statements to decide upon the flow of
code.

'if' - The first part of an if statement that defines a condition for a result.
'elif' - The second part which defines an alternate condition for an alternate result.
'else' - The last part which runs only when no condition has been met.
```python 
if a == b:
    print("a is equal to b")
elif a > b:
    print("a is greater than b")
else:
    print("a is none of the above")
```
##Loops
###What are for loops?
For loops are loops that are generally used to iterate through objects or collections of objects. They are
also used when the number of times a loop should loop is known beforehand

For use iterating through an object instead of explicit print statements

```python
shopping_list = ["bread", "eggs", "milk", "orange"]


print(shopping_list)
print(shopping_list[0])
print(shopping_list[1])
print(shopping_list[2])
print(shopping_list[3])


for items in shopping_list:
    print(items)
```

Dictionaries can be looped through too:
```python
food_bill = {1: {"name": "James", "bill": "£1"}, 2: {"name": "Bond", "bill": "£2"},
             3: {"name": "shah", "bill": "£3"}}

for items in food_bill.keys():
    print(items)

for items in food_bill.values():
    print(f"{items['name']}'s total is: {items['bill']}")
```
