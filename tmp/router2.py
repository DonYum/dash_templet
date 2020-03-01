import dash
import dash_core_components as dcc
import dash_html_components as html
from dash_router import Router


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
router = Router()


@router.route('/')
def page1():
    return html.H1(children='Hello from Page 1')


@router.route('/page-2')
def page2():
    return html.H1(children='Hello from Page1 2')


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    dcc.Link('Navigate to "/page-2"', href='/page-2'),

    html.Div(id='page-content'),
])


@app.callback(
    dash.dependencies.Output('page-content', 'children'),
    [dash.dependencies.Input('url', 'pathname')]
)
def display_page(pathname):
    return router.dispatch(pathname)


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
