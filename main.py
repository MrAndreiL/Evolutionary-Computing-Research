#!/usr/bin/env python
import random

from Problem import Problem
from Genetic import Genetic
from Competition import Competition
from settings import config

random_seed = config.get('basic_config', 'random_seed')
problem_folder = config.get('folder_config', 'problem_folder')
output_folder = config.get('folder_config', 'results_folder')
population_size = config.get('run_config', 'population_size')

if __name__ == "__main__":
    """
        This method runs the program
    """
    random.seed(random_seed)

    competition = Competition()#"a280-n279",
    problem_names = ["fnl4461-n22300"]#["fnl4461-n4460", "fnl4461-n22300", "fnl4461-n44600", "pla33810-n33809", "pla33810-n169045", "pla33810-n338090"]
    for instance in competition.instances:
        for problemName in problem_names:
            problem = Problem(problem_folder, problemName)
            algorithm = Genetic(problem)
            non_dominated_solutions = algorithm.solve()
            competition.print_solutions(problem, non_dominated_solutions.entries)
            competition.write_solutions(output_folder, problem, non_dominated_solutions.entries)