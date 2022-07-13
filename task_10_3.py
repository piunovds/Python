# Клетка
class Cell:
    def __init__(self, cellule):
        self.cellule = cellule

    def __add__(self, other):
        return Cell(self.cellule + other.cellule)

    def __sub__(self, other):
        if self.cellule - other.cellule > 0:
            return Cell(self.cellule - other.cellule)
        else:
            print("ERROR! Negative difference")
            
    def __mul__(self, other):
        return Cell(self.cellule * other.cellule)
    
    def __floordiv__(self, other):
        return Cell(self.cellule // other.cellule)

    def __truediv__(self, other):
        return Cell(self.cellule // other.cellule)

    def make_order(self, qty):
        f = ''
        for _ in range(self.cellule // qty):
            for _ in range(qty):
                f += '*'
            f += '\n'
        for _ in range(self.cellule % qty):
            f += '*'
        return f
    
c1 = Cell(10)
c2 = Cell(1)
c3 = c1 // c2
print(c1.make_order(3))
