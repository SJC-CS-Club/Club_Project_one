from enum import IntEnum, auto


class Member:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
    
    def intro(self):
        ...


class Majors(IntEnum):
    COSC = auto()
    MATH = auto()
    BUSI = auto()
    EDUC = auto()
    ARTS = auto()
    BIOL = auto()
    CHEM = auto()
    COMM = auto()
    GAME = auto()
    ECON = auto()
    ENGR = auto()
    ENGL = auto()
    MUSI = auto()
    PHYS = auto()
