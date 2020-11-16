
from matplotlib.ticker import MaxNLocator
requirement = {"pandas": "python -m pip install pandas", "geopandas": "python -m pip install geopandas", "numpy": "python -m pip install numpy", "matplotlib": "python -m pip install matplotlib", "altair": "python -m pip install altair", "folium": "python -m pip install folium", "plotly": "python -m pip install plotly"}
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

try:
    import folium
except:
    missing.append("folium")

try:
    import plotly.graph_objects as go
except:
    missing.append("plotly")

#import baishali as goru
if missing != []:
    print(f'''\n\nYou are missing {len(missing)} package(s) in your system that are required to run this program.
Please execute this following command(s) in your terminal to resolve this issue.''')
    for i in missing:
        print(f"\nMissing : {i}\nCommand : {requirement[i]}")
    exit()


def main():
    while (True):
        print("************************************")
        print("\n\nWelcome to corona world!")
        print("************************************")
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

        print("\n\n1.For world map")
        print("2.For pie chart")
        print("3.For line chart")
        print("4.For scatter plot")
        print("5.For choropleth chart")
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
        
        if ch == '0':
            break

        if ch == "#":
            exit()

        else:
            print("Wrong input, Try again!")
            continue

def worldMap():
    df = pd.read_csv("assets/time_series_covid19_confirmed_global.csv")
    df.head()
    df = df.rename(columns= {"Country/Region" : "Country", "Province/State": "Province"})
    df.head()

    df['text'] = df['Country'] + " " + df["10/11/20"].astype(str)
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

    fig.write_html('first_figure.html', auto_open=True)


def pieChart():
    slices = [62, 142, 195]
    activities = ['Travel', 'Place Visit', 'Unknown']

    cols=['#4C8BE2','#00e061','#fe073a']
    exp = [0.2,0.02,0.02]
    
    plt.pie(slices,
            labels=activities, 
            textprops=dict(size=10,color='black'),
            radius=1,
            colors=cols,
            autopct='%2.2f%%',
            explode=exp,
            shadow=True,
            startangle=90)
    
    plt.title('Transmission\n\n\n\n',color='#4fb4f2',size=40)
    plt.show()

def lineChart():
    data = pd.read_csv('case_time_series.csv') 

    Y = data.iloc[61:,1].values  
    R = data.iloc[61:,3].values  
    D = data.iloc[61:,5].values   
    X = data.iloc[61:,0]  

    plt.figure(figsize=(25,8)) 
    plt.style.use('dark_background')

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

    plt.title("COVID-19 IN : Daily Confrimed\n", 
            size=50,color='#28a9ff') 

    ax.plot(X,Y, 
        color='#1F77B4', 
        marker='o', 
        linewidth=4, 
        markersize=15, 
        markeredgecolor='#035E9B')
    
    plt.show()

def scatterPlot():
    data=pd.read_csv("case_time_series.csv")
    from pandas.plotting import scatter_matrix
    plt.style.use('dark_background')
    df = pd.DataFrame(data)
    scatter_matrix(df)
    plt.show()

def choroplethPlot():

    df = pd.read_csv("assets/time_series_covid19_confirmed_global.csv")
    df = df.rename(columns= {"Country/Region" : "Country", "Province/State": "Province"})

    total_list = df.groupby('Country')['4/13/20'].sum().tolist()

    country_list = df["Country"].tolist()
    country_set = set(country_list)
    country_list = list(country_set)
    country_list.sort()

    new_df = pd.DataFrame(list(zip(country_list, total_list)), 
                    columns =['Country', 'Total_Cases'])

    colors = ["#F9F9F5", "#FAFAE6", "#FCFCCB", "#FCFCAE",  "#FCF1AE", "#FCEA7D", "#FCD97D",
            "#FCCE7D", "#FCC07D", "#FEB562", "#F9A648",  "#F98E48", "#FD8739", "#FE7519",
            "#FE5E19", "#FA520A", "#FA2B0A", "#9B1803",  "#861604", "#651104", "#570303",]


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

    fig.write_html('first_figure.html', auto_open=True)



def countryMenu():
    while(True): 
        print("*************************************")
        print("\nRead data from file in different ways::::")
        print("1.Read complete csv file:")
        print("2.Reading complete file without index::")
        print("***************************************")
        
        print("\nData visualization::::")
        print("3.For bar chart")
        print("4.For pie chart")
        print("5.For scatter plot")
        print("6.For line chart")
        print("========================================")
        
        print('\nApply Data Manipulation in the record of CSV file::')
        print('7.Sorting data as per your choice:')
        print("8.Read top and bottom records from file as per requirement")
        print("9.Make the copy of csv file:")
        print('10.Read the specific columns')
        print('#.To exit')
        print("***************************************************")


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
            file()

        if ch == '9':
            copyCSV()

        if ch == '10':
            readColumns()

        if ch == "#":
            exit()

        else:
            print("Wrong input, Try again!")
            continue

def readCSV():
    print('::::Reading Data from CSV File::::')
    df = pd.read_csv("assets/covid_19_india.csv")
    print(df)

def no_index():
    print('::::Reading Data from CSV filr without index value::::')
    df = pd.read_csv('assets/covid_19_india.csv',index_col = 0)
    print(df)

def bar_chart():
    df = pd.read_csv("assets/covid_19_india.csv")
    
    st = df['State/UnionTerritory']
    cnf = df['Confirmed']
    rc = df['Cured']
    dth = df['Deaths']

    plt.xlabel("state")
    plt.xticks(rotation = 'vertical')

    print("Select Specific bar Chart as given below:")
    print("press 1 to print the data for State vs Confirmed Cases")
    print("press 2 to print the data for State vs Cured Cases")
    print("press 3 to print the data for State vs Death Cases")
    print("press 4 to print all the data in the form of stack bar chart")
    print("press 5 to print all the data in the form of multibar bar chart")

    op = int(input("Please enter your choice:"))

    if op == 1:
        plt.ylabel("confirmed cases")
        plt.title("state wise confirmed cases")
        
        plt.bar(st,cnf,color = 'pink')
        
        plt.style.use('dark_background')
        plt.show()

    if op == 2:
        plt.ylabel("cured cases")
        plt.title("state wise cured cases")
        
        plt.bar(st,rc,color = 'green')
        plt.style.use('dark_background')
        
        plt.show()

    if op == 3:
        plt.ylabel("death cases")
        
        plt.title("state wise fth cases")
        plt.bar(st,dth,color = 'red')
        
        plt.style.use('dark_background')
        plt.show()
    
    if op == 4:
        plt.bar(st,cnf,width = 0.2,label = 'state wise confirmed cases')
        plt.bar(st,rc,width = 0.2,label = 'state wise cured cases')
        plt.bar(st,dth,width = 0.2,label = 'state wise death cases')
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
    df = pd.read_csv("assets/covid_19_india.csv")
    
    st = df['State/UnionTerritory']
    cnf = df['Confirmed']
    rc = df['Cured']
    dth = df['Deaths']

    plt.xlabel("state")
    plt.xticks(rotation = 'vertical')

    print("Select Specific Pie Chart as given below:")
    print("press 1 to print the data for State vs Confirmed Cases")
    print("press 2 to print the data for State vs Cured Cases")
    print("press 3 to print the data for State vs Death Cases")

    ch = int(input("Enter your choice:"))

    if ch == 1:
        plt.title("State wise confirmed cases")
        plt.pie(cnf,labels = st,autopct = "%3d%%")
        plt.style.use('dark_background')
        plt.show()

    if ch == 2:
        plt.title("State wise cured cases")
        plt.pie(rc,labels = st,autopct = "%3d%%")
        plt.style.use('dark_background')
        plt.show()

    if ch == 3:
        plt.title("State wise death cases")
        plt.pie(dth,labels = st,autopct = "%3d%%")
        plt.style.use('dark_background')
        plt.show()
    
    else:
        print("Invalid input")

def scatter_chart():
    df = pd.read_csv("assets/covid_19_india.csv")
    
    st = df['State/UnionTerritory']
    cnf = df['Confirmed']
    rc = df['Cured']
    dth = df['Deaths']
    ax = plt.gca()
    
    ax.scatter(st,cnf,color = 'b',label = 'State wise confirmed cases')
    ax.scatter(st,rc,color = 'r',label = 'State wise cured cases')
    ax.scatter(st,dth,color = 'g',label = 'State wise death cases')

    plt.style.use('dark_background')

    plt.xlabel("state")
    plt.xticks(rotation = 'vertical')

    plt.title('complete scatter chart')
    plt.legend()

    plt.show()



def lineCh():
    df = pd.read_csv("assets/covid_19_india.csv")
    
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
        plt.title('State vs Confirmed Cases')
        
        plt.plot(st,cnf,color = 'yellow',marker = "*",linestyle = 'dashed')
        plt.style.use('dark_background')
        
        plt.show()
    
    if opt == 2:
        plt.ylabel('Cured cases:')
        plt.title('State vs Cured Cases')
        
        plt.plot(st,rc,color = 'green',marker = "*",linestyle = 'dotted')
        plt.style.use('dark_background')
        
        plt.show()
    
    if opt == 3:
        plt.ylabel('Death cases:')
        plt.title('State vs Death Cases')
        
        plt.plot(st,dth,color = 'pink',marker = "*",linestyle = 'dashed')
        plt.style.use('dark_background')
        
        plt.show()
    
    if opt == 4:
        plt.ylabel("No of cases")
        
        plt.plot(st,cnf,color = 'yellow',marker = "*",label = 'State wise confirmed cases')
        plt.plot(st,rc,color = 'green',marker = "*", label = 'State wise cured cases')
        plt.plot(st,dth,color = 'black',marker = "*",label = 'State wise death cases')
        
        plt.legend()

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
    
    if ch == 2:
        df.sort_values(['Confirmed'],inplace = True)
        print(df)
    
    if ch == 3:
        df.sort_values(['Cured'],inplace = True)
        print(df)

    if ch == 3:
        df.sort_values(['Deaths'],inplace = True)
        print(df)
    
    else:
        print("Please enter valid input")

main()