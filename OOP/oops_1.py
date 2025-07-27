# #oops first concept:

# class Car:
#     color= "Blue"
#     brand= "BMW"
#     price= 50000

# car1= Car()
# print(car1)
# print(car1.color)
# print(car1.brand)
# print(car1.price)

#oops init concept:

# class student:
#     def __init__(self):
#         print(self)
#         print("hey self is created")
# s1= student()
# s2=student()
# print(s1,s2)

#accesing attributes using init & self:

# class student:
#     def __init__(self,name,age):
#         self.name= name
#         self.age= age
    
# s1= student("John", 20)
# s2= student("Doe", 22)

# print(s1.name, s2.age)

#class attributes vs object attributes:

class Student:

    college_name = "AEC"

    def __init__(self,name,department):
        self.name = name
        self.department = department

s1 = Student("Alice", "CSE")
s2 = Student("Bob", "ECE")

print(s1.name,s1.college_name) #college is class attribute, name is object attribute
print(s2.department,Student.college_name) #the class attribute can be accessed using the class name or the object instance