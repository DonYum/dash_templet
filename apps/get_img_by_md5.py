import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Output, Input, State

from ..app import app, router
from ._struct import place_to_page
from ..logger import logger


# 根据md5查询图片信息
@router.route('/get_img')
@place_to_page
def get_img_view():
    return html.Div(
        [
            html.H2('查询图片信息'),
            dbc.Input(id="get_img_md5", placeholder="pls input md5...", type="text"),
            html.Br(),
            dbc.Col(html.Img(id="get_img_res_img", height="200px")),
            html.Div(
                dcc.Markdown('请在上面输入要查询的MD5。', id="get_img_doc"),
                style={'border': '1px solid #000', 'margin': '20px 20px 20px 20px', 'padding': '10px 10px 0px 10px'}),
        ]
    )


@app.callback(Output("get_img_res_img", "src"), [Input("get_img_md5", "value")])
def get_img(md5):
    res = ''
    if md5:
        res = app.get_asset_url('plotly-logo.png')
    return res


@app.callback(Output("get_img_doc", "children"), [Input("get_img_md5", "value")])
def get_img(md5):
    _doc = md5

    res = f'''

num={1}

Info:

```
{_doc}
```
        '''
    return res
