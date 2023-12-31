from Chromosome import Chromosome

class Solution(object):
    """Problem solution model."""
    def __init__(self, chromosome: Chromosome, profit: float, time: float, 
                 single_objective: float, objectives: [float]) -> None:
                 self.chromosome = chromosome
                 self.profit = profit
                 self.time   = time
                 self.single_objective = single_objective
                 self.objectives = objectives

    def get_relation(self, other: 'Solution') -> int:
            """This method returns the relationship between two solutions
            regarding which one is dominant."""
            val = 0

            for objective_self, objective_other in zip(self.objectives, other.objectives):
                    if objective_self < objective_other:
                        if val == -1:
                            return 0
                        val = 1
                    elif objective_self > objective_other:
                        if val == 1:
                              return 0
                        val = -1
            return val

    def equals_in_chromosome(self, other: 'Solution') -> bool:
          return self.chromosome == other.chromosome
                    