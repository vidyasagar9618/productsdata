print("--------For loop with range-------")
'''
Range:   single value:  (end_val+1)                - range(10)       --> 0,1,2,3..9
         two values  : (st_val, end_val+1)         - range(1, 21)    --> 1,2,3....20
         three values: (st_val, end_val+1, diff)   - range(5, 101, 6) --> 5,11,17,23.....95
'''
# here range is special function
print(range(1, 100, 2))
'''
for i in [1,2,3,4,5...100]:
    print(i)
    
for i in range(101):  # [0 to 100]
    print(i)
    
range(10) ==> 0-9
range(5)  ==> 0-4

'''
print("----10------")
for val in range(10):  # 0 to 9  [0,1,2,3,4,5,6,7,8,9]
    print("Range val : ", val)

for val in range(10, 21):  # 10 to 20 [10,11,12,....20]
    print("Range val : ", val)

print("----5------")
for val in range(5):   # 0 1 2 3 4
    print("Range val : ", val)

print("-----0-----")
for val in range(0):
    print("Range val : ", val)

print("-----1-----")
for val in range(1):
    print("Range val : ", val)

print("----15 to 47----")
for val in range(15, 48):  # 15 to 47
    print("Range val: ", val)

print("----1 to 15----")   # 1 to 15
for val in range(1, 16):
    print("Range val: ", val)


print("----1 to 15 difference with 2----")
for val in range(1, 16, 2):
    print("Range val: ", val)


print("----1 to 30 difference with 3----")
for val in range(1, 31, 3):
    print("Range val: ", val)

print("-------------100 to 20------------")
for val in range(100, 20, -1):
    print(val)


print("-----Range with negative---------")
for val in range(20, 1, -1):
    print("Range val: ", val)
# -5 -4 -3 -2 -1 0 1 2 3 4 5 6
print("------ -20 to -40  1-------")
for val in range(-20, -10):
    print("Range val: ", val)

print("------ -20 to -40-------")
for val in range(-20, -40, -1):
    print("Range val: ", val)



for val in '':
    print(val)

for val in []:
    print(val)

for val in ():
    print(val)

for val in {}:
    print(val)

for val in set({}):
    print(val)

for val in range(0):
    print(val)
'''
for val in 10:
    print(val)

for val in None:
    print(val)
'''