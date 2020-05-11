# my_lambdata/polos.py

class Polo:
   def __init__(self, size, color, price = 69.99):
      self.size = size
      self.color = color
      self.price = price
      pass

   def wash(self):
      print(f"Washing the {self.size.upper()} {self.color.upper()} Polo!")

if __name__ == "__main__":
   polo = Polo(size = 'large', color = 'Blue')
   print(polo.size, polo.color, polo.price)
   polo.wash()


   polo2 = Polo(size = 'large', color = 'Yellow')
   print(polo2.size, polo2.color, polo2.price)
   polo2.wash()