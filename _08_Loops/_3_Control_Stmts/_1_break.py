# REQ: Print first 7 numbers between 1 to 100 which are divisible by 5.

'''
1. print 1 to 100
2. divisible by 5
3. only first 7

1 2 3 4 5 6 7 ..... 100
10

5 10 15 20 25 30 35      36 to 100

count : 7
'''
count = 0
for val in range(1, 101):
    if val % 5 == 0:
        print("Value : ", val)
        count += 1
        if count == 7:
            break
print("Come out of loop")



print("----------End of for loop----------")








# State
vals = range(1, 101)
# Behavior
counter = 0
for val in vals:
    if val % 5 == 0:
        print("Value  ", val)
        counter += 1
        if counter == 7:
            break

print("------end of the loop------")




count = 0
for val in range(1, 101):
    if val % 5 == 0:
        print("Value : ", val)
        count += 1
        if count == 7:
            break

print("-----------------------------")


# State
st = 1
end = 100
# Behavior
counter = 0
for val in range(1, 101):
    if val % 5 == 0:
        counter += 1
        print("Value : ", val)
        if counter == 7:
            break

print("-------------------------------------")







count = 0
for val in range(1, 101):
    if val % 5 == 0:
        print(val)
        count += 1
        if count == 7:
            break

print("---Remaining statements----")
count = 0
for val in range(1, 101):
    if val % 5 == 0:
        print(val)
        count += 1
        if count == 7:
            break


'''
1. print 1 to 1000
2. divisible by 5
3. only first 7      5 10  15  20   25  30 35 | 7 
'''
'''
First 7 Last 7 numbers which are divisble by 5 between 1 to 100
    1...............1000
    ---->         <-----
'''

li = []
for val in range(1, 101):
    if val % 5 == 0:
        li.append(val)
print("Divisibe by 5 :", li)
print("First 7 : ", li[0:7])
print("Last 7  : ", li[:7:-1])


x = 10
a = 10
i = 10
eid = 10

x = 100
patient_id = 100 # pid pat_id



# Control statements : break continue pass
# Will use control statements in  while for loops
'''
REQ: Print first 7 even numbers between 1 to 100
    1. Get all numbers from 1 to 100
    2. Filter only even numbers
    3. Get only first 7 even numbers

            1    2  3  4  5  6  7  8  9 10
            11  12 13 14 15 16 17 18 19 20
            21  22 23 24 25 26 27 28 29 30......

            first 3 even numbers
                    solution                   roguht work                      count
              | 2 4 6 8 10 12 14        | 1%2 == 0 2%2 == 0                  3
                                          3%2 == 0 4%2 == 0
                                          5%2 == 0 6%2 == 0  Stops here
                                          7%2 == 0  8%2 == 0  XXX
'''

'''
   Steps:     1. Get all numbers from 1 to 100
              2. Filter only even numbers
              3. Get only first 7 even numbers
1.  Print numbers  between 1 to 100
2.  Print even numbers
3.  Get only first 7 even nos
4.  Break the loop 
'''
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

# Print FIRST 5 even numbers between 50 to 80
count = 0
for val in range(50, 81):
    if val % 2 == 0:
        print(val)
        count += 1
        if count == 5:
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