class calculator:
    """A calculator class for vector-vector operations."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the dot product of two vectors."""
        result = [V1[i] * V2[i] for i in range(len(V1))]
        print(sum(result))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors element-wise and print the result."""
        result = [float(V1[i]) + float(V2[i]) for i in range(len(V1))]
        print(result)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract two vectors element-wise and print the result."""
        result = [float(V1[i]) - float(V2[i]) for i in range(len(V1))]
        print(result)
