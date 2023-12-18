

# REQ: Printing patterns
'''
1
12
123
1234
12345

   *
  *  *
*   *  *
'''

# REQ: Print numbers from 1 to 100, Number should be even and
'''
    Technical Analysis:    STATE   : int 1,100
                           Behavior: Operators: <=  == %
                                     DM       : if else 
                                     Loops    : while
'''
# State
num1 = 1
num2 = 100

# Behavior
if num1 < num2:
    print("---Valid Data---")
    while num1 <= num2:
        # if num1 % 2 == 0 and num1 % 5 == 0:
        if num1 % 2 == 0:
            if num1 % 5 == 0:
               print("Value : ", num1)
        num1 += 1
else:
    print("---Invalid Data")