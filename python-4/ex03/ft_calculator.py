class calculator:
#your code here
    def __init__ (self, list: list):
        self.vector = list

    def __add__(self, object) -> None:
        for index, i in enumerate (self.vector):
            self.vector[index] = i + object
        print(self.vector)


    def __mul__(self, object) -> None:
        for index, i in enumerate (self.vector):
            self.vector[index] = i * object
        print(self.vector)
    
    def __sub__(self, object) -> None:

        for index, i in enumerate (self.vector):
                self.vector[index] = i - object
        print(self.vector)

    def __truediv__(self, object) -> None:
        for index, i in enumerate (self.vector):
            if (i == 0 and object == 0):
                print("impossible")
                return 
            self.vector[index] = i / object
        print(self.vector)
