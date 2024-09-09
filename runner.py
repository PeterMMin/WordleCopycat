from character import Character
from item import Item
from wordle import playWordle

print("Welcome to the game!")

def fight(dragon, character):
    winner = fight_player(dragon, character)  # Ensure fight_player returns a winner
    print("The winner is " + winner)
    if winner == character:
        print("You won the game!")
    else:
        print("You lost the game!")


d1 = input("You are walking and see a dragon. Type Y to talk to it: ")
character = Character(0, [], {"I don't want to fight": "Let's fight!"})

if d1 == "Y":
    dragon = Character(1, [], "You picked the wrong dragon to mess with. I have an immortality token. You better go find some, whoever has more will win the fight.")
    dragon.talk_to_player("You picked the wrong dragon to mess with. I have an immortality token. You better go find some, whoever has more will win the fight.")
    
    d2 = input("Would you like to fight the dragon right now? (Y/N): ")
    
    if d2 == "Y":
        character.talk_to_player("Let's fight!")
        fight(dragon, character)
        
    if d2 == "N":
        print("You run into a wizard.")
        wizard = Character(2, ["token1", "token2"], "If you want one of my tokens, you must play wordle!")
        wizard.talk_to_player("If you want one of my tokens, you must play wordle!")
        
        playWordle()
        
        if win == "Y":
            wizard.talk_to_player("Congrats. Pick up my token!")
            token1 = Item("token1", 1)
            d3 = input("Type Y to pick up the token: ")
            if d3 == "Y":
                gain_item(token1, character, wizard)
                
        d4 = input("Do you want to go fight the dragon now or do you want to meet the wizard again? (D/W): ")
        
        if d4 == "D":
            fight(dragon, character)
            
        if d4 == "W":
            wizard.talk_to_player("If you want one of my tokens, you must play wordle!")
            playWordle()
            if win == "Y":
                wizard.talk_to_player("Congrats. Pick up my token!")
                token2 = Item("token2", 1)
                d5 = input("Type Y to pick up token: ")
                if d5 == "Y":
                    gain_item(token2, character, wizard)
        
        print("It's time to go fight the dragon!")
        fight(dragon, character)
