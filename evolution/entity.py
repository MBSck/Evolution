from typing import Optional, Any, Self, Tuple
from random import random as rnd
from random import choice
from dataclasses import dataclass


@dataclass
class Gene:
    """Contains the description of a gene."""
    name: str
    value: int
    description: str


class Entity:
    """An entity in the game.

    Parameters
    ----------
    position : Tuple[int, int]
        The position of the entity.
    energy : int
        The amount of energy the entity has.
    max_age : int
        The maximum age of the entity.
    max_energy : int
        The maximum amount of energy the entity has.
    speed : int
        The speed of the entity.
    color : str
        The color of the entity.
    birth_rate : int
        The birth rate of the entity.
    birth_count : float
        The birth count of the entity.
    size : int
        The size of the entity.
    mutation_rate : float
        The mutation rate of the entity.

    Attributes
    ----------
    age : int
        The age of the entity.
    alive : bool
        Whether the entity is alive.
    position : Tuple[int, int]
        The position of the entity.
    energy : int
        The amount of energy the entity has.
    genes : dict of Gene
    speed : float

    Methods
    -------
    update()
    mutate()
    eat()
    death()
    kill()
    create_children_asexually()
    create_children_sexually()
    """

    def __init__(self: Self,
                 position: Tuple[int, int],
                 energy: int,
                 max_age: int,
                 max_energy: int,
                 speed: int,
                 color: str,
                 birth_rate: int,
                 birth_count: float,
                 size: int,
                 mutation_rate: float) -> None:
        """Initializes the entity."""
        self.age = 0
        self.alive = True  # duh
        self.max_energy = max_energy
        self.position = position
        self.energy = energy
        self.size = size
        self._speed = speed
        # NOTE: Genes defines variables changable through mutation & passed
        # on to children
        self._genes = {
            "max_age": Gene("Max Age", max_age, "Max age of the entity"),
            "max_energy": Gene("Max Energy", max_energy, "expected max energy of the entity"),
            "color": Gene("Color", color, "Color of the entity"),
            "speed": Gene("Speed", speed, "Speed of the entity"),
            "birth_rate": Gene("Birth Rate", birth_rate, "frequency of birth-events"),
            "birth_count": Gene("Birth Count", birth_count, "expected number of offspring per birth-event"),
            "size": Gene("Size", size, "Size of the entity"),
            "mutation_rate": Gene("Mutation Rate", mutation_rate, "Frequency of mutations occuring")
        }

    @property
    def genes(self):
        """Returns Genes (e.g., to create children)."""
        # NOTE: Return any of: self.max_age, self.max_energy, self.color,
        # self.speed, self.birth_rate, self.size, ...
        return self._genes

    @property
    def speed(self):
        """Gets the speed of the entity."""
        return self._speed

    @speed.setter
    def speed(self, value: Any) -> float:
        """Sets the speed of the entity."""
        self._speed = value * (1 / self.size**3)

        # CHECK: Other options: vision (distance/angle), other senses
        # TODO: Source of food/energy herd behaviour (?)
        # TODO: Dealing with offspring immitation?

    def update(self) -> None:
        """Update functions is called every frame/tick."""
        self.age += 1
        self.energy -= 1
        if self.age > self.max_age:
            self.death()
        if self.energy <= 0:
            if not self.alive:
                self.kill()
            self.death()
        if self.alive:
            # take some action
            # deduct energy based on action taken
            ...

    def mutate(self, magnitude: Optional[float] = 0.1) -> None:
        """Mutates entity variables."""
        if self.genes["mutation_rate"] < rnd():
            for gene in self.genes:
                gene.value *= 1 - magnitude + 2 * magnitude * rnd()
        ...

    def eat(self, edible_object: Any) -> None:
        """Eats an edible object."""
        self.energy = max(edible_object.energy+self.energy, self.max_energy)
        edible_object.kill()

    def death(self) -> None:
        """Death of natural causes leaves organic matter with energy."""
        self.alive = False
        self.energy += 10

    def kill(self) -> None:
        """Kills the entity."""
        self.alive = False
        self.energy = 0

    # TODO: Use mutated copy of genes
    # TODO: Missing values for the Entity call. Copy the parents' values?
    def create_children_asexually(self) -> None:
        """Creates a child using its own genes."""
        return Entity(self.position, self.energy/2, self.genes.copy())

    # TODO: Missing values for the Entity call. Copy the parents' values?
    def create_children_sexually(self, parent):
        """Creates a child entity using genes from itself and another
        parent.
        """
        child_genes = self.genes.copy()
        for element in parent.genes():
            if choice([0, 1]):
                child_genes[element.name] = element.value
        # TODO: Improve way to determine starting energy of child
        return Entity(self.position, self.energy/2, child_genes)


if __name__ == "__main__":
    ...
