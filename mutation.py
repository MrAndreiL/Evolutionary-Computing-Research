import random

from settings import config
from Chromosome import Chromosome


class Mutation:
    @staticmethod
    def reverse_sequence_mutation(self, parent: Chromosome, rate: float) -> None:
        """
            This method implements reverse sequence mutation algorithm
        """
        seq = random.sample(range(1, len(parent.order_city)), k=2)
        seq.sort()
        i, j = seq

        order_city = parent.order_city[:i] + parent.order_city[i:j][::-1] + parent.order_city[j:]
        pick_items = parent.pick_items[:i] + parent.pick_items[i:j][::-1] + parent.pick_items[j:]

        for x in range(len(pick_items)):
            if random.random() > rate:
                pick_items[x] = random.choice([False, True])

        parent.order_city = order_city
        parent.pick_items = pick_items


def mutation(parents: [Chromosome]) -> [Chromosome]:
    """
        Gets a list of parents and mutates the children according to mutation method in .ini file
    """
    parent_a, parent_b = parents
    mutation_rate = float(config.get('run_config', 'mutation_rate'))
    getattr(Mutation, config.get('algorithm_config', 'mutation').lower().strip())(Mutation(), parent_a, mutation_rate)
    getattr(Mutation, config.get('algorithm_config', 'mutation').lower().strip())(Mutation(), parent_b, mutation_rate)

    return parents


def mutate(parent: Chromosome) -> Chromosome:
    """
        Takes a child and mutates it according to mutation method in .ini file
    """
    mutation_rate = float(config.get('run_config', 'mutation_rate'))
    getattr(Mutation, config.get('algorithm_config', 'mutation').lower().strip())(Mutation(), parent, mutation_rate)
    return parent