import math as m
from genepy.brain import Brain


class BrainImpl(Brain):
    def __init__(self, action_sequence: list[float] = None):
        super().__init__()
        self.gene_length = 1000
        self.i_action = 0
        if action_sequence is None:
            self.action_sequence: list[float] = [self._rng.uniform(0, 2 * m.pi) for _ in
                                                 range(self.gene_length)]
        else:
            self.action_sequence = action_sequence

    def mutate(self, mutation_rate: float) -> None:
        action_list = list(self.action_sequence)
        for i in range(self.gene_length):
            r = self._rng.random()
            if r > (1 - mutation_rate):
                action_list[i] = self._rng.uniform(0, 2 * m.pi)

        self.action_sequence = action_list

    def copy(self):
        return BrainImpl(list(self.action_sequence))

    def next_action(self) -> list[float, float]:
        action = self.action_sequence[self.i_action]
        self.i_action += 1
        return [m.cos(action), m.sin(action)]

    def __str__(self):
        return ",".join([f"Gene Length={self.gene_length}"])
