from member import Member, Majors


class Valisa(Member):
    def __init__(self):
        super().__init__(
            "Valisa", 20, Majors.COSC
        )

    def intro(self):
        print("My major is computer science and I like to draw and learn about coding")
        