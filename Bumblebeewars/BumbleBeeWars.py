#Imports
import random
import time
#Set till later
difficulty = "Easy"
easy_bee_amt = "10 Bees"
medium_bee_amt = "8 Bees"
hard_bee_amt = "5 Bees"
easy_damage = [
  3,
  5,
  10,
  15,
  20,
  25
]
medium_damage = [
  2,
  4,
  8,
  12,
  16,
  20
]
hard_damage = [
  1,
  3,
  6,
  10,
  14,
  18
]
damage = easy_damage
start_bee = "69 Bees"
#Start
print("Welcome to Bumblebee Wars!")
time.sleep(2)
name = input("What would you like to be called? ")
time.sleep(2)
print(f"Hello {name}! Welcome to Bumblebee Wars!")
time.sleep(2)
print("(1) Basic Beekeeper")
print("(2) Beekeeper Venuckensnucker")
print("(3) Beekeper HimHar")
Starter_Char = int(input("Who would you like to be? "))
if Starter_Char == 1:
  Starter_Char = "Basic Beekeeper"
elif Starter_Char == 2:
  Starter_Char = "Beekeeper Venuckensnucker"
elif Starter_Char == 3:
  Starter_Char = "Beekeeper HimHar"
else:
  print("Invalid Choice! Game crashed!!!")
print(f"Welcome to the world of Bumblebee Wars {name}!")
time.sleep(3)
print(f"You are {Starter_Char}, a beekeeper, tasked with keeping the hive safe.")
time.sleep(3)
print("You need to protect the Honeybee's from the Bumblebee's")
time.sleep(5)
print("Lets start with your first encounter!")
encounters = [
  "Bumblebee!",
  "duo (2) of Bumblebees!",
  "group (4) of Bumblebees!"
]
while True:  # Loop until the player flees or wins
  encounters = [
      "Bumblebee!",
      "duo (2) of Bumblebees!",
      "group (4) of Bumblebees!"
  ]
  encounter = random.choice(encounters)
  print(f"You encounter a {encounter}")
  print("(1) Fight")
  print("(2) Flee")
  encounter_choice = int(input("What would you like to do? "))
  flee = [
      "You successfully fled!",
      "You failed to flee!"
    ]
  fleed = random.choice(flee)
  if encounter_choice == 2:
      if fleed == "You successfully fled!":
          print(fleed)
          break  # Exit the loop if the flee is successful
      else:
          print(fleed)
          print("You're back to the encounter!")  # Indicate the player is back
  elif encounter_choice == 1:
      fight = random.choice(damage)
      print("You chose to fight!")
      print(f"You've done {fight} damage")
      print(f"You've defeated the {encounter}")
      break  # Exit the loop if the fight is successful
  else:
      print("Invalid Choice! Game crashed!!!")
print(f"Good job! You've completed your first encounter {name}!")
time.sleep(2)
print("Now, let's get some things squared away!")
time.sleep(2)
print("(1) Easy")
print("(2) Medium")
print("(3) Hard")
difficulty = int(input("What difficulty would you like to play on? "))
time.sleep(2)
if difficulty == 1:
  difficulty = "Easy"
elif difficulty == 2:
  difficulty = "Medium"
elif difficulty == 3:
  difficulty = "Hard"
else:
  print("Invalid Choice! Game crashed!!!")
if difficulty == "Easy":
  damage = easy_damage
  start_bee = easy_bee_amt
elif difficulty == "Medium":
  damage = medium_damage
  start_bee = medium_bee_amt
elif difficulty == "Hard":
  damage = hard_damage
  start_bee = hard_bee_amt
print(f"You've chosen to play on {difficulty} difficulty!")
time.sleep(2)
print("Now, let's introduce you to the hive!")
time.sleep(2)
print(f"Since you picked {difficulty} difficulty, you start with {start_bee}")
time.sleep(2)
print("Well, that's it for the tutorial!")
time.sleep(2)
print("I'll let you play around now!")
time.sleep(2)
player_health = 100  # Initial player health
honeycombs = 0  # Global currency
current_beekeeper = Starter_Char # Tracks the current beekeeper
experience = 0  # Player's experience points
level = 1  # Player's level
exp_to_next_level = 100  # Experience needed for the next level
while True:
    print("(1) Start Encounter")
    print("(2) Shop")
    print("(3) End game")
    main_menu_choice = int(input("What would you like to do? "))
    if main_menu_choice == 1:
      # Encounter Logic:
      while True:  # Loop until the player flees or wins
          encounters = [
              "Bumblebee!",
              "duo (2) of Bumblebees!",
              "group (4) of Bumblebees!"
          ]
          encounter = random.choice(encounters)
          print(f"You encounter a {encounter}")
          # Bumblebee Health:
          bumblebee_health = random.randint(10, 20) # Adjust the health range as needed
          print(f"The bumblebee has {bumblebee_health} health.")
          while bumblebee_health > 0 and player_health > 0:
            print("(1) Fight")
            print("(2) Flee")
            encounter_choice = int(input("What would you like to do? "))
            flee = [
                "You successfully fled!",
                "You failed to flee!"
            ]
            fleed = random.choice(flee)
            if encounter_choice == 2:
                if fleed == "You successfully fled!":
                    print(fleed)
                    break  # Exit the encounter loop
                else:
                    print(fleed)
                    print("You're back to the encounter!")  # Indicate the player is back
            elif encounter_choice == 1:
                # Player Damage
                fight = random.choice(damage)
                print("You chose to fight!")
                print(f"You've done {fight} damage")
                bumblebee_health -= fight  # Reduce bumblebee health
                print(f"The bumblebee has {bumblebee_health} health left.")
                # Bumblebee Damage:
                bumblebee_damage = random.randint(1, 5)  # Adjust damage range as needed
                print(f"The bumblebee attacks and does {bumblebee_damage} damage!")
                player_health -= bumblebee_damage
                print(f"Your health is now {player_health}")
                if bumblebee_health <= 0:
                    print(f"You've defeated the {encounter}!")
                    # Reward Honeycombs for victory, scaling with difficulty
                    if difficulty == "Easy":
                        honeycombs += random.randint(5, 15)
                    elif difficulty == "Medium":
                        honeycombs += random.randint(10, 25)
                    elif difficulty == "Hard":
                        honeycombs += random.randint(15, 35)
                    print(f"You earned {honeycombs} Honeycombs! You now have {honeycombs}")
                    # Gain experience for victory, scaling with difficulty and encounter type
                    if difficulty == "Easy":
                        if encounter == "Bumblebee!":
                            experience += random.randint(10, 35)
                        elif encounter == "duo (2) of Bumblebees!":
                            experience += random.randint(20, 50)
                        elif encounter == "group (4) of Bumblebees!":
                            experience += random.randint(30, 75)
                    elif difficulty == "Medium":
                        if encounter == "Bumblebee!":
                            experience += random.randint(15, 45)
                        elif encounter == "duo (2) of Bumblebees!":
                            experience += random.randint(30, 65)
                        elif encounter == "group (4) of Bumblebees!":
                            experience += random.randint(45, 100)
                    elif difficulty == "Hard":
                        if encounter == "Bumblebee!":
                            experience += random.randint(20, 60)
                        elif encounter == "duo (2) of Bumblebees!":
                            experience += random.randint(40, 85)
                        elif encounter == "group (4) of Bumblebees!":
                            experience += random.randint(60, 125)
                    print(f"You gained {experience} experience points! You now have {experience} experience.")
                    if experience >= exp_to_next_level:
                        level += 1
                        experience -= exp_to_next_level
                        exp_to_next_level *= 1.5  # Increase exp needed for next level
                        print(f"You leveled up to level {level}!")
                        print(f"You need {exp_to_next_level} experience to reach the next level.")
                    break  # Exit the encounter loop
                elif player_health <= 0:
                    print("You have been defeated!")
                    break  # Exit the encounter loop
            else:
                print("Invalid Choice! Game crashed!!!")
          # Check player health after the encounter
          if player_health <= 0:
            print("You've lost the game! Game Over.")
            break
          if bumblebee_health <= 0:
            print(f"You've defeated the {encounter}!")
            break  # Exit the encounter loop
      # Check player health after the encounter
      if player_health <= 0:
        print("You've lost the game! Game Over.")
        break
      print(f"Good job! Keeping the hive safe {name}!")
    elif main_menu_choice == 2:
        # Shop Logic:
        print("Welcome to the shop! You have", honeycombs, "Honeycombs.")
        print("(1) Buy a Healing Potion (10 Honeycombs)")
        print("(2) Buy a Beekeeper Rufus (20 Honeycombs)")
        print("(3) Leave Shop")
        shop_choice = int(input("What would you like to buy? "))
        if shop_choice == 1:
            if honeycombs >= 10:
                honeycombs -= 10
                print("You bought a Healing Potion!")
                player_health = 100 # Apply Healing Potion effect
            else:
                print("You don't have enough Honeycombs!")
        elif shop_choice == 2:
            if honeycombs >= 20:
                honeycombs -= 20
                print("You bought Beekeeper Rufus!")
                current_beekeeper = "Beekeeper Rufus" # Apply Beekeeper Rufus effect
            else:
                print("You don't have enough Honeycombs!")
        elif shop_choice == 3:
            print("Leaving the shop...")
        else:
            print("Invalid Choice! Game crashed!!!")
    elif main_menu_choice == 3:
        print("Thank you for playing!")
        break  # Exit the game
    else:
        print("Invalid Choice! Please try again.")