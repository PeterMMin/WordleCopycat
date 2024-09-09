class Character:
    def __init__ (self, count, inventory, dialogue):
        self.count
        self.inventory
        self.dialogue

    def fight_player(x,y):
        if x.count > y.count:
            winner= x 
        if y.count > x.count:
            winner=y
        else:
            winner= "tie"
        return winner

    def pick_up_item(self, item):
        self.inventory.append(item)

    def talk_to_player(self, player_msg):
        for sentence in self.dialgoue:
            if player_msg == sentence:
                print(self.dialgoue[sentence])
