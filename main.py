requirement = {"pandas": "python -m pip install pandas", "geopandas": "python -m pip install geopandas", "numpy": "python -m pip install numpy", "matplotlib": "python -m pip install matplotlib", "altair": "python -m pip install altair"}
missing = []
try:
    import pandas as pd
except:
    missing.append("pandas")
try:
    import geopandas as geo
except:
    missing.append("geopandas")
try :
    import numpy as np#no problem😇
except:
    missing.append("numpy")
try:
    import matplotlib.pyplot as plt
#import coronavirus as cv
except:
    missing.append("matplotlib")
try:
    import altair as alt
except:
    missing.append("altair")
#import baishali as goru
if missing != []:
    print(f'''\n\nYou are missing {len(missing)} package(s) in your system that are required to run this program.
    Please execute this following command(s) in your terminal to resolve this issue.''')
    for i in missing:
        print(f"\nMissing : {i}\nCommand : {requirement[i]}")
    exit()


def main():
    while (True):
        print("\n\nWelcome to corona world!")
        print("1.To explore to world wide data")
        print("2.To explore nation wise data")
        print("n#.To quit")

        choice = input("\nEnter your choice : ")

        if choice=='1':
            worldMenu()
            continue

        if choice=='2':
            countryMenu()
            continue

        if choice == "#":
            exit()

        else:
            print("Wrong input, Try again!")
            continue


def worldMenu():
    while(True):

        print("\n\n1.For world map")
        print("2.For pie chart")
        print("3.For line chart")
        print("4.For scatter plot")
        print("0.Return to previous menu")
        print("#.To exit")

        ch = input("\nEnter your choice : ")

        if ch == '1':
            worldMap()
            continue

        if ch == '2':
            pieChart()
            continue

        if ch == '3':
            lineChart()
            continue

        if ch == '4':
            scatterPlot()
            continue
        
        if ch == '0':
            break

        if ch == "#":
            exit()

        else:
            print("Wrong input, Try again!")
            continue


def countryMenu():
    while(True):               
        print("2.For pie chart")
        print("3.For line chart")
        print("4.For scatter plot")
        print("0.Return to previous menu")
        print("#.To exit")

        ch =  input("\nEnter your choice:")

        if ch == '1':
            worldMap()
            continue
        if ch == '2':
            pieChart()  
            continue

        if ch == '3':
            lineChart()
            continue

        if ch == '4':
            scatterPlot()
            continue

        if ch == "#":
            exit()

        else:
            print("Wrong input, Try again!")
            continue


def worldMap():
    #reading the csv file
    confirmed_df = pd.read_csv("assets/time_series_covid19_confirmed_global.csv")
    deaths_df = pd.read_csv("assets/time_series_covid19_deaths_global.csv")
    recovered_df = pd.read_csv("assets/time_series_covid19_recovered_global.csv")

    print(confirmed_df)
    print(deaths_df)
    print(recovered_df)


def pieChart():
    #reading csv file
    confirmed_df = pd.read_csv("assets/time_series_covid19_confirmed_global.csv")
    deaths_df = pd.read_csv("assets/time_series_covid19_deaths_global.csv")
    recovered_df = pd.read_csv("assets/time_series_covid19_recovered_global.csv")

    print(confirmed_df)

    dates = confirmed_df.columns[4:]

    confirmed_df_long = confirmed_df.melt(
        id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
        value_vars=dates, 
        var_name='Date', 
        value_name='Confirmed'
    )
    
    deaths_df_long = deaths_df.melt(
        id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
        value_vars=dates, 
        var_name='Date', 
        value_name='Deaths'
    )
    
    recovered_df_long = recovered_df.melt(
        id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
        value_vars=dates, 
        var_name='Date', 
        value_name='Recovered'
    )
    
    # Merging confirmed_df_long and deaths_df_long
    
    full_table = confirmed_df_long.merge(
    right=deaths_df_long, 
    how='left',
    on=['Province/State', 'Country/Region', 'Date', 'Lat', 'Long']
    )
    # Merging full_table and recovered_df_long
    
    full_table = full_table.merge(
    right=recovered_df_long, 
    how='left',
    on=['Province/State', 'Country/Region', 'Date', 'Lat', 'Long']
    )

    confirmed_cases = full_table['Confirmed']
    death_cases = full_table['Deaths']
    recovered_cases = full_table['Recovered']

    country = full_table['Country/Region']

    print("\n1.For confirmed cases")
    print("\n2.For deaths cases")
    print("\n3.For recovered cases")
    print("\n#.To exit")

    ch = input("\nEnter your choice:")
    
    
    #pie chart of confirmed cases
    if ch == 1:
        plt.pie(confirmed_cases,labels= country, shadow = True, startangle = 140)
        plt.title('confirmed cases')

    #pie chart of deaths
    if ch == 2:
        plt.pie(death_cases,labels= country, shadow = True, startangle = 140)
        plt.title('death_cases')

    #pie chart of recovered cases
    if ch == 3:
        plt.pie(recovered_cases,labels = country, shadow = True, startangle = 140 )
        plt.title('recovered_cases')
    
    plt.show()


def lineChart():
    #reading the csv file
    data = pd.read_csv("assets/time_series_covid19_confirmed_global.csv")

    #group the data by the country
    data = data.groupby('Country/Region').sum()


    #drop lat and and long columns
    data = data.drop(columns = ['Lat','Long'])

    #create a transpose of the dataframe
    data_transposed = data.T

    #plotting 
    data_transposed.plot( y =['US','India','Brazil','Spain','Argentina','Colombia','Peru','Mexico','France','South Africa','Iran','Chile','Iraq','Bangladesh','Italy'],use_index = True, figsize = (10,10),marker = '*',markersize = 0.7)

    plt.show()


def scatterPlot():
    df = pd.read_csv("assets/time_series_covid19_confirmed_global.csv")

    x = df['Country/Region']
    print(x)

    y = df['10/3/20']
    print(x)

    
    plt.xlabel('Country/Region')
    plt.ylabel('10/3/20')

    plt.scatter(x,y, c = 'r',marker= '*')
    
    plt.show()


def pieChart():
    covid = pd.read_csv('covid_19_india.csv')
    print(covid)   


main()