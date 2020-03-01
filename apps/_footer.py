import dash
# import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
# from dash.dependencies import Output, Input, State


# footer
footer = dbc.Row(
    dbc.Col(html.Div('AiniRobot ©2018 Created by ainirobot', style={'textAlign': 'center'}), align="end", className='mt-20'),
    className='mt-20'
)
