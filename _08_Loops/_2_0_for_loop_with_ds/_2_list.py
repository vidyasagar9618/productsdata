x = 10
m_bill = 10
print("--------For loop with list-------")

list1 = [10, 32, 43, 13, 45, 65, 24, 75, 12]
      #  0    1   2   3   4   5   6  7   8
for num in list1:
    print("Number : ", num)

emp_ids = [10, 32, 43, 13, 45, 65, 24, 75, 12]
for eid in emp_ids:  # eid e_id empid emp_id
    print("Employee id : ", eid)

print("Square of each values in list ")

list1 = [1, 2, 3, 4, 5, 6, 7]
for each in list1:
    print("Square : ", each ** 2)

for s_no in [10, 32, 43, 13, 45, 65, 24, 75, 12]:  # stu_no
    print("Student no : ", s_no)

print("---------Filter even and odd numbers in list -----------")
'''
1. Get all values 
2. Filter  even or odd
'''

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # O  E  O  E  O  E

for val in li:
    if val % 2 == 0:
        print("Even : ", val)
    else:
        print("Odd  : ", val)





print("---------Print only indexes of list ******* -----------")

# Print only indexes
list1 = [10, 32, 43, 13, 45, 65, 24, 75, 12]
        # 0  1   2    3   4   5   6   7  8
le = len(list1)  # 9

for ind in range(le):  # 0 to 8
    print("Indexes :", ind)

print("----------Value based on index---------------------")
# ***** Iterate based on index
le = len(list1)
for ind in range(le):  # range(9)   0 to 8
    print(ind, "-----", list1[ind])


le = len(list1)
ind = 0
while ind < le:
    print(list1[ind])
    ind += 1



print("---------------------")

for val in list1:
    print(10)
    print(32)
    print(24)
    print(12)


'''
1. For loop with list of 1. All Integers
                         2. All Floats
                         3. All Boolean
                         4. All Strings
                         5. All Lists
                         6. All tuples
                         7. All dicts
                         8. All Sets
                         9. Heterogenous Data                
                
                
'''

# Find type of each element in list
# State
list1 = [10, 10.4, True, 'Hello', [1, 2, 3], (1, 2, 3), {1: 1, 2: 2}, {10, 20, 30}]
# Behavior
for val in list1:
    print("Value : ", val, type(val))



# Print only data structures  in list
# State
list1 = [10, 10.4, True, 'Hello', [1, 2, 3], (1, 2, 3), {1: 1, 2: 2}, {10, 20, 30}]
# Behavior
for val in list1:
    if type(val) == str or type(val) == list:
        print("Value : ", val, type(val))











