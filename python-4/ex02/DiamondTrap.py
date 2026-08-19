from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """A king with both Baratheon and Lannister attributes."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a king with a name and life status."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes):
        """Set the king's eye color."""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Set the king's hair color."""
        self.hairs = hairs

    def get_hairs(self):
        """Return the king's hair color."""
        return self.hairs

    def get_eyes(self):
        """Return the king's eye color."""
        return self.eyes
