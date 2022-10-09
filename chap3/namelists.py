# store a list of friend's names. for now, we will hardcode it. 
friends = ["David", "Kyle", "Chris"]
#print(friends[0])
#print(friends[1])
#print(friends[2])
friends.append("KTara")
#print(friends[3])

# use a for loop. not introduced in text, but i already know some Python.:-)
intro = f"We are doing to print a greeting to each person in my list of friends:"
blank_line = ""
print(blank_line)
print(intro)
print(blank_line)
for friend in friends:
    message = f"Hello, {friend}"
    print(message)

print(blank_line)





