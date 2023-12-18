# Dynamic way of writing program

# REQ: Print even numbers in a given range
#    Criteria:     I. Range of value can be of 2 types
#                 II. Ascending Order
'''
1. It should be only in forward direction 100 to 200  "not 200 to 100"
2. Both numbers should not be same

Steps:
----------
1. CRUD
2. State
3. Validation
4. Behavior


'''

# Problem : No validation
print("===========With out validation==========")
st = int(input("Enter start value : "))
end = int(input("Enter end value : "))
while st < end:  # Business Logic
    if st % 2 == 0:
        print("Value : ", st)
    st += 1
print("---------------------------------")

# Solutions: Implement validation for input data
print("===========With validation==========")
# State
st = int(input("Enter start value : "))
end = int(input("Enter end value : "))

# validation logic: outer if else
if st < end:
    print("Valid data")
    # business logic
    while st <= end:
        print("Value : ", st)
        st += 1
else:
    print("Invalid data")
print("----------------------------------")








# Dynamic way of writing program
# Print even numbers in a given range
#    Criteria: 1. Range of value can be of 2 types
#                    I.Ascending II. Descending
# While ascending print even number, else odd numbers
# STATE
st = int(input("Enter start value : "))
end = int(input("Enter end value : "))

if st < end:
    while st < end:
        if st % 2 == 0:
            print("Value : ", st)
        st += 1
elif st > end:
    while st >= end:  # 200 - 100    99 >= 100
        if st % 2 == 1:
            print("Value : ", st)
        st -= 1
else:
    print("Cant iterate")

while st <= end:
    print("Value is : ", st)
    st += 1

print("-----------Result with class-----------")

# STATE
marks = int(input("Enter exam marks  :"))

# BEHAVIOR

# 1. Validation
# if marks >= 0 and marks <= 100:
if 0 <= marks <= 100:
    print("Valid marks")
    if marks >= 35:
        print("Result PASS ")
        if marks >= 60:
            print("First Class")
            if marks >= 90:
                print("Distinction")
                if marks == 100:
                    print("Congratulations")
        elif marks >= 50:
            print("Second Class")
        else:
            print("Third Class")
    else:
        print("Result FAIL")
else:
    print("Invalid marks")

print("--------------------------------------")

# I REQ. Gathering : Print numbers from 1 to 10
# 1
# Code duplication, we can't extend when requirement changes

# State    : Is changing in each iteration
# Behavior : Same: Printing the data

print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

# I REQ. Gathering : Print numbers from 1 to 10

# Maths: 2 subprocesses
# write current number
# +1 in each iteration
# check whether values is <= 10
'''
1 2 3 4 5 6 7 8 9 10 

'''

'''
while <condition>:
    <stmts. body> 
'''
print("------------while loop----------------")
i = 1
while i <= 10:  # 3. check whether value reaches to 10
    print(i)  # 1. write it on paper
    i += 1  # 2. increment the value

print("End of program")

print("-----End of while loop-----")

'''
Print numbers between 1 to 10 except 5.

P1: Print number        1 2 3 4 6 7 8 9 10
P2: Increment number
P3: Check number <= 10
P4: Check num == 5
'''
print("----Numbers between 1 to 10 except 5----")
i = 1
while i <= 10:
    if i != 5:
        print(i)
    i = i + 1

print("----Even Numbers between 1 to 10 ----")

i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

print("------Numbers between 1 to 30 divisible by 3 and 5")

i = 1
while i <= 30:
    if i % 3 == 0 and i % 5 == 0:
        print("Value : ", i)
    i += 1

print("------Numbers between 1 to 100 divisible by 4 or 5 or 7")

i = 1
while i <= 100:
    if i % 4 == 0 or i % 5 == 0 or i % 7 == 0:
        print(i)
    i += 1

'''
# STATE 
--------
1. Data initialization     x = 1

# BEHAVIOR
------------
2. Condition verification       while x <= 10:
3. Business logic                   print(x)
4. Operation on input data          x += 1
'''

print("--------------")
# II REQ. Gathering : Print numbers from 10 to 1
# 10 9 8 7 6 5 4 3 2 1
# STATE
x = 10
while x >= 1:
    print(x)
    x -= 1

# SDLC - Agile methodology

# I REQ. Gathering : Print even numbers from 15 to 100
'''



'''
'''
# II - ANALYSIS
        1. Functional analysis : We need to print the numbers between starting and 
                                 ending number given by customer
        2. Technical analysis  : STATE    :  input: start, end (int)
                                 BEHAVIOR :  Operators: <= ==  
                                             DM       : if,else 
                                             Loops    : while  
III.  Design : NA
'''
# IV. DEVELOPMENT
print("-----------While 15 to 30-----------")
print("--------WIHTOUT VALIDTAION---------")
# STATE
start = int(input("Enter number1 :"))
end = int(input("Enter number2 :"))
# BEHAVIOR
while start <= end:  # less than or equal 15 <= 15
    if start % 2 == 0:
        print(start)
    start += 1
print("***** End of program *****")

# V. TESTING:    tester found that validation is missing
'''
Test cases                                    Exp output           Act. output     Result
----------------------------------------------------------------------------------------------
    T1. Give lower,upper value and test      Print numbers b/w     As Expected          PASS 
    T2. Give upper,lower value and test      Should dispaly error  Its not displaying   FAIL
'''

# As a developer, will fix the issue by adding validation
print("--------AFTER FIXING THE ISSUE---------")
start = int(input("Enter number1 :"))
end = int(input("Enter number2 :"))
if start <= end:
    print("### Valid Input ###")
    while start <= end:
        print(start)
        start += 1
else:
    print("### Invalid Input ###")

print("***** End of program *****")

'''
Print even numbers between 1 to 100
    I. Print numbers 1 to 100
    II. Filter even numbers
'''

st = 1
end = 100
while st <= end:
    if st % 2 == 0:
        print("Value : ", st)



