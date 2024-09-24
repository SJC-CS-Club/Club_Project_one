from member import Member, Majors


class Ryley(Member):
    def __init__(self):
        super().__init__(
            "Ryley", 25, Majors.COSC
        )

    def intro(self):
        print("My major is computer science and I like to play video games, and I would like to make games as well.")
        