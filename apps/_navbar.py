import logging
import sys
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import datetime
import random
from dash.dependencies import Output, Input, State
import functools

from ..app import app
from ..apis import get_cur_time

logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',
                    datefmt='%y-%m-%d %H:%M:%S', stream=sys.stdout)
logger = logging.getLogger()


# ## NavBar
drop_menu = dbc.Row(
    [
        dbc.Col(html.Div(id='navbar-time', children=f'{get_cur_time()}', className="mr-2", style={'color': '#FFFFFF'})),
        dbc.DropdownMenu(
            children=[
                # dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("文件大小", href="/fmt_f_size"),
                dbc.DropdownMenuItem("查看图片", href="/get_img"),
                dbc.DropdownMenuItem("文件MD5", href="/calc_md5"),
            ],
            className="mr-2",
            label="小工具",
        ),
        dbc.DropdownMenu(
            children=[
                # dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("人脸可视化", href="/fmt_f_size"),
            ],
            className="mr-2",
            label="人脸数据",
        ),
        dbc.DropdownMenu(
            children=[
                # dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("数据平台", href="#"),
                dbc.DropdownMenuItem("标注平台", href="#"),
            ],
            className="mr-2",
            label="外部链接",
        ),
        # # 自动更新
        # dcc.Interval(
        #     id='interval-component',
        #     interval=3 * 1000,   # in milliseconds / refresh the webpage in every 60 seconds
        #     n_intervals=0
        # ),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=app.get_asset_url('plotly-logo.png'), height="30px")),
                    dbc.Col(dbc.NavbarBrand("工具箱", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="/",
        ),
        dbc.NavbarToggler(id="navbar-toggler", children='123'),
        dbc.Collapse(drop_menu, id="navbar-collapse", navbar=True),
    ],
    color="dark",
    dark=True,
)


@app.callback(Output('navbar-time', 'children'), [Input('interval-component', 'n_intervals')])
def update_navbar_time(n):
    return f'{get_cur_time()}'


# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
