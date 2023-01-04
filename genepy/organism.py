from abc import ABC, abstractmethod
from typing import final, Self

from genepy.brain import Brain


class Organism(ABC):
    """

    """
    number: int = 0

    @classmethod
    def get_next_number(cls) -> int:
        cls.number += 1
        return cls.number

    def __init__(self, i_generation: int, target, brain: Brain = None):
        """

        :param target:
        """
        self.fitness = 0.0
        self.brain = brain
        self.done = False
        self.i_generation: int = i_generation
        self._number: int = Organism.get_next_number()
        self.target = target

    @abstractmethod
    def calculate_fitness(self) -> None:
        """
        Calculate the fitness of the organism. This will depend on the problem
        being solved, and it could involve evaluating the chromosome as a solution
        to the problem and measuring how well it performs.
        :return: Fitness of the organism.
        """
        pass

    @abstractmethod
    def breed(self, n_offspring: int = 1, partner: Self = None) -> list[Brain]:
        pass

    @final
    def mutate(self, mutation_rate: float):
        """
        Call the mutate function of the brain.
        """
        self.brain.mutate(mutation_rate)

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def copy(self):
        pass

    def __str__(self):
        info = "\n\t".join([f"Organism {self.i_generation}.{self._number}:",
                            f"Brain: {self.brain}",
                            f"Target: {self.target}",
                            f"Fitness: {self.fitness:.6f}"])

        return info
