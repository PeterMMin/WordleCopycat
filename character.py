"""
    Represents a character in the game, with a count, inventory, and dialogue.
    
    The `Character` class provides methods to interact with the character, such as picking up items and talking to the player.
    
    Attributes:
        count (int): The count or number of the character.
        inventory (list): The items the character has in their inventory.
        dialogue (dict): The dialogue the character can say, keyed by a trigger string.
    
    Methods:
        pick_up_item(item: Any) -> None:
            Adds the given item to the character's inventory.
        talk_to_player(trigger: str) -> None:
            Prints the dialogue associated with the given trigger string, if it exists in the character's dialogue.
    """
class Character:
    def __init__ (self, count, inventory, dialogue):
        self.count = count
        self.inventory = inventory
        self.dialogue = dialogue

   
    def pick_up_item(self, item):
        self.inventory.append(item)

    def talk_to_player(self, trigger):
        for sentence in self.dialogue:
            if trigger == sentence:
                print(self.dialogue[sentence])
