# 3) Write a program with the following:
#       classes and methods: None
#       control structures: Sequence
#       data structures: Strings (arguably... a string is a Python data structure!)
#       error handling: None
#       functions: At least two user-defined functions. One with 3 parameters corresponding to the 3 user-input values
#           and another that will accept a string and find and return the first dollar amount in the string. You will
#           also use at least 3 of the 67 bulit-in Python functions -- print(), float(), str()
#       input: User input for:
#           name, number of weeks worked in a year, weekly pay
#       output: A string echoing the input values and the calculated annual salary properly
#            formatted in US Standard English e.g. "Katrina's annual salary working 52 weeks at $852.10 per
#            week is $10,225.20 USD per year." (Annual means yearly, but it is good to say things twice when
#            dealing with money.
#       processing: Calculate annual pay (weekly pay * 12)




# This is the start where I ask for the users name
print("\n\nHello! Welcome to my program! To start, what is your name?")
print("\n")
user_name = input()

# Next, I as them how many weeks they work per year and assemble it into one statement
print("\nHello " + user_name + "!")
print("\nNext, how many weeks do you work per year? Enter Below:")
print("\n")
weeks_worked = input()
print("\nAlright, your name is " + user_name + " and you have worked " + weeks_worked + " weeks this year!")

# Next, I ask for their weekly pay
print("\nNext, how much do you get paid per week? Be accurate!")
print("\n")
weekly_pay = input()

# Here I define big_pay as the function that compiles all the collected info into one string
def big_pay(user_name, weeks_worked, weekly_pay):
    return "\nOkay, " + user_name + ", you have or will work " + weeks_worked + " weeks this year at $" + weekly_pay + " per week!"
# prints big pay
print(big_pay(user_name, weeks_worked, weekly_pay))
# Here we calculate the pay and then format it and assign it to a new var.
calculated_pay = int(weeks_worked) * float(weekly_pay)
formatted_pay = f'${calculated_pay:,.2f}'

# Next, I call the formatted pay onto a string that then prints it
print("\nAccording to my calculations you should make " + formatted_pay + " USD per year!")
print("\nThank you for using my program!")
# f'${my_new_num:,.2f}' This is an example I used in the code

# Here I created the function, DollarFinder, to look for the dollar and then find its position. Then, I sliced
# the text to only find the spot I wanted.
def dollarFinder(input):
    dollar_found = input.index("$")
    my_val = input.find(" ", dollar_found)
    return input[dollar_found+1:my_val]

# here the user gets to pick a number to use in the example
print("\n\n\nHello, " + user_name + " please enter a number:")
print("\n")
user_dollar = input()

# here is a sample text to use the function on and then I printed it
a = "I have lots of money I have $" + user_dollar + " dollars"
# a = "I have lots of money I have $1000000.95 dollars"
print("\n\n\n" + str(a))

# Finally, I make total money, that formats the money given and then prints it. 
total_money = f'${float(dollarFinder(a)):,.2f}'
print("\n" + "My total money is: " + str(total_money))

