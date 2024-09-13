# 1
# class Person:
#     def __init__(self,name):
#         self.name=name
#     def greet(self):
#         print(f"My name is {self.name}")
# obj1=Person(input())
# obj1.greet()


# 2
# class Area:
#     def __init__(self,height,width):
#         self.height=height
#         self.width=width
#     def find(self):
#         print(self.height*self.width)
# a=[int(i) for i in input().split()]
# height=a[0]
# width=a[1]
# obj1=Area(height,width)
# obj1.find()


# 3
# class Circle:
#     pi=3.14
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         print(Circle.pi*self.radius**2)
# a=float(input())
# obj1=Circle(a)
# obj1.area()


# 4
# class Car:
#     count = 0
#     def __init__(self):
#         self.count = 0
#     def total_count(self):
#         self.count += 1
# car_instance = Car()
# car_numbers = input("Enter the name of cars: ").split()

# for i in car_numbers:
#     car_instance.total_count()
# print(car_instance.count)
