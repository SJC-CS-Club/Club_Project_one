from member import Member, Majors


class Victoria(Member):
    def __init__(self):
        super().__init__(
            "Victoria", 19, Majors.COSC
        )

    def intro(self):
        print("My major is computer science and I like to watch anime and game on my spare time!")
        