import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, title= 'Portfolio Manager', update_title=None, external_stylesheets=[dbc.themes.BOOTSTRAP], assets_folder = 'assets')
server = app.server  #the Flask app