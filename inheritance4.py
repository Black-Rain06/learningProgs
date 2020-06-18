class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
    self.classStart = False

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
    
  def startClass(self):
      self.classStart = True
      return self.classStart

x = Student("Mike", "Olsen", 2019)
x.welcome()
x.startClass()
print(x.classStart)
