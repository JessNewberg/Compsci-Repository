
Main():
    startgame = input ("It’s time to live out your feline dreams! You have 12 hours to do everything a housecat would do. \n Pay attention to both the time you have left in the day and your energy bar. \n Most activities will give you a choice of possible options, and depending on your choice, different things will happen. \n Follow the instructions for inputs, and have fun! \n  ✧/ᐠ-ꞈ-ᐟ\ \n Would you like to play or exit?")
    if startgame == "play":
        hoursleft = 12
        energyleft = 10 
        print ("Good Morning, Whiskers! It's a wonderful day to be a cat.")
        while hoursleft > 0 and energyleft > 10: 
            action = input ("What would you like to do? Hours: [hoursleft] Energy: [energyleft] \n To Pester Owner, Press 1. \n To Play with Toys, Press 2. \n To Take a Nap, Press 3. \n To Go in the Yard, Press 4. \n To Search for Treasures, Press 5. \n To Grab a Snack, Press 6. \n To Exit, Press 7." )
            if action == "1":
                pester_owner()
            elif action == "2":
                toy_play()
            elif action == "3":
                take_nap()
            elif action == "4":
                go_yard()
            elif action == "5":
                treasure_search()
            elif action == "6":
                grab_snack()
            elif action == "7":
                /break