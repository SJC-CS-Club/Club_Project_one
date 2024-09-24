from member import Member, Majors


class Kirsten(Member):
    def __init__(self):
        super().__init__(
            "Kirsten", 20, Majors.COSC
        )

    def intro(self):
        print("My major is computer science and I like to play sports and listen to music!")
        