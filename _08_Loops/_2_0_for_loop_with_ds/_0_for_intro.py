# Why for Loop: To iterate through group of values

print("-----------Result with class-----------")
# Get all student results
smarks = [45, 3, -5, 200, 65, 34, 78, 89]

for marks in smarks:
    print("---Student marks----", marks)
    # Decision Making



for marks in smarks:
    print("Student marks : ", marks)
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


# Data types
x = 10  # int(input("Enter number:"))  # 10 --> '10'  --> int('10') --> 10
print(x, type(x))

x = "Madhu"  # input("Enter name : ")
print("Name is : ", x, type(x))

# Data types

x = 10   # integer
x = 10.5  # float
x = True   # boolean
# char c = 'A' in other languages
msg = 'Hello World'  # string

# Data structures

msg = 'Hello World'         # string  # 'c' "Madhu"
list1 = [12, 23, 30, 443, 53]     # list  [43,23,564,32]  [10,10.4,True,'M','Madhu'] [[1,2],[3,4]]
tup1 = (1, 2, 3, 4, 5)      # tuple
dict1 = {1: 1, 2: 2, 3: 3}  # dictionary {'eid':100,'name':'MadhuN','sal':10000}  datatypes+str+tuple
set1 = {1, 2, 3, 4, 5, 6}   # set

# SEQUENCE:
'''
Sequence in Python:
=======================
String  : 'Hello World'
List    : [1,2,3,4,5,6,7]
Tuple   : (1,2,3,4,5,6,7)
range   : range(5)    ==>   0,1,2,3,4
          range(3)    ==>   0,1,2
          range(4)    ==>   0,1,2,3
          range(1,5)  ==>   1,2,3,4
          range(2,6)  ==>   2,3,4,5
          range(2,11,2) =>  2,4,6,8,10
          range(2,20,4) =>  2,6,10,14,18 
          range(3,50,6) =>  3,9,15,21,27,33,39,45   
-----------------------------------------------------
Dict 
Set



'''

# while
i = 1
while i <= 10:
    print(i)
    i += 1
print("---Outside loop---")



# for loop
'''
    Collection of elements

# Maths  :  collection of elements   : Matrix             Sequence   Set   
    
# Python :  Sequence                  : String List Tuple  Range         Dict Set  
                                         <bytearrays, buffers>
                                        -------------------------       --------------
                                              Sequences                 Not Sequences
                                          Indexing mechanism            Hashing algorithm
SYNTAX:
--------
Sequence: String, List, Tuple, range 

for <var> in <sequence>:
    # perform business logic
'''
print("--------For loop with String-------")

# REQ: Print each character of  String
# STATE
course = "PYTHON-PROGRAMMING-LANGUAGE"
         #0123456789..................
         #'python-programminng-language'
# BEHAVIOR
for char in course:
    print("Char : ", char)

print("----------String----------")
val = '12345'
for num in val:   # '1'  '2' '3' '4' '5'
    print("Value : ", num)

print("-------------------------")


'''
for num in 12345:
    print(num)

for num in 124.56:
    print(num)

for val in True:
    print(val)


'''
for val in "HE":
    print("Value : ", val)
for val in "H":
    print("Value : ", val)
ch = 'H'
print("Value : ", ch)


for val in [1, 2]:
    print("Value : ", val)


print("-------------------------")




print("----------End-----------------------")

print(10)  # SINGLE USAGE

x = 10
print(x)  # MULTIPLE TIMES USAGE
print(x*x)

print(10)
print(10*10)


# SINGE TIME USAGE
# -------------------------
for element in 'Python World':
    print("Character : ", element)

# MULTIPLE TIME USAGE
# -------------------------
msg = 'Python world'
for element in msg:
    print("Character : ", element)

# further business logic
print("data is : ", msg)

# DONT WRITE AS BELOW
# String with for loop
for char in 'Welcome to Python':
    print("Char : ", char)

# Code Pollution
for char in 'aflkdsfdsalfsdf  324324SDFDSF@!#@!$#@%fsdfsd dsfdsFDSf!@#@!#!@':
    print("Char : ", char)

password = 'aflkdsfdsalfsdf  324324SDFDSF@!#@!$#@%fsdfsd dsfdsFDSf!@#@!#!@'
for char in password:
    print("Char : ", char)


print("----FOR LOOP WITH LIST-------------")
# List with for loop
li = [1, 2, 3, 4, 5, 6, 7]

for val in li:
    print("value : ", val)

for val in li:
    print("Square of value : ", val ** 2)
print("------------------------------------------")

list1 = [1, 2.5, True, 'Madhu', [1, 2, 3], 5.0, False, 7]
      #  0    1    2      3        4       5    6     7

for val in list1:
    print("Value : ", val)

for val in list1:
    print("Value : ", val)  # Madhu [1,2,3]
    if type(val) == str or type(val) == list:
        for v in val:
            print("Char : ", v)



print("Further usage : ", list1)

print("----FOR LOOP WITH TUPLE-------------")
# Tuple with for loop
t1 = (1, 2, 3, 4, 5, 6, 7)
for val in t1:
    print("Tuple data :", val)
print("----------------------------")

print("----FOR LOOP WITH DICTIONARY-------------")

# Dictionary with for loops
e_data = {'eid': 100, 'name': 'Madhu Nettem', 'sal': 10000}

for key in e_data.keys():  # ['eid', 'name', 'sal']
    print("Dict key :", key)
print("--------------------------------")

for val in e_data.values():  # [100, 'Madhu Nettem', 10000]
    print("Dict val :", val)
print("--------------------------------")

for item in e_data:
    print("Dict data2 :", item)
print("--------------------------------")

for item in e_data.items():
    print("Dict data3 :", item)
print("--------------------------------")

for key, val in e_data.items():  # [('eid',100), ('name','Madhu Nettem'), ('sal',10000)]
    print("Dict data1:", key, val)
print("--------------------------------")


print("--------------FOR LOOP WITH SET---------------------")
# set with for loop
set1 = {1, 2, 3, 4, 5, 6}
for val in set1:
    print("Set value : ", val)

# Decimal number   0 to 255 1 byte
'''
 ASCII TABLE   
    -----------------------
    -----------------------
    7  6  5  4  3  2  1  0

0 to 255 -  ASCII TABLE    A 65  a 97
367  ---     10000001 
'''