#!/usr/bin/python3
from abc import ABC, abstractmethod


# Abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


# Subclass Dog implementing the abstract method
class Dog(Animal):
    def sound(self):
        return "Bark"


# Subclass Cat implementing the abstract method
class Cat(Animal):
    def sound(self):
        return "Meow"
