# simplied version of CASE WHEN ELSE in SQL
# IF STATEMENT CAN EXIST WITHOUT ELSE
# syntax 
'''
if condition: 
     do something
else: 
     do something else
'''
##IF ELSE
if 1>2:
    print('different!')
else:
    print('Not Different')

## ELSEIF

if 1>2:## THE VALUE THE CONDITION GIVES IS TRUE AND FALSE and IF always chooses TRUE
    print('different!')
elif (12<9) == False:
    print('RIGHT!')
else:
    print('Not Different')


if (5 in [1,2,3,4,5]) and (1>2):
    print('Different')
elif 2<3:
    print('RIGHT!')
else:
    print('Not Different')

# multiple IF
if 1<2:
    print('NEW1')

if 2<3:
    print('NEW2')
else:
    print('RIGHT')



