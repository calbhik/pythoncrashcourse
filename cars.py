# # Python's sort() method makes it relatively easy to sort a list. Imagine we have a list of cars and want to change the order of the list to store them alphjabetically.
# # To keep the task simple, let's assume that all the values in the list are lowercase:
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)

# # You can also sort this list in reverse-alphabetical order by passing the argument reverse=true to the sort() method. The following example sorts the list of cars in 
# # reverse-alphabetical order:
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort(reverse=True)
# print(cars)

# # To maintain the original order of a list but present it in a sorted order, you can use the sorted() function. 
# # The sorted() function lets you display your list in a particular order, but doesn't affect the actual order of the list. 
# cars = ['bmw', 'audi', 'toyota', 'subaru']

# print("here is the original list:")
# print(cars)

# print("\nHere is the sorted list:")
# print(sorted(cars))

# print("\nHere is the original list again:")
# print(cars)



# # If we originally stored the list of cars in chronological order according to when we owned them, we could easily rearrange the list into reverse-chronological order:
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

# # Notice that reverse() doesn't sort backward alphabetically; it simply reverses the order of the list
cars.reverse()
print(cars)


# # You can quickly find the length of a list using the len() function. The list in this example has four items, so its length is 4:
print(len(cars))