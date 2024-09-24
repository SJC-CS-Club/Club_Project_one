from member import Member, Majors

class Josh(Member):
    def __init__(self):
        super().__init__("Josh", 25, Majors.COSC)

    def into(self):
        print("My major is Computer science. I run D&D and train dogs!")