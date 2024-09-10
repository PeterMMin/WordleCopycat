"""
Represents an item that can be gained or lost by players.

The `Item` class encapsulates the properties and behavior of an item that can be gained or lost by players in a game or application. Each item has a name and a point value associated with it.

The `gain_item` method updates the point counts of the two provided player objects, adding the item's points to the first player's count and subtracting the points from the second player's count. After the points have been transferred, the item's own point value is set to 0.
"""
class Item:
    def __init__ (self, name, points):
        self.name = name
        self.points= points

    def gain_item(self, playerGain, playerLoss):
        playerGain.count += self.points
        playerLoss.count -= self.points
        self.points=0

        
      