from functions import *
from pages import my_portfolio, Transactions
from app import app
###################################App structure##############################


app_layout = html.Div(
    [
        dbc.Navbar(
            [
                html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src=app.get_asset_url('inteli.png'), height="33px"), style={'margin-left':'1rem'}),
                        ],
                        align="center",
                    ),
                    href="https://github.com/mmirz94",
                ),
                dbc.NavLink("Portfolio", href="/portfolio", active='exact', className='link',style={'color':colors['text'], 'margin-left':'2rem', 'hover': {'font-weight':'bold'}}),
                dbc.NavLink("Transactions", href="/transactions", active='exact', className='link', style={'color':colors['text'], 'margin-left':'1rem'}),
                dbc.NavLink("Logout", href="/logout", active='exact', className='link', style={'color':colors['text'], 'margin-left':'62rem'}),
                dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                dbc.Collapse(
                    id="navbar-collapse", navbar=True, is_open=False
                ),
            ],
            color=colors['heading'],
            dark=True,
        ),
        dcc.Location(id='url', refresh=False),
        html.Div(
            id='page_content'
        )
    ],
    style={'overflow-x': 'hidden'}
)

app.layout=app_layout

# "complete" layout
app.validation_layout = html.Div([
    app_layout,
    my_portfolio.layout_portfolio,
    Transactions.layout_transactions
])
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(

                Output('page_content', 'children'),
                Output('url', 'pathname'),
                [
                    Input('url', 'pathname')
                ]
              )
def display_page(pathname):
    if pathname == '/portfolio':
        return my_portfolio.layout_portfolio, no_update
    elif pathname == '/transactions':
        return Transactions.layout_transactions, no_update
    elif pathname=='/':
        return my_portfolio.layout_portfolio, '/portfolio'
    else:
        return '404'



if __name__ == '__main__':
    app.run_server(host = 'localhost',debug=False, dev_tools_hot_reload=False, port = 8000)


