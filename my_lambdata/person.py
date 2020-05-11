# my_lambdata/person.py

from datetime import datetime

class Person:
   def __init__(self, sex, age, height, birthdate, eye_color):
      self.sex = sex
      self.age = age
      self.height = height
      self.birthdate = birthdate
      self.eye_color = eye_color
      

   def split_birthdate(self):
      dt = datetime.strptime(self.birthdate, '%Y/%m/%d')
      print (f"Born {dt.month}/{dt.day}/{dt.year}")


if __name__ == "__main__":
    person1 = Person("Male", 35, "5ft-4in", "1993/05/23", "blue" )
    person1.split_birthdate()
