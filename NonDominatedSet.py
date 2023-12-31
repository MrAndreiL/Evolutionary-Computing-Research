#!/usr/bin/env python
from Solution import Solution

class NonDominatedSet(object):
    """
        This class is used to represent the non dominated solutions
    """
    def __init__(self):
        self.entries = []

    def add(self, solution: Solution) -> bool:
        """
            This method is used to add a solution to non dominated set
        """
        is_added = True

        for entry in self.entries:
            rel = solution.get_relation(entry)

            if rel == -1 or (rel == 0 and solution.equals_in_chromosome(entry)):
                is_added = False
                break
            elif rel == 1:
                self.entries.remove(entry)

        if is_added:
            self.entries.append(solution)

        return is_added

    def adds(self, solutions: [Solution]) -> None:
        """
            This method is used to add a list of solutions to non dominated set
        """
        for solution in solutions:
            self.add(solution)