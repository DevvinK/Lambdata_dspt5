# my_lambdata/assignment.py
import pandas as pd

# Convert State abbreviations -> Full name and vise versa. FL -> 
# Florica, etc.
# Create an new coloumn that is a copy of the first, but mapped

def add_state_names(my_df):
   new_df = my_df.copy()

   names_map = {"CA":"Cali", "CO":"Colo", "CT":"Conn"}
   # type(my_df['abbrev']) #> class 'pandas.core.series.Series <

   new_df['name'] = my_df['abbrev'].map(names_map)
   return new_df



if __name__ == "__main__":
   df = pd.DataFrame({"abbrev" : ["CA", "CO", "CT", "DC", "TX"]})
   print(df.head())  

   df2 = add_state_names(df)
   print(df2.head())  
