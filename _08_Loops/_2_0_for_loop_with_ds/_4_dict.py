print("-------For loop with Dictionary--------")
for val in range(0):
    print(val)

emp_details = {'eid': 100,
               'ename': 'MadhuN',
               'sal': 12500}

print("------All Keys-------")
for key in emp_details.keys():  # ['eid','name','sal']
    print(key)

print("------All Values-------")
for val in emp_details.values():  # [100,'Madhu',10000]
    print(val)

print("------All Items-------")
for item in emp_details.items():  # [('eid', 100),('ename', 'MadhuN'),('sal', 12500)]
    print(item)

print("------All Items-------")
for key, val in emp_details.items():  # [('eid', 100),('ename', 'MadhuN'),('sal', 12500)]
    print(key, val)


print("--------Only keys------")
for val in emp_details:
    print(val)

'''
e_details = { 'eid':100,
              'name':'MadhuN',
              'mobile': [1324324324,324324324]
              'emailid':['abc.xyz.com','adfdsfasdf']
              'address':[addr1,adr,addr2.....] 
}
'''

emp_details = {'eid': 100,
               'ename': 'MadhuN',
               'sal': 12500}

print(emp_details)

list1 = []
for key, val in emp_details.items():
    list1.append([key, val])
print(list1)


emp_details = {'eid': 100,
               'ename': 'MadhuN',
               'sal': 12500}

for data in emp_details.items():
    print(data)


