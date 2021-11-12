import random,sys,time

#intro slide
print('ROCK, PAPER, SCISSORS')

#stats variables
wins = 0
losses = 0
draws = 0

#main loop
while True: #main game loop
    print ('%s Wins, %s Loss, %s Ties' % (wins,losses,draws))
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            print('don\'t wan\'t none of this smoke huh')
            print ('FINAL TALLY IS... %s Wins, %s Loss, %s Ties' % (wins,losses,draws))
            sys.exit() # quit
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop, move on  to calculation.
        print('Type one of (r)ock, (p)aper, (s)cissors, or (q)uit.') #book had this in the wrong place
        #print player choice
    if playerMove == 'r':
        print('ROCK versus...')
        time.sleep(1)
    elif playerMove == 'p':
        print('PAPER versus...')
        time.sleep(1)
    elif playerMove == 's':
        print('SCISSORS versus...')
        time.sleep(1)

    randNum = random.randint(1,3)
    if randNum == 1:
        computerMove = 'r'
        print('ROCK!')
    elif randNum == 2:
        computerMove = 'p'
        print('PAPER!')
    elif randNum == 3:
        computerMove = 's'
        print('SCISSOR ME TIMBERS!')


    if playerMove == computerMove:
        draws=draws+1
        print("DRAW!")
    elif playerMove == 'r' and computerMove == 's':
        wins=wins+1
        print("WINNER WINNER CHICKEN DINNER!")
    elif playerMove == 'p' and computerMove == 'r':
        wins=wins+1
        print("WINNER WINNER CHICKEN DINNER!")
    elif playerMove == 's' and computerMove == 'p':
        wins=wins+1
        print("WINNER WINNER CHICKEN DINNER!") 
    elif playerMove == 'r' and computerMove == 'p':
        losses=losses+1
        print("LUH-HOO-SA-HER!")
    elif playerMove == 'p' and computerMove == 's':
        losses=losses+1
        print("LUH-HOO-SA-HER!")
    elif playerMove == 's' and computerMove == 'r':
        losses=losses+1
        print("LUH-HOO-SA-HER!") 