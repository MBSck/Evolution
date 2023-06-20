from typing import Self, Tuple
from random import random as rnd


class Entity:
    def __init__(self: Self, age: int,
                 max_age: int,
                 position: Tuple[int, int],
                 color: str,
                 energy: int,
                 max_energy: int,
                 speed: int,
                 birth_rate: int,
                 size: int) -> None:
        self.age = age
        self.max_age = age
        self.position = position
        self.color = color
        self.energy = energy
        self.max_energy = max_energy
        self.alive = True 
        self.speed = speed
        self.birth_rate = birth_rate
        self.size = size
        #genes defines variables changable through mutation & passed on to children, perhaps better implemented with dict?
        self.genes = ["max_age", "max_energy", "color", "speed", "birth_rate", "size"]

        #other options: vision (distance/angle), other senses
        #source of food/energy
        #herd behaviour (?)
        #dealing with offspring
        #immitation?

    #mutates entity variables
    def mutate(self) -> None:
        for gene in self.genes:
            #returns the attribute defined by gene to mutate by +-10%
            locals()[gene] *= 0.9 + 0.2 * rnd()
        pass

    #returns "genes" e.g. to create children
    def genes(self):
        #return self.max_age, self.max_energy, self.color, self.speed, self.birth_rate, self.size
        return [locals()[gene] for gene in self.genes]

    #update functions is called every frame/tick
    def update(self) -> None:
        self.age += 1
        if self.age > self.max_age:
            self.death()
        if self.energy <= 0:
            if self.alive == False:
                self.kill()
            self.death()
    
    #death of natural causes leaves organic matter with energy
    def death(self) -> None:
        self.alive = False
        self.energy += 10
        pass

    def kill(self) -> None:
        self.alive = False
        self.energy = 0
        pass

    #creates a child using "genes" from self + other parent
    def create_children(self) -> None:
        pass

    #creates a child using "genes" from self + other parent
    def create_children(self, parent) -> None:
        pass


    def eat(self, eadible_obj) -> None:
        self.energy = max(eadible_obj.energy+self.energy, self.max_energy)
        eadible_obj.kill()
        pass

    

if __name__ == "__main__":
    ...

