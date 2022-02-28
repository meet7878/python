class Person:
      def __init__(self, fname, lname):
       self.firstname = fname     # proper initialize of  data member
       self.lastname = lname

      def printname(self):
        print(self.firstname, self.lastname)



x = Person("meet", "ved")
x.printname()