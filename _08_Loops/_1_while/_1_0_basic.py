print(range(1, 11))
'''
Loops: while for

# WHY LOOPS
# Print numbers between 1 to 10

# 1 2 3 4 5 6 7 8 9 10   

Step1: Assume starting number is  1
Step2: Print it
Step3: Increment current value by 1
Step4: Check whether it is less than or equal to 10
Step5: Print it or Stop it
'''
'''
REQ: Print numbers between 1 to 10 
==================================
S1: Initiate the value i.e,  starting value, ending value
S2: Increment each value 
S3: While writing on paper, check whether we reached to 10 or not 

1 2 3 4 5 6 7 8 9 10   
'''
print(1)
print(2)
print(3)
print(4)
print(5)

'''
REQ: Print numbers between 1 to 10 

Step1: Assume starting number is  1 
Step2: Check whether it is less than or equal to 10
Step3: Print it 
Step4: Increment current value by 1 

'''
st = 1
while st <= 10:
    print("Value : ", st)
    st += 1

print("-------End of Program-------")

'''
CRUD       : Create
STATE*     : int 
    Validation :  
Behavior*  : <=, while  
'''
# 1 2 3 4 5 6 7 8 9 10
'''
1 2 3 4 5 6 7 8 9 10
P1: Starting value 1                       x = 1
P2: Check we reached to 10 or not          x <= 10
P3: Write each value then increment by 1   x += 1
'''
# State
st = 1
end = 10
while st <= end:
    print("Value : ", st)
    st += 1

print("----End of Logic----")

'''
while 10:
    pass
    # send statement
    # sleep(24 hours)
    # cron job or Scheduler
'''
# Syntax:
'''
while <condition>:
    body of statements
'''

# Print numbers between 1 to 10 in reverse order
# 10 9 8 ..... 1

# State
x = 10
# Behavior
while x >= 1:
    print("Value : ", x)
    x -= 1
print("----End of while loop----")


# State
st = 10
end = 1
# Behavior
while st >= end:
    print(st)
    st -= 1

# Print even numbers  in a given range
print("-------Print even numbers in a given range (1 to 100)-----------")
'''
T0. Validate input data
T1. Print numbers in range 
T2. Only even numbers

 State*    : Data types/Structures  : int 
 Behavior* : Operators/DM/Loops     : <= += % ==  if  while     
'''
n1 = int(input("Enter starting value: "))
n2 = int(input("Enter ending value: "))


if n1 < n2:
    print("Valid input data")
    while n1 <= n2:
        if n1 % 2 == 0:
            print("Number : ", n1)
        n1 += 1
else:
    print("Invalid data")

print("----End of Program---------")




st = 200
end = 100

if st < end:  # 100,200   200,100    100,99 100,101
    print("Valid input")
    while st <= end:   # 100,200 100,101
        if st % 2 == 0:
            print("Value : ", st)
        st += 1
else:
    print("Invalid input")

st = 1
end = 100
while st <= end:
    if st % 2 == 0:
        print("Value : ", st)
    st += 1
print("-----------------------------------")




# State
st = 1
end = 100

# Behavior

while st <= end:
    if st % 2 == 0:
        print("Value : ", st)
    st += 1







while st <= end:
    if st % 2 == 0:
        print("Value : ", st)
    st += 1

print("----End of while loop----")

print("-----------Dynamic way-------------")
# STATE, Validation, Behavior
# STATE

n1 = int(input("Enter number 1 : "))  # 1
n2 = int(input("Enter number 2 : "))  # 100

# Validation   10 100,  100 10, 100 100
if n1 < n2:
    print("---Valid input data---")
    while n1 <= n2:
        if n1 % 2 == 0:
            print("Value : ", n1)
        n1 += 1
else:
    print("---Invalid data-------")



print("-----------------------------------------")


# REQ : Print Numbers between 1 to 100 which are divisible by 3 or 5
'''
   1. CRUD 
   2. State 
   3. Validation
   4. Behavior
   
1. High Level   : Numbers between 1 to 100 
2. Second Level : divisible by 3 or 5 
                  divisible by 3 or divisible by 5
# 3 5 6 9 10 12 15 18 20 21  ....
'''
# STATE
num1 = int(input("Enter start value1 : "))
num2 = int(input("Enter end value2 : "))

# Validation
if num1 < num2:
    print("---Valid Input---")
    while num1 <= num2:
        if num1 % 3 == 0 or num1 % 5 == 0:
            print("Value  : ", num1)
        num1 += 1
else:
    print("---Invalid Input---")




print("--------------------------------")

# Print numbers between 1 to 100 which divisible by 4 and 7
'''
1. Print numbers between 1 to 100
2. Only if divisible by 4 and 7
'''
# 28 56 84
# State
n1 = 1
n2 = 100
# Behavior
while n1 <= n2:
    if n1 % 4 == 0 and n1 % 7 == 0:
        print("Value : ", n1)
    n1 += 1





