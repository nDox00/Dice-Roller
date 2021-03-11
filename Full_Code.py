def ask_to_roll():
    answer = input("Do you wanna roll: Y/N ").title()
    return answer
  
def dice_roll():
    diceroll = random.randint(1,6)
    rolled.append(diceroll)
    print(diceroll)
    print(f'Previous numbers are {rolled}:')
    
def play_game():
    play = input("Ready to Play? Y/N: ").title()
    if play == 'Y':
        gameon = True
    else:
        gameon = False
    return gameon

import random
rolled = []
gameon = play_game()

while gameon:
    answer = ask_to_roll()
    if answer == 'Y':
        print("Rolling..")
        dice_roll()
    else:
        print("\nThank you for playing.")
        break
else:
    print("That's Okay!")

