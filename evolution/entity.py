from typing import Self, Tuple
from random import random as rnd
from random import choice
from dataclasses import dataclass


@dataclass
class Gene:
    name: str
    value: int
    description: str

class Entity:
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
        self.age = 0
        self.alive = True #duh
        self.position = position
        self.energy = energy       
        #genes defines variables changable through mutation & passed on to children
        self.genes = {
            "max_age": Gene("Max Age", max_age, "Max age of the entity"),
            "max_energy": Gene("Max Energy", max_energy, "expected max energy of the entity"),
            "color": Gene("Color", color, "Color of the entity"),
            "speed": Gene("Speed", speed, "Speed of the entity"),
            "birth_rate": Gene("Birth Rate", birth_rate, "frequency of birth-events"),
            "birth_count": Gene("Birth Count", birth_count, "expected number of offspring per birth-event"),
            "size": Gene("Size", size, "Size of the entity"),
            "mutation_rate": Gene("Mutation Rate", mutation_rate, "Frequency of mutations occuring")
             }

    def __init__(self: Self,
                 position: Tuple[int, int],
                 energy: int,
                 gene_dict: dict
                 ) -> None:
        self.age = 0
        self.alive = True #duh
        self.position = position
        self.energy = energy
        self.genes = gene_dict
 
    @property
    def speed(self):
        if self._speed is None:
            (1 / self.size**3)*self._speed
        return self._speed

        #other options: vision (distance/angle), other senses
        #source of food/energy
        #herd behaviour (?)
        #dealing with offspring
        #immitation?

    #mutates entity variables
    def mutate(self, magnitude: float=0.1) -> None:
        if self.gene("mutation_rate") < rnd():
            for g in self.genes:
                g.value *= 1 - magnitude + 2 * magnitude * rnd()
        pass

    #returns "genes" e.g. to create children
    def genes(self):
        #return self.max_age, self.max_energy, self.color, self.speed, self.birth_rate, self.size, ...
        return self.genes

    #update functions is called every frame/tick
    def update(self) -> None:
        self.age += 1
        self.energy -= 1
        if self.age > self.max_age:
            self.death()
        if self.energy <= 0:
            if self.alive == False:
                self.kill()
            self.death()
        if self.alive:
            #take some action
            #deduct energy based on action taken
            pass
            
    #death of natural causes leaves organic matter with energy
    def death(self) -> None:
        self.alive = False
        self.energy += 10

    def kill(self) -> None:
        self.alive = False
        self.energy = 0

    #creates a child using own genes
    def create_children(self) -> None:
        #TODO: use mutated copy of genes
        return Entity(self.position, self.energy/2, self.genes.copy())

    #creates a child Entity using genes from self + other parent
    def create_children(self, parent):
        child_genes = self.genes.copy()
        for el in parent.genes():
            if (choice([0, 1])):
                child_genes[el.name] = el.value
        return Entity(self.position, self.energy/2, child_genes) #TODO: improve way to determine starting energy of child 

    def eat(self, eadible_obj) -> None:
        self.energy = max(eadible_obj.energy+self.energy, self.max_energy)
        eadible_obj.kill()
        pass

    

if __name__ == "__main__":
    ...

