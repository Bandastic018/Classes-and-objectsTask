from ast import arg
from turtle import end_fill


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    def change_name(self, newname):
        self.name = newname
        print("The Student's new name is", newname, ".")

    def change_age(self, newage):
        self.age = 30
        print("The Student's new age is", newage, ".")

    def add_track(self, newtrack):
        tracks = self.tracks
        print(f"The Student's tracks are", [newtrack] + tracks, "tracks")

    def get_score(self,):
        score = self.score
        print("The Student's score is", score, ".")


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

# Expected methods
print(Bob.change_name("Peter"))
print(Bob.change_age(34))
print(Bob.add_track("Product Design"))
print(Bob.get_score())
