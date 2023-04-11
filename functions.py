import plotly.express as px
import os
from dotenv import load_dotenv
import plotly.graph_objects as go

import streamlit as st

load_dotenv()
def visualize_scatter(df, style):
    access_token = os.environ['MAPBOX_ACCESS_TOKEN']

    fig = px.scatter_mapbox(df, lon="latitude", lat="longitude", zoom=10.8,  hover_name='Адрес',opacity=1,
                            color_continuous_scale="Inferno", hover_data={'Год постройки':True,'Этажей':True,'Квартир':True,'latitude':False,'longitude':False,'Магазинов по близости':True})

    fig.update_layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=access_token,
            bearing=1,
            center=dict(
                lat=59.94,
                lon=30.32
            ),
            pitch=0,
            zoom=10.8
        ),
    )
    fig.update_layout(mapbox_style=style)
    fig.update_layout(height=1400)
    fig.update_layout(
        margin=dict(pad=16, l=0, r=0),
    )
    fig.update_layout(legend=dict(x=0, y=1))
    return fig



def visualize_shop(df, style, color):
    access_token = os.environ['MAPBOX_ACCESS_TOKEN']
    fig = px.scatter_mapbox(df, lon="latitude", lat="longitude", zoom=10.8,  hover_name='Адрес',opacity=1, color=color,color_discrete_sequence=['#1AE5F6', '#1A45F6'],
                            color_continuous_scale="Inferno", hover_data={'Год постройки':True,'Этажей':True,'Квартир':True,'latitude':False,'longitude':False,'Магазинов по близости':True})

    fig.update_layout(
        autosize=True,
        hovermode='closest',
        showlegend=False,
        mapbox=dict(
            accesstoken=access_token,
            bearing=1,
            center=dict(
                lat=59.94,
                lon=30.32
            ),
            pitch=0,
            zoom=10.8
        ),
    )
    fig.update_layout(mapbox_style=style)
    fig.update_layout(height=1200)
    fig.update_layout(
        margin=dict(pad=16, l=0, r=0),
    )
    # Create a custom trace with the desired text and color

    return fig

def visualize_vkuster(df, style, color):
    access_token = os.environ['MAPBOX_ACCESS_TOKEN']
    fig = px.scatter_mapbox(df, lon="latitude", lat="longitude", zoom=10.8,  hover_name='Адрес',opacity=1, color=color,color_discrete_sequence=['#1A45F6','#1AE5F6'],
                            color_continuous_scale="Inferno", hover_data={'Год постройки':True,'Этажей':True,'Квартир':True,'latitude':False,'longitude':False,'Магазинов по близости':True})

    fig.update_layout(
        autosize=True,
        hovermode='closest',
        showlegend=False,
        mapbox=dict(
            accesstoken=access_token,
            bearing=1,
            center=dict(
                lat=59.94,
                lon=30.32
            ),
            pitch=0,
            zoom=10.8
        ),
    )
    fig.update_layout(mapbox_style=style)
    fig.update_layout(height=1200)
    fig.update_layout(
        margin=dict(pad=16, l=0, r=0),
    )

    return fig

def create_metrics(shop_name, df_houses, df_shop):
    col1, col2, col3 = st.columns(3)
    c1 = col1.metric("Магазинов", len(df_shop[df_shop['shop'] == str(shop_name)]), f"{int(round(len(df_shop[df_shop['shop'] == str(shop_name)])/len(df_shop),2)*100)}% от общего числа")
    c2 = col2.metric("Охват квартир", df_houses[df_houses[str(shop_name)] == True]['Квартир'].sum(), f"{int(round((df_houses[df_houses[str(shop_name)] == True]['Квартир'].sum())/df_houses['Квартир'].sum(),2)*100)}%")
    c3 = col3.metric("Охват ближайших домов", len(df_houses[df_houses[str(shop_name)] == True]), f"{int(round(len(df_houses[df_houses[str(shop_name)] == True])/len(df_houses),2)*100)}%")
    return c1,c2,c3