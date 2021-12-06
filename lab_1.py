import pandas as pd


def read_data():
    """Reads the data from csv file and returns DataFrame
    >>> read_data().loc["Algeria", "Gold"]
    5
    """
    df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)
    for col in df.columns:
        if col[:2] == '01':
            df.rename(columns={col: 'Gold'+col[4:]}, inplace=True)
        elif col[:2] == '02':
            df.rename(columns={col: 'Silver'+col[4:]}, inplace=True)
        elif col[:2] == '03':
            df.rename(columns={col: 'Bronze'+col[4:]}, inplace=True)
        elif col[:1] == '№':
            df.rename(columns={col: '#'+col[1:]}, inplace=True)

    names_ids = df.index.str.split('\\s\\(')

    df.index = names_ids.str[0]
    df['ID'] = names_ids.str[1].str[:3]

    df = df.drop('Totals')
    return df


def first_country(df):
    """Returns the firts item of datafile
    >>> first_country(read_data())["Gold"]
    0
    """
    first_row = df.loc[df.index[0]]
    return pd.Series(first_row.values, index=df.columns)


def summer_biggest(df):
    """Returns the country with the biggest amount of gold medal
    >>> summer_biggest(read_data())
    'United States'
    """
    max_value = df["Gold"].max()
    return df.loc[df["Gold"] == max_value].index[0]


def difference_biggest(df):
    """Returns the country with the biggest difference between gold medals
    in summer and winter
    >>> difference_biggest(read_data())
    'United States'
    """
    df["difference"] = abs(df["Gold"] - df["Gold.1"])
    max_value = df["difference"].max()
    df = df.loc[df["difference"] == max_value]
    return df.index[0]


def difference_biggest_relative(df):
    """Returns the country with the biggest difference according to the formula
    >>> difference_biggest_relative(read_data())
    'Bulgaria'
    """
    df = df.loc[(df["Gold"] > 0) & (df["Gold.1"] > 0)]
    df["difference"] = abs(df["Gold"] - df["Gold.1"]) / df["Gold.2"]
    max_value = df["difference"].max()
    df = df.loc[df["difference"] == max_value]
    return df.index[0]


def get_points(df):
    """Returns Series with total sum of medal
    >>> get_points(read_data())["Austria"]
    569
    """
    df["Points"] = 3 * df["Gold.2"] + 2 * df["Silver.2"] + df["Bronze.2"]
    return pd.Series(df["Points"].values, index=df.index)
