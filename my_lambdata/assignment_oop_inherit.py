# my_lambdata/assignment_oop_inherit.py
from pandas import DataFrame
import numpy as np

class MyFrame(DataFrame):
    
    def add_state_names(self):
        """
        Adds a column of state naems to accompany a corresponding column of state abbreviation.
        """

        names_map = {"CA": "Cali", "CO": "Colo", "CT": "Conn"}
        self['name'] = self['abbrev'].map(names_map)


def split_dates(df):
    new_df = df.copy()

    new_df['Date'] = pd.to_datetime(new_df['Date'], infer_datetime_format=True)

    new_df['Day'] = new_df['Date'].dt.day
    new_df['Month'] = new_df['Date'].dt.month
    new_df['Year'] = new_df['Date'].dt.year

    return new_df


def has_null(df):
    new_df = df.copy()

    nulls = pd.isnull(new_df)
    breakpoint()
    print(new_df[nulls])

    pass


if __name__ == "__main__":
    my_frame = MyFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(my_frame.columns)
    print(my_frame.head())
    
    my_frame.add_state_names()
    print(my_frame.head())