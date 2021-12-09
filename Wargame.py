import random
    
def rules():
    print ("The rules of the game are simple.\n When you begin the game, a standard deck of 52 cards will be shuffled.")
    print ("26 of those cards will be dealt to you, and the other 26 will be dealt to the computer player.")
    print ("Once the decks have been shuffled, you and the computer (Their name is Sally) will both flip a card at the same time.")
    print ("If your number is bigger, you win a point, and Sally loses a point. If your number is smaller, the opposite occurs.")
    print ("If you and Sally tie, you enter a tiebreaker. Another card is drawn, the stakes are raised to  points.")
    print ("At the end of a round(26 draws), whoever has more points wins!")
    play = input ("So.... Would you like to play? (yes or no)")
    if play == "yes":
        war()
    else:
        print ("Okay! Maybe another time.")

def shuffle():
    global carddeck
    carddeck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4
    random.shuffle(carddeck)
    print (".\n.\n.\n")
    print ("cards have been shuffled!")
    return carddeck

def deal():
    global playerdeck
    global compdeck
    global cardsleft
    global playertotal
    global comptotal
    cardsleft = 26
    playertotal = 0
    comptotal = 0
    playerdeck = carddeck[0:26]
    print("Player's Deck:")
    print (playerdeck)
    compdeck = carddeck[26:52]
    print("Sally's Deck:")
    print (compdeck)
    print (".\n.\n.\n")
    print ("cards have been dealt!")

def draw():
    global playercard
    global compcard
    playercard = playerdeck.pop(random.randint(0,len(playerdeck)-1))
    compcard = compdeck.pop(random.randint(0,len(compdeck)-1))

def finalscore():
    print (".\n.\n.\n")
    global playertotal
    global comptotal
    print (f'the game is complete! Time to compare the results. playertotal = {playertotal}. comptotal = {comptotal}.')
    if playertotal == comptotal:
        print ("IT'S A TIE! What are the odds?")
    elif playertotal > comptotal:
        print ("YOU WON! Congratulations!!!") 
    else:
        print ("You Lost... Better luck next time!")
    choice = input ("\n Would you like to play again? y or n")
    if choice == "y":
        war()
    elif choice == "n":
        print ("Good Game! Sally enjoyed it, and we hope you did too. Bye!")
        exit()

def compare():
    global playerdeck
    global compdeck
    global cardsleft
    global playertotal
    global comptotal
    if playercard == compcard:
        if playercard == compcard:
            draw()
            if playercard == compcard:
                print (f'playercard: {playercard}. compcard: {compcard}. Tie! +0.')
                cardsleft = cardsleft - 1
            elif playercard > compcard:
                print (f'TIEDRAW! playercard: {playercard}. compcard: {compcard}. Player +2!')
                playertotal = playertotal + 2
                cardsleft = cardsleft - 1
            else:
                print (f'TIEDRAW! playercard: {playercard}. compcard: {compcard}. Sally +2!')
                comptotal = comptotal + 2
                cardsleft = cardsleft - 1
    elif playercard > compcard:
        print (f'playercard: {playercard}. compcard: {compcard}. Player +1!')
        playertotal = playertotal + 1
    else:
        print (f'playercard: {playercard}. compcard: {compcard}. Sally +1!')
        comptotal = comptotal + 1

def war():
    global cardsleft
    shuffle()
    deal()
    while cardsleft > 0:
        global a
        a = int (input (f'type the number(integer)of rounds you want to play! rounds left: {len(playerdeck)}'))
        while a > 0 and len(playerdeck) > 0:
            draw()
            compare()
            a = a - 1
            cardsleft - 1
            if len(playerdeck) == 0:
                finalscore()
    
        
    
start = input ("Hello! Welcome to.... War! To begin, type 'play'. To see the rules, type 'rules'.")

if start == "play":
    war()
elif start == "rules":
    rules()
else:
    print ("Uh Oh! That's not a valid response.")
