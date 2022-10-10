# import necessary modules
import math


# store the names in a list, of three people you would like to ask to dinnner
dinner_list = ["Amelia Earhart", "M.K Gandhi", "Albert Einstein"]

def print_pretty(message):
    print("")
    print(message)
    print("")

# print a message announcing how many people you have invited to dinner
my_message = "It looks like you have invited " + str(len(dinner_list)) + " people to dinner."
print_pretty(my_message)

# Let's create a function to print the invitations. Yes, I know that is from later in the course. This is not my first Python rodeo!

def print_invitations():
    for dinner_guest in dinner_list:
        invitation = f"Hello, {dinner_guest}, you are invited to dinner at Chez Forrest, Oct 11, 2022.\nDinner starts at 7 PM, drinks and appetizers before starting at 6:30 PM"
        print_pretty(invitation)


# make a change to the guest list

print("Oops, it looks like M.K Gandhi can't make it, as he is on a hunger strike.")

dinner_list.remove("M.K Gandhi")
print_pretty(dinner_list)

# add another guest

dinner_list.insert(1, "Marie Curie")
print_pretty(dinner_list)


# Well we have found a bigger table, print out a message telling us that.
# Note that the instructions for exercise 3-6 specified to use the insert method to add a value to the middle of the list. 
# I assign a value for the middle of the list to the variable 'middle_of_list' by using the ceil function from the math module,
# which I apply to the value resulting from this operation: taking the len property of the dinner_list list, dividing by 2.
# anyway it seems to work

my_message = "We have found a bigger table and will be adding guests."
print_pretty(my_message)
middle_of_list = math.ceil(len(dinner_list) / 2)

print(math.ceil(middle_of_list))
dinner_list.insert(0, "Hypatia of Alexandria")
print(dinner_list)
dinner_list.insert(middle_of_list, "Mikhail Gorbachev")
print(dinner_list)
dinner_list.append("Prince Siddhartha")
print(dinner_list)

# now print the invitations

print_invitations()

my_message = "Well, we just found out that we have to have our dinner at our friend's house, as a water main broke. Therefore we can have only two dinner guests."
print_pretty(my_message)

while len(dinner_list) > 2:
    guest_we_must_uninvite = dinner_list.pop()
    print(f"With great regret, {guest_we_must_uninvite}, I must inform you that we had to reduce the guest list, and you are invited for our dinner next month")

print(dinner_list)

print_invitations()

my_message = "Now we will clear the list."

while len(dinner_list) > 0:
    del dinner_list[-1]

print_pretty(my_message)
print(dinner_list)

