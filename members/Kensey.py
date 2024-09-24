from member import Member, Majors


class Derrick(Member):
    def __init__(self):
        super().__init__(
            "Kensey", 19, Majors.COSC
        )

    def intro(self):
        print("My major is computer science and I like to play Fortnite in my free time :3")
        