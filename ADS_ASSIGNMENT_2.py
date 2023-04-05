"""Here are the python modules which help in data analysis for 
   ploting required comparing graphs along with the heatmap 
 
 """
# necessary imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# initial data for analysis

# Countries and years for analysis

countries = ["Austria","United Kingdom", "Australia",'Belgium',"Kuwait"]
years = ["1990","1995","2000", "2005", "2010", "2015"]
# read the csv file
main_dataframe = pd.read_csv("World_bank_data.csv")

"""defining the function to read the CSV file in the mata data format and 
   then Transpose the CSV file to get the required rows and cloumns to 
   access the datato plot countries and years with the required indicators
"""   

def countries_years(file_name):
    """This function takes a filename as argument, reads a dataframe in World bank format
    and returns two dataframes:one with years as columns and one with countries as columns."""

    # read the csv file
    read_data = pd.read_csv(file_name)

    #read and transpose the CSV file
    country_columns = read_data.set_index("Country Name").transpose()

    # get the columns data from index 3
    columns_data = read_data.columns[3:]

    # set the index as Country Name and filter the dataframe with given columns data
    years_columns = read_data.set_index("Country Name")
    years_columns = years_columns.loc[:, columns_data]

    return country_columns, years_columns #returing to the function

#creating a variable to mean of the electricity efficiency
country_as_columns, years__as_columns = countries_years(
    file_name="World_bank_data.csv"
)