class Student:

    class_year = 2024  # It will apply to all the students
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Said", 21)
student2 = Student("Eldor", 22)
student3 = Student("Amir", 25)


print(f"Our class has {Student.num_students} students with the graduation year of {Student.class_year}")
print(student1.name)
print(student2.name)
print(student3.name)