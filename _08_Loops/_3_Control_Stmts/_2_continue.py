
print("------Continue---------")

# For a particular condition, we need to stop executing remaining lines of program
# and go to next iteration
# 1 2 3 4 5 6 7 8 9 10

'''
REQ:  # Numbers between 1 to 100 which are divisible by 5.
      # If value is also divisible by 10 don't display it.

Tasks: 1. Print between 1 to 100
       2. Find numbers divisible by 5  # 5 10 15 20 25 30 ....
       3. If same num divisible by 10 don't print it

'''
st = 1
end = 100

for val in range(st, end+1):
    if val % 5 == 0:
        if val % 10 == 0:
            continue
        print("Value :", val)





st = 1
end = 100
for val in range(st, end+1):
    if val % 5 == 0:
        if val % 10 == 0:
            continue
        print("value : ", 100)



print("-------------------------------")





st = 1
end = 100
for val in range(st, end+1):
    if val % 5 == 0:  # 5 10 15 20 25 30 35 ...
        if val % 10 != 0:   # if val % == 0 and val % 10 != 0:   5 15 25 ... 95
            print(val)
print("---------------------------")




for val in range(1, 101):    #  1 2 3 4 5 6 7 8 9 10 11 12
    if val % 5 == 0:
        if val % 10 == 0:
            continue
        print(val)  # business logic

# Print numbers between 1 to 100. Skip b/w 20 to 30. And stop after 90

for val in range(1, 101):
    if val >= 20 and val <= 30:
        continue
    print(val)
    if val > 90:
        break



'''
break    : 1. Remaining stmts will not be executed
           2. It breaks the loop and come out of it 
           
continue : 1. It will skip remaining stmts, will go to next iteration
pass     : 
'''
'''
if True:
    pass

while True:
    pass

for each in range(1,100):
    pass

print("Hello")
'''
# if elif else while for break continue pass

print("-------- Even numbers -------------")
# Print only first 3 even numbers between 1 to 50
counter = 1
for each in range(1,51):
    if each % 2 == 0:
        if counter > 3:
            break
        print(each)
        counter += 1
print("------Both continue break -----")

# Print even numbers.Skip first 3 even numbers and after 7th even number onwards
# Print even number count from 4 to 7 #  2 4 6 8  10 12 14 16.......
counter = 1
for each in range(1, 51):
    if each % 2 == 0:
        counter += 1
        if counter <= 4:
            continue
        print(each)
        if counter > 7:
            break

# Find even numbers count in list and print it
print("----Even number count---------")
list1 = [3, 5, 20, 6, 8, 2, 7, 3, 1, 6, 2, 6, 8, 4, 2]

count = 0
for val in list1:
    if val % 2 == 0:
        count += 1
        print(val)

print("Total even numers : ",count)


print("----Even number count tuple---------")
tupl1 = (3, 5, 20, 6, 8, 2, 7, 3, 1, 6, 2, 6, 8, 4, 2)

sum = 1
for val in tupl1:
    sum = sum * val  # 0+3 = 3 + 5 = 8
print("Sum of tuple :", sum)