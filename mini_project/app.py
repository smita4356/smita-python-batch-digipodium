from plotly.tools import return_figure_from_figure_or_data
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
from collections import Counter
import matplotlib.ticker as tick
import streamlit as st
from streamlit.elements.arrow import Data
import matplotlib
st.set_option('deprecation.showPyplotGlobalUse', False)
@st.cache



def load_data():
    data = pd.read_csv('vgsales.csv.zip')
    return data
st.header('Video Game Sales Analysis')

data = load_data()
st.subheader('Raw data')
st.write(data)




data= data.dropna()
data['Year'] = data['Year'].astype(int)
data["Platform" ] = data["Platform"].replace(
    ["GB", "NES", "DS", "X360", "SNES", "GBA", "3DS", "N64", "PS", "XB",
     "XOne", "PSV", "TG16", "3DO", "PCFX"],
    ["Game Boy", "Nintendo Entertainment System", "Nintendo DS", "Xbox 360",
     "Super Nintendo Entertainment System",
     "Nintendo Game Boy Advance", "Nintendo 3DS", "Nintendo 64","PlayStation",
     "Xbox","Xbox One", "PlayStation Vita", "TurboGrafx-16",
     "3DO Interactive Multiplayer", "NEC PC‑FX"])
data.loc[data['Name'] == "FIFA Soccer 13", "Genre"] = "Sports"

data.Platform.unique()
PlayStation = ['PS3', 'PS4', 'PS2', 'PlayStation', 'PSP', 'PlayStation Vita']
Nintendo = ['Wii', 'Nintendo Entertainment System', 'Game Boy','Nintendo DS', 
            'Super Nintendo Entertainment System', 'Nintendo Game Boy Advance',
            'Nintendo 3DS', 'Nintendo 64','WiiU']
Microsoft = ['Xbox', 'Xbox One', 'Xbox 360']
Other = ['PC', '2600', 'GC', 'GEN', 'DC', 'SAT', 'SCD', 'WS', 'NG', 'TurboGrafx-16', 
         '3DO Interactive Multiplayer', 'GG', 'NEC PC‑FX']

def ProductFamily (c):
  if c['Platform'] in PlayStation:
    return 'PlayStation'
  elif c['Platform'] in Nintendo:
    return 'Nintendo'
  elif c['Platform'] in Microsoft:
    return 'Microsoft'
  elif c['Platform'] in Other:
    return 'Other'
  else:
    return 'o'

data['ProductFamily'] = data.apply(ProductFamily, axis=1)



def x_fmt(tick_val, pos): # define a function to make axis values show with $ sign and follow by M(million) or B(Billion)
    if tick_val >= 1000:
        val = tick_val/1000
        return '${0:.1f}B'.format(val)
    elif tick_val > 1:
        val = int(tick_val)
        return '${:d}M'.format(val)
    else:
        return tick_val
    
def y_fmt(tick_val, pos): 
    if tick_val >= 1000:
        val = tick_val/1000
        return '${0:.1f}B'.format(val)
    elif tick_val > 1:
        val = int(tick_val)
        return '${:d}M'.format(val)
    else:
           return tick_val




#which product family generates most sALES
def pro_family_sales():
    sns.set_style("darkgrid")
    Pfamily_sale = data.groupby('ProductFamily')['Global_Sales'].sum().sort_values(ascending=False).reset_index()
    plt.figure(figsize=(16,10))
    sns.barplot(y=Pfamily_sale["ProductFamily"], x=Pfamily_sale["Global_Sales"], linewidth=1)
    plt.yticks(fontsize=22)
    plt.xticks(fontsize=22)
    plt.ylabel("Product Family", labelpad=15, fontsize=26)
    plt.xlabel("Total Sales", labelpad=15, fontsize=26)
    plt.title("Global Sales by Product Family", color='Black', fontsize=28, y=1.02)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(tick.FuncFormatter(x_fmt))



ops=['Genere','platform','publisher','region']
choice=st.selectbox('Data Analyse by',ops)
if choice==ops[0]:
    st.subheader('Most popular game genre')
    genre = Counter(data['Genre'].dropna().tolist()).most_common(10)
    genre_name = [name[0] for name in genre]
    genre_counts = [name[1] for name in genre]

    def genre_fig():
        fig,ax = plt.subplots(figsize=(15,10))
        sns.barplot(x=genre_name, y=genre_counts, ax=ax)
        plt.title('Top Ten Genre', fontsize=28, y=1.02)
        plt.yticks(fontsize=22)
        plt.xticks(fontsize=22)
        plt.xlabel('Genre',labelpad=20, fontsize=26)
        plt.ylabel('Count of Game', labelpad=20, fontsize=24)
        ticks = plt.setp(ax.get_xticklabels(), fontsize=16, rotation=360)
    fig=genre_fig()
        
    st.pyplot(fig)
    st.markdown('Conclusion::')
    st.text('''1.Action games were one of the most popular genres.
    2.Action genre has over 3000 games across multiple platforms''')

    
    game_genres=['action','sport','misc','racing']
    choice=st.selectbox('select a Genre',game_genres)
    if choice==game_genres[0]:
        
        def top_action():
            Sports=data[data.Genre == 'Sports']
            Actions=data[data.Genre == "Action"]
            topsales=Actions.groupby(['Name'])['Global_Sales'].sum().sort_values(ascending = False).reset_index().head(10)
            plt.figure(figsize = (16,10))
            sns.barplot(y=topsales["Name"], x=topsales["Global_Sales"], linewidth=1)
            plt.yticks(fontsize=24)
            plt.xticks(fontsize=24)
            plt.ylabel("Game Name", labelpad=15, fontsize=28)
            plt.xlabel("Total Sales", labelpad=15, fontsize=28)
            plt.title("Global Sales in U.S. Dollars of Top Selling Action Games", color='Black', fontsize=30, y=1.02)
            ax = plt.gca()
            ax.xaxis.set_major_formatter(tick.FuncFormatter(x_fmt))
        topaction=top_action()
        st.pyplot(topaction)
        st.markdown('Conclusion::')
        st.text('1.Wii Sports,Wii Sports Resort, Wii Fit ,and Wii Fit Plus are amount the top global sales in the sports')
    
    if choice==game_genres[1]:
        def top_sports():
            Sports=data[data.Genre=='Sports']
            topsales=Sports.groupby(['Name'])['Global_Sales'].sum().sort_values(ascending = False).reset_index().head(10)
            plt.figure(figsize = (16,10))
            sns.barplot(y=topsales["Name"], x=topsales["Global_Sales"], linewidth=1)
            plt.yticks(fontsize=24)
            plt.xticks(fontsize=24)
            plt.ylabel("Game Name", labelpad=15, fontsize=28)
            plt.xlabel("Total Sales", labelpad=15, fontsize=28)
            plt.title("Global Sales in U.S. Dollars of Top Selling Sports Games", color='Black', fontsize=30, y=1.02)
            ax = plt.gca()
            ax.xaxis.set_major_formatter(tick.FuncFormatter(x_fmt))
        topsport=top_sports()
        st.pyplot(topsport)
        st.markdown('Conclusion::')  
        st.text('Wii Sports,Wii Sports Resort, Wii Fit ,and Wii Fit Plus are amount the top global sales in the sport genre. And all these four games are part of Nintindo Family.')
    if choice==game_genres[2]:
        def top_misc():
            Misc=data[data.Genre=='Misc']
            topsales=Misc.groupby(['Name'])['Global_Sales'].sum().sort_values(ascending = False).reset_index().head(10)
            plt.figure(figsize = (16,10))
            sns.barplot(y=topsales["Name"], x=topsales["Global_Sales"], linewidth=1)
            plt.yticks(fontsize=24)
            plt.xticks(fontsize=24)
            plt.ylabel("Game Name", labelpad=15, fontsize=28)
            plt.xlabel("Total Sales", labelpad=15, fontsize=28)
            plt.title("Global Sales in U.S. Dollars of Top Selling Misc Games", color='Black', fontsize=30, y=1.02)
            ax = plt.gca()
            ax.xaxis.set_major_formatter(tick.FuncFormatter(x_fmt))
        topmisc=top_misc()
        st.pyplot(topmisc)
        st.markdown('Conclusion::')  
        st.text('Wii play is the top selling misc game.. and minecraft has second position.')

    if choice==game_genres[3]:
        def top_racing():
            Racing=data[data.Genre=='Racing']
            topsales=Racing.groupby(['Name'])['Global_Sales'].sum().sort_values(ascending = False).reset_index().head(10)
            plt.figure(figsize = (16,10))
            sns.barplot(y=topsales["Name"], x=topsales["Global_Sales"], linewidth=1)
            plt.yticks(fontsize=24)
            plt.xticks(fontsize=24)
            plt.ylabel("Game Name", labelpad=15, fontsize=28)
            plt.xlabel("Total Sales", labelpad=15, fontsize=28)
            plt.title("Global Sales in U.S. Dollars of Top Selling Racing Games", color='Black', fontsize=30, y=1.02)
            ax = plt.gca()
            ax.xaxis.set_major_formatter(tick.FuncFormatter(x_fmt))
        topracing=top_racing()
        st.pyplot(topracing)
        st.markdown('Conclusion::')  
        st.text('Mario Kart Wii  is the top selling misc game.. and Mario Kart DS has second position.')    
        



if choice==ops[1]:
    def platform():
        sns.set_style("darkgrid")
        num_games=data.groupby('Platform').size().sort_values(ascending=False).reset_index()[:11]
        num_games.columns=['Platform', 'Count']
        plt.figure(figsize=(16,10))
        sns.barplot(y=num_games["Platform"], x=num_games["Count"], linewidth=1)
        plt.yticks(fontsize=24)
        plt.xticks(fontsize=24)
        plt.ylabel("Platform", labelpad=16, fontsize=28)
        plt.xlabel("Count", labelpad=16, fontsize=28)
        plt.grid(True)
        plt.title("Platform With Most Number Of Video Games", color='Black', fontsize=28, y=1.02)
   
    platform=platform()
    st.pyplot(platform)
    st.markdown('Conclusion:')
    st.text('''1.Nintendo DS has the most number of video games selection in its platform, followed by PS2.
    2.PS3, Wii , and Xbox 360 has only about 50% of the games selection compared to Nintendo DS and PS2.'''
    )


    st.subheader('platform earned the highest::--')
    #highest earned platform
    def plat_earn():
        platf = data.groupby(by = ['Platform'])['Global_Sales'].sum()
        platf = platf.reset_index()
        platf = platf.sort_values(by = ['Global_Sales'])

        sns.barplot(x="Platform", y="Global_Sales", data = platf)
        plt.xticks(rotation=90)
    earnedplat=plat_earn()
    st.pyplot(earnedplat)
    st.markdown('conclusion::--')
    st.text('Looks like PS2 has grossed highest.')


if choice==ops[2]:
    #top ten publisher
    def top_publisher():
        publish = data.groupby(by=['Publisher'])['Year'].count().sort_values(ascending=False).head(10)
        pblish = pd.DataFrame(publish).reset_index()
        sns.countplot(x="Publisher", data = data, order = data.groupby(by=['Publisher'])['Year'].count().sort_values(ascending=False).iloc[:10].index)
        plt.xticks(rotation=90)
    toppublisher=top_publisher()
    st.pyplot(toppublisher)
    st.markdown('conclusion::')
    st.text('EA has been given the most games, where as Activision has earned most name from its Call Of Duty Series.')
if choice==ops[3]:
    
    def byregion():
        df1=data.rename(index=str, columns={"NA_Sales": "North America", "EU_Sales": "Europe",
                                  "JP_Sales": "Japan","Other_Sales": "Other"})
        df1=df1.loc[:, 'Name': 'Global_Sales'].sort_values(by="Global_Sales", ascending=True).tail(10)
        sns.set_style("darkgrid")
        ax=df1.set_index('Name')[['North America', 'Europe', 'Japan', 'Other']].plot(kind='barh',
        figsize=(18, 12), stacked=True)
        plt.title("Top 10 Most Sales Game by Regions", fontsize=28, y=1.01)
        plt.xlabel("Total Sales in U.S. Dollars", fontsize=26, labelpad=15)
        plt.ylabel("Name", fontsize=26, labelpad=15)
        plt.yticks(fontsize=24)
        plt.xticks(fontsize=24)
        ax = plt.gca()
        ax.xaxis.set_major_formatter(tick.FuncFormatter(x_fmt))
        plt.legend(fontsize=22)

    byregion=byregion()
    st.pyplot(byregion)
    st.markdown('conclusion::')
    st.text('Looks like NA has the most sales.')

before2011=data[(data["Year"]>=2005) & (data["Year"]<2011)].groupby("ProductFamily")['Global_Sales'].sum().sort_values(ascending = False).reset_index()
after2011=data[(data["Year"]>=2011) & (data["Year"]<2017)].groupby("ProductFamily")['Global_Sales'].sum().sort_values(ascending = False).reset_index()
combined=pd.merge(before2011, after2011, on="ProductFamily")
combined=combined.rename(index=str, columns={"Global_Sales_x": "2005-2010 Sales", "Global_Sales_y": "2011-2016 Sales"})
def global_span():
    sns.set_style("darkgrid")
    combined.set_index('ProductFamily')[['2005-2010 Sales', '2011-2016 Sales']].plot(kind='bar', 
                                                                        figsize=(18, 12))
    plt.xticks(rotation=0)
    plt.title("Comparison of Global Sales for ProductFamily in Two Time Spans", fontsize=26, y=1.01)
    plt.xlabel("Product Family", fontsize=26, labelpad=15)
    plt.ylabel("Total Sales", fontsize=26, labelpad=15)
    plt.yticks(fontsize = 24 )
    plt.xticks(fontsize = 24 )
    ax = plt.gca()
    ax.yaxis.set_major_formatter(tick.FuncFormatter(y_fmt))
    plt.legend(fontsize=20)
globalsales=global_span()
st.pyplot(globalsales)



df1=data.rename(index=str, columns={"NA_Sales": "North America", "EU_Sales": "Europe",
                                  "JP_Sales": "Japan","Other_Sales": "Other"})
df1=df1.loc[:, 'Name': 'Global_Sales'].sort_values(by="Global_Sales", ascending=True).tail(10)

#sales since 1980
def sales_since():
    SaleByYear=data.groupby('Year')['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales',
                                    'Global_Sales'].sum().reset_index()
    SaleByYear=SaleByYear[SaleByYear.Year<2017]
    SaleByYear=SaleByYear.rename(index=str, columns={"NA_Sales": "North America",   
                    "EU_Sales": "Europe", "JP_Sales":"Japan", "Other_Sales":"Other"})
    SaleByYear.set_index('Year')[['North America', 'Europe', 'Japan', 'Other']].plot(style='-o', 
        color=('steelblue', "seagreen", "firebrick", "darkorange"), figsize=(16, 14), linewidth=2)
    plt.title("Sales By Year in U.S. Dollars", fontsize=28, y=1.02)
    plt.yticks(fontsize = 24 )
    plt.xticks(fontsize = 24 )
    plt.xlabel("Year", fontsize=26, labelpad=12)
    plt.ylabel("Sales", fontsize=26, labelpad=15)
    plt.legend(fontsize=20)
    ax = plt.gca()
    ax.yaxis.set_major_formatter(tick.FuncFormatter(y_fmt))
salesince=sales_since()
st.pyplot(salesince)
st.markdown('Conclusion::')
st.text(''' 1.We can see that sales have been continually increasing. There was a peak in 2008, which was around the start of the recession, which affected the video game industry as severely as many other industries.
2.
North America has been the leader in video game sales for the most part,however, Japan looks like it was able to surpass North America briefly between 1992 and 1996.''')


