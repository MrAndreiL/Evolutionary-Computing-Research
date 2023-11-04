import copy

from City import City

class Chromosome(object):
    """Chormosome modelling in a solution."""
    def __init__(self, order_city: [City], pick_items: [bool]) -> None:
        self.order_city = order_city
        self.pick_items = pick_items

    def __eq__(self, obj) -> bool:
        return self.order_city == obj.order_city and self.pick_items == obj.pick_items

    def __ne__(self, obj) -> bool:
        return self.order_city != obj.order_city or self.pick_items != obj.pick_items

    def copy(self):
        return Chromosome(copy.deepcopy(self.order_city), self.pick_items.copy())