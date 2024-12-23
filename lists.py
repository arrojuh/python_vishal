#List is a collection of elements in [] brackets

list1= [1,2.03,'Python',True,[1,'a','b']]
print(list1)

#indexing is applicable for list - starts from 0

print(list1[4])

print(type(list1[3]))


print(type(list1[2]))

list2 = ['1','a',5,56,00]

list3 = [1,2,3,4]
len(list3)

list2[2] = 'new_value' #modifying a list
print(list2)

list2.remove('1') #removing a list
print(list2)

print(list2)
list2.pop() #removes the end element of the list
print(list2)

list2.append('new_value2') #simply adds the element at the end
print(list2)

list2.insert(2,'new_value3') #insert the element at specific position
print(list2)

print(list2[1:4:2])

list3 = list1 + list2 #adding two lists

print(list1,list2,list3)
list4 = list2.copy() #creates a shallow copy and doesnt affect the original list
print(list4,list2)

list4[3] = 'test1'
print(list4,list2)

list5 = list2 #creates a copy and does affect the original list
print(list5,list2)

list5[2] = 'test2'
print(list5,list2)

print(list1,list2)
list1.extend(list2) #extends or absorbs the other list
print(list1)

list2.clear()
print(len(list2)) #len keyword to check the length of the list

list1[2] = 3.04
print(list1)

list1[1:3] = [1,2,3,4] #automatically expands the list

print(list1) 

del list2 #delete from the memory of python

print(list2)

print(list1)
list1.count(1) # counts all the occurences even within the nested list

list4 = ['a','b','e','c']

list4.sort() #sorts the list in ascending order, and only accepts the similar datatype

list4.reverse() #reverses the list
print(list4)

list5 = [1,2,3.04]
list5.sort(reverse= True) #does the sorting in descending order
print(list5)

print([1,2,3]*5) #simply repeats the list
print([1,2,3]*[3,4,5]) #doesnt multiply two lists

print(list4)
list4[list4.index('e'):list4.index('a')+1] #index lets us take the position of the element.



list6 = [1,2,4,[7,[5,6]],'a',['b','c','d']]

print(list6[3][1][0]) #use a nested indexing to access the desired element.
