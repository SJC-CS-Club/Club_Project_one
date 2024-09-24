from member import Member, Majors


class Natalie(Member):
    def __init__(self):
        super().__init__(
            "Natalie", 21, Majors.COSC
        )

    def intro(self):
        print("My major is computer science and I like to play video games and watch video essays!")
        