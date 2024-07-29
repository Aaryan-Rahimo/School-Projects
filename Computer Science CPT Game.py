import random #Random Numbers
import time #Timing, this is seen throughout my code as the time.sleep()

#enemy names
enemy_names = ["Bytefang", "Codezilla", "Syntaxterror", "Hexsplicer", "Debugmoth", "Cybershade", "Malwareon", "Bytebasher", "Crashrider", "Logicbane", "Devouron", "Codelord", "Viruspawn", "Bytebreaker", "Glitchfiend"]
enemy_names2 = ["Syntax Brute", "Binary Reaper", "Error Master", "Cryptic Deviant", "Malware Tyrant", "Rogue Debugger", "Fatal Glitch", "Codebreaker Demon", "Dark Compiler", "Shadow Cipher"]

"""
This is where the begining of the adventure starts
The user is asked for their name and where they would like to go
"""
def playerQuest():
    time.sleep(1)
    #assign user name
    global user_name
    user_name = input("What is your name traveller?: ")

    time.sleep(2)
    print(f"{user_name}, up for the challenge I see. The chief has tasked you with finding a mystical treasure either within the Dunes of Data(1) or the Byte Forest(2).")
    time.sleep(2)
    #assign player path
    global path
    path = input("\nWhich one would you like to venture? (1 or 2): ")

    #check if the answer is invalid
    while path != '1' and path != '2':
        #when invalid, ask again
        path = input("\nInvalid choice. Please enter 1 or 2: ")

    #If the player chooses path 1, they will be meeted with this dialogue
    if path == '1':
        time.sleep(0.5)
        print("Very well then! Safe travels to the Dunes of Data. You may encounter some enemies!")
        time.sleep(0.5)
        print("A companion, Bit-Bot, will be with you and guide you (essentially the narrator)")
        time.sleep(2)
        commence = input("\n<<<< Press Enter To Continue >>>>")
    #If the player chooses path 2, they will be meeted with this dialogue
    elif path == '2':
        time.sleep(0.5)
        print("\nBe careful, traveler. Don't get caught in the vines of bytes!")
        time.sleep(0.5)
        print("A companion, Bit-Bot, will be with you and guide you (essentially the narrator)")
        time.sleep(2)
        commence = input("\n<<<< Press Enter To Continue >>>>")
    
    #Calls the explore function
    explore(path)

"""
This makes dialogue dependant on which path the user chose
If the user chooses either one, there will be 3 different random dialogues that could print
"""
def explore(location):
    if location == '1':  # Dunes of Data
        prompt = random.randint(1, 3)
        
        if prompt == 1:
            time.sleep(.5)
            print("\nAs you venture into the Dunes of Data, you find yourself surrounded by vast stretches of golden sand.")
            time.sleep(2)
            print("The dunes rise and fall like waves frozen in time, creating an awe-inspiring landscape.")
            time.sleep(2)
            commence = input("\n<<<< Press Enter To Continue >>>>")

        elif prompt == 2:
            time.sleep(.5)
            print("\nYou trudge through the endless expanse of the Dunes of Data, the scorching sun beating down upon you.")
            time.sleep(2)
            print("The hot sand beneath your feet shifts with every step, making each movement a challenge.")
            time.sleep(2)
            commence = input("\n<<<< Press Enter To Continue >>>>")
       
        elif prompt == 3:
            time.sleep(.5)
            print("\nThe wind howls through the Dunes of Data, carrying with it a symphony of sand grains in motion.")
            time.sleep(2)
            print("The ever-changing patterns in the sand dunes create a mesmerizing sight that captivates your senses.")
            time.sleep(2)
            commence = input("\n<<<< Press Enter To Continue >>>>")

    elif location == '2':  # Byte Forest
        prompt = random.randint(1, 3)

        if prompt == 1:
            time.sleep(0.5)
            print("\nYou step into the Byte Forest, and immediately, a sense of tranquility washes over you.")
            time.sleep(2)
            print("The forest is dense with towering trees, their branches intertwined like lines of code.")
            time.sleep(2)
            commence = input("\n<<<< Press Enter To Continue >>>>")
        elif prompt == 2:
            time.sleep(0.5)
            print("\nAs you enter the Byte Forest, beams of sunlight filter through the thick foliage above.")
            time.sleep(2)
            print("The forest floor is carpeted with fallen leaves, creating a soft and muted pathway.")
            time.sleep(2)
            commence = input("\n<<<< Press Enter To Continue >>>>")
        elif prompt == 3:
            time.sleep(0.5)
            print("\nThe Byte Forest welcomes you with a symphony of chirping birds and rustling leaves.")
            time.sleep(2)
            print("The air is crisp, and the scent of pine lingers, creating a serene and calming ambiance.")
            time.sleep(2)
            commence = input("\n<<<< Press Enter To Continue >>>>")

#Checks if the players choice was valid or not, if not it'll ask them again

def handlePlayerChoice(choice):
    #Loop
    while True:
        #checks if it is yes
        if "y" in choice.lower():
            print("")
            #if yes, run this function
            playerQuest()
            break
        #checks if it is no
        elif "n" in choice.lower():
            #salute user
            print(f"May we meet again, {user_name}.")
            break
        #if anything else, ask again
        else:
            choice = input("Please choose y or n: ")

"""
This function creates moves and returns a damage which is applied to the enemy health
Remaining : The avaible moves the user has
Choice : What move the user chooses
"""
def userAttackOptions(remaining, choice):
    #Make moves list
    moves = [
        f"\n1. Sword Slash [20-40 DMG], {remaining[0]} uses",
        f"2. Shield Bash [10-30 DMG], {remaining[1]} uses",
        f"3. Mana Punch [5-35 DMG], {remaining[2]} uses",
        f"4. Ice Lance [10-20 DMG], {remaining[3]} uses",
    ]
    #Prints moves on seperate lines
    for move in moves:
        time.sleep(0.5)
        print(move)

    time.sleep(1)
    #Checks if choice is 0, since 0 isn't an option, ask the user to input something
    if choice <= 0:
        time.sleep(1)
        choice = int(input("\nWhat move would you like to use: "))

#If choice corresponds with its value, create the attack damage (applies to all of these if statemnets)
    if choice == 1:
        #Check if there are moves left
        if remaining[0] > 0:
            #Generate values
            damage = random.randrange(20, 41, 5)
            #remove 1 move from the remaining moves
            remaining[0] -= 1
            time.sleep(1)
            #print the players move
            print(f"\n{user_name} uses Sword Slash and deals " + str(damage) + " DMG!")
            return damage
        else:
            print("\nYou have no remaining uses of Sword Slash!")
            return userAttackOptions(remaining, chooseDifferentMove(remaining))
    elif choice == 2:
        #Check if there are moves left
        if remaining[1] > 0:
            #Generate values
            damage = random.randrange(10, 31, 5)
            #remove 1 move from the remaining moves
            remaining[1] -= 1
            time.sleep(1)
            #print the players move
            print(f"\n{user_name} uses Shield Bash and deals " + str(damage) + " DMG!")
            return damage
        else:
            print("\nYou have no remaining uses of Shield Bash!")
            return userAttackOptions(remaining, chooseDifferentMove(remaining))
    elif choice == 3:
        #Check if there are moves left
        if remaining[2] > 0:
            #Generate values
            damage = random.randrange(5, 36, 5)
            #remove 1 move from the remaining moves
            remaining[2] -= 1
            time.sleep(1)
            #print the players move
            print(f"\n{user_name} uses Mana Punch and deals " + str(damage) + " DMG!")
            return damage
        else:
            print("\nYou have no remaining uses of Mana Punch!")
            return userAttackOptions(remaining, chooseDifferentMove(remaining))
    elif choice == 4:
        #Check if there are moves left
        if remaining[3] > 0:
            #Generate Values
            damage = random.randrange(10, 21, 10)
            #remove 1 move from the remaining moves
            remaining[3] -= 1
            time.sleep(1)
            #print the players move
            print(f"\n{user_name} uses Ice Lance and deals " + str(damage) + " DMG!")
            return damage
        else:
            print("\nYou have no remaining uses of Ice Lance!")
            return userAttackOptions(remaining, chooseDifferentMove(remaining))
    else:
        return userAttackOptions(remaining, chooseDifferentMove(remaining))


def chooseDifferentMove(remaining):
    # Create a list of valid choices based on remaining move uses
    valid_choices = [str(i+1) for i in range(len(remaining)) if remaining[i] > 0]

    while True:
        # Prompt the user to choose an attack
        choice = input("\nChoose your attack!: ")

        # Check if the chosen attack is a valid choice
        if choice in valid_choices:
            return int(choice)  # Convert the choice to an integer and return it
        else:
            print("Invalid choice. Please choose a different move.")

def enemyAttack(maxDamage1, maxDamage2, lowDamage1, lowDamage2, rate):
    # Generate random damage for the two attack options
    enemy_attack1 = random.randrange(lowDamage1, maxDamage1, rate)
    enemy_attack2 = random.randrange(lowDamage2, maxDamage2, rate)

    # Generate a random number to determine which attack the enemy will use
    random_attack = random.randint(0, 100)

    # Check the random number and determine the enemy's attack
    if random_attack > 20:
        return enemy_attack1  # Return the damage for attack 1
    elif random_attack <= 20:
        return enemy_attack2  # Return the damage for attack 2


def fightSequence(enemyHealthLow, enemyHealthHigh, health, enemyNameChoice):
    # Print the name of the encountered enemy
    time.sleep(1)
    print(f"\nYou encountered a wild {random.choice(enemyNameChoice)}!")

    # List to track remaining uses of player's moves
    moves_remaining = [2, 5, 5, 7]

    # Set the player's health to the provided value
    global user_health
    user_health = health

    # Generate random enemy health within the given range
    enemy_health = random.randrange(enemyHealthLow, enemyHealthHigh, 10)

    while True:
        time.sleep(2)
        # Print the current player health
        print(f"Player Health: {user_health} HP")
        
        # Print the current enemy health
        print(f"Enemy Health: {enemy_health} HP")

        # Player's turn
        # Call the userAttackOptions function to get the player's chosen move and its damage
        user_damage = userAttackOptions(moves_remaining, 0)
        
        # Call the enemyAttack function to get the enemy's attack damage
        enemy_damage = enemyAttack(16, 36, 5, 10, 5)

        # Decrease enemy's health by the player's damage
        enemy_health -= user_damage
        time.sleep(.5)
        # Print the enemy's attack damage
        print(f"The enemy attacks! It dealt {enemy_damage} DMG!")

        # Decrease player's health by the enemy's damage
        user_health -= enemy_damage

        if user_health <= 0:
            time.sleep(2)
            # Print a message if the player's health reaches 0 or below
            print("\nOh no! The enemy has defeated you!")
            break

        if enemy_health <= 0:
            time.sleep(2)
            # Print a message if the enemy's health reaches 0 or below
            print("\nCongratulations, you defeated the enemy!")
            break

"""
Contains riddles which are used later
Instace: Check the scenario
"""
def puzzle(instance):
    #The follwoing code will run if the isntance is 1
    if instance == 1: 
        time.sleep(2)

        print("\nAfter defeating the enemy, you decide to explore further.")
        time.sleep(2)
        print("You venture deeper into the land and find a dungeon, cautiously moving forward.")
        time.sleep(2)
        print("As you continue your exploration, you come across a mysterious door.")
        time.sleep(2)
        print("The door has a password?....")
        time.sleep(3)
        print("\nWait... It's a puzzle!")
        time.sleep(3)
        print("It reads: ")
        time.sleep(2)

        print("\nBorn from rain and sunlights glow")
        time.sleep(2)
        print("I come from one, that you should know")
        time.sleep(2)
        print("After gloomy day's, I come out to play")
        time.sleep(2)
        print("To your eyes, I bring wonder and joy")
        time.sleep(2)
        
        user_guess = input("\nWhat am I?: ")
        # Continue asking for user's guess until it matches "rainbow"
        #Check if rainbow
        if user_guess.lower() == "rainbow":
            time.sleep(2)
            print("\nWoohoo!, you guessed the correct answer!")
            time.sleep(2)
            print("You are restored to full health, as well as + you are now at 150 health and a new secret move is unlocked!")
                 
        while user_guess.lower() != "rainbow":
           
             # Check if the user's guess contains "rain" or "light"
            if user_guess.lower() in "rain" or user_guess.lower() in "light":
                print("On the right track!")
            time.sleep(1)               
            # Prompt the user to try again
            user_guess = input("Incorrect, try again : ")
            # If the user's guess is now "rainbow", print a success message and break the loop
            if user_guess.lower() == "rainbow":
                time.sleep(2)
                print("\nWoohoo!, you guessed the correct answer!")
                time.sleep(2)
                print("You are restored to full health, as well as + you are now at 150 health and a new secret move is unlocked!")
                break

            else:
                continue
    #If it is the second instance, this will run
    elif instance == 2:

        time.sleep(2)
        print("\nThat was a close one but you've made it out alive!")
        time.sleep(2)
        print("\nHold on ...")
        time.sleep(3)
        print("...")
        time.sleep(3)
        print("...")
        time.sleep(2)
        print("\nThe, the floor!")
        time.sleep(1)
        print(f"\nHOLD ON {user_name.upper()}!!!!")
        time.sleep(3)
        print("< You fall into a mysterious room >")
        time.sleep(2)
        print("It appears to be another riddle!")
        time.sleep(2)
        print("\nLets see what it says!")
        time.sleep(2)

        print("It reads: ")
        time.sleep(1)
        print("")
        time.sleep(2)
        print("In the land of myths, I soar the skies")
        time.sleep(2)
        print("With fiery breath and piercing eyes")
        time.sleep(2)
        print("\nMajestic and feared, both near and far,")
        time.sleep(2)
        print("A riddle to challenge, an answer bizarre.")
        time.sleep(2)
        print("\nWith wings unfurled, it soars in the sky,")
        time.sleep(2)
        user_guess = input("\nWhat am I, this mystical being, oh my? ")
        # Continue asking for user's guess until it matches "dragon"
        while user_guess.lower() != "dragon":
            #First check if the user guess is right
            if user_guess.lower() == "dragon":
                time.sleep(2)
                print("\nYAY! You guessed solved the riddle!")
                time.sleep(2)
                print("You are restored to full health, which is now 350 and you have gained 2 new moves which will be revealed later.")
                break
            # Check if the user's guess contains "scales" or "mythical creature"
            if user_guess.lower() in "scales" or user_guess.lower() in "mythical creature":
                print("On the right track!")
            time.sleep(2)
            # Prompt the user to try again
            user_guess = input("Incorrect, try again : ")
            # If the user's guess is now "Dragon", print a success message and break the loop
            if user_guess.lower() == "dragon":
                time.sleep(2)
                print("\nYAY! You guessed solved the riddle!")
                time.sleep(2)
                print("You are restored to full health, which is now 350 and you have gained 2 new moves which will be revealed later.")
                break
"""
Similar to the explore() function, this makes dialogue for the upcoming battle
Each prompt will run the next fight instance
"""
def adventureSequence():
    print("\nYou finally enter the dark and mysterious dungeon...")
    time.sleep(2)
    #create random prompt value
    prompt = random.randint(1, 3)

    if prompt == 1: #Checks if 1, then this will run, same for the other 2
        print("\nYou explore deeper into the dungeon and suddenly encounter a wild enemy!")
        time.sleep(2)
        print("The enemy stares at you with menacing eyes, ready to attack!")
        time.sleep(2)
        print("Prepare yourself for battle, this enemy is stronger than before!")
        time.sleep(2)
        #Initiate fight
        fightSequence(120, 171, 150, enemy_names2)


    elif prompt == 2:
        print("As you cautiously navigate through the dungeon, you stumble upon an enemy!")
        time.sleep(2)
        print("The enemy notices your presence and prepares to strike!")
        time.sleep(2)
        print("Get ready to defend yourself!")
        time.sleep(2)
        print("Brace yourself for a fierce encounter this enemy is stronger than before!")
        time.sleep(2)
        #Initiate fight
        fightSequence(130, 171, 150, enemy_names2)

    elif prompt == 3:
        print("While exploring the depths of the dungeon, you encounter an enemy lurking in the shadows!")
        time.sleep(2)
        print("The enemy senses your presence and swiftly moves to attack!")
        time.sleep(2)
        print("Prepare to engage in a fierce battle, this enemy is stronger than before!")
        time.sleep(2)
        #Initiate fight
        fightSequence(120, 171, 150, enemy_names2)

"""
Dialogue for the boss fight
The user can choose to attempt an escape or straight fight the dragon
In either case, the user ends up fighting the dragon
"""
def bossFightDialogue():
    time.sleep(2)
    print("\nAfter solving the riddle, all seems good, but . . .")
    time.sleep(2)
    print("You start connecting the dots")
    time.sleep(2)
    print("As the door opens, your brain knows whats behid the door before it fully opens")
    time.sleep(2)
    print("Before the door opens, you whisper to yourself"+' "Please dont be a dragon" ')
    time.sleep(2)
    print("Though your realize it is your impendinng doom as you see the protector of the tressure, the legendary dragon Codeflame ")
    time.sleep(2)
    print("You are faced with fighting the dragon but think you can flee")
    #Makes a loop to ensure the user chooses a valid answer, if they do the loop will stop
    while True:
        #user choice is defined 
        fightOrFlee = int(input("\nWill you fight(1) or flee(2):? "))

        if fightOrFlee == 1:
            #Call fight sequence to start fight
            bossFightSequence()
            break
        #player attempts to flee
        elif fightOrFlee == 2:
            time.sleep(2)
            print("Uh... I think I'm going to go with... fleeing. Yeah, definitely fleeing.")
            time.sleep(2)
            print("As you start to run away, the dragon starts to wake up from his slumber:")
            time.sleep(2)
            print("Dragon : ROARRRRR")
            time.sleep(2)
            print("Oh no! Looks like I'm fighting then. Let's do this!")
            time.sleep(2)
            #Call fight sequence to start fight
            bossFightSequence()
            break

        else:
            #When an invalid answer that is not 1 or 2 is entered, this will print
            print("Invalid input! Please enter 1 to fight or 2 to flee.")
"""
Exact same as the other function, except there are 2 more moves
"""
def bossFightAttackOptions(remaining, choice):
    moves = [
        f"\n1. Sword Slash [20-40 DMG], {remaining[0]} uses",
        f"2. Shield Bash [10-30 DMG], {remaining[1]} uses",
        f"3. Mana Punch [5-35 DMG], {remaining[2]} uses",
        f"4. Ice Lance [10-20 DMG], {remaining[3]} uses",
        f"5. Thunder Clap [100-150 DMG], {remaining[4]} uses",
        f"6. Almighty Bane [75-300 DMG], {remaining[5]} uses",
    ]

    for move in moves:
        time.sleep(0.5)
        print(move)
    time.sleep(1)
    if choice <= 0:
        time.sleep(1)
        choice = int(input("\nWhat move would you like to use: "))

    if choice == 1:
        if remaining[0] > 0:
            damage = random.randrange(20, 41, 5)
            remaining[0] -= 1
            time.sleep(1)
            print(f"\n{user_name} uses Sword Slash and deals " + str(damage) + " DMG!")
            return damage
        else:
            print("\nYou have no remaining uses of Sword Slash!")
            return userAttackOptions(remaining, chooseDifferentMove(remaining))
    elif choice == 2:
        if remaining[1] > 0:
            damage = random.randrange(10, 31, 5)
            remaining[1] -= 1
            time.sleep(1)
            print(f"\n{user_name} uses Shield Bash and deals " + str(damage) + " DMG!")
            return damage
        else:
            print("\nYou have no remaining uses of Shield Bash!")
            return userAttackOptions(remaining, chooseDifferentMove(remaining))
    elif choice == 3:
        if remaining[2] > 0:
            damage = random.randrange(5, 36, 5)
            remaining[2] -= 1
            time.sleep(1)
            print(f"\n{user_name} uses Mana Punch and deals " + str(damage) + " DMG!")
            return damage
        else:
            print("\nYou have no remaining uses of Mana Punch!")
            return userAttackOptions(remaining, chooseDifferentMove(remaining))
    elif choice == 4:
        if remaining[3] > 0:
            damage = random.randrange(10, 21, 10)
            remaining[3] -= 1
            time.sleep(1)
            print(f"\n{user_name} uses Ice Lance and deals " + str(damage) + " DMG!")
            return damage
        else:
            print("\nYou have no remaining uses of Ice Lance!")
            return userAttackOptions(remaining, chooseDifferentMove(remaining))
    elif choice == 5:
        if remaining[4] > 0:
            damage = random.randrange(100, 151, 10)
            remaining[4] -= 1
            time.sleep(1)
            print(f"\n{user_name} uses Thunder Clap and deals " + str(damage) + " DMG!")
            return damage
        else:
            print("\nYou have no remaining uses of Thunder Clap!")
            return userAttackOptions(remaining, chooseDifferentMove(remaining))
    elif choice == 6:
        if remaining[5] > 0:
            damage = random.randrange(100, 301, 20)
            remaining[5] -= 1
            time.sleep(1)
            print(f"\n{user_name} uses Almighty Bane and deals " + str(damage) + " DMG!")
            return damage
        else:
            print("\nYou have no remaining uses of Almighty Bane!")
            return userAttackOptions(remaining, chooseDifferentMove(remaining))
    else:
        return userAttackOptions(remaining, chooseDifferentMove(remaining))
"""
Similar to fight sequence, but this has set peremeters
"""
def bossFightSequence():
    time.sleep(1)
    print("You must fight the legendary dragon Codeflame!")
    moves_remaining = [4, 7, 7, 9, 2, 3]
    global user_health
    user_health = 250
    enemy_health = 800

    while True:
        time.sleep(2)
        print(f"Player Health: {user_health} HP")
        print(f"Dragon Health: {enemy_health} HP")

        # Player's turn to attack
        user_damage = bossFightAttackOptions(moves_remaining, 0)
        enemy_damage = enemyAttack(36, 46, 10, 20, 5)

        # Update enemy's health based on player's damage
        enemy_health -= user_damage
        time.sleep(.5)
        
        # Randomly select a prompt to describe the dragon's attack
        random_prompt = random.randint(0, 2)
        if random_prompt == 0:
            print(f"Codeflame attacks! It dealt {enemy_damage} DMG!")
        elif random_prompt == 1:
            print(f"The Codeflame dealt a devastating blow.\nYou lost {enemy_damage} HP!")
        elif random_prompt == 2:
            print(f"Watch out! Codeflame attacked you for {enemy_damage} DMG!")

        # Update player's health based on dragon's damage
        user_health -= enemy_damage

        # Check if the player's health is depleted
        if user_health <= 0:
            time.sleep(2)
            print("\nOh no! The Codeflame has defeated you!")
            break

        # Check if the dragon's health is depleted
        if enemy_health <= 0:
            time.sleep(2)
            print("\nCongratulations, you defeated the legendary dragon Codeflame!")
            break

def resetGame():
    """
    Resets the game after the player's health reaches 0.
    Asks the player if they want to play again, and either starts a new game or exits based on their response.
    """
    print("Your health reached 0. Game over!")
    user_play = input("Do you want to play again? (y/n): ")
    if user_play.lower() == "y":
        mainGameLoop()  # Starts a new game by calling the main game loop
    else:
        print("")  # Empty print statement for spacing or additional functionality



def mainGameLoop():
    """
    Executes the main game loop.
    Prompts the player to start the game and continues until the player decides to stop.
    Handles player choices, fights, puzzles, adventure sequences, boss fights, and game completion.
    """
    user_play = input("Welcome traveller to the village of Bitsville! We have a mission for you. Are you up for the challenge? (y/n): ")
    
    while "y" in user_play.lower():
        handlePlayerChoice(user_play)  # Handles the player's choice and performs corresponding actions
        
        fightSequence(100, 151, 100, enemy_names)  # Initiates a fight sequence with specified enemy health and names
        if user_health > 0:  # Check if the player is still alive
            puzzleOption = 1
            puzzle(puzzleOption)  # Calls the puzzle function with the specified option
        
        if user_health > 0:  # Check if the player is still alive
            adventureSequence()  # Initiates an adventure sequence
            puzzleOption = 2
            puzzle(puzzleOption)  # Calls the puzzle function with the specified option
        
        if user_health > 0:  # Check if the player is still alive
            bossFightDialogue()  # Initiates a boss fight dialogue
        
        if user_health > 0:  # Check if the player is still alive
            time.sleep(1)
            print(f"Congratulations {user_name}, what a wonderful journey we had!")
            time.sleep(1)
            print("You truly are an amazing warrior!")
        
        if user_health <= 0:  # Check if the player has died
            resetGame()  # Resets the game
        
        resetGame()  # Resets the game after completion or player's death
        break
    
    print("Thank you for playing!")

#Start the
mainGameLoop()
