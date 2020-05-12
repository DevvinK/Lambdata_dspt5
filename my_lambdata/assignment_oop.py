# my_lambdata/assignment.py
import pandas as pd
import numpy as np

# Convert State abbreviations -> Full name and vise versa. FL ->
# Florica, etc.
# Create an new coloumn that is a copy of the first, but mapped


def add_state_names(my_df):
    """
    Adds a column of state naems to accompany a corresponding column of state abbreviation.

    Params:
       my_df (pandas.DataFrame) has a column called "abbrev" with state abbreviations

    Returns:
       Copy of the original dataframe, with another column
    """
    new_df = my_df.copy()

    names_map = {"CA": "Cali", "CO": "Colo", "CT": "Conn"}
    # type(my_df['abbrev']) #> class 'pandas.core.series.Series <

    new_df['name'] = my_df['abbrev'].map(names_map)
    return new_df


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
    # df = pd.DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    # print(df.columns) # property
    # print(df.head()) # method

    # df2 = add_state_names(df)
    # print(df2.head())

    # df3 = pd.DataFrame({"a": [1,2,3,4]})

    df_date = pd.DataFrame(
        {"Date": ["5/10/2020", "5/9/2020", "5/8/2020", "5/7/2020", ]})
    df_date = split_dates(df_date)
    print(df_date)

    scores = {'First Score': [100, 90, np.nan, 95],
              'Second Score': [30, 45, 56, np.nan],
              'Third Score': [55, 40, 80, 98]}
    df4 = pd.DataFrame(scores)
    has_null(df4)
