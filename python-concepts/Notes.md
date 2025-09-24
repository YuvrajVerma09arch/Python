# 1. Lambda Functions
Lambda functions give you a concise way to write small, throwaway functions in your code.

## lists
container which can contain any other values even other list.

## Basic Methods
my_list = [1, 2]

my_list.append(3)
print(my_list)

print(my_list[0])

my_list[0] = 0
print(my_list)

my_list.insert(1, 1)
print(my_list)

my_list.pop()
print(my_list)

## Dictionaries data-type
Dictionaries are defined with curly braces ({}) and 
they contain key-value pairs separated by commas. 
Each key is followed by a colon (:) and the value:

## Filter Functions
The filter() function allows you to select items from
an iterable, such as a list, 
based on the output of a function:
filter() takes a function as its first argument and 
an iterable as its second argument.
It returns an iterator, which is a special object 
that enables you to iterate over the elements of a 
collection, like a list.

# Simple Expense Tracker
function:- add_expense.
parameters:- expenses,amount and category.


# 2. List Comprehension
Makes Code more concise.
In Python, a list comprehension is a construct that allows you to generate a new list by 
applying an expression to each item in an existing iterable and optionally filtering 
items with a condition. Apart from being briefer, list comprehensions often run faster.


# In-Built Methods used
* .isupper()-checks if the char is in uppercase. returns true or false.
* .lower-converts the char into lowercase.
* .join-used to attach the char in the list with empty string separator.
* .strip-used to clean the string from leading and trailing with any special characters.


# Case Converter
Converts the camelCase,PascalCase into snake_case.
Using Two Ways For loop and List Comprehension.
