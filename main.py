import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import folium  

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
        print("5.For bubble chart")
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
            bubbleChart()
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
    df = pd.DataFrame(data)
    scatter_matrix(df)
    plt.show()

def bubbleChart():
    df_conf = pd.read_csv("/home/baishaliroy/Desktop/project/COVID19_Proj_Python/assets/time_series_covid19_confirmed_global.csv")
    cols_to_select = list(df_conf.columns[0:4]) + list(df_conf.columns[-6:])
    df_conf.loc[(df_conf['Country/Region'] == "Netherlands"), cols_to_select]

    cols_to_keep = list(df_conf.columns[0:4]) + list(df_conf.columns[-1:])
    df_conf_last = df_conf[cols_to_keep]
    df_conf_last.columns.values[-1] = "Confirmed"

    df_conf_last.head()

    df_conf_last['Confirmed'] = df_conf_last['Confirmed']

    map1 = folium.Map(location=[30.6, 114], zoom_start=3) #US=[39,-98] Europe =[45, 5]

    for i in range(0,len(df_conf_last)):
        folium.Circle(
        location=[df_conf_last.iloc[i]['Lat'], df_conf_last.iloc[i]['Long']],
        tooltip = "Country: "+df_conf_last.iloc[i]['Country/Region']+"<br>Province/State: "+str(df_conf_last.iloc[i]['Province/State'])+"<br>Confirmed cases: "+str(df_conf_last.iloc[i]['Confirmed'].astype(int)),
        radius=df_conf_last.iloc[i]['Confirmed']*5,
        color='crimson',
        fill=True,
        fill_color='crimson'
        ).add_to(map1)

    map1
    plt.show()
main()
