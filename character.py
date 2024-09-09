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
