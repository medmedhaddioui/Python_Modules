from abc import ABC, abstractmethod

class Character(ABC):
    """Your docstring for Class"""

    @abstractmethod
    def __init__(self, first_name, stats_health):
        """my doc for parent init"""
        pass
    def die(self):
        """my doc for parent die"""
        pass

class Stark(Character):
    """Your docstring for Class"""
 
    def __init__(self, first_name, stats_health=True):
        """doc for my child init"""
        self.first_name = first_name
        self.is_alive = stats_health
    
    def die (self):
        """my doc for child die"""
        self.is_alive = False
        return self.is_alive
