import dash
# import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash_router import Router

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True
router = Router()
router.register_callbacks(app)
