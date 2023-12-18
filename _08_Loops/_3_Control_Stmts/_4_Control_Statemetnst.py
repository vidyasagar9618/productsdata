# Control statements : break continue pass
# Will use control statements in  while/for loops

# Print first 25 even numbers without 10 multiplier values between 1 to 100
'''
  1. Print 1 to 100
  2. Filter even numbers
  3. First 25
  4. Dont print 10 multiple values

 2 4  6 8 10 12 14 ...48 50                   |    25
'''
n1 = int(input("Enter start value : "))
n2 = int(input("Enter end value : "))
if n1 < n2:
    count = 0
    for val in range(n1, n2):
        if val % 2 == 0:
            if val % 10 == 0:
                continue
            print(val)
            count += 1
            if count == 25:
                break
else:
    print("-----Enter valid numbers-----")

print("------------End of program------------")


count = 0
for val in range(1,101):
    if val % 2 == 0:
        print(val)
        count += 1
        if count == 7:
            break


'''
REQ: Print first 7 even numbers between 1 to 100
                1. Get all numbers from 1 to 100
                2. Filter only even numbers
                3. Get only first 7 even numbers

            1    2  3  4  5  6  7  8  9 10
            11  12 13 14  .............100 

            first 3 even numbers
                    solution                   rough work                      count
              | 2  4  6  8 10 12 14  |     | 1%2 == 0 2%2 == 0                   2
                                          3%2 == 0 4%2 == 0
                                          5%2 == 0 6%2 == 0  Stops here
                                          7%2 == 0  8%2 == 0  XXX
'''

'''Steps:     1. Get all numbers from 1 to 100
              2. Filter only even numbers
              3. Get only first 7 even numbers
              
1.  Print numbers  between 1 to 100
2.  Print even numbers
3.  Get only first 7 even nos
4.  Break the loop 
'''
# REQ: Print first 7 even numbers between 1 to 100
count = 0
for val in range(1, 101):
    if val % 2 == 0:
        print(val)
        count += 1
        if count == 7:
            break

print("--------End of program--------")


st = int(input("Enter st value"))
end = int(input("Enter end value"))
counter = 0
# add validation
for val in range(st, end+1):
    if val % 2 == 0:
        print(val)
        counter += 1
        if counter == 7:
            break
print("End of for loop")
print("------------------------")
num = 1
count = 0
while num <= 100:
    if num % 2 == 0:
        print(num)
        count += 1
        if count == 7:
            break
    num += 1
print("End of while loop")






# Print first 7 even numbers between 1 to 100

'''
From 1 to 100
1.  Print numbers  between 1 to 100
2.  Print even numbers
3.  Get only first 7 even nos
4.  Break the loop 
'''
print("----Print only first 7 numbers-------")
count = 0
for val in range(1, 101):
    if val % 2 == 0:
        count += 1
        print(val)
        if count == 7:
            break
print("After for loop break")



num = 1
counter = 0
while num <= 100:
    if counter > 7:
        break
    if num % 2 == 0:
        print(num)
        counter += 1
    num += 1
print("Exited while loop")


print("--------Using for loop-------------")

# REQ: Print first 7 even numbers betweeen 1 to 100
'''
1.  Print numbers between 1 to 100
2.  Print even numbers
3.  Get only first 7 even nos
4.  Break the loop 
'''
counter = 0
for val in range(1, 101):
    if val % 2 == 0:
        print(val)
        counter += 1
        if counter == 7:
            break
print("-----End of for loop-----")


print("----Other program-------")
# Print even numbers between 50 to 80
for val in range(1, 101):
    if val >= 50 and val <= 80:  # val > 49 and val < 81
        if val % 2 == 0:
            print(val)
    elif val > 80:
        break
print("End of for loop")



# break continue pass


# sequence string list tuple dict set

# range
'''
i = 1
while i <= 100:
    print(i)
    i += 1


for val in range(50, 101):  # 0 1 2 3 4 ..... 99
    print(val)
'''
'''
break
REQ: Find first 3 numbers which are divisible by 3 between 500 to 1000
501
504
507                  500 501 502 503 504 505 506 507 508   3



1. Print numbers bw 500 to 1000
2. Filter divisible by 3 
3. Break the loop once we get 15 count


i = 500
counter = 0
while i <= 1000:
    if i % 3 == 0:
        counter += 1
        print(counter," : ",i)
        if counter == 15:
            break
    i += 1
# Approach2
counter = 1
for val in range(500,1001):
    if val % 3 == 0:
        print(counter, " : ",val)
        counter += 1
        if counter > 15:
            break
'''