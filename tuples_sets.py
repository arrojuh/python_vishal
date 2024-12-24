# TUPLES
# tuple is a collection of items/elements in a () 
# it can be defined by putting the elements in () or  use the tuple() constructor/method

tup1  = (1,2,3,4,5) # using brackets
tup2 = tuple(('a','v',1,2,4,1.0)) # using tuple keyword
tup3 = tuple(['l','k',11,200]) # converting a list to tuple using tuple() constructor
tup4 = ([1,2,3,4]) #using paranthesis is not optimal to convert the data types to tuple
print(tup4)

list1 = [1,2,3,4,5]
list1[3] = 200

tup1[3] = 200

tup1[0]

tup1[1:4]

tup1[1:3:2]

tup1[-3]

empty_list = []
len(empty_list)

empty_tuple = ()
len(empty_tuple)

print(tup1,tup2,tup1+tup2)

tup1.count(3) #gives the count of element

sorted(tup1,reverse = True) # descending
sorted(tup1) # ascending

a,b,c = (1,2,3) # important aspect of tuple where it can be unpacked directly
print(a,b,c)

tup5 = (11,23,(44,55,66))
tup5[2][1]

# SETS
# collection of unique elements (no duplicates)
# automatically removes duplicates

set1 = {1,2,3,4,5,5,5,'a','a','b'}
print(set1)

set2 = {1,2,(4,5,6),[99,100,101,100]}

set3 = {1,2,2,(1,2,2),(1,2,2)}
print(set3)

set3[2] # set is not accessible by this method because the duplicates are removed and indexes are changed

a,b,c = set3

list(set3) #one method is to convert the set to list or tuple(wont let us modify)

for item in set3: # one way is running a loop on the items and extract them.
    print(item)
 

list3= ['o','p','1','1']

set4 = set(list3) # using a set constructor
print(set4)

set4 = set('Pyython')
print(set4)

list(set(list3)) # set is used to remove the duplicates from the list and converted back to list for additional properties

set2 = {'A','b',1,2,3}
print(set1,set2)

print(set1.intersection(set2))
print(set1^set2)
print(set1-set2)
print(set2-set1)
print(set1.isdisjoint(set2))

# in operator
print(list1,set1,tup1)
1 in list1
100 in tup1
't' in set1

# not in operator
print(list1,set1,tup1)
1 not in list1
100 not in tup1
't' not in set1

list2= [1,2,[6,7]]
6 in list2 # doesnt exist as a individual element
[6,7]  in list2 # True as it  exists as list

frz = frozenset((11,12,13))
print(frz)