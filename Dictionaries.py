# Dicitonary is a collection of Key:Value pairs in braces

dict1 = {'key1':450,'key2':'Python','key3':[11,12,13,14]}

#keys are always unique and only can contain string, integer or a tuple
#dictionary cannot exist in either key or value form
#values can be duplictes and can consist of different data types.

dict2= {'a':1,'b':1}

dict2['c'] = 3
#create a dictionary
#method1 -- creating a dictionary directly (can give integers as keys)
dict3 = {'y':'xyz','x':'123',1:23}
#method2 -- providing variables to dict to create a dictionary(no integers as variables)
dict4 = dict(name='hari',age =27,_2 = '23')
#method3
#creating a dictionary using a zipped/listed set of tuples
list_tup = [('name',1),(1,2),(199,'kim')]
dict5 = dict(list_tup)
print(dict5)


#Accessing the Elements

##-- input to give --()
##--- input to take --[]

dict4['name'] #always use the key to output the value

dict4.keys() # to print out all the keys of the dictionary

dict4['_2']

dict4.values()# to print out all the values of the dictionary

dict4.items() # to print out all the key,value pairs of the dictionary

dict4.get(None) #None is equalent to empty in python

dict4.get('ABC')# doesnt give error when key is not present

dict4['ABC'] # does give error when key is not present.

dict4.get('_2')


#DICT OPERATIONS

dict4['_2'] = 'new_value'
print(dict4)

dict4['_3'] = "New_Value2"
print(dict4)

dict4.popitem()
print(dict4)

dict4.pop('_2')
dict4

del dict4['age']
print(dict4)

del dict4
print(dict4)

dict5.update(dict3) # Absorb one dictionary to another.
print(dict5)

dict5 + dict3 # cannot add two dictionaries
len(dict3)
a,b,c = dict3.keys()
d,e,f = dict3.values()
dict5.items()
dict5[a] = d
dict5[b] = e
dict5[c] = f

print(dict5)


dict6 = {'a':1,'b':2,"c":{'aa':11,'bb':12}} #nested dictionary
dict6['c']['aa']

dict6.setdefault('key','Default') #doesnt affect the key if its already present else key and default value are added.
dict6.setdefault('key','Hello')
