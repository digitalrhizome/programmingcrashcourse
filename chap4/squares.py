# putting together what we learned so far, to print a list of squares

# initialize an empty list, assign it to the variable
squares = []
for value in range(1,11):
    # we can make the program more concise by eliminating the temporary variable 'square'
    #square = value ** 2
    # and append each value directly to the list:
    squares.append(value**2)
# print the resulting list, it should print all the squares between 1 and 100, inclusive:
print(squares)

# Now we will use a list comprehension
print("Now we will generate and print the same list of squares, using a list comprehension")

squares = []
squares = [value**2 for value in range(1,11)]
print(squares)


