class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def result(self):
        if self.score >= 60:  
            return "Pass"
        else:
            return "Fail"
student1 = Student("Alice", 75)
student2 = Student("Bob", 45)

print(f"{student1.name}: {student1.result()}")  
print(f"{student2.name}: {student2.result()}")
