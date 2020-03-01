import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Output, Input, State

from http_service.lib.format import format_file_size

from ..app import app, router
from ._struct import place_to_page
from ..logger import logger


# 格式化文件大小
@router.route('/fmt_f_size')
@place_to_page
def fmt_f_size_view():
    return [
        dbc.Row(
            [
                dbc.Col(
                    html.Div(children='文件大小转换： '),
                    width="auto", className="ml-20", align="center"
                ),
                dbc.Col(dbc.Input(id='calc_f_size_size', type="number", placeholder="pls input size..."), width=2),
                dbc.Col(
                    html.Div(id="calc_f_size_size_res", children=''),
                    width="auto", className="ml-20", align="center"
                ),
            ],
            # no_gutters=True,
            # className="ml-auto flex-nowrap mt-3 mt-md-0",
            # align="center",
            justify="center",
        ),
    ]


@app.callback(Output("calc_f_size_size_res", "children"), [Input("calc_f_size_size", "value")])
def fmt_f_size(value):
    res = format_file_size(value)
    logger.debug(f'input={value}, result={res}.')
    return res
