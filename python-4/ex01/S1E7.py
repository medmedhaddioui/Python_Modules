from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a Baratheon with a name and life status."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Mark this character as dead."""
        super().die()

    def __repr__(self):
        """Return the formal Baratheon representation."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self):
        """Return the readable Baratheon description."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a Lannister with a name and life status."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Mark this character as dead."""
        super().die()

    def __repr__(self):
        """Return the formal Lannister representation."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self):
        """Return the readable Lannister description."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Create a new Lannister instance."""
        return cls(first_name, is_alive)
