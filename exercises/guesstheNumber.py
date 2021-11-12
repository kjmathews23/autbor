import random

supersecretnumber = random.randint(1,20)
print ('I am thinking of a number between 1 and 20')

#prompt user to try 6 times

for i in range(6):
    print('Try #' + str(i) + '; Guess your number')
    
    response = int(input())
    
    if response < supersecretnumber:
        print ('Too low, bitch.')
    elif response > supersecretnumber:
        print('Too high, biatch')
    elif response == supersecretnumber:
        print('You win you demon')
        break


