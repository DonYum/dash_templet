# import dash_core_components as dcc
# import dash_bootstrap_components as dbc
import dash_html_components as html
import functools

from ._footer import footer
from ._navbar import navbar
# from ..logger import logger


# 框架
# 注意：该装饰器需要放到所有装饰器下面
def place_to_page(children):
    @functools.wraps(children)
    def func_wrap():
        return html.Div([
            html.Div(children=navbar),
            html.Div(
                children(),
                style={'margin': '40px 100px 100px 100px'},
            ),
            html.Div(children=footer),
        ])
    return func_wrap
