import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64

st.title('Top Goal Scorer Stats')

st.markdown("""
This App provides the stats of different Goal Scorers from Different Leagues

Libraries Used : Pandas, Streamlit, Matplotlib

Dataset Used : [Top Football Leagues Scorers](https://www.kaggle.com/mohamedhanyyy/top-football-leagues-scorers)

""")

st.sidebar.header('User Input Features')
x = st.sidebar.selectbox('Year',list(range(2016,2021)))

#reading the csv data
df = pd.read_csv('Data.csv')

#data editing
df['League'] = df['League'].replace([ 'France Ligue 11',
       'France Ligue 20', 'France Ligue 2', 'France Ligue 12',
       'France Ligue 9', 'France Ligue 15', 'France Ligue 6',
       'France Ligue 3', 'France Ligue 16', 'France Ligue 14',
       'France Ligue 4', 'France Ligue 1', 'France Ligue 10',
       'France Ligue 7', 'France Ligue 13', 'France Ligue 8',
       'France Ligue 5', 'France Ligue 19', 'France Ligue 18',
       'France Ligue 17',],'Ligue 1')

df = df.rename(columns={"Club":"Present Club"})

# sum of the goals scored each year
x16 = df[df['Year'] == 2016]
y16 = x16['Goals'].sum()

x17 = df[df['Year'] == 2017]
y17 = x17['Goals'].sum()

x18 = df[df['Year'] == 2018]
y18 = x18['Goals'].sum()

x19 = df[df['Year'] == 2019]
y19 = x19['Goals'].sum()

x20 = df[df['Year'] == 2020]
y20 = x20['Goals'].sum()

# total goal scored by each league
ls = df[df['League'] == 'La Liga']
a1 = ls['Goals'].sum()

l1 = df[df['League'] == 'Ligue 1']
a2 = l1['Goals'].sum()

lb = df[df['League'] == 'Bundesliga']
a3 = lb['Goals'].sum()

lse = df[df['League'] == 'Serie A']
a4 = lse['Goals'].sum()

lpl = df[df['League'] == 'Premier League']
a5 = lpl['Goals'].sum()

le = df[df['League'] == 'Eredivisie']
a6 = le['Goals'].sum()

lmls = df[df['League'] == 'MLS']
a7 = lmls['Goals'].sum()

lbr = df[df['League'] == 'Campeonato Brasileiro SÃ©rie A']
a8 = lbr['Goals'].sum()

lpor = df[df['League'] == 'Primeira Liga']
a9 = lpor['Goals'].sum()

#function for top 5 scorers
def top_5(X):
	if X == 2016:
    		top_5 = x16[['League','Present Club','Player Names','Goals']].sort_values(by='Goals',ascending=False).head()

	elif X == 2017:
    		top_5 = x17[['League','Present Club','Player Names','Goals']].sort_values(by='Goals',ascending=False).head()

	elif X == 2018:
    		top_5 = x18[['League','Present Club','Player Names','Goals']].sort_values(by='Goals',ascending=False).head()

	elif X == 2019:
    		top_5 = x19[['League','Present Club','Player Names','Goals']].sort_values(by='Goals',ascending=False).head()

	else:
    		top_5 = x20[['League','Present Club','Player Names','Goals']].sort_values(by='Goals',ascending=False).head()
	
	return top_5

#matplotlib part of the bar graph
x_year =  ['2016','2017','2018','2019','2020']
y = [y16,y17,y18,y19,y20]
plt.xlabel('Seasons')
plt.ylabel('Goals scored each Year across all Leagues')
plt.bar(x_year,y,color=['r','y','g','orange','#34ebdb'])

sorted_team = sorted(df.League.unique())
selected_team = st.sidebar.multiselect('Leagues',sorted_team,sorted_team)

selected_df = df[df.League.isin(selected_team)]
selected_df = selected_df[selected_df['Year'] == x] 

#displaying shape and the dataframe according to the year selected
st.write(f'Dimension is {selected_df.shape[0]} rows and {selected_df.shape[1]} columns.')
st.dataframe(selected_df)

#top 5 scorers
top_5_scorers = top_5(x)
st.write(f'Top 5 Goal Scorers of the year {x} across all leagues')
st.dataframe(top_5_scorers)

# bargraph
st.write('Below is BarGraph Depicting the No of Goals scored in each season')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

# pie chart for total goals scored in each league
st.write('Pie chart displaying total goals scored in each league')
values = [a1,a2,a3,a4,a5,a6,a7,a8,a9]
lab = ['La Liga','Ligue 1','Bundesliga','Serie A','Premier League','Eredivisie','MLS','Campeonato Brasileiro SÃ©rie A','Primeira Liga']
plt.pie(values,labels=lab,radius=1.5,autopct='%0.2f%%')
st.pyplot()





