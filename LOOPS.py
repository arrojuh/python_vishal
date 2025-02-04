# syntax
'''
for item in iterable:
    do something
'''
list1 = [1,2,3,4,5]
tup1 = (6,7,8,9)
t = range(10,20)

for i in list1:
    print(i)

num = 'yayati'
for j in tup1:
    print(num)

for t in range(10,20):
    print(t)

''' 
while condition is true:
     do something'''


i = 10
while i>5:
    print(i)
    i = i-1

i = 10
k = 'yes'
while k == 'yes':
    print(i)
    i = i-1
    if i == 0:
        k = 'no'
        