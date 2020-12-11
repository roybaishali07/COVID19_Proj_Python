
requirement = {"pandas": "python -m pip install pandas", "geopandas": "python -m pip install geopandas", "numpy": "python -m pip install numpy", "matplotlib": "python -m pip install matplotlib", "altair": "python -m pip install altair", "folium": "python -m pip install folium", "plotly": "python -m pip install plotly"}
missing = []

import os
try:
    import pandas as pd
except:
    missing.append("pandas")

try:
    import geopandas as geo
except:
    missing.append("geopandas")

try:
    from matplotlib.ticker import MaxNLocator
except:
    missing.append("matplotlib.ticker")

try :
    import numpy as np
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

try:
    import folium
except:
    missing.append("folium")

try:
    import plotly.graph_objects as go
except:
    missing.append("plotly")


if missing != []:
    print(f'''\n\nYou are missing {len(missing)} package(s) in your system that are required to run this program.
Please execute this following command(s) in your terminal to resolve this issue.''')

    for i in missing:
        print(f"\nMissing : {i}\nCommand : {requirement[i]}")
    exit()

def clear_scr():
    if os.name = "nt":
        os.system("cls")
    
    else:
        os.system("clear")

def main():
    while (True):
        clear_scr()
        print("\n************************************")
        print("WELCOME TO CORONA WORLD!")
        print("**************************************")
        print("\n1.To explore to world wide data")
        print("2.To explore nation wise data")
        print("#.To quit")

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
        clear_scr
        print("WORLD MENU")
        print("\n===========================================")
        print("Data visualisation::::")
        print("1.For world map")
        print("2.For pie chart")
        print("3.For line chart")
        print("4.For scatter plot")
        print("5.For choropleth chart")
        print("========================================")
        print("\n========================================")
        print("Read data from file in different ways::::")
        print("6.Read complete csv file:")
        print("7.Reading complete file without index::")
        print("========================================")
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
        
        if ch == '5':
            choroplethPlot()
            continue

        if ch == '6':
            csv_file()
            continue

        if ch == '7':
            no_indx()
        
        if ch == '0':
            break

        if ch == "#":
            exit()

        else:
            print("Wrong input, Try again!")
            continue
        input("Press Enter to continue")

def worldMap():
    df = pd.read_csv("assets/time_series_covid19_confirmed_global.csv")
    df.head()
    df = df.rename(columns= {"Country/Region" : "Country", "Province/State": "Province"})
    df.head()

    df['text'] = df['Country'] + " " + df["11/17/20"].astype(str)
    fig = go.Figure(data = go.Scattergeo(
        lon = df["Long"],
        lat = df["Lat"],
        text = df["text"],
        mode = "markers",
        marker = dict(
            size = 12,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = True,
            symbol = 'square',
            line = dict(
                width = 1,
                color = 'rgba(102, 102, 102)'
            ),
            cmin = 0,
            color = df['10/11/20'],
            cmax = df['10/11/20'].max(),
            colorbar_title = "COVID 19 Reported Cases"
        )
    ))

    fig.update_layout(
        title = "COVID19 Confirmed Cases Around the World",
        geo = dict(
            scope = "world",
            showland = True,
        )
    )

    fig.write_html('world_map.html', auto_open=True)


def pieChart():
    #read csv file
    df = pd.read_csv("assets/final.csv")
    top = int(input("Select the number of countries you want to visualize from top:"))

    #manipulate dataframe
    
    st = df['country'].head(top)
    ncases = df['new_cases'].head(top)
    ndth = df['new_deaths'].head(top)
    tcases = df['total_cases'].head(top)
    tdth = df['total_deaths'].head(top)

    plt.xlabel("Country")
    plt.xticks(rotation = 'vertical')

    #options and creating pie chart
    
    print("Select Specific Pie Chart as given below:")
    print("press 1 to print the data for Country vs New Cases")
    print("press 2 to print the data for Country vs New death  Cases")
    print("press 3 to print the data for Country vs Total Cases")
    print("press 4 to print the data for Country vs Total Death Cases")

    ch = int(input("Enter your choice:"))

    if ch == 1:
        plt.style.use('dark_background')
        plt.title("State wise new cases")
        plt.pie(ncases,labels = st,autopct = "%3d%%")
        plt.show()

    elif ch == 2:
        plt.style.use('dark_background')
        plt.title("State wise new death cases")
        plt.pie(ndth,labels = st,autopct = "%3d%%")
        plt.show()
    
    elif ch == 3:
        plt.style.use('dark_background')
        plt.title("State wise total cases")
        plt.pie(tcases,labels = st,autopct = "%3d%%")
        plt.show()

    elif ch == 4:
        plt.style.use('dark_background')
        plt.title("State wise  total death cases")
        plt.pie(tdth,labels = st,autopct = "%3d%%")
        plt.show()
    
    else:
        print("Invalid input")


def lineChart():
    #read csv file
    data = pd.read_csv('case_time_series.csv') 

    #manipulate dataframe
    Y = data.iloc[61:,1].values  
    R = data.iloc[61:,3].values  
    D = data.iloc[61:,5].values   
    X = data.iloc[61:,0]  

    #figure size of our line chart
    plt.figure(figsize=(25,8))

    # for dark background
    plt.style.use('dark_background')

    #plotting line chart
    ax = plt.axes() 
    ax.grid(linewidth=0.4, color='#8f8f8f')  

    ax.set_facecolor("black")  
    ax.set_xlabel('\nDate',size=25,color='#4bb4f2') 
    ax.set_ylabel('Number of Confirmed Cases\n', 
                size=25,color='#4bb4f2') 

    plt.xticks(rotation='vertical',size='20',color='white') 
    plt.yticks(size=20,color='white') 
    plt.tick_params(size=20,color='white')

    for i,j in zip(X,Y): 
        ax.annotate(str(j),xy=(i,j+100),color='white',size='13') 

        ax.annotate('Second Lockdown 15th April', 
            xy=(15.2, 860), 
            xytext=(19.9,500), 
            color='white', 
            size='15', 
            arrowprops=dict(color='white', 
                            linewidth=0.025)) 

    plt.title("COVID-19 IN : Daily ConfIrmed\n", 
            size=40,color='#28a9ff',fontstyle = "italic") 

    ax.plot(X,Y, 
        color='#1F77B4', 
        marker='o', 
        linewidth=4, 
        markersize=15, 
        markeredgecolor='#035E9B')
    
    plt.show()

def scatterPlot():
    #read csv file
    df = pd.read_csv("assets/final.csv")

    # for dark_background
    plt.style.use('dark_background')

    #manipulate dataframe
    st = df['country']
    cnf = df['total_cases']
    rc = df['new_cases']
    dth = df['total_deaths']
    ndth = df['new_deaths']
    ax = plt.gca()

    #Create the scatter ploth
    ax.scatter(st,cnf,color = 'b',label = 'State wise total cases')
    ax.scatter(st,rc,color = 'r',label = 'State wise new cases')
    ax.scatter(st,dth,color = 'g',label = 'State wise total death death cases')
    ax.scatter(st,ndth,color = 'violet',label = 'State wise new death death cases')


    plt.xlabel("state")
    plt.xticks(rotation = 'vertical')

    plt.title('complete scatter chart')
    plt.legend()

    plt.show()

    

def choroplethPlot():
    #read data
    
    df = pd.read_csv("assets/time_series_covid19_confirmed_global.csv")

    #rename columns
    df = df.rename(columns= {"Country/Region" : "Country", "Province/State": "Province"})

    # manipulate the dataframe
    
    total_list = df.groupby('Country')['11/17/20'].sum().tolist()

    country_list = df["Country"].tolist()
    country_set = set(country_list)
    country_list = list(country_set)
    country_list.sort()

    new_df = pd.DataFrame(list(zip(country_list, total_list)), 
                    columns =['Country', 'Total_Cases'])

    colors = ["#F9F9F5", "#FAFAE6", "#FCFCCB", "#FCFCAE",  "#FCF1AE", "#FCEA7D", "#FCD97D",
            "#FCCE7D", "#FCC07D", "#FEB562", "#F9A648",  "#F98E48", "#FD8739", "#FE7519",
            "#FE5E19", "#FA520A", "#FA2B0A", "#9B1803",  "#861604", "#651104", "#570303",]


    #Create the Chropleth
    fig = go.Figure(
        data=go.Choropleth(
            locationmode = "country names",
            locations = new_df['Country'],
            z = new_df['Total_Cases'],
            text = new_df['Total_Cases'],
            colorscale = colors,
            autocolorscale=False,
            reversescale=False,
            colorbar_title = 'Reported Covid-19 Cases',
        )
    )
        

    fig.update_layout(
        title_text='Reported Covid-19 Cases',
        geo=dict(
            showcoastlines=True,
        ),
    )

    fig.write_html('choropleth_map.html', auto_open=True)

def csv_file():
    print('::::Reading Data from CSV File::::')
    df = pd.read_csv("case_time_series.csv")
    print(df)

def no_indx():
    print('::::Reading Data from CSV filr without index value::::')
    df = pd.read_csv('case_time_series.csv',index_col = 0)
    print(df)



def countryMenu():
    while(True): 
        print("\n========================================")
        print("Read data from file in different ways::::")
        print("-------------------------------------------")
        print("\n1.Read complete csv file:")
        print("2.Reading complete file without index::")
        print("========================================")
        
        print("\n========================================")
        print("Data visualization::::")
        print("------------------------------------------")
        print("\n3.For bar chart")
        print("4.For pie chart")
        print("5.For scatter plot")
        print("6.For line chart")
        print("========================================")
        
        print("\n========================================")
        print('Apply Data Manipulation in the record of CSV file::')
        print("-------------------------------------------------------")
        print('\n7.Sorting data as per your choice:')
        print("8.Read top and bottom records from file as per requirement")
        print("9.Make the copy of csv file:")
        print('10.Read the specific columns')
        print("0.Return to previous menu")
        print('#.To exit')
        print("========================================")


        ch =  input("\nEnter your choice:")

        if ch == '1':
            readCSV()
            continue
        
        if ch == '2':
            no_index()  
            continue

        if ch == '3':
            bar_chart()
            continue

        if ch == '4':
            pie_chart()
            continue

        if ch == '5':
            scatter_chart()
        
        if ch == '6':
            lineCh()

        if ch == '7':
            sortData()
        
        if ch == '8':
            top_bottom_records()

        if ch == '9':
            duplicate_csv()

        if ch == '10':
            specific_col()
        
        if  ch == '0':
            break

        if ch == "#":
            exit()

        else:
            print("Wrong input, Try again!")
            continue
        input("Press Enter to continue.")

def readCSV():
    print('::::Reading Data from CSV File::::')
    df = pd.read_csv("assets/covid_19_india.csv")
    print(df)

def no_index():
    print('::::Reading Data from CSV filr without index value::::')

    #read csv
    df = pd.read_csv('assets/covid_19_india.csv',index_col = 0)
    print(df)

def bar_chart():
    df = pd.read_csv("assets/covid_19_india.csv")
    
    #manipulate df
    st = df['State/UnionTerritory']
    cnf = df['Confirmed']
    rc = df['Cured']
    dth = df['Deaths']

    plt.xlabel("state")
    plt.xticks(rotation = 'vertical')

    print("Select Specific bar Chart as given below:")
    print("\npress 1 to print the data for State vs Confirmed Cases")
    print("\npress 2 to print the data for State vs Cured Cases")
    print("\npress 3 to print the data for State vs Death Cases")
    print("\npress 4 to print all the data in the form of stack bar chart")
    print("\npress 5 to print all the data in the form of multibar bar chart")
    print("\n0.Return to previous menu")

    op = int(input("Please enter your choice:"))

    if op == 1:
        plt.style.use('dark_background')
        plt.ylabel("confirmed cases")
        plt.title("state wise confirmed cases",fontsize = 25,fontstyle = "italic",color = "purple")
        
        plt.bar(st,cnf,color = 'pink',label = "Confirmed Cases")
        plt.legend()
        plt.show()

    if op == 2:
        plt.style.use('dark_background')
        plt.ylabel("cured cases")
        plt.title("state wise cured cases",fontsize = 25,fontstyle = "italic",color = "yellow")
        
        plt.bar(st,rc,color = 'green',label = "Cured Cases")
        plt.legend()
        
        plt.show()

    if op == 3:
        plt.style.use('dark_background')
        plt.ylabel("death cases")
        
        plt.title("state wise death cases",fontsize = 25,fontstyle = "italic",color = "orange")
        plt.bar(st,dth,color = 'red',label = 'Death Cases')
        plt.legend()

        plt.show()
    
    if op == 4:
        plt.style.use('dark_background')
        plt.bar(st,cnf,width = 0.2,label = 'state wise confirmed cases')
        plt.bar(st,rc,width = 0.2,label = 'state wise cured cases')
        plt.bar(st,dth,width = 0.2,label = 'state wise death cases')
        plt.title("Stack Bar Chart Of Confirmed,Cured and Death Cases")
        plt.legend()
        plt.show()

    if op == 5:
        ind = np.arange(len(st))
        width = 0.25
        
        plt.bar(ind,cnf,width,label = "state wise confirmed cases")
        plt.bar(ind+0.25,cnf,width,label = "state wise cured cases")
        plt.bar(ind+0.75,cnf,width,label = "state wise death cases")
        
        plt.legend()
        plt.show()


def pie_chart():
    #read csv
    df = pd.read_csv("assets/covid_19_india.csv")
    top = int(input("Select the number of countries you want to visualize from top:"))
    
    #manipulate dataframe
    st = df['State/UnionTerritory'].head(top)
    cnf = df['Confirmed'].head(top)
    rc = df['Cured'].head(top)
    dth = df['Deaths'].head(top)

    plt.xlabel("state")
    plt.xticks(rotation = 'vertical')

    print("Select Specific Pie Chart as given below:")
    print("press 1 to print the data for State vs Confirmed Cases")
    print("press 2 to print the data for State vs Cured Cases")
    print("press 3 to print the data for State vs Death Cases")

    ch = int(input("Enter your choice:"))

    if ch == 1:
        plt.style.use('dark_background')
        plt.title("State wise confirmed cases",fontsize = 25,fontstyle = "italic",color = "green")
        plt.pie(cnf,labels = st,autopct = "%3d%%")
        plt.show()

    if ch == 2:
        plt.style.use('dark_background')
        plt.title("State wise cured cases")
        plt.pie(rc,labels = st,autopct = "%3d%%")
        plt.show()

    if ch == 3:
        plt.style.use('dark_background')
        plt.title("State wise death cases",fontsize = 25,fontstyle = "italic",color = "green")
        plt.pie(dth,labels = st,autopct = "%3d%%")
        plt.show()
    
    else:
        print("Invalid input")

def scatter_chart():
    #read csv file
    df = pd.read_csv("assets/covid_19_india.csv")
    
    #manipulate dataframe
    st = df['State/UnionTerritory']
    cnf = df['Confirmed']
    rc = df['Cured']
    dth = df['Deaths']
    ax = plt.gca()
    
    ax.scatter(st,cnf,color = 'b',label = 'State wise confirmed cases')
    ax.scatter(st,rc,color = 'r',label = 'State wise cured cases')
    ax.scatter(st,dth,color = 'g',label = 'State wise death cases')
    
    #for dark background
    plt.style.use('dark_background')
    
    #labelling and plotting scatter plot
    plt.xlabel("state")
    plt.xticks(rotation = 'vertical')

    plt.title('complete scatter chart',fontsize = 25,fontstyle = "italic",color = "green")
    plt.legend()

    plt.show()



def lineCh():
    #read csv file
    df = pd.read_csv("assets/covid_19_india.csv")
    
    #manipulate dataframe
    st = df['State/UnionTerritory']
    cnf = df['Confirmed']
    rc = df['Cured']
    dth = df['Deaths']

    plt.xlabel("state")
    plt.xticks(rotation = 'vertical')

    print("Select Specific Line Chart as given below:")
    print("press 1 to print the data for State vs Confirmed Cases")
    print("press 2 to print the data for State vs Cured Cases")
    print("press 3 to print the data for State vs Death Cases")
    print("press 4 to merge all the data in one line chart")
    #print("press 0 Return to previous menu")

    opt =int(input("Please enter your choice:"))

    if opt == 1:
        plt.ylabel('Confirmed cases:')
        plt.title('State vs Confirmed Cases',fontsize = 25,fontstyle = "italic",color = "green")
        
        plt.plot(st,cnf,color = 'yellow',marker = "*",linestyle = 'dashed')
        plt.style.use('dark_background')
        
        plt.show()
    
    elif opt == 2:
        plt.ylabel('Cured cases:')
        plt.title('State vs Cured Cases',fontsize = 25,fontstyle = "italic",color = "green")
        
        plt.plot(st,rc,color = 'green',marker = "*",linestyle = 'dotted')
        plt.style.use('dark_background')
        
        plt.show()
    
    elif opt == 3:
        #labelling
        plt.ylabel('Death cases:')

        #giving title 
        plt.title('State vs Death Cases',fontsize = 25,fontstyle = "italic",color = "green")
        
        #plotting
        plt.plot(st,dth,color = 'pink',marker = "*",linestyle = 'dashed')

        #for dark background
        plt.style.use('dark_background')
        
        plt.show()
    
    elif opt == 4:
        #labelling
        plt.ylabel("No of cases")
        
        #plotting
        plt.plot(st,cnf,color = 'yellow',marker = "*",label = 'State wise confirmed cases')
        plt.plot(st,rc,color = 'green',marker = "*", label = 'State wise cured cases')
        plt.plot(st,dth,color = 'black',marker = "*",label = 'State wise death cases')
        
        plt.legend()
        
        #for dark background
        plt.style.use('dark_background')
        plt.show()


    else:
        print("Please enter valid input")

def sortData():
    df = pd.read_csv("assets/covid_19_india.csv")

    print("press 1 to arrange the record as per the state name")
    print("press 2 to arrange the record as per the confirmed cases")
    print("press 3 to arrange the record as per the cured cases")
    print("press 4 to arrange the record as per the death cases")

    ch = int(input("Enter your choice::"))

    if ch == 1:
        df.sort_values(['State/UnionTerritory'],inplace = True)
        print(df)
    
    elif ch == 2:
        df.sort_values(['Confirmed'],inplace = True)
        print(df)
    
    elif ch == 3:
        df.sort_values(['Cured'],inplace = True)
        print(df)

    elif ch == 3:
        df.sort_values(['Deaths'],inplace = True)
        print(df)
    
    else:
        print("Please enter valid input")

def top_bottom_records():
    #read csv
    df = pd.read_csv("assets/covid_19_india.csv")
    
    top = int(input("How many records to display from top::"))
    print("First",top,"records")
    print(df.head(top))

    bottom = int(input("How many records to display from bottom::"))
    print("First",bottom,"records")
    print(df.head(bottom))


def duplicate_csv():
    print("Duplicate the file with new file::")
    #read csv file
    df = pd.read_csv("assets/covid_19_india.csv")
    
    #converting dataframe to csv
    df.to_csv("assets/covid_19_india.csv")

    print("Data from the new file::")
    print(df)

def specific_col():
    print("Readind specific column from CSV file")

    #read csv
    df = pd.read_csv("assets/covid_19_india.csv",usecols = ['State/UnionTerritory','Cured'],index_col = 0)

    print(df)


main()
