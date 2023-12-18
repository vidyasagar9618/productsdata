# Variables
'''
if we want to use value in one place,
then directly use the value
'''
print(10)
print(10+20)

'''
if we want to use value in multiple places,
then assign the value to a variable 
'''
x = 10
print(x)
print(x+20)

res = x+20
print(res)
print(res+100)


print("Addition is : ", 10+20)

x = 40
y = 50
print("Addition is : ", x+y)
print("Subtraction is : ", x-y)
print("Mulitplication is : ", x*y)
print("Division is : ", x/y)

print("Addition is : ", 10+20)
# Ideal approach
x = 10
y = 20
res = x+y
print("Addition is : ", res)

# Syntax of for loop
'''
for var in <sequence>:
    # body 

#Sequence:  String   "Hello World"
            List     [1,2,3,4,5,6]
            Tuple    [1,2,3,4,5,6]
            range    range(1,100)
'''
print("-----Single usage------")

for char in 'Hello World':
    print("Character : ", char)

print("-----Multiple usage-----")

msg = 'Hello World'
for char in msg:
    print("Character : ", char, char.upper())

print("Further usage : ", msg)