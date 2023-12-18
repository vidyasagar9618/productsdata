
'''
n1 = 100
n2 = 200
# 5 values
'''
# 123 156 135 175 153
'''
list1 = [10,20,30,40,50]
         0   1 2   3  4
for val in list1:
    print(val)


x = 10
Syntax :
------------
# for loop syntax
        for <var> in <sequence>:
           # statements

string list tuple
'''
'''
       4
       S    5x   = 5(1) + 5(2) + 5(3) + 5(4)    [1,2,3,4]
     x = 1       = 5 + 10 + 15 + 20  = 50
'''
sum = 0
for x in range(1, 5):   # 1,2,3,4
    result = 5 * x
    sum += result
print("Sum : ", sum)

n1 = int(input("Enter number1 : "))
n2 = int(input("Enter number2 : "))

for val in range(n1, n2):
    print(val)


'''
numbers system -1,-2/4, 34.4, 56, 3 4/5, 0 ,00
advanced concepts : Sequence,Series  1 to 100 -- n(n+1)/2
                  : Sets {1,2,3} U {2,3,4}
                  : Matrix []


'''

# 1. Find sum of numbers from 1 to 100
    # Using while
i = 1
sum = 0
while i < 101:  # i <= 100
    sum += i  # sum = sum + i
    i += 1
print("Total : ", sum)

sum = 0
for i in range(1, 11):  # #  1 2 3 4 5 6 7 8 9 10
    sum += i
print("Total : ", sum)






# Data Types
x = 10    # integer
x = 10.5  # float  complex long
is_male = True  # boolean

# Data structures
message = "Hello World"  # String
numbers = [1, 2, 3, 4, 5]  # list  # List<Integer> list1 = new ArrayList<Integer>()  list1.add(1)
numbers = (1, 2, 3, 4, 5)  # tuple
emp_details = {'eid': 100, 'name': 'Madhu', 'sal': 1000}  # Dictionary
emp_ids = {1, 2, 3, 4, 5, 6}   # Set

print("---------String--------------")
# for loop with strings
message = "Hello World"
print(message)
for char in message:
    print(char)
print("End of for loop")

number = "12345"
for num in number:  # "1" "2" "3"
    print(num)

print("---------List--------------")
# for loop with list
numbers = [1, 2, 3, 4, 5]
for value in numbers:  # 1 2 3 4 5
    print(value)
print("End for loop")

numbers = ['1', '2', '3', '4', '5']
for value in numbers:  # '1' '2' '3' '4' '5'
    print(value)
print("End for loop")

numbers = (1, 2, 3, 4, 5)

print("---------Tuple--------------")
for val in numbers:
    print(val)

print("---------Dictionary--------------")
emp_details = {'eid': 100, 'name': 'Madhu','sal': 1000}

print("----Items-----")
for key, val in emp_details.items():
    print(key, " : ", val)

print("----Keys------")
for key in emp_details.keys():
    print(key)

print("-----Values-----")
for val in emp_details.values():
    print(val)

print("---------Set--------------")
emp_ids = {1, 2, 3, 4, 5, 6}
for eid in emp_ids:
    print(eid)


# Find student grade (Operators, DM, Loops with CS)

# marks = int(input("Enter marks :"))

# data = [-1, 0, 1, 99, 100, 101, 34, 35, 36, 59, 60, 61, 49, 50, 51]
marks = {143243: 23, 2234324: -35, 3543543: 506, 4543543: 98, 532434: 0, 65435: 100}

for rno, marks in marks.items():
    print("Details : ", rno, marks)
    if marks >= 0 and marks <= 100:
        print("Valid marks")
        if marks >= 35:
            print("Result : PASS")
            # Student Division
        else:
            print("Result : FAIL")
    else:
        print("Invalid marks")
    print("-------------------------")





for rno, marks in marks.items():
    # Validation
    print(" ****** RESULT FOR ******", rno)
    if marks >= 0 and marks <= 100:
        if marks >= 35:
            print("-- RESULT : PASS --")
            if marks >= 60 and marks <= 100:
                print("- First Class -")
                if marks == 100:
                    print("** Distinction **")
            elif marks >= 50 and marks < 60:
                print("- Second Class -")
            else:   # 35 - 50
                print("- Third Class - ")
        else:
            print("-- RESULT : FAIL --")
    else:
        print("---Invalid marks---")
    print("--------------------THANK YOU--------------------")

