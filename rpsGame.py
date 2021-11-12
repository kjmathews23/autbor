import random,sys
print('ROCK, PAPER, SCISSORS')

#stats variables
wins = 0
losses = 0
draws = 0

#main loop
while True:
    print ('%s Wins, %s Loss, %s Ties' % (wins,losses,draws))
    playerMove = input()
    if playerMove == 'q':
        print('don\'t wan\'t none of this smoke huh')
        sys.exit() # quit
    if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop, move on  to calculation.
    print('Type one of r, p, s, or q.') #why is this here? end of the 1st loop iteration?
