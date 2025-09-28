from block import Block
from cell import Cell

class LBlock(Block):
    def __init__(self):
        super().__init__()
        self.cells = {
            0: [Cell(0, 2, [0, 2], 1),
                Cell(1, 0, [3, 1], 1),
                Cell(1, 1, [3, 1], 1),
                Cell(1, 2, [3, 0], 1)],

            1: [Cell(0, 1, [0, 2], 1),
                Cell(1, 1, [0, 2], 1),
                Cell(2, 1, [0, 1], 1),
                Cell(2, 2, [3, 1], 1)],

            2: [Cell(1, 0, [1, 2], 1),
                Cell(1, 1, [3, 1], 1),
                Cell(1, 2, [3, 1], 1),
                Cell(2, 0, [0, 2], 1)],

            3: [Cell(0, 0, [3, 1], 1),
                Cell(0, 1, [3, 2], 1),
                Cell(1, 1, [0, 2], 1),
                Cell(2, 1, [0, 2], 1)],


        }
        self.move(0, 3)

class JBlock(Block):
    def __init__(self):
        super().__init__()
        self.cells = {
            0: [Cell(0, 0, [0, 2], 2),
                Cell(1, 0, [0, 1], 2),
                Cell(1, 1, [3, 1], 2),
                Cell(1, 2, [3, 1], 2)],

            1: [Cell(0, 1, [1, 2], 2),
                Cell(0, 2, [3, 1], 2),
                Cell(1, 1, [0, 2], 2),
                Cell(2, 1, [0, 2], 2)],

            2: [Cell(1, 0, [3, 1], 2),
                Cell(1, 1, [3, 1], 2),
                Cell(1, 2, [3, 2], 2),
                Cell(2, 2, [0, 2], 2)],

            3: [Cell(0, 1, [0, 2], 2),
                Cell(1, 1, [0, 2], 2),
                Cell(2, 0, [3, 1], 2),
                Cell(2, 1, [3, 0], 2)]
        }
        self.move(0, 3)

class IBlock(Block):
    def __init__(self):
        super().__init__()
        self.cells = {
            0: [Cell(1, 0, [3, 1], 3),
                Cell(1, 1, [3, 1], 3),
                Cell(1, 2, [3, 1], 3),
                Cell(1, 3, [3, 1], 3)],

            1: [Cell(0, 2, [0, 2], 3),
                Cell(1, 2, [0, 2], 3),
                Cell(2, 2, [0, 2], 3),
                Cell(3, 2, [0, 2], 3)],

            2: [Cell(2, 0, [3, 1], 3),
                Cell(2, 1, [3, 1], 3),
                Cell(2, 2, [3, 1], 3),
                Cell(2, 3, [3, 1], 3)],

            3: [Cell(0, 1, [0, 2], 3),
                Cell(1, 1, [0, 2], 3),
                Cell(2, 1, [0, 2], 3),
                Cell(3, 1, [0, 2], 3)]
        }
        self.move(-1, 3)

class OBlock(Block):
    def __init__(self):
        super().__init__()
        self.cells = {
            0: [Cell(0, 0, [1, 2], 4),
                Cell(0, 1, [2, 3], 4),
                Cell(1, 0, [0, 1], 4),
                Cell(1, 1, [3, 0], 4)],

            1: [Cell(0, 0, [1, 2], 4),
                Cell(0, 1, [2, 3], 4),
                Cell(1, 0, [0, 1], 4),
                Cell(1, 1, [3, 0], 4)],

            2: [Cell(0, 0, [1, 2], 4),
                Cell(0, 1, [2, 3], 4),
                Cell(1, 0, [0, 1], 4),
                Cell(1, 1, [3, 0], 4)],

            3: [Cell(0, 0, [1, 2], 4),
                Cell(0, 1, [2, 3], 4),
                Cell(1, 0, [0, 1], 4),
                Cell(1, 1, [3, 0], 4)],

        }
        self.move(0, 4)

class SBlock(Block):
    def __init__(self):
        super().__init__()
        self.cells = {
            0: [Cell(0, 1, [1, 2], 5),
                Cell(0, 2, [3, 1], 5),
                Cell(1, 0, [3, 1], 5),
                Cell(1, 1, [3, 0], 5)],

            1: [Cell(0, 1, [0, 2], 5),
                Cell(1, 1, [0, 1], 5),
                Cell(1, 2, [3, 2], 5),
                Cell(2, 2, [0, 2], 5)],

            2: [Cell(1, 1, [1, 2], 5),
                Cell(1, 2, [3, 1], 5),
                Cell(2, 0, [3, 1], 5),
                Cell(2, 1, [3, 0], 5)],

            3: [Cell(0, 0, [0, 2], 5),
                Cell(1, 0, [0, 1], 5),
                Cell(1, 1, [3, 2], 5),
                Cell(2, 1, [0, 2], 5)],
        }
        self.move(0, 3)

class TBlock(Block):
    def __init__(self):
        super().__init__()
        self.cells = {
            0: [Cell(0, 1, [0, 2], 6),
                Cell(1, 0, [3, 1], 6),
                Cell(1, 1, [3, 0, 1], 6),
                Cell(1, 2, [3, 1], 6)],

            1: [Cell(0, 1, [0, 2], 6),
                Cell(1, 1, [0, 1, 2], 6),
                Cell(1, 2, [3, 1], 6),
                Cell(2, 1, [0, 2], 6)],

            2: [Cell(1, 0, [3, 1], 6),
                Cell(1, 1, [1, 2, 3], 6),
                Cell(1, 2, [3, 1], 6),
                Cell(2, 1, [0, 2], 6)],

            3: [Cell(0, 1, [0, 2], 6),
                Cell(1, 0, [3, 1], 6),
                Cell(1, 1, [2, 3, 0], 6),
                Cell(2, 1, [0, 2], 6)]
        }
        self.move(0, 3)

class ZBlock(Block):
    def __init__(self):
        super().__init__()
        self.cells = {
            0: [Cell(0, 0, [3, 1], 7),
                Cell(0, 1, [3, 2], 7),
                Cell(1, 1, [0, 1], 7),
                Cell(1, 2, [3, 1], 7)],

            1: [Cell(0, 2, [0, 2], 7),
                Cell(1, 1, [1, 2], 7),
                Cell(1, 2, [3, 0], 7),
                Cell(2, 1, [0, 2], 7)],

            2: [Cell(1, 0, [3, 1], 7),
                Cell(1, 1, [3, 2], 7),
                Cell(2, 1, [0, 1], 7),
                Cell(2, 2, [3, 1], 7)],

            3: [Cell(0, 1, [0, 2], 7),
                Cell(1, 0, [1, 2], 7),
                Cell(1, 1, [3, 0], 7),
                Cell(2, 0, [0, 2], 7)],
        }
        self.move(0, 3)
