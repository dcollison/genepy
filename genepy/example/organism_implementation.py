import math as m
from typing import Self

from genepy.brain import Brain
from genepy.organism import Organism

from brain_implementation import BrainImpl


class OrganismImpl(Organism):

    def __init__(self, i_generation: int, target, brain: Brain = None):
        super().__init__(i_generation, target, brain)

        if self.brain is None:
            self.brain = BrainImpl()
        self.steps = 0
        self.dead = False
        self.elite = False
        self.target_reached = False
        self.velocity = [0, 0]
        self.position = [0, -90]

    def calculate_fitness(self) -> None:
        distance_to_target = m.dist(self.position, self.target.position)
        if self.target_reached:
            fitness = (1 / 16) + 10000 / (self.steps ** 2)
        else:
            fitness = 1 / (distance_to_target ** 2)

        self.fitness = max(self.fitness, fitness)

    def run(self):
        if self.done:
            return

        action = self.brain.next_action()
        self.velocity = [self.velocity[0] + action[0], self.velocity[1] + action[1]]
        self.velocity[0] = min(self.velocity[0], 3)
        self.velocity[1] = min(self.velocity[1], 3)
        self.position = [self.position[0] + self.velocity[0], self.position[1] + self.velocity[1]]
        self.check_done()
        self.steps += 1
        self.calculate_fitness()

    def check_done(self):
        x = self.position[0]
        y = self.position[1]
        if x >= 100 or \
                x <= -100 or \
                y >= 100 or \
                y <= -100:
            self.done = True
            self.dead = True

        # temp obstacle
        # if -20 <= x <= 20 and 30 <= y <= 35:
        #     self.done = True
        #     self.dead = True

        if -100 <= x <= 50 and -40 <= y <= -35:
            self.done = True
            self.dead = True

        if -20 <= x <= 100 and 20 <= y <= 25:
            self.done = True
            self.dead = True

        if -20 <= x <= -15 and -5 <= y <= 25:
            self.done = True
            self.dead = True

        if -100 <= x <= -50 and 10 <= y <= 15:
            self.done = True
            self.dead = True

        if -100 <= x <= 25 and 60 <= y <= 65:
            self.done = True
            self.dead = True

        if self.brain.i_action >= self.brain.gene_length:
            self.done = True

        if m.dist(self.position, self.target.position) <= 3:
            self.target_reached = True
            self.done = True

    def __str__(self):
        info = super().__str__()
        return info

    def copy(self):
        organism_copy = OrganismImpl(i_generation=self.i_generation, target=self.target, brain=self.brain.copy())
        organism_copy.number = self.number
        organism_copy.fitness = self.fitness
        organism_copy.elite = True
        return organism_copy

    def breed(self, n_offspring: int = 1, partner: Self = None) -> list[Brain]:
        child_brains: list[Brain] = []
        if partner is None:
            for i in range(n_offspring):
                child_brains.append(self.brain.copy())

        else:
            raise NotImplementedError("")

        return child_brains
