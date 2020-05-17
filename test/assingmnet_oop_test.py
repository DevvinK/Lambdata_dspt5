#  test/assignment_oop_test.py

import unittest
from pandas import DataFrame
from my_lambdata.assignment_oop import DataProcessor



# OBJECTIVE: test the add_state_names() function from the my_lambdata/assignment.py file
class TestDAtaProcessord(unittest.TestCase):

    def test_add_state_names_oop(self):
      
      df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
      processor = DataProcessor(df)
      self.assertEqual(list(df.columns),['abbrev'])
     
      processor.add_state_names()

      self.assertEqual(list(processor.df.columns),['abbrev', 'name'])
      self.assertEqual(processor.df.iloc[0]["abbrev"], "CA")
      self.assertEqual(processor.df.iloc[0]["name"], "Cali")

   #Afer we invoke the fucntion:
      #expect a second column with the same number of rows
      #expect certain column names exist before and after


      #df.columns
      #   self.assertEqual('foo'.upper(), 'FOO') #True or False



if __name__ == '__main__':
    unittest.main()