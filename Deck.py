from random import shuffle
color_dict = {True: "Red", False : "Black"}
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.red = (suit == "Hearts" or suit == "Diamonds")
        self.value = value
    def __str__(self):
        if self.value == 1:
            return "{0} ace of {1}".format(color_dict[self.red],self.suit)
        elif self.value <= 10 and self.value >= 2: 
            return "{0} {1} of {2}".format(color_dict[self.red], self.value, self.suit)
        elif self.value == 11:
            return "{0} jack of {1}".format(color_dict[self.red], self.suit)
        elif self.value == 12:
            return "{0} queen of {1}".format(color_dict[self.red], self.suit)
        elif self.value == 13:
            return "{0} king of {1}".format(color_dict[self.red],self.suit)
    def __repr__(self):
        return str(self)
    
class Deck:
    def __init__(self):
        self.deck = [Card(suit,value) for suit in ["Hearts", "Diamonds", "Clubs", "Spades"] for value in range(1,13+1)]
    def draw(self):
        self.deck.reverse()
        card = self.deck.pop()
        self.deck.reverse()
        return card
    def draw_n(self, n):
        return [self.draw() for i in range(n)]
    def shuffle(self):
        shuffle(self.deck)
