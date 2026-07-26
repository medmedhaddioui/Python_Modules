from abc import ABC, abstractmethod

class Character(ABC):
    """Your docstring for Class"""
    @abstractmethod
    def is_alive():
        pass
Stark(Character):
    """Your docstring for Class"""




# class Character():
#     name = "haddioui"
#     def set_name (self, name):
#         self.name += name
#         print(self.name)

# simo = Character ()
# simo.set_name("simo")