class Student:
    def print_name(self):
        print(f"名前：{self.name}")
        
    def print_grade(self):
        print(f"学年：{self.grade}")
        
    def print_major(self):
        print(f"専攻: {self.major}")

student1 = Student()
student1.name = input("学生の名前を入力してください:")
student1.grade = input("学年：")
student1.major = input("学生の専攻を入力してください: ")

student1.print_name()
student1.print_grade()
student1.print_major()