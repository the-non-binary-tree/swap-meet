from .item import Item

class Clothing(Item):
    def __init__(self, category = 'Clothing', condition = 0.0, age = 0):
        super().__init__(category, condition, age = 0)

    def __str__(self, description = 'The finest clothing you could wear.'):
        return super().__str__(description)
