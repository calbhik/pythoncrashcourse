# functions
# print('a value')
# print(input('ask for a value'))

# methods -> functions of datatypes
# print('value'.upper())
# print('VALUE'.lower())
# print('value'.replace('e', '3'))
# # print(123.upper()) # integers do not have this method, it is only available for strings

# new functions
# print(abs(-10)) # returns the absolute value
# print(max(10,5)) # returns the biggest number
# print(min(0,1)) # returns the lowest number
# print(len('test')) # counts the number of characters inside the container and returns it to you

# pythagorean theorem calculator
side_a = int(input('The width of the triangle: '))
side_b = int(input('The height of the triangle: '))
hypotenuse = (side_a ** 2 + pow(side_b, 2)) ** 0.5
print('The hypotenuse is:', round(hypotenuse,2))