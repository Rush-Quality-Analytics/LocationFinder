import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
#import dash_table
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import warnings
import sys
#import re
#import numpy as np
#import urllib
#from urllib.request import urlopen
import json
from geopy.geocoders import Nominatim
import os
#import base64
#import io
#import ast

geolocator = Nominatim(user_agent="my_user_agent")

#########################################################################################
################################# CONFIG APP ############################################
#########################################################################################


warnings.filterwarnings('ignore')

px.set_mapbox_access_token('pk.eyJ1Ijoia2xvY2V5IiwiYSI6ImNrYm9uaWhoYjI0ZDcycW56ZWExODRmYzcifQ.Mb27BYst186G4r5fjju6Pw')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.config.suppress_callback_exceptions = True


#########################################################################################
################################# LOAD DATA #############################################
#########################################################################################

ls = []
with open('./data/geojson/Boundaries - Community Areas (current).geojson') as f:
    com_area_geo = json.load(f)
for feature in com_area_geo["features"]:
    com_area = feature['properties']['community']
    feature['id'] = com_area
    ls.append(com_area)


js = com_area_geo
df = pd.DataFrame(columns=['community'])
df['community'] = ls
clrs = [0] * len(ls)
    
for i, val in enumerate(ls):
    if val == 'AUSTIN':
        clrs[i] = 10
        
df['num'] = clrs
    
#########################################################################################
################# DASH APP CONTROL FUNCTIONS ############################################
#########################################################################################


def generate_control_card1():
    
    """
    :return: A Div containing controls for graphs.
    """
    
    return html.Div(
        id="control-card1",
        children=[
            html.B("Enter an address and press Return", style={'textAlign': 'left', 'color': '#3385ff'}),
            html.Br(),
            dcc.Input(
                id="address1",
                type="text",
                debounce = True,
                value='545 N Pine Ave, Chicago, IL 60644',
                placeholder="Street address",
                style={
                    'textAlign': 'left',
                    'width': '100%',
                    },
                ),
            
        ],
    )

def description_card1():
    """
    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card1",
        children=[
            html.H3("Location finder", 
                    style={'textAlign': 'left', 'color': '#3385ff'}),
            html.P("This tool allows the user to type in a street address and to know which" +
                   " Chicago community area (e.g., Austin) the address is located within.",
                    style={
            'textAlign': 'left',
            }),           
        ],
    )

#########################################################################################
################################# DASH APP LAYOUT #######################################
#########################################################################################

app.layout = html.Div([
    
        dcc.Tabs([
            
            dcc.Tab(label='Find a location', children=[
        
            html.Div(
                    id='df1', 
                    style={'display': 'none'}
                ),
            
            html.Div(
                    style={'background-color': '#f9f9f9'},
                    id="banner12",
                    className="banner",
                    children=[html.Img(src=app.get_asset_url("RUSH_full_color.jpg"), 
                                       style={'textAlign': 'left'}),
                              ],
                ),
            
            
            
            html.Div(
                    id="left-column1",
                    className="five columns",
                    children=[description_card1(), generate_control_card1()],
                    style={'width': '24%', 'display': 'inline-block',
                                         'border-radius': '15px',
                                         'box-shadow': '1px 1px 1px grey',
                                         'background-color': '#f0f0f0',
                                         'padding': '10px',
                                         'margin-bottom': '10px',
                    },
                ),
            
            html.Div(
                    id="right-column1",
                    className="eight columns",
                    children=[
                        
                        html.Div(
                            id="map1",
                            children=[
                                dcc.Graph(id="map_plot1"),
                                
                            ],
                            style={'width': '100%', 'display': 'inline-block',
                                         'border-radius': '15px',
                                         'box-shadow': '1px 1px 1px grey',
                                         'background-color': '#f0f0f0',
                                         'padding': '10px',
                                         'margin-bottom': '20px',
                                    },
                        ),
                        ]),
            
            
                ]),
        ]),
])




#########################################################################################
############################    Call backs   ############################################
#########################################################################################


############################    Update Tab1   ###########################################


@app.callback( # Update available sub_categories
    Output("map_plot1", "figure"),
    [
     Input("address1", "value"),
     ],
    )
def update_output1(v1):
    
    if v1 == None:
        lat = 41.8902467 
        lon = -87.76294496956751
    
    try:
        loc = geolocator.geocode(v1)
        lat = loc.latitude
        lon = loc.longitude
    except:
        lat = 41.8902467 
        lon = -87.76294496956751
        v1 = None
    
    figure = px.choropleth_mapbox(df, 
                                  geojson = js, 
                                  locations = 'community', 
                                  color = 'num',
                                  color_continuous_scale = "Blues",
                                  mapbox_style="carto-positron",
                                  zoom=11.7, center = {"lat": lat, "lon": lon},
                                  opacity=0.6,
                                  #hover_data=[lab, 'No. of times greater than average'],
                                  )
    
    figure.update_layout(
        autosize=True,
        coloraxis_showscale=False,
        showlegend=False,
        hovermode='closest',
        mapbox_style="light",
        height=500, 
        margin={"r":0,"t":0,"l":0,"b":0},
        )
    
    if v1 == None or v1 == '':
        pass
    else:
        tdf = pd.DataFrame(columns=['Latitude', 'Longitude'])
        tdf['Latitude'] = [lat]
        tdf['Longitude'] = [lon]
        
        figure.add_trace(go.Scattermapbox(
            lon = tdf['Longitude'],
            lat = tdf['Latitude'],
            text = v1,
            
            marker = dict(
                size = 20,
                color = '#ff0066',
                opacity = 0.9,
                #line=dict(
                #          width=2,
                #          color='DarkSlateGrey')
                ),
            ),
            )
    
    return figure



#########################################################################################
############################# Run the server ############################################
#########################################################################################


if __name__ == "__main__":
    app.run_server(host='127.0.0.1', port=8050, debug=True)