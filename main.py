
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


    fig = go.Figure(data=go.Choropleth(
        locationmode = "country names",
        locations = new_df['Country'],
        z = new_df['Total_Cases'],
        text = new_df['Total_Cases'],
        colorscale = colors,
        autocolorscale=False,
        reversescale=False,
        colorbar_title = 'Reported Covid-19 Cases',
    ))
        

    fig.update_layout(
        title_text='Reported Covid-19 Cases',
        geo=dict(
            showcoastlines=True,
        ),
    )

    fig.write_html('first_figure.html', auto_open=True)

'''

def countryMenu():
    while(True):               
        print("1..For bar chart")
        print("2..For pie chart")
        print("3..For scatter plot")
        print("4..Return to previous menu")
        print("#.To exit")

        ch =  input("\nEnter your choice:")

        if ch == '1':
            barGraph()
            continue
        
        if ch == '2':
            pieChart()  
            continue

        if ch == '3':
            lineChart()
            continue

        if ch == '4':
            choroplethPlot()
            continue

        if ch == "#":
            exit()

        else:
            print("Wrong input, Try again!")
            continue

def lineChart():
    data = pd.read_csv('assets/covid_19_india.csv') 

    Y = data.iloc[61:,1].values 
    R = data.iloc[61:,3].values 
    D = data.iloc[61:,5].values 
    X = data.iloc[61:,0] 

    plt.figure(figsize=(25,8)) 

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
			size='25', 
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

def pieChart():
    df = pd.read_csv('assets/covid_19_india.csv')

    country_data = df["State/UnionTerritory"]
    confirmed_data = df["ConfirmedIndianNational"]  
    
    plt.pie(confirmed_data, labels=country_data, shadow=True, startangle=140)
    
    plt.title("Confirmed cases of corona virus in India")
    plt.show()
'''
main()
