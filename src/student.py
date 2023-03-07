class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name}. Age: {self.age}")

ram = Student("Ram", 28)
ram.info()
