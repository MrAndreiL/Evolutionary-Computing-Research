#!/usr/bin/env python
import random
import sys
from collections import defaultdict

from settings import config
from Chromosome import Chromosome


class Crossover(object):
    @staticmethod
    def ordered_crossover(self, parent_a: Chromosome, parent_b: Chromosome) -> (Chromosome, Chromosome):
        """
            This method implements the ordered crossover algorithm
        """
        seq = random.sample(range(0, len(parent_a.order_city) - 1), k=2)
        seq.sort()
        i, j = seq

        seq = random.sample(range(0, len(parent_a.pick_items) - 1), k=2)
        seq.sort()
        p, q = seq

        cities_a = parent_a.order_city[1:]
        items_a = parent_a.pick_items
        cities_b = parent_b.order_city[1:]
        items_b = parent_b.pick_items

        b_without_a = [x for x in parent_b.order_city[j:] + parent_b.order_city[1:j] if x not in cities_a[i:j]]
        a_without_b = [x for x in parent_a.order_city[j:] + parent_a.order_city[1:j] if x not in cities_b[i:j]]
        b_i_a = parent_b.pick_items[q:] + parent_b.pick_items[:q]
        a_i_b = parent_a.pick_items[q:] + parent_a.pick_items[:q]

        for x in range(j, len(cities_a) + i - 1):
            cities_a[x % len(cities_a)] = b_without_a[x - j - 1]
            cities_b[x % len(cities_b)] = a_without_b[x - j - 1]

        for x in range(q, len(items_a) + p - 1):
            items_a[x % len(items_a)] = b_i_a[x - q]
            items_b[x % len(items_b)] = a_i_b[x - q]

        cities_b.insert(0, parent_b.order_city[0])
        cities_a.insert(0, parent_a.order_city[0])

        return Chromosome(cities_a, items_a), Chromosome(cities_b, items_b)

def crossover(parents: [Chromosome]) -> (Chromosome, Chromosome):
    """
        This function calls the required crossover method based on .ini file
    """
    parent_a, parent_b = parents

    if random.random() > float(config.get('run_config', 'crossover_rate')):
        return parents

    child_a, child_b = getattr(Crossover, config.get('algorithm_config', 'crossover').lower().strip())(Crossover(),
                                                                                                       parent_a,
                                                                                                       parent_b)
    return [child_a, child_b]