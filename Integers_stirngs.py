##Integers

int1 = 234
int2 = 454

#basic math operations on integers
mult = int1*int2
addit = int1+int2
subt = int1 - int2
divd = int1/int2
print(mult,addit,subt,divd)

#Comparision Operators on Integers
eq_int = int1 == int2 #equals to  comparisons
print(eq_int)

not_int = int1 != int2 #not equals
print(not_int)

grt_int = int1 >= int2 #greater than
print(grt_int)


#Assign operators

var1 = 45
var1 = var1 + 50
var1 += 100
print(var1)

var1 = var1**2 #same as below
var1**=2 #same as above

#Logical Operators

int3 = 145
int4 = 199

print(int3 and int4)# always goes for higer value

print(int3 or int4) # always goes for lower value

print((int3 == int4) and (int3 < int4)) # Always gives precendence to False or both should be True for it to be True

print((int3 == int4) or (int3 < int4)) # Always gives precendence to True or both should be False for it to be False

print(int3 or int4) 
print(not (int3 > int4))

#Float 

# same as integer

flt1 = 124.099
flt2 = 245.124

flt1*flt2 #multiplication

flt1+flt2 #addition

flt1 - flt2 #subtraction


#all the operations done on Integer can be done on Float.

#STRINGS

#similar to character type(varchar) in SQL

str1 = 'tyopeisanak12e-@#1-00'

int1 = 123
str2 = '123'

len(str2)

str31 = 'Harikrishna'
str3 = 'Hari Krishna'
len(str31)
len(str3)

#pyhton inbuilt or functions or objects we use ()
#when we want acess indexes something then we use [] or a list
#for dictionary and set we use {} only in specific cases we use {} other than sets, whenever there is a key value pair we use {}

#Syntax for accessing one element  'string[index]'
max_index = length of the string -1
max_ind = len(str31)-1
last_index = str31[len(str31)-1]

print(str31[7])

print(str31[-1])
print(str31[-5])

#Syntax for accessing more than element 'string[start_index:end_index]' end_index is not included

print(str31[0:9])

print(str31[0:-1])

print(str31[5:])

print(str31[:9])

#Syntax for accessing more than one element skipping/jumping some elements 'string[start:end:jump]'

#illustration ::: start from 0, use the jump to increase the index 
# 0+1, 0+1+1, 0+1+1+1.... for positive indexing
# 0-1, 0-1-1, 0-1-1-1 .... for negative indexing

print(str31[::1])

print(str31[::2]) # even indexes

print(str31[::3])

print(str31[1::2]) # odd indexes

print(str31[::-2])

print(str31[::-1])


# adding two strings

str_add = 'hari'+' krishna' + ' 123'

#multiplying a string with integer repeats the string
str_mult = 'h'*10

#string allows equals and not equals operators
res1 = 'hari' == 'Hari' #becasuse its case sensitive

res2 = 'hari' != 'Hari'

print(res1,res2)

print(res1 and res2)

var1 = 'Harikrishna'
var2= 'Vishal'

 #.format method

 'Hello! {name}'.format(name=var1)
 'Hello! {name}'.format(name=var2)
 'Hello! {name}'.format(name= 98245)

print('value of abc {name} is this'.format(name = var1))
  
print('value of abc ', var1, ' is this') # combine multiple strings/datatypes and print

#f interpolation method

f'Hello! {var2}'

print(f'Hello! {var2}')

#STRING OPERATIONS

'Harikrishna'.upper()

str4 = 'Python'

str4[3] = 't'

str4.replace('y','t')

str4 = str4.replace('y','t')

print(str4)

str5 = 'Vis.h.a.l'

str5.replace('.','') #repalce the elements in string with other elements

split1= str5.split('.') #split the elements at specific string value or any value

''.join(split1) #join all the elements in the list using a singular value

str5.count('.') #count of occurencies 

#CONVERINT STRING TO other data types and vice versa

int1 = 12345

int_str = str(int1) #converting integer to string

import datetime 

str(datetime.datetime.now())

int_str = int_str.replace('3','9')
print(int_str)

str_int = int(int_str)

#string to other data types

int('123') # converting string to integer

float('23') # converting string to float



