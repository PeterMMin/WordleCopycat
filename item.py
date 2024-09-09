class Item:
    def __init__ (self, name, points):
        self.name = name
        self.points= points

    def gain_item(self, playerGain, playerLoss):
        playerGain.count += self.points
        playerLoss.count -= self.points
        self.points=0

        
      