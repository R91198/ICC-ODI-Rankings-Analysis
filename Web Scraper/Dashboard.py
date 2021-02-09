import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
import pydeck as pdk
import plotly
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt

#Title for the dashboard
st.title('ICC ODI Rankings (last 5 years)')
st.markdown('This dashboard will be comprising of some  interesting analysis of cricket players in ODI '
            'format in all three departments i.e. Batsmen, Bowlers and All-rounders '
            'for the last 5 years ranging between January-2016 to December-2020.')

#Header
st.header('Dataset')

data_url = ('All_ODI_Rankings.csv')
@st.cache
def load_data():
    data = pd.read_csv(data_url)
    data.set_index('Date', inplace=True)
    data = data.drop('Unnamed: 0', axis=1)
    return data

df = load_data()

# Show dataset on streamlit
#st.write(df)

#Sidebar
st.sidebar.title('Selector')
st.sidebar.markdown('Select the options accordingly')

# Get the players selected in the selectbox
if st.checkbox('Show dataset'):
    select_type = st.sidebar.radio("Player Type", ('Batsmen', 'Bowler', 'All-rounder'))
    st.markdown('Select the data accordingly with Player type.')
    if select_type == 'Batsmen':
        st.write(df[df.Type == 'Batsmen'])
    elif select_type == 'Bowler':
        st.write(df[df.Type == 'Bowler'])
    elif select_type == 'All-rounder':
        st.write(df[df.Type == 'All-rounder'])

# Players by their respective countries included in the rankings
st.sidebar.markdown("### Visualizations of Top Rank players by Country")
select_team = st.sidebar.selectbox('Select Country', df.Team.unique())

fig = go.Figure()
if select_team == 'IND':
    ind_players = df[(df.Team == 'IND')][['Player Names', 'Rating', 'Type']].\
    sort_values(by = 'Rating', ascending = False).drop_duplicates()
    fig.add_trace(go.Bar(x=ind_players['Player Names'], y=ind_players.Rating))
    fig.update_layout(xaxis_title = 'Players', yaxis_title = 'Ratings')

elif select_team == 'PAK':
    pak_players = df[(df.Team == 'PAK')][['Player Names', 'Rating', 'Type']]. \
        sort_values(by='Rating', ascending=False).drop_duplicates()
    fig.add_trace(go.Bar(x=pak_players['Player Names'], y=pak_players.Rating))
    fig.update_layout(xaxis_title='Players', yaxis_title='Ratings')

elif select_team == 'NZ':
    nz_players = df[(df.Team == 'NZ')][['Player Names', 'Rating', 'Type']]. \
        sort_values(by='Rating', ascending=False).drop_duplicates()
    fig.add_trace(go.Bar(x=nz_players['Player Names'], y=nz_players.Rating,))
    fig.update_layout(xaxis_title='Players', yaxis_title='Ratings')

elif select_team == 'SA':
    sa_players = df[(df.Team == 'SA')][['Player Names', 'Rating', 'Type']]. \
        sort_values(by='Rating', ascending=False).drop_duplicates()
    fig.add_trace(go.Bar(x=sa_players['Player Names'], y=sa_players.Rating))
    fig.update_layout(xaxis_title='Players', yaxis_title='Ratings')

elif select_team == 'ENG':
    eng_players = df[(df.Team == 'ENG')][['Player Names', 'Rating', 'Type']]. \
        sort_values(by='Rating', ascending=False).drop_duplicates()
    fig.add_trace(go.Bar(x=eng_players['Player Names'], y=eng_players.Rating))
    fig.update_layout(xaxis_title='Players', yaxis_title='Ratings')

elif select_team == 'WI':
    wi_players = df[(df.Team == 'WI')][['Player Names', 'Rating', 'Type']]. \
        sort_values(by='Rating', ascending=False).drop_duplicates()
    fig.add_trace(go.Bar(x=wi_players['Player Names'], y=wi_players.Rating))
    fig.update_layout(xaxis_title='Players', yaxis_title='Ratings')

elif select_team == 'AUS':
    aus_players = df[(df.Team == 'AUS')][['Player Names', 'Rating', 'Type']]. \
        sort_values(by='Rating', ascending=False).drop_duplicates()
    fig.add_trace(go.Bar(x=aus_players['Player Names'], y=aus_players.Rating))
    fig.update_layout(xaxis_title='Players', yaxis_title='Ratings')

elif select_team == 'BAN':
    ban_players = df[(df.Team == 'BAN')][['Player Names', 'Rating', 'Type']]. \
        sort_values(by='Rating', ascending=False).drop_duplicates()
    fig.add_trace(go.Bar(x=ban_players['Player Names'], y=ban_players.Rating))
    fig.update_layout(xaxis_title='Players', yaxis_title='Ratings')

elif select_team == 'IRE':
    ire_players = df[(df.Team == 'IRE')][['Player Names', 'Rating', 'Type']]. \
        sort_values(by='Rating', ascending=False).drop_duplicates()
    fig.add_trace(go.Bar(x=ire_players['Player Names'], y=ire_players.Rating))
    fig.update_layout(xaxis_title='Players', yaxis_title='Ratings')

elif select_team == 'SL':
    sl_players = df[(df.Team == 'SL')][['Player Names', 'Rating', 'Type']]. \
        sort_values(by='Rating', ascending=False).drop_duplicates()
    fig.add_trace(go.Bar(x=sl_players['Player Names'], y=sl_players.Rating))
    fig.update_layout(xaxis_title='Players', yaxis_title='Ratings')

elif select_team == 'SCO':
    sco_players = df[(df.Team == 'SCO')][['Player Names', 'Rating', 'Type']]. \
        sort_values(by='Rating', ascending=False).drop_duplicates()
    fig.add_trace(go.Bar(x=sco_players['Player Names'], y=sco_players.Rating))
    fig.update_layout(xaxis_title='Players', yaxis_title='Ratings')

elif select_team == 'OMA':
    oma_players = df[(df.Team == 'OMA')][['Player Names', 'Rating', 'Type']]. \
        sort_values(by='Rating', ascending=False).drop_duplicates()
    fig.add_trace(go.Bar(x=oma_players['Player Names'], y=oma_players.Rating))
    fig.update_layout(xaxis_title='Players', yaxis_title='Ratings')

elif select_team == 'ZIM':
    zim_players = df[(df.Team == 'ZIM')][['Player Names', 'Rating', 'Type']]. \
        sort_values(by='Rating', ascending=False).drop_duplicates()
    fig.add_trace(go.Bar(x=zim_players['Player Names'], y=zim_players.Rating))
    fig.update_layout(xaxis_title='Players', yaxis_title='Ratings')

elif select_team == 'AFG':
    afg_players = df[(df.Team == 'AFG')][['Player Names', 'Rating', 'Type']]. \
        sort_values(by='Rating', ascending=False).drop_duplicates()
    fig.add_trace(go.Bar(x=afg_players['Player Names'], y=afg_players.Rating))
    fig.update_layout(xaxis_title='Players', yaxis_title='Ratings')

elif select_team == 'UAE':
    uae_players = df[(df.Team == 'UAE')][['Player Names', 'Rating', 'Type']]. \
        sort_values(by='Rating', ascending=False).drop_duplicates()
    fig.add_trace(go.Bar(x=uae_players['Player Names'], y=uae_players.Rating))
    fig.update_layout(xaxis_title='Players', yaxis_title='Ratings')

elif select_team == 'PNG':
    png_players = df[(df.Team == 'PNG')][['Player Names', 'Rating', 'Type']]. \
        sort_values(by='Rating', ascending=False).drop_duplicates()
    fig.add_trace(go.Bar(x=png_players['Player Names'], y=png_players.Rating))
    fig.update_layout(xaxis_title='Players', yaxis_title='Ratings')

st.plotly_chart(fig, use_container_width=True)

#Visualization by Country
st.markdown('Australia is having the maximum number of players that are '
            'within the top 100 rankings(approx. 12%) for the past 5 years')

df['Team'].value_counts().plot(kind='bar')
plt.xlabel('Teams')
plt.ylabel('Count')
plt.show()
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)







