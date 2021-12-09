
def computer_choice():
    computer_choice_options = ("rock","paper","scissors")
    import random
    computer_choice = random.choice(computer_choice_options)
    return computer_choice

def play_again_lose():
    choice2 = input ("Uh Oh! You lost. Do you want to play again? (y or n)")
    if choice2 == "y":
        rock_paper_scissors()
    else:
        print ("Good Game! :)")

def play_again_win():
    choice2 = input ("Yay you win! Do you want to play again? (y or n)")
    if choice2 == "y":
        rock_paper_scissors()
    else:
        print ("Good Game! :)")

           
def rock_paper_scissors():
    player_choice = input (str("Type 'rock!','paper!', or 'scissors!'"))
    def compare():
        if player_choice == computer_choice():
            choice2 = input ("Wow! We tied. What are the chances? Let's try again! Do you want to play again? (y or n)")
            if choice2 == "y":
                rock_paper_scissors()
            else:
                print ("Good Game! :)")
        elif player_choice == "rock!":
            if computer_choice() == "paper":
                play_again_lose()
            else:
                play_again_win()
        elif player_choice == "paper!":
            if computer_choice() == "scissors":
               play_again_lose()
            else:
               play_again_win()
        elif player_choice == "scissors!":
            if computer_choice() == "rock":
               play_again_lose()
            else:
               play_again_win()
    compare()
    
start = input ("Hello! Welcome to Rock, Paper, Scissors. To begin, type 'play'.")
if start == "play":
    rock_paper_scissors()
else:
    print ("Uh Oh! That's not a valid response.")


    
