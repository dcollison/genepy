import random
import time
import math as m

import matplotlib.pyplot as plt

from genepy.population import Population
from genepy.defaults import Defaults
from genepy.organism import Organism
from genepy.logger import Logger

random.seed(time.time_ns())


class GeneticAlgorithm:
    """

    """

    def __init__(self, organism_type: type[Organism] = None, target=None,
                 population_size: int = Defaults.POPULATION_SIZE,
                 mutation_rate: float = Defaults.MUTATION_RATE,
                 n_generations: int = Defaults.N_GENERATIONS,
                 elitism: int = 4):
        Logger.debug("Creating instance of GeneticAlgorithm...")
        self.target = None
        self.organism_type = None
        self._population = None
        self.organism_type = organism_type
        self.target = target
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.n_generations = n_generations
        self.elitism = elitism
        self.mutation_rate_fcn = \
            lambda x: self.mutation_rate * (1-x/self.n_generations) ** 2

    def main(self) -> None:
        Logger.debug("Running 'main' of GeneticAlgorithm...")
        self.create_population()
        plt.title(f"Generation {self._population.i_generation}")
        self._population.run()
        self._population.calculate_fitnesses()

        for _ in range(self.n_generations - 1):
            self._population.natural_selection()
            self._population.breed()
            self._population.mutate()
            plt.title(f"Generation {self._population.i_generation}")
            self._population.run()
            self._population.calculate_fitnesses()
            self._population.mutation_rate = self.mutation_rate_fcn(self._population.i_generation)

    def get_fittest(self) -> [Organism]:
        Logger.debug("Getting fittest organism from GeneticAlgorithm...")
        return self._population.get_fittest()

    def create_population(self):
        Logger.debug("Creating population...")
        self._population = Population(self.population_size, self.mutation_rate, self.organism_type, self.target,
                                      self.elitism)
        self._population.generate()
