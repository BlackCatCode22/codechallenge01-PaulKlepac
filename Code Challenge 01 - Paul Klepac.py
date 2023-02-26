
# Example Code from Code Challenge 1
print("\n\n\n\n")
print("Welcome to CIT-95 Fall 2022 Module 01 Code Challenge!")

print()
print()

print("\n\n\n\n\n")

name = "Dmitriy"
weeks = "22 weeks"
weekly_pay = "$1234.56 per week"

long_string = name + " worked " + weeks + " for " + weekly_pay + "!"

print("\n\n", long_string, "\n\n")

# some_decimal_number = float("1234.56")
# these two are commented to test the one below (update it works)
# some_decimal_number = float("1234.56")

some_decimal_number = float("1234.56")
annual_salary = some_decimal_number * 52
print(annual_salary)

print(some_decimal_number)

my_math_number = 852.10
print("I needed this number:", str(my_math_number * 12))

my_new_num = some_decimal_number * 52
print(my_new_num)

print("\n\nThe annual salary is $" + str(my_new_num))

formatted_annual_salary = f'${my_new_num:,.2f}'
print("\n\nA better-looking salary figure: ", formatted_annual_salary, "\n\n")

def find_number_hiding_in_str(the_str_num):
    the_number_result = 0.0
    the_index = the_str_num.index("$")
    return the_index

pay_statement = "Dmitriy made " +str(formatted_annual_salary) + " last year."
print(pay_statement)

print("The $ in our figure is at index: ", str(find_number_hiding_in_str(pay_statement)))

index_of_space_after_money = pay_statement.find(" ", find_number_hiding_in_str(pay_statement))
print(index_of_space_after_money)



# Start of Three Coding Examples from Each Ref

# Example of python built in functions

print("\n\n\nThis is my example of Python Built-in Functions!")

basic_statement_a = "414235.10"
basic_statement_b = float(basic_statement_a)
basic_statement_c = (basic_statement_b * 12)
basic_statement_d = round(basic_statement_c)
print("\nMy pre round number is " + str(basic_statement_c))
print("My new rounded statement is " + str(basic_statement_d))

formatted_basic_statement = f'${basic_statement_d:,.0f}'
print("My formatted statement is " + formatted_basic_statement)

# Example of Python String Methods

print("\n\n\nThis is my example of Python String Methods!")

# use count, capitalize and lowercase and find

example_string = "Wow! This is a great example!"
lowercase_example_string = "this string is in all lowercase letters!"
uppercase_example_string = "THIS STRING IS IN ALL UPPERCASE LETTERS!"

print("\nFor this activity I will use '" + example_string + "' as an example string!")

string_count = example_string.count("!")
print("\nMy string uses '!' " + str(string_count) + " times!")

string_uppercase = lowercase_example_string.capitalize()
print("\nThis is before I use the uppercase function: " + lowercase_example_string)
print("Now this is the function after: " + string_uppercase)
#Now the first letter is uppercase yay

string_lowercase = uppercase_example_string.lower()
print("\nHere is the string before I make it all lowercase: " + uppercase_example_string)
print("Here is the string after: " + string_lowercase)

string_find = example_string.find("great")
print("\nIn the string: '" + str(example_string) + "', the phrase 'great' shows up " + str(string_find) + " letters in!")

# Here are my examples of Built-in Data Types

print("\n\n\nThis is my example of Built-in Data Types!")

# Do examples of the three main types and use the type function to show it.
#display the data type of x:
#print(type(x))
example_number = 123.45
integer_number = int(example_number)
string_number = str(example_number)
floating_number = float(example_number)

print("\nHere is my example number: " + str(example_number) + "!")
print("Here is my example number as an integer: " + str(integer_number) + ". The class is " + str(type(integer_number)))
print("Here is my example number as an floating number: " + str(floating_number) + ". The class is " + str(type(floating_number)))
print("Here is my example number as an string: " + str(string_number) + ". The class is " + str(type(string_number)))

# now multiply them all to demonstrate the type

print("\nHere is the Integer multiplied by 5: " + str(integer_number * 5))
print("Here is the Floating number multiplied by 5: " + str(floating_number * 5))
print("Here is the String multiplied by 5: " + str(string_number * 5))

#this concludes my examples
print("\nThis concludes my examples of the three catagories!")