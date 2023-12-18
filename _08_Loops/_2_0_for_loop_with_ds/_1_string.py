'''
for <var> in <sequence>:
    # perform business logic
'''
for val in "":
    print("Value1 : ", val)

for val in "H":
    print("Value2 : ", val)

for val in [1]:
    print("Li Value3 : ", val)

for val in (1,):
    print("Tuple Value4 : ", val)


print("--------For loop with String-------")
msg = 'Hello World'

for char in msg:
    print("Character : ", char)

for element in msg:
    print("Character : ", element)



# practice more use cases here

'''
1. Find char count 
2. Find capital letters,small letters
3. Find repeated char count 
4. Find vowels, consonants
5. Get alphabets, numbers, special chars 'DFDAS234sfddF$@##@$DSFS@#$FSDF'
6. Reverse a String*
7. Check Palindrome*
8. Find words in a string 
'''
# 1. Find char count   'Hello World'
# State
msg = 'Hello World'
# Behavior
counter = 0
for char in msg:
    counter += 1
print("Length of string : ", counter)



print("------------Parents Details------------")

family = ['Father', 'Mother', 'Brother1', 'Sister1']


for each in family:
    print("Family member name : ", each)
    for ch in each:
        print(ch)
    print("---------------------")





