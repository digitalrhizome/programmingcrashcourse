# This program will store the quote and its famous author  in memory, then assemble a message and print that to std.output
# assign the quote to a variable
quote = "A person who never made a mistake never learned anything new."
famous_person = "Albert Einstein"
blank_line = "\n"
number_to_repeat = 80
screen_extras = "*" * number_to_repeat
print(blank_line)
print(screen_extras)
message = f"{famous_person} once said, \"{quote}\""
print(message)
print(screen_extras)
print(blank_line)