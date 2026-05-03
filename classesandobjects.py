class Student():
    #properties
    age = 12
    avg_grade = "0"
    teacher = "kelly"
    school = "wanaka primary"
    #constructor
    def __init__(self,n):
        print("making a student function")
        self.n = n
    #functions
    def showdetails(self):
        print(self.age,self.n,self.avg_grade,self.teacher,self.school)
    def change_details(self):
        self.n = input(str("enter name of student "))
        self.avg_grade = input(str("enter avg grade "))+"%"
        self.age = input(str("enter age "))
        self.teacher = input(str("enter teacher "))

student_1 = Student("bob")
#student_1.change_details()
student_1.showdetails()
