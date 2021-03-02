#import dash
import dash_core_components as dcc
import dash_html_components as html
#from dash.dependencies import Input, Output, State
#import dash_table
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.colors import n_colors
#import warnings
#import sys
#import re
import numpy as np
#from scipy import stats
#import statsmodels.api as sm
#import urllib
#from urllib.request import urlopen
#import json

#import base64
#import io
#import json
#import ast
#import time

#import numpy.polynomial.polynomial as poly
#from statsmodels.regression.linear_model import OLS
#from statsmodels.tools import add_constant


def description_card1():
    """
    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card1",
        children=[
            html.H3("Predicting crimes in Chicago", style={'textAlign': 'left', 'color': '#3385ff'}),
            html.P("This tool uses over 7.2 million crimes committed from 2001 to present. " +
                   " It allows the user to build profiles for specific crimes. It then displays " +
                   " the chance of that crime profile happening across Chicago. " +
                   " The app tests its own accuracy by predicting where crimes" +
                   " fitting the profile have occurred in 2020 and 2021.",
                    style={
            'textAlign': 'left',
            }),
            html.P("This tool crunches a lot of data to find its predictions. Updating takes a few seconds.",
                    style={
            'textAlign': 'left',
            }),
           
        ],
    )

def description_card12():
    """
    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card12",
        children=[
            html.H3("Examining crimes in Chicago throughout 2020 and 2021", 
                    style={'textAlign': 'left', 'color': '#3385ff'}),
            html.P("This tool allows users to examine crimes committed in Chicago from " + 
                   "Jan 1st 2020 to present.",
                    style={
            'textAlign': 'left',
            }),
            html.P("This tool crunches a lot of data. Updating takes a few seconds.",
                    style={
            'textAlign': 'left',
            }),
           
        ],
    )


def description_card2():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card2",
        children=[
            html.H5("Comparisons between Loshiko, City of Chicago, and Neighborhood Scout", style={
            'textAlign': 'left',
            }),
            html.H6('Our measure of app quality', style={'textAlign': 'left', 'color': '#3385ff'}),
            dcc.Markdown('''
                         We award a point for whether an app satisfies each of 10 criteria.
                         These criteria do not include features that all apps have.
                         For example, if each app provides a map, then providing a map
                         is not a useful criterion for comparison. An app's score can range
                         between 0 and 10.
                         '''),
            #html.Br(),
        ],
    )



def comparison_table():
    
    cr = ['The app uses data from the current year',
          'The app actually maps crimes',
          'The app allows users to filter crime data',
          'The app provides useful statistics',
          'The app makes predictions',
          'The map includes useful hover-over information',
          'The app provides trends across time',
          'The app allows users to download data',
          'The app is easy to use, not complicated or cumbersome',
          'The app provides text summaries of data insights']
    
    
    #colors = n_colors('rgb(255, 200, 200)', 'rgb(200, 0, 0)', 2, colortype='rgb')
    
    lo  = ['<b>Yes</b>', '<b>Yes</b>', '<b>Yes</b>', '<b>Yes</b>', '<b>Yes</b>', 
           '<b>Yes</b>', '<b>No</b>', '<b>No</b>', '<b>Yes</b>', '<b>Yes</b>']
    lo_clrs = []
    for l in lo:
        if l == '<b>Yes</b>':
            lo_clrs.append('#9ae59a')
        else:
            lo_clrs.append('#ffb3b3')
    
    
    ch  = ['<b>Yes</b>', '<b>Yes</b>', '<b>Yes</b>', '<b>No</b>', '<b>No</b>', 
           '<b>No</b>', '<b>No</b>', '<b>Yes</b>', '<b>No</b>', '<b>No</b>']
    ch_clrs = []
    for l in ch:
        if l == '<b>Yes</b>':
            ch_clrs.append('#9ae59a')
        else:
            ch_clrs.append('#ffb3b3')
            
            
    ns  = ['<b>No</b>', '<b>No</b>', '<b>No</b>', '<b>Yes</b>', '<b>Yes</b>', 
           '<b>No</b>', '<b>No</b>', '<b>No</b>', '<b>No</b>', '<b>Yes</b>']
    ns_clrs = []
    for l in ns:
        if l == '<b>Yes</b>':
            ns_clrs.append('#9ae59a')
        else:
            ns_clrs.append('#ffb3b3')
            
    
    
    figure = go.Figure(data=[go.Table(
        
      columnwidth = [80,40,40,40],
      header=dict(
        values=['<b>Criterion</b>', 
                '<b>Loshiko (Score = 8)</b>', 
                '<b>City of Chicago (Score = 4)</b>', 
                '<b>Neighborhood Scout (Score = 3)</b>'],
        #line_color='black', 
        #fill_color='white',
        align='center',
        font = dict(color='black', size=14)
      ),
      cells=dict(
        values=[cr, lo, ch, ns],
        #line_color='black',
        fill_color=[['#f2f2f2']*10,
                    lo_clrs, ch_clrs, ns_clrs],
        align=['left', 'center', 'center', 'center'],
        
        font=dict(color=['black', 'white', 'white', 'white'], size=14),
        height=45,
        ))
    ])
    
    figure.update_layout(
        #coloraxis_showscale=False,
        #autosize=True,
        #showlegend=False,
        #hovermode='closest',
        #mapbox_style="light",
        height=502, 
        margin={"r":0,"t":0,"l":0,"b":0},
        )
    
    return figure
    
    
    
    




def replace_fields(crimes_df):
    
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
        ['AIRCRAFT',
         'AIRPORT BUILDING NON-TERMINAL - NON-SECURE AREA',
         'AIRPORT BUILDING NON-TERMINAL - SECURE AREA',
         'AIRPORT EXTERIOR - NON-SECURE AREA',
         'AIRPORT EXTERIOR - SECURE AREA',
         'AIRPORT PARKING LOT',
         'AIRPORT TERMINAL LOWER LEVEL - NON-SECURE AREA',
         'AIRPORT TERMINAL LOWER LEVEL - SECURE AREA',
         'AIRPORT TERMINAL MEZZANINE - NON-SECURE AREA',
         'AIRPORT TERMINAL UPPER LEVEL - NON-SECURE AREA',
         'AIRPORT TERMINAL UPPER LEVEL - SECURE AREA',
         'AIRPORT TRANSPORTATION SYSTEM (ATS)',
         'AIRPORT VENDING ESTABLISHMENT',
         ], 'AIRPORT/AIRCRAFT')
    
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['CHA APARTMENT',
             'CHA BREEZEWAY',
             'CHA ELEVATOR',
             'CHA GROUNDS',
             'CHA HALLWAY',
             'CHA HALLWAY / STAIRWELL / ELEVATOR',
             'CHA HALLWAY/STAIRWELL/ELEVATOR',
             'CHA LOBBY',
             'CHA PARKING LOT',
             'CHA PARKING LOT / GROUNDS',
             'CHA PARKING LOT/GROUNDS',
             'CHA PLAY LOT',
             'CHA STAIRWELL',
             ], 'CHA Property')
        
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['CHURCH',
             'CHURCH / SYNAGOGUE / PLACE OF WORSHIP',
             'CHURCH PROPERTY',
             'CHURCH/SYNAGOGUE/PLACE OF WORSHIP',
             ], 'PLACE OF WORSHIP')
        
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['SCHOOL - PRIVATE BUILDING',
             'SCHOOL - PRIVATE GROUNDS',
             'SCHOOL - PUBLIC BUILDING',
             'SCHOOL - PUBLIC GROUNDS',
             'SCHOOL YARD',
             'SCHOOL, PRIVATE, BUILDING',
             'SCHOOL, PRIVATE, GROUNDS',
             'SCHOOL, PUBLIC, BUILDING',
             'SCHOOL, PUBLIC, GROUNDS',
             'PUBLIC GRAMMAR SCHOOL',
             'PUBLIC HIGH SCHOOL',
             ], 'SCHOOL')
        
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['VACANT LOT', 
             'VACANT LOT / LAND', 
             'VACANT LOT/LAND'], 'VACANT LOT')
        
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['RESIDENCE',
             'APARTMENT',
             'RESIDENCE - GARAGE',
             'RESIDENCE - PORCH / HALLWAY',
             'RESIDENCE - YARD (FRONT / BACK)',
             'RESIDENCE PORCH/HALLWAY',
             'RESIDENCE-GARAGE',
             'RESIDENTIAL YARD (FRONT/BACK)',
             'YARD', 'PORCH', 'APARTMENT', 
             'ROOMING HOUSE',
             'DRIVEWAY',
             'GARAGE',
             'HOUSE',
             'BASEMENT',
             'DRIVEWAY - RESIDENTIAL'], 'RESIDENTIAL')
        
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['HOTEL', 
             'HOTEL / MOTEL',
             'MOTEL',
             ], 'HOTEL/MOTEL')
        
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['LAKEFRONT / WATERFRONT / RIVERBANK',
             ], 'LAKEFRONT/WATERFRONT/RIVERBANK')
        
     
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['HOSPITAL', 
             'HOSPITAL BUILDING/GROUNDS',
             'HOSPITAL BUILDING / GROUNDS',
             ], 'HOSPITAL')
        
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['MEDICAL / DENTAL OFFICE', 
             ], 'MEDICAL/DENTAL OFFICE')
        
        
     
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['GAS STATION DRIVE/PROP.',
             ], 'GAS STATION')
        
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['FACTORY',
             'FACTORY / MANUFACTURING BUILDING',
             'FEDERAL BUILDING',
            ], 'FACTORY/MANUFACTURING BUILDING')
        
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['GOVERNMENT BUILDING',
             'GOVERNMENT BUILDING / PROPERTY',
             ], 'GOVERNMENT BUILDING/PROPERTY')
     
     
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['CTA "L" PLATFORM',
             'CTA "L" TRAIN',
             'CTA BUS',
             'CTA BUS STOP',
             'CTA GARAGE / OTHER PROPERTY',
             'CTA PARKING LOT / GARAGE / OTHER PROPERTY',
             'CTA PLATFORM',
             'CTA PROPERTY',
             'CTA STATION',
             'CTA SUBWAY STATION',
             'CTA TRACKS - RIGHT OF WAY',
             'CTA TRAIN',
             ], 'CTA PROPERTY')
            
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['COLLEGE / UNIVERSITY - GROUNDS',
             'COLLEGE / UNIVERSITY - RESIDENCE HALL',
             'COLLEGE/UNIVERSITY GROUNDS',
             'COLLEGE/UNIVERSITY RESIDENCE HALL',
             ], 'COLLEGE/UNIVERSITY')
        
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['APPLIANCE STORE', 
             'ATHLETIC CLUB',
             'AUTO', 
             'BAR OR TAVERN', 
             'BARBERSHOP', 
             'BARBER SHOP/BEAUTY SALON',
             'BOWLING ALLEY', 
             'CAR WASH', 
             'CLEANING STORE', 
             'CLUB', 
             'COMMERCIAL / BUSINESS OFFICE', 
             'DEPARTMENT STORE', 
             'DRUG STORE', 
             'GROCERY FOOD STORE', 
             'MOVIE HOUSE/THEATER', 
             'MOVIE HOUSE / THEATER',
             'NEWSSTAND', 
             'POOL ROOM', 
             'POOLROOM', 
             'RESTAURANT', 
             'RETAIL STORE', 
             'SMALL RETAIL STORE', 
             'TAVERN', 
             'TAVERN/LIQUOR STORE', 
             'YMCA', 
             'TAVERN / LIQUOR STORE',
             'PAWN SHOP',
             'AUTO / BOAT / RV DEALERSHIP',
             'CONVENIENCE STORE',
             'BANQUET HALL',
             'FUNERAL PARLOR',
             'LAUNDRY ROOM',
             'LIQUOR STORE',
             'LIVERY AUTO',
             'LIVERY STAND OFFICE',
             'LOADING DOCK',
             'OFFICE',
             'WAREHOUSE',
             ], 'BUSINESS')
        
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['HIGHWAY / EXPRESSWAY',
             'EXPRESSWAY EMBANKMENT',
             ], 'HIGHWAY/EXPRESSWAY')
        
     
               
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['DELIVERY TRUCK', 'VEHICLE NON-COMMERCIAL',
             'VEHICLE-COMMERCIAL', 'VEHICLE - COMMERCIAL',
             'VEHICLE - COMMERCIAL: ENTERTAINMENT / PARTY BUS',
             'VEHICLE - COMMERCIAL: TROLLEY BUS',
             'VEHICLE - DELIVERY TRUCK',
             'VEHICLE - OTHER RIDE SERVICE',
             'VEHICLE - OTHER RIDE SHARE SERVICE (E.G., UBER, LYFT)',
             'VEHICLE - OTHER RIDE SHARE SERVICE (LYFT, UBER, ETC.)',
             'VEHICLE NON-COMMERCIAL',
             'VEHICLE-COMMERCIAL',
             'VEHICLE-COMMERCIAL - ENTERTAINMENT/PARTY BUS',
             'VEHICLE-COMMERCIAL - TROLLEY BUS',
             'TAXI CAB',
             'TAXICAB',
             'TRUCK',
             'AUTO',
             ], 'VEHICLE')
        
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['BOAT / WATERCRAFT', 
             ], 'BOAT/WATERCRAFT')
        
        
     
     
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['BANK',
             'CREDIT UNION',
             'CURRENCY EXCHANGE',
             'SAVINGS AND LOAN',
             ], 'FINANCIAL INST.')
        
        
                
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['SPORTS ARENA / STADIUM',
             ], 'SPORTS ARENA/STADIUM')
        
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['POLICE FACILITY / VEHICLE PARKING LOT',
             'POLICE FACILITY/VEH PARKING LOT',
             ], 'POLICE FACILITY')
        
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['PARKING LOT', 
             'PARKING LOT / GARAGE (NON RESIDENTIAL)',
             'PARKING LOT/GARAGE(NON.RESID.)',
             ], 'PARKING LOT')
        
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['OTHER RAILROAD PROP / TRAIN DEPOT',
             'OTHER RAILROAD PROPERTY / TRAIN DEPOT',
             'RAILROAD PROPERTY',
             ], 'RAILROAD PROPERTY')
        
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['OTHER (SPECIFY)', 
             'VESTIBULE',
             'OTHER COMMERCIAL TRANSPORTATION',
             ], 'OTHER')
        
    crimes_df['Location Description'] = crimes_df['Location Description'].replace(
            ['NURSING / RETIREMENT HOME',
             'NURSING HOME',
             'NURSING HOME/RETIREMENT HOME',
             ], 'NURSING HOME')
    
    return crimes_df







