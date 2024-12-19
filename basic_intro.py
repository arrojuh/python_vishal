# no @,$,!,% or other punctuations can be used to start the variable name
#no numbers can be used for starting a variable name
# alphabets or _ to be used for starting a variable name
# python is case sensititve and dynamic language.

# Print Statement


#Integer -- whole number
a = -1 # any whole number positive or negative included 0
type(a)

b = 1.0455 #any number with a decimal is float

c = 'kjbhvW923789873!!-O-9-239' #anything between " " or ''
type(c)

d = True  #either True or False
type()

e = '2023-02-23'  #2023-02-23 , 2023/02/23, 23 February 2023 #Timestamp, Datetime Format, Epoch Timestamp, Helix Timestamp

f = [1,'g','2023-02-23',1.023,True] #List is a collection of items within square brackets.
type(f)

g = {'key':'value','g':123} # dictionary is a collection of key value pairs in the braces({})
type(g)

h = (1,2,'a',True) # Tuple is a collection of items within parenthesis
type(h)

i = {1,2,3,'g','h','g'} #Set is a collection of unique elements (it removes duplicates) in {}
type(i)
print(i)

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




