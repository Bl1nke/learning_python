class Student:
    def __init__(self, name, grades:list = None):
        self.name = name
        self.grades = grades if grades is not None else []


    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            raise ValueError("Grade must be from 0 to 100")
        
    def avarage_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def is_passing(self, passing_score=60):
        return self.avarage_grade() >= passing_score

        
    def __str__(self):
        return f"Student {self.name}: avarage grade = {self.avarage_grade()}"


if __name__ == "__main__":
    list_grade = [50, 70, 70, 65]
    student1 = Student("Pavel", list_grade)
    student1.avarage_grade()
    print(student1)

