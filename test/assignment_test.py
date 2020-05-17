#  test/assignment_test.py

import unittest
from pandas import DataFrame
from my_lambdata.assignment import add_state_names

# OBJECTIVE: test the add_state_names() function from the my_lambdata/assignment.py file
class TestAssignment(unittest.TestCase):

    def test_add_state_names(self):
      
      df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
      self.assertEqual(list(df.columns),['abbrev'])
     
     
      result = add_state_names(df)
      self.assertEqual(list(result.columns),['abbrev', 'name'])

   #Afer we invoke the fucntion:
      #expect a second column with the same number of rows
      #expect certain column names exist before and after


      #df.columns
      #   self.assertEqual('foo'.upper(), 'FOO') #True or False



if __name__ == '__main__':
    unittest.main()