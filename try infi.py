import pandas as pd
import geopandas as geo
import numpy as np
import matplotlib.pyplot as plt
#import coronavirus as cv
import altair as alt


def main():
    while (True):
        print("\n\nWelcome to corona world!")
        print("\n1.To explore to world wide data")
        print("\n2.To explore nation wise data")
        print("\n#.To quit")

        choice = input("\nEnter your choice:")

        if choice=='1':
            worldMenu()
            continue

        if choice=='2':
            countryMenu()
            continue

        if choice == "#":
            exit()

        else:
            print("Try again!")
            continue


def worldMenu():
    while(True):

        print("\n1.For world map")
        print("\n2.For pie chart")
        print("\n3.For line chart")
        print("\n4.For scatter plot")
        print("\n0.Return to previous menu")
        print("\n#.To exit")

        ch = input("\nEnter your choice:")

        if ch == '1':
            worldMap()

        if ch == '2':
            pieChart()

        if ch == '3':
            lineChart()

        if ch == '4':
            scatterPlot()
        
        if ch == '0':
            break

        if ch == "#":
            exit()

def worldMap():
    #reading the csv file
    confirmed_df = pd.read_csv("time_series_covid19_confirmed_global.csv")
    deaths_df = pd.read_csv("time_series_covid19_deaths_global.csv")
    recovered_df = pd.read_csv("time_series_covid19_recovered_global.csv")

    print(confirmed_df)
    print(deaths_df)
    print(recovered_df)




def pieChart():
    #reading csv file
    confirmed_df = pd.read_csv("time_series_covid19_confirmed_global.csv")
    deaths_df = pd.read_csv("time_series_covid19_deaths_global.csv")
    recovered_df = pd.read_csv("time_series_covid19_recovered_global.csv")

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

    print(full_table)

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
    data = pd.read_csv("time_series_covid19_confirmed_global.csv")

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
    df = pd.read_csv("time_series_covid19_confirmed_global.csv")

    x = df['Country/Region']
    print(x)

    y = df['10/3/20']
    print(x)

    
    plt.xlabel('Country/Region')
    plt.ylabel('10/3/20')

    plt.scatter(x,y, c = 'r',marker= '*')
    
    plt.show()

def countryMenu():

    print("\n1.For world map")
    print("\n2.For pie chart")
    print("\n3.For line chart")
    print("\n4.For scatter plot")
    print("\n0.Return to previous menu")
    print("\n#.To exit")

    ch =  int(input("\nEnter your choice:"))

    if ch == '1':
        worldMap()

    if ch == '2':
        pieChart()

    if ch == '3':
        lineChart()

    if ch == '4':
        scatterPlot()

    if ch == "#":
        exit()

def pieChart():
    covid = pd.read_csv('covid_19_india.csv')
    print(covid)   

main()
