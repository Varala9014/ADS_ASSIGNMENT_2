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


"""defining the function to plot the graphs of the selected countires with 
   respect to particular years to plot the bar graphs with the indicator to 
   do the data analysis
"""

def plotting_data(indicator_name):
    """This function takes indicator name as argument, It plots the bar graph for the dataframe and
    returns the filtered dataframe for the indicator with given countries and years"""

    if indicator_name == "Agriculture, forestry, and fishing, value added (% of GDP)":
        label = "(% of GDP)"
    elif indicator_name == "CO2 emissions from gaseous fuel consumption (% of total)":
        label = "% of total"
    elif indicator_name == "Total greenhouse gas emissions (kt of CO2 equivalent)":
        label = "kt of CO2 equivalent"

    # filter the dataframe with given countries and indicator name and set the index as Country Name.
    selected_data = main_dataframe[
        (main_dataframe["Country Name"].isin(countries))
        & (main_dataframe["Indicator Name"] == indicator_name)
    ].set_index("Country Name")

    # filter the dataframe with given years and reset the index
    refined_df = selected_data.loc[:, years].reset_index()
    # plt.legend(bbox_to_anchor=(1.0, 1.0))
    refined_df.set_index("Country Name").plot.bar(
        rot=0, xlabel="Countries", ylabel=label, title=indicator_name
    )

    return refined_df #returning to the function

"""calling the plotting_data function to plot the bar graph with respect the
  indicator so that the graph produce require data analyis with respect to
  countries and years mentioned to represent plotting
"""
plotting_data(indicator_name="Agriculture, forestry, and fishing, value added (% of GDP)")
plotting_data(indicator_name="CO2 emissions from gaseous fuel consumption (% of total)")
plotting_data(indicator_name="Total greenhouse gas emissions (kt of CO2 equivalent)")
