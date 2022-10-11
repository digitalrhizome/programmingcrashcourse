# putting together what we learned so far, to print a list of squares

# initialize an empty list, assign it to the variable
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
# print the resulting list, it should print all the squares between 1 and 100, inclusive:
print(squares)
