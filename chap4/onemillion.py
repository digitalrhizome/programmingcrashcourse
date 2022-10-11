# since we are going to be keeping track of time, let's import the proper python library
import datetime,time

# make a list of numbers from one to one million
number_list = []
for value in range(1,(1 + int(1E6))):
    number_list.append(value)

time.sleep(5)

print(min(number_list))
print(max(number_list))

time.sleep(5)

#for number in number_list:
#    print(number)

start_time = time.time()
atotal = sum(number_list)
end_time = time.time()
total_time = end_time - start_time
print(atotal)
print(f"To sum one million integers, Python took {total_time:0.4f} seconds")


