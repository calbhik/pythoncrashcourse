# Assigning a first name variable
first_name = "ada"

# Assigning a last name variable
last_name  = "lovelace"

# Creating an fstring that will replace the name of any variable in braces with its value
full_name = f"{first_name} {last_name}"

# Printing the full name using the fstring from before and capitalizing the first characters of 
# the first and last name using the title case method
# print(f"Hello, {full_name.title()}!")

# Using fstrings we can compose and assign an entire message to a variable
message = f"Hello, {full_name.title()}!"

#Printing the whole message "Hello, Ada Lovelace!"
print(message)

