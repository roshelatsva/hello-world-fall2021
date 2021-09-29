from typing import overload



# score = 0
# score = int(score)



#play again
def play_again():
    print ("\nDo you want to play again? (y or n) ")

    answer = input (">").lower()

    if answer == "y":
        start ()
    else:
        exit()    

#game over
def game_over(reason):
    print ("\n" + reason )
    print ("  ---.  ,--,--.,--,--,--. ,---.      ,---.,--.  ,--.,---. ,--.--.    ")
    print (" | .-. |' ,-.  ||        || .-. :    | .-. |\  `'  /| .-. :|  .--'   ")    
    print (" ' '-' '\ '-'  ||  |  |  |\   --.    ' '-' ' \    / \   --.|  |      ")       
    print (" .`-  /  `--`--'`--`--`--' `----'     `---'   `--'   `----'`--'      ")      
    print (" `---'                                                               ")                                                                 



#diamond room
def diamond_room():
    print ("\nYou are now in a room full of diamonds!")
    print ("  .     '     ,                         .     '     ,      ")
    print ("    _________        .     '     ,        _________        ")  
    print (" _ /_|_____|_\ _       _________       _ /_|_____|_\ _     ")   
    print ("   '. \   / .'      _ /_|_____|_\ _      '. \   / .'       ")    
    print ("     '.\ /.'          '. \   / .'          '.\ /.'         ")   
    print ("       '.'              '.\ /.'              '.'           ")     
    print ("                          '.'                              ")
    print ("And there is a another door...")
    print ("Choose the following options: ") 
    print ("1. Take some diamonds and go through the door.")
    print ("2. Leave the diamonds and exit the door.")

    answer = input (">")
   
    if answer == "1":
        game_over("They were cursed diamonds! The moment you touched them, the building collapsed and you died!")
    elif answer == "2":
        print ("You are not a greedy person! Congrats you have won the game!")  
        play_again()  
    else:
        game_over("Sorry try again later!")


#monster room
def monster_room():
    print ("\nDamn! You have entered a room full of monsters!")
    print ("                _.------.                        .----.__       ")       
    print ("               /         \_.       ._           /---.__  \      ")      
    print ("              |  O    O   |\ ___  //|          /       `\ |     ")     
    print ("              |  .vvvvv.  | )   `(/ |         | o     o  \|     ")    
    print ("              /  |     |  |/      \ |  /|   ./| .vvvvv.  |\     ")    
    print ("             /   `^^^^^'  / _   _  `|_ ||  / /| |     |  | \    ")     
    print ("          ./  /|         | O)  O   ) \|| //' | `^vvvv'  |/. \   ")
    print ("         /   / |         \        /  | | ~   \          | \  \  ")  
    print ("         \  /  |        / \ Y   /'   | \     |          |   ~   ")  
    print ("          `'   |  _     |  `._/' |   |  \     7        /        ")  
    print ("         _.-'-' `-'-'|  |`-._/   /    \ _ /    | .    |         ")     
    print ("        __.-'            \  \   .  /  \_.  \    \-|_/\/         ")           
    print ("     --'                  \oo  oo/    |  |                      ")           
    print ("The monsters are busy chasing each other! \nBehind them there is another door. Choose one option: ")
    print ("1. Reach for the door silently")
    print ("2. Kill the monsters before reaching for the door!")

    answer = input (">")
    # score = 0
    # score = int (score)

    if answer == "1":
        diamond_room()    # score += 5       
    elif answer == "2":
        game_over ("\nYou're dead!The monsters caught you and ate you.") # score += 0   
        play_again()      
    else:
        game_over("Sorry try again later!")



#bear room
def bear_room():
    print ("\nThere is a bear here.")
    print ("      (()__(()           ")
    print ("     /       \           ")           
    print ("    ( /    \  \          ")      
    print ("     \ o o    /          ")        
    print ("     (_()_)__/ \         ")                     
    print ("     / _,==.____ \       ")       
    print ("    (   |--|      )      ")        
    print ("    /\_.|__|'-.__/\_        ")       
    print ("   / (        /     \       ")        
    print ("   \  \      (      /       ")        
    print ("    '._____)    /   )       ")         
    print ("   (((____.--(((____/       ")      
    print ("Behind the bear there is another door...")
    print ("The bear is busy eating honey!")
    print ("Choose what would you do: ")
    print ("1. Eat honey with the bear.")
    print ("2. Dodge the bear and run to the door.")

    answer = input(">")

    if answer == "1":
        game_over ("The bear ate you with the honey.")
        play_again()
    elif answer == "2":
        print ("\nYou run fast enough. The bear did not see you!")
        diamond_room()
        print ("Your current score is + str")
    else:
        game_over("Sorry try again later!")



def start():
    #giving it some prompts to start the game
 
    playerName = input ("Enter your name")
    print( "Hello!")
    print( f"{playerName} You are standing in a dark room.") 
    print("There is a door to your left and to your right. Choose one (l or r) ")


  # convert the player's input() to lower_case with .lower()
    answer = input(">").lower()

    if answer == "l": 
        bear_room()
    elif answer == "r":
        monster_room()
    else:
        game_over("Sorry try again later!")     

start ()









    
    

