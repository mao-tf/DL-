class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def greet(self):
        print(f"{self.name}さんの点数は {self.score} 点です。")