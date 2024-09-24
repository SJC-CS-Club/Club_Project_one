from member import Member, Majors


class Erin(Member):
    def __init__(self):
        super().__init__(
            "Erin", 18, Majors.COSC
        )

    def intro(self):
        print("My major is computer science and I like to listen to 80s music and code¡")
        