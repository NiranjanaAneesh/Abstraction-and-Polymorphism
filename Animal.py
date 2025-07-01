from abc import ABC
class Animal(ABC):
    def move(self):
      pass
class Human(Animal):
   def move(self):
      print("I can walk and run")
class Snake(Animal):
   def move(self):
      print("I can crawl")
class Dog(Animal):
   def move(self):
      print("I can bark")
class Lion(Animal):
   def move(self):
      print("I can roar")
R = Human()
R.move()
R = Snake()
R.move()
R = Dog()
R.move()
R = Lion()
R.move()