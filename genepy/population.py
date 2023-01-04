from matplotlib import pyplot as plt
import random

from genepy.logger import Logger
from genepy.organism import Organism


class Population:
    """

    """

    def __init__(self, size: int, mutation_rate: float, organism_type: type[Organism], target, elitism: int):
        """

        :param size:
        :param mutation_rate:
        :param organism_type:
        :param target:
        """
        self.size: int = size
        self.mutation_rate: float = mutation_rate

        self.i_generation: int = 1

        self.organism_type = organism_type
        self.organisms: list[Organism] = []
        self.parents: list[Organism] = []
        self.offspring: list[Organism] = []
        self.fitnesses: list[float] = []
        self.fittest: float = 0
        self.elitism = elitism

        self.target = target

    def generate(self) -> None:
        """
        Generate a population of organisms, where each organism has a
        chromosome with 'gene_length' genes (each gene can be thought of as a
        binary digit).
        """
        self.organisms: list[Organism] = []
        for i in range(self.size):
            organism = self.organism_type(self.i_generation, self.target)
            self.organisms.append(organism)

    def run(self):
        Logger.debug(
            f"Generation {self.i_generation:0>4}, mutation rate={self.mutation_rate:.6f}, best fitness={self.fittest:.6f}")
        visuals = []
        for organism in self.organisms:
            if organism.elite:
                visuals.append(plt.gca().add_patch(plt.Circle(xy=organism.position, radius=1, color='g')))
            else:
                visuals.append(plt.gca().add_patch(plt.Circle(xy=organism.position, radius=1, color='k')))
        while not all([organism.done for organism in self.organisms]):
            i = 0
            for organism in self.organisms:
                organism.run()
                visuals[i].center = organism.position
                i += 1
            if self.i_generation >= 1:
                plt.pause(0.001)
        for vis in visuals:
            vis.remove()

    def calculate_fitnesses(self) -> None:
        for organism in self.organisms:
            organism.calculate_fitness()
        self.fitnesses = [organism.fitness for organism in self.organisms]
        self.fittest = max(self.fitnesses)

    def get_fittest(self, n: int = 1) -> [Organism]:
        """
        :return: The fittest organism in the population
        """
        if n == 0:
            return []

        sorted_organisms = sorted(self.organisms, key=lambda organism: organism.fitness, reverse=True)
        return [organism.copy() for organism in sorted_organisms[:n]]

    def natural_selection(self):
        """
        Select individuals for reproduction based on their fitness. There are many
        ways to do this, but one simple method is to select the top performing
        individuals with a probability proportional to their fitness.
        :return:
        """
        parents = []
        for _ in range(int(self.size / 2) - int(self.elitism / 2)):
            max_fitness = max(self.fitnesses)
            normalised_fitness = [fitness / max_fitness for fitness in self.fitnesses]
            # Generate a random number between 0 and 1
            r = random.random()

            # Select the first individual whose normalized fitness score is greater than r
            for i, individual in enumerate(self.organisms):
                if r <= normalised_fitness[i]:
                    parents.append(individual)
                    break

        self.parents: list[Organism] = parents

        self.organisms = self.get_fittest(self.elitism)

    def breed(self):
        """
        Combine the genetic material of two parents to produce two offspring.
        This can be done by randomly selecting a crossover point and swapping the
        genetic material of the two parents at that point.
        :return:
        """
        self.i_generation += 1
        Organism.number = 0
        self.offspring = []

        for parent in self.parents:
            child_brains = parent.breed(n_offspring=2)
            for child_brain in child_brains:
                self.offspring.append(self.organism_type(self.i_generation, self.target, brain=child_brain))

    def mutate(self):
        for offspring in self.offspring:
            offspring.mutate(self.mutation_rate)

        self.organisms.extend(self.offspring)
        self.offspring = []
