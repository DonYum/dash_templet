import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Output, Input, State

from http_service.lib.format import format_file_size

from ..app import app, router
from ._struct import place_to_page
from ..logger import logger


# import ipyvolume as ipv
# from sklearn.datasets import make_blobs
# X, _ = make_blobs(n_samples=500, n_features=3, centers=5)
# fig = ipv.figure(height=600, width=600, layout={'width': '100%', 'height': '100%'})
# scatter = ipv.scatter(*X.T, size=1, marker="sphere")
# ipv.xyzlim(-10, 10)
# ipv.pylab.save('./ipv.html')
# display(fig)


# 主页
@router.route('/')
@router.route('/index')
@place_to_page
def main():
    return [
        html.H1(
            id='example-h1',
            children=f'Hello Dash!',
            style={'textAlign': 'center', 'color': '#515151'},
        ),

        html.Div(
            id='example-div',
            children='Dash: A web application framework for Python.',
            style={'textAlign': 'center', 'color': '#515151'},
        ),

        html.Div(
            [
                html.A('源文件', href=app.get_asset_url('ipv.html')),
                html.Br(),
                html.Br(),
                # html.Iframe(
                #     id='example-ipv',
                #     src=app.get_asset_url('ipv.html'),
                #     height=1100, width=1100,
                # ),
            ],
            style={'textAlign': 'center', 'margin': '20px 20px 20px 20px', 'padding': '10px 10px 0px 10px'},
        ),
    ]
