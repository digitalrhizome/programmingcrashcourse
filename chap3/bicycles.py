# start working with lists
# define our first list
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
print("The first item in the list is:", bicycles[0])
print(bicycles[0].title())
print(bicycles[0].upper())
print("The second item in the list is:", bicycles[1])
print(bicycles[3])
print("Using an index of -1, we can print the last item in this list, which is:", bicycles[-1])

# now let's start doing more with individual values and combinations of these values
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)
