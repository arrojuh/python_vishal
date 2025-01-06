print('Enter the name and it has to be a word')
name = input() # within the input keyword we can mention a string which can be used as a instruction
print('Hi', name)

age = int(input('ENTER THE AGE:: '))

print('age',age)

list_of_values = input('Input the values using a comma but not quotes:: ')
print(list_of_values)
list_of_values.split(',')

list(map(str,input('Enter::'))) # map function converts the input into individual element converting the element into provided datatype

tuple(map(float,input('Enter::')))

### TRY EXCEPT FINALLY
## ERROR HANDLING

inpt = input('ENTER ONLY DIGITS::')
if not int(inpt):
    print('Please enter a number')
    inpt = int(input('::'))
else:
    print('You have entered ',inpt)


inpt = input('ENTER ONLY DIGITS::')


finally:
    print('You have entered a number',inpt)

inpt = input('ENTER ONLY DIGITS::')

try:
    if int(inpt)>100:
        print('the input is greater than 100')
    else:
        print('NO WORRIES')
except:
    print('You didnt enter a number')
    inpt = input('ENTER ONLY DIGITS::')
    try:
        if int(inpt)>100:
            print('the input is greater than 100')
        else:
            print('NO WORRIES')
    except:
        print('You didnt enter a number')
finally:
    print("You have entered this number")

    