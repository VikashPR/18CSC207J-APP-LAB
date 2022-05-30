class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getMarks(self, marks):
        self.marks = int(marks)

    def printDetails(self):
        print(self.name)
        print(self.age)
        print(self.calcAvg())

    def calcAvg(self):
        Sum = sum(self.marks)
        return Sum/len(self.marks)


name = input("Enter your name: ")
age = input("Enter your age: ")
marks = []

for i in range(0, 6):
    print("Enter mark")
    mark = input()
    marks.append(mark)
subjects = ["COA", "DAA", "OS", "DSA", "APP", "BRUH"]

fSubject = frozenset(subjects)

student1 = Student(name, age)

student1.getMarks(marks)
student1.calcAvg()
for i in subjects:
    print(subjects[i])

student1.printDetails()
