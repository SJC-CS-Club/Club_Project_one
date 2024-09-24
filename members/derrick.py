from member import Member, Majors


class Derrick(Member):
    def __init__(self):
        super().__init__(
            "Derrick", 19, Majors.COSC
        )

    def intro(self):
        print("My major is computer science and I like to listen to music and code!")
        