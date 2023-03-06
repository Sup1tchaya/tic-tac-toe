class Shape:
   def __inint__(self,name,length):
      self.name = name
      self.length = length
   def area(self):
      return 0
class Square(Shape):
   def __init__(self, name, length):
      super().__init__(name, length)
   def describe(self):
      print('This is a:',self.name)
   def area(self):
      print('The area is: ')
      return self.length ** 2
    
s = Square('square',5)
s.area()
