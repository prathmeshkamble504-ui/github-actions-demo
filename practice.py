# class student:
#      def __init__(self,name,marks):
#           self.name=name
#           self.marks=marks
# class college:
#      def calculate_grade(self,student):
#         if   student.marks >=90:
#              grade = 'A+'
#         elif student.marks >=80:
#              grade = 'A'
#         elif student.marks >=70:
#              grade = 'B'
#         elif student.marks >=60:
#              grade = 'C'
#         elif student.marks >=40:
#              grade = 'D'
#         else:
#              grade = 'FAIL'
#         return grade
 
# student1 = student("Prathmesh", 38)

# college1 = college()

# grade = college1.calculate_grade(student1)

# print(f"student.name =  {student1.name}")
# print(f"student.marks= {student1.marks}")
# print(f"student.grade= {grade}")

# a = 5
# b = 10 

# if a < b:
#     print("b is greater than a")
# else:
#     print("b is not greater than a")

#1
a = 5
b = 10
c = 15

if a > b and a > c:
    print("a is the greatest no")
elif b > a and b > c:
    print("b is the greatest no")
else:
    print("c is the greatest no")

#2
a = 2
b = 5
c = 7

if a % 2 == 0:
    print("a is an even no")
else:
    print("a is not an even no")

if b % 2 == 0:
    print("b is an even no")
else:
    print("b is not an even no")

if c % 2 == 0:
    print("c is an even no")
else:
    print("c is not an even no")
    

#3
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


class Result:
    def check_result(self, student):
        if student.marks >= 40:
            print(student.name, "is Pass")
        else:
            print(student.name, "is Fail")



s1 = Student("Rahul", 55)

r1 = Result()
r1.check_result(s1)


#4
num = int(input("enter the no: "))

if num % 2 == 0:
    print("it is a even no")
else:
    print("it is a odd no")
