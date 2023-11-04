from Item import Item

class City(object):
    "Class modelling each city in the problem."
    def __init__(self, idx: int, x: float, y: float) -> None:
        self.idx   = idx
        self.x     = x
        self.y     = y
        self.items = []

    def __eq__(self, obj) -> bool:
        return self.idx == obj.idx

    def __ne__(self, obj) -> bool:
        return self.idx != obj.idx

    def add_item(self, item: Item) -> None:
        self.items.append(item)