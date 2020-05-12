# my_lambdata/assignment_oop_inherit
# .py
import pandas as pd
import numpy as np

class DataProcessor:
    def __init__(self, my_df):
        """
        Params: 
            my_df (pandas.DataFrame) has a column called "abbrex" with state abbreviations
        """
        self.df = my_df


    def add_state_names(self):
        """
        Adds a column of state naems to accompany a corresponding column of state abbreviation.
        """

        names_map = {"CA": "Cali", "CO": "Colo", "CT": "Conn"}
        # type(my_df['abbrev']) #> class 'pandas.core.series.Series <

        self.df['name'] = self.df['abbrev'].map(names_map)
        return self.df


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
    df = pd.DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})

    processor = DataProcessor(df)
    print(processor.df.head()) # method

    processor.add_state_names()
    print(processor.df.head()) # method


    
