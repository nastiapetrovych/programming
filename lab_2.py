import pandas as pd


def read_data(path_to_file):
    """ Reads the data from cvs file
    """
    df = pd.read_csv(path_to_file)
    return df


def max_counties(df):
    """ Returns the country with the biggest amount of states
    >>> max_counties(df=pd.DataFrame({'STNAME':['m','n','m'],
    ... 'SUMLEV':[50,50,50]},index=[1,2,3]))
    'm'
    """
    df = df[df["SUMLEV"] == 50]
    return df['STNAME'].value_counts().index[0]
import doctest
print(doctest.testmod())


def max_difference(df):
    """ Returns the max difference among population info
    """
    different_values = []
    df = df[df["SUMLEV"] == 50]
    for index in df.index:
        years_values = []
        for year in range(2010, 2016):
            years_values.append(df.loc[index, f"POPESTIMATE{year}"])
        different_values.append(abs(max(years_values) - min(years_values)))
    
    df["Difference"] = different_values
    max_value = df["Difference"].max()
    return df.loc[df["Difference"] == max_value]["CTYNAME"].values[0]


def conditional_counties(df):
    df = df[(df["REGION"] == 1) | (df["REGION"] == 2)]
    df = df[df["CTYNAME"].str.startswith("Washington")]
    df = df[(df["POPESTIMATE2015"]) > (df["POPESTIMATE2014"])]
    df = df[['STNAME', 'CTYNAME']]
    return df.head(5)

