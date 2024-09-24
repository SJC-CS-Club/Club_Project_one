from member import Member, Majors


class Cosette(Member):
    def __init__(self):
        super().__init__(
            "Cosette", 17, Majors.COSC
        )

    def intro(self):
        print("My major is computer science, but I want to go to University to get my Bachelor's in software development. I also like to read and listen to music.")
        
        