from S1E9 import Character

class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__ (self, first_name, is_alive=True):
        print("Baratheon class")
        Character.__init__(self, first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"
    
    def die (self):
        super().die()

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
    
    def __str__ (self): 
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

class Lannister(Character):
    def __init__ (self, first_name, is_alive=True):
        Character.__init__(self,first_name, is_alive)
        print("Lannister class")
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die (self):
        super().die()

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__ (self): 
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
    
    @classmethod
    def create_lannister(cls, first_name, is_alive: bool):
        return cls(first_name, is_alive)
