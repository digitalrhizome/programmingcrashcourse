# store the names in a list, of three people you would like to ask to dinnner
dinner_list = ["Amelia Earhart", "M.K Gandhi", "Albert Einstein"]

def print_pretty(message):
    print("")
    print(message)
    print("")


my_message = "It looks like you have invited " + str(len(dinner_list)) + " people to dinner."
print_pretty(my_message)

def print_invitations():
    for dinner_guest in dinner_list:
        invitation = f"Hello, {dinner_guest}, you are invited to dinner at Chez Forrest, Oct 11, 2022.\nDinner starts at 7 PM, drinks and appetizers before starting at 6:30 PM"
        print_pretty(invitation)

#print_invitations()

print("Oops, it looks like M.K Gandhi can't make it, as he is on a hunger strike.")

dinner_list.remove("M.K Gandhi")
print_pretty(dinner_list)
dinner_list.insert(1, "Marie Curie")
print_pretty(dinner_list)

print_invitations()