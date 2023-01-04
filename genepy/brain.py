import random
from abc import ABC, abstractmethod
from typing import Any
import random


class Brain(ABC):
    """

    """

    def __init__(self):
        """
        """
        self._rng = random.Random()

    @abstractmethod
    def mutate(self, mutation_rate: float) -> None:
        """

        :param mutation_rate:
        :return:
        """
        pass

    @abstractmethod
    def copy(self):
        pass

    def __str__(self):
        return f"Brain of type '{self.__class__.__name__}'"
