class Item(object):
    """Class modelling each item available for pickup."""
    def __init__(self, idx: int, profit: float, weight: float, city: int) -> None:
        self.idx    = idx
        self.profit = profit
        self.weight = weight
        self.city   = city

    def __eq__(self, obj) -> bool:
        return self.idx == obj.idx

    def __ne__(self, obj) -> bool:
        return self.idx != obj.idx