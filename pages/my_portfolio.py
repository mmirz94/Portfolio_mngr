'''
Author: Salar Mirzaloo
Email: Mirzaloo.salar@gmail.com
This file includes the layout and callbacks used for the Portfolio page of the app!
'''
#------------------------------------------------------------------------------------------------------
from app import app
from functions import *

layout_portfolio= html.Div(
    id='prtflio-mngr',
    children=[
        dbc.Row(
            dbc.Col(
                [
                    html.Div(
                        [
                            default_stocks_table
                        ],
                        style={'width':'90%', 'margin-left': 'auto', 'margin-right': 'auto'}
                    ),
                ],
                style={'margin-top': '1rem'},
            ),
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            [
                               html.Div(
                                   children = [],
                                   id='individual_stock_cards',
                                   style={'overflow-x':'scroll','white-space':'nowrap'}
                               )
                            ],
                            style={'border-color': colors['text'],'width':'90%', 'margin-left': 'auto', 'margin-right': 'auto', 'backgroundColor':colors['bg_color']}
                        )
                    ],
                )
            ],
            style={'margin-top':'1rem'}
        ),


        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Card(
                                            [
                                                dbc.ListGroup(
                                                    [
                                                        dbc.ListGroupItem("Total Portfolio Metrics",
                                                                          style={'background-color':colors['heading'], 'font-weight': 'bold',
                                                                                 'font-family': 'cursive','font-size': '15px', 'color':colors['text'], 'border':'1px solid rgba(255,255,255)'}),
                                                        dbc.ListGroupItem(html.Div(
                                                                [
                                                                    html.Div("Total Market Value:", className='portfolio_metrics_left_text',
                                                                             style={'display': 'inline-block',
                                                                                    'color':colors['text']}),
                                                                    html.Div("Total Book Value:", className='portfolio_metrics_left_text',
                                                                             style={'display': 'inline-block',
                                                                                    'color': colors['text']}),
                                                                    html.Div("Total Return:", className='portfolio_metrics_left_text',
                                                                             style={'display': 'inline-block',
                                                                                    'color': colors['text']}),
                                                                    html.Div("Return Percentage:", className='portfolio_metrics_left_text',
                                                                             style={'display': 'inline-block',
                                                                                    'color': colors['text']}),
                                                                ],
                                                            style={'backgroundColor': colors['bg_color']}
                                                            ), id='portfolio_metrics_item1',
                                                            style={'backgroundColor': colors['bg_color'], 'border':'1px solid rgba(255,255,255)'}
                                                        ),

                                                        dbc.ListGroupItem(
                                                            html.Div(
                                                                [
                                                                    html.Div("Yearly Dividend:", className='portfolio_metrics_left_text',
                                                                             style={'display': 'inline-block',
                                                                                    'color': colors['text']}),
                                                                    # html.Div("Dividends collected:", className='portfolio_metrics_left_text', style={'display': 'inline-block'}),
                                                                    html.Div("Yield as % of portfolio:", className='portfolio_metrics_left_text',
                                                                             style={'display': 'inline-block',
                                                                                    'color': colors['text']}),

                                                                ],
                                                                style={'backgroundColor': colors['bg_color']}
                                                            ),
                                                            id='portfolio_metrics_item2',
                                                            style={'backgroundColor': colors['bg_color'], 'border':'1px solid rgba(255,255,255)'}
                                                        ),

                                                    ],
                                                    id='portfolio_metrics',
                                                    flush=True
                                                )
                                            ],
                                            style= {'top':'25px', 'margin-left':'81px', 'backgroundColor': colors['bg_color']}
                                        )
                                    ]
                                )
                            ]
                        ),

                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Card(
                                            [
                                                dbc.ListGroup(
                                                    [
                                                        dbc.ListGroupItem("Transactions",
                                                                          style={'background-color': colors['heading'],
                                                                                 'font-weight': 'bold',
                                                                                 'font-family': 'cursive',
                                                                                 'font-size': '15px',
                                                                                 'color': colors['text'],
                                                                                 'border': '1px solid rgba(255,255,255)'}),
                                                        dbc.ListGroupItem(html.Div(
                                                            [
                                                                html.Div("Deposits",
                                                                         style={'font-family': 'cursive',
                                                                                'fontWeight':'bold',
                                                                                'font-size': '17px',
                                                                                'width':'70%',
                                                                                'display': 'inline-block',
                                                                                'color': colors['text']}),
                                                                html.Div("1 Week:",
                                                                         className='portfolio_metrics_left_text',
                                                                         style={'display': 'inline-block',
                                                                                'color': colors['text']}),
                                                                html.Div("1 Month:",
                                                                         className='portfolio_metrics_left_text',
                                                                         style={'display': 'inline-block',
                                                                                'color': colors['text']}),
                                                                html.Div("1 Year:",
                                                                         className='portfolio_metrics_left_text',
                                                                         style={'display': 'inline-block',
                                                                                'color': colors['text']}),
                                                                html.Div("Total:",
                                                                         className='portfolio_metrics_left_text',
                                                                         style={'display': 'inline-block',
                                                                                'color': colors['text']})
                                                            ],
                                                            style={'backgroundColor': colors['bg_color']}
                                                        ), id='portfolio_deposits_item1',
                                                            style={'backgroundColor': colors['bg_color'],
                                                                   'border': '1px solid rgba(255,255,255)'}
                                                        ),

                                                        dbc.ListGroupItem(
                                                            html.Div(
                                                                [
                                                                    html.Div("Withdrawals",
                                                                             style={'font-family': 'cursive',
                                                                                   'fontWeight':'bold',
                                                                                   'font-size': '17px',
                                                                                   'width':'70%',
                                                                                   'display': 'inline-block',
                                                                                   'color': colors['text']}),
                                                                    html.Div("1 Week:",
                                                                             className='portfolio_metrics_left_text',
                                                                             style={'display': 'inline-block',
                                                                                    'color': colors['text']}),
                                                                    html.Div("1 Month:",
                                                                             className='portfolio_metrics_left_text',
                                                                             style={'display': 'inline-block',
                                                                                    'color': colors['text']}),
                                                                    html.Div("1 Year:",
                                                                             className='portfolio_metrics_left_text',
                                                                             style={'display': 'inline-block',
                                                                                    'color': colors['text']}),
                                                                    html.Div("Total:",
                                                                             className='portfolio_metrics_left_text',
                                                                             style={'display': 'inline-block',
                                                                                    'color': colors['text']})

                                                                ],
                                                                style={'backgroundColor': colors['bg_color']}
                                                            ),
                                                            id='portfolio_deposits_item2',
                                                            style={'backgroundColor': colors['bg_color'],
                                                                   'border': '1px solid rgba(255,255,255)'}
                                                        ),

                                                    ],
                                                    id='portfolio_deposits',
                                                    flush=True
                                                )
                                            ],
                                            style={'top': '43px', 'margin-left': '81px', 'backgroundColor': colors['bg_color']}
                                        )
                                    ]
                                )
                            ],
                            style={'margin-top':'5px'}
                        )
                    ],
                    width=4
            ),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.Row([
                                    dbc.Col(
                                        [
                                            html.P('Percentage Holdings', className='pie_chart_text_row1', style={'fontWeight': 'bold','color':colors['text']}),
                                            dash_charts.pie(
                                                id='percentage_holdings_pie_chart', width='450px', height='300px',
                                                data=[['Symbol', 'Market value']], title=None, is3D= True, pieHole=0,
                                                backgroundColor=colors['bg_color'], legendTextColor=colors['text']

                                            ),
                                        ],
                                        width=6
                                    ),
                                    dbc.Col(
                                        [
                                            html.P('Sector Weighting',className='pie_chart_text_row1', style={'fontWeight': 'bold','color':colors['text']}),
                                            dash_charts.pie(
                                                    id='sector_weighting_pie_chart', width='450px', height='300px',
                                                    data=[['Sector', 'Weight']], title=None, is3D= True, pieHole=0,
                                                    backgroundColor=colors['bg_color'], legendTextColor=colors['text']
                                            ),
                                        ],
                                        width=6,
                                        style={'left':'-15px'}
                                    )],
                                    no_gutters=True
                                ),

                                dbc.Row([
                                    dbc.Col(
                                        [
                                            html.P('Dividend Stock Percentage',className='pie_chart_text_row2', style={'fontWeight': 'bold','color':colors['text']}),
                                            dash_charts.pie(
                                                    id='dividend_stocks_percentage_pie_chart', width='450px', height='300px',
                                                    data=[['Dividend', 'weight']], title=None, is3D= True, pieHole=0,
                                                    backgroundColor=colors['bg_color'], legendTextColor=colors['text']
                                                ),
                                        ],
                                        width=6
                                    ),
                                    dbc.Col(
                                        [   html.P('Portfolio Risk',className='pie_chart_text_row2', style={'fontWeight': 'bold', 'color':colors['text'],}),
                                            dash_charts.pie(
                                                    id='portfolio_risk_pie_chart', width='450px', height='300px',
                                                    data=[['Portfolio risk', 'weights']], title=None, is3D= True, pieHole=0,
                                                    backgroundColor=colors['bg_color'], legendTextColor=colors['text']
                                                ),
                                        ],
                                        width=6,
                                        style={'left':'-15px'}
                                    )],
                                    no_gutters=True
                                ),
                            ],
                            style={'position':'absolute', 'width':'923px', 'margin-left':'3px', 'height':'680px', 'backgroundColor': colors['bg_color'], 'border-color': colors['text']}
                        )
                    ],
                    width=8,
                    style={ 'margin-top':'25px', 'width':'923px', 'height':'710px'}
                )
            ],
        ),
        dcc.Store(id='datastore'),
        dcc.Store(id='store_stock_cards', data={'Cards':[]}),
        dcc.Interval(id="interval", interval=10*60*1000),


    ],
    style={'backgroundColor': colors['bg_color']}
)

#-------------------------------------Portfolio callbacks---------------------------------------#

@app.callback(
    Output('datastore', 'data'),
    Input('interval', 'n_intervals')
)
def update_store(n_intervals):
    # [ 'Symbol', 'Exchange', 'Company Name', 'Sector', 'QTY', 'Cost Per Share', 'Current Price', 'Book Value',
    #  'Market Value', 'Profit/Loss', '% Return']
    if 'transactions.csv' in os.listdir(PATH_DATA) and len(pd.read_csv(os.path.join(PATH_DATA, 'transactions.csv')))!= 0:
        transactions_data = pd.read_csv(os.path.join(PATH_DATA, 'transactions.csv'))
        transactions_data['QTY'] = np.where(transactions_data['Transaction Type'] == 'Sell', transactions_data['QTY'] * -1, transactions_data['QTY'])
        transactions_data['Total Amount'] = np.where(transactions_data['Transaction Type'] == 'Sell', transactions_data['Total Amount'] * -1, transactions_data['Total Amount'])
        data = transactions_data.groupby(by='Symbol').sum().reset_index()[['Symbol', 'Total Amount', 'QTY']]
        data['Company Name'] = transactions_data.groupby(by='Symbol')['Company Name'].unique().apply(lambda x: x[0]).reset_index()['Company Name']
        data['Exchange'] = transactions_data.groupby(by='Symbol')['Exchange'].unique().apply(lambda x: x[0]).reset_index()['Exchange']
        data['Risk'] = transactions_data.groupby(by='Symbol')['Risk'].unique().apply(lambda x: x[0]).reset_index()['Risk']
        data['Book Value'] = data['Total Amount']
        data.drop(columns='Total Amount', inplace=True)
        data['Cost Per Share'] = data['Book Value'] / data['QTY']
        filtered_stocks_tsx = tsx_stocks[tsx_stocks['Symbol'].isin(data['Symbol'])]
        filtered_stocks_tsxv = tsxv_stocks[tsxv_stocks['Symbol'].isin(data['Symbol'])]
        filtered_stocks = pd.concat([filtered_stocks_tsx, filtered_stocks_tsxv])
        data['Sector'] = data['Symbol'].apply(lambda symbol: filtered_stocks[filtered_stocks['Symbol'] == symbol]['Sector'].values[0])
        data['Dividend'] = data['Symbol'].apply(lambda symbol: filtered_stocks[filtered_stocks['Symbol'] == symbol]['Dividend'].values[0])

        tickers_str = ''
        for i in data['Symbol'].values:
            tickers_str = tickers_str + i + ' '
        time_frame_data = yf.download(tickers=tickers_str, period="1d", interval="5m", group_by='ticker', auto_adjust=True)
        data['Current Price'] = data['Symbol'].apply(lambda symbol: time_frame_data[symbol].dropna().iloc[-1]['Close'])
        data['Market Value'] = data['Current Price'] * data['QTY']
        data['Profit/Loss'] = data['Market Value'] - data['Book Value']
        data['% Return'] = ((data['Market Value'] / data['Book Value']) - 1) * 100
        data.loc[:,['Cost Per Share', 'Dividend', 'Current Price', 'Market Value', 'Profit/Loss', '% Return']] = data.loc[:,['Cost Per Share', 'Dividend', 'Current Price', 'Market Value', 'Profit/Loss', '% Return']].astype(float).round(2)
        # data.to_csv(os.path.join(PATH_DATA, 'data.csv'), index=False)
        time_frame_data.reset_index().to_csv(os.path.join(PATH_DATA, 'time_frame_data.csv'), index=False)
        return {'data': data.to_json()}

    else:
        data=pd.DataFrame(columns=['Symbol', 'QTY', 'Company Name', 'Exchange', 'Risk', 'Book Value', 'Cost Per Share', 'Sector', 'Dividend', 'Current Price', 'Market Value', 'Profit/Loss', '% Return'])
    return {'data':data.to_json()}


@app.callback(
    [
        Output('stocks_table','data'),
        Output('percentage_holdings_pie_chart', 'data'),
        Output('sector_weighting_pie_chart', 'data'),
        Output('dividend_stocks_percentage_pie_chart', 'data'),
        Output('portfolio_risk_pie_chart', 'data'),
        Output('portfolio_metrics_item1', 'children'),
        Output('portfolio_metrics_item2', 'children')
    ],
    [
        Input('datastore', 'data'),
     ],
)
def update_plots_and_tables(store):
    data = pd.read_json(store['data'])
    # data.to_csv('./dataaaaaaaaaaaaaaaaa.csv')
    if len(data)==0:
        percentage_holdings_data = [['Symbol', 'Market Value']]
        sector_weighting_data = [['Sector', 'Weight']]
        dividend_stocks_percentage_data = [['Dividend', 'weight']]
        portfolio_risk_data = [['Portfolio risk', 'weights']]
        portfolio_metrics_item1= html.Div(
            [
                html.Div("Total Market Value:", className='portfolio_metrics_left_text',
                         style={'display': 'inline-block',
                                'color': colors['text']}),
                html.Div("Total Book Value:", className='portfolio_metrics_left_text',
                         style={'display': 'inline-block',
                                'color': colors['text']}),
                html.Div("Total Return:", className='portfolio_metrics_left_text',
                         style={'display': 'inline-block',
                                'color': colors['text']}),
                html.Div("Return Percentage:", className='portfolio_metrics_left_text',
                         style={'display': 'inline-block',
                                'color': colors['text']}),
            ],
            style={'backgroundColor': colors['bg_color']}
        )
        portfolio_metrics_item2 = html.Div(
            [
                html.Div("Yearly Dividend:", className='portfolio_metrics_left_text',
                         style={'display': 'inline-block',
                                'color': colors['text']}),
                # html.Div("Dividends collected:", className='portfolio_metrics_left_text', style={'display': 'inline-block'}),
                html.Div("Yield as % of portfolio:", className='portfolio_metrics_left_text',
                         style={'display': 'inline-block',
                                'color': colors['text']}),


            ],
            style={'backgroundColor': colors['bg_color']}
        )

        return data.to_dict('records'), percentage_holdings_data, sector_weighting_data, dividend_stocks_percentage_data, portfolio_risk_data, portfolio_metrics_item1, portfolio_metrics_item2
    else:
        percentage_holdings_data = [['Symbol', 'Market Value']] + [[data.loc[i, 'Symbol'], data.loc[i, 'Market Value']] for i in range(len(data))]

        sector_unique_weights = data.groupby(['Sector'])['Market Value'].sum()
        sector_weighting_data = [['Sector', 'Weight']]+[[sector_unique_weights.keys()[i],(sector_unique_weights.values)[i]] for i in range(len(sector_unique_weights.values))]

        dividend_stocks_percentage_data= [['Dividend', 'weight']]+[['Dividend',data[data['Dividend'] != 0]['Book Value'].sum()],['No Dividend', data[data['Dividend'] == 0]['Book Value'].sum() ]]

        portfolio_risk_data= [['Portfolio risk', 'weights']]+[['High', data[data['Risk']=='High']['Market Value'].sum()],['Medium', data[data['Risk']=='Medium']['Market Value'].sum()],['Low', data[data['Risk']=='Low']['Market Value'].sum()]]

        portfolio_metrics_item1= html.Div(
            [
                html.Div("Total Market Value:", className='portfolio_metrics_left_text', style={'display': 'inline-block', 'color':colors['text']}),
                html.Div("${0:.2f}".format(data['Market Value'].sum()), className='portfolio_metrics_right_text', style={'display': 'inline-block',  'color':colors['text']}),
                html.Div("Total Book Value:", className='portfolio_metrics_left_text', style={'display': 'inline-block',  'color':colors['text']}),
                html.Div("${0:.2f}".format(data['Book Value'].sum()), className='portfolio_metrics_right_text', style={'display': 'inline-block',  'color':colors['text']}),
                html.Div("Total Return:", className='portfolio_metrics_left_text', style={'display': 'inline-block',  'color':colors['text']}),
                html.Div("${0:.2f}".format((data['Market Value'].sum())-(data['Book Value'].sum())), className='portfolio_metrics_right_text', style={'display': 'inline-block',  'color':colors['text']}),
                html.Div("Return Percentage:", className='portfolio_metrics_left_text', style={'display': 'inline-block',  'color':colors['text']}),
                html.Div("{0:.2f}%".format((((data['Market Value'].sum())/(data['Book Value'].sum()))-1)*100), className='portfolio_metrics_right_text', style={'display': 'inline-block',  'color':colors['text']})
             ],
            style={'backgroundColor': colors['bg_color']}
        )

        portfolio_metrics_item2= html.Div(
            [
                html.Div("Yearly Dividend:", className='portfolio_metrics_left_text', style={'display': 'inline-block',  'color':colors['text']}),
                html.Div("${0:.2f}".format((data['QTY']*data['Dividend']).sum()), className='portfolio_metrics_right_text', style={'display': 'inline-block',  'color':colors['text']}),
                # html.Div("Dividends collected:", className='portfolio_metrics_left_text', style={'display': 'inline-block'}),
                # html.Div("${0:.2f}".format(data['Market value'].sum()), className='portfolio_metrics_right_text', style={'display': 'inline-block'}),
                html.Div("Yield as % of portfolio:", className='portfolio_metrics_left_text', style={'display': 'inline-block',  'color':colors['text']}),
                html.Div("{0:.2f}%".format((((data['QTY']*data['Dividend']).sum())/(data['Book Value'].sum()))*100), className='portfolio_metrics_right_text', style={'display': 'inline-block',  'color':colors['text']}),
            ],
            style={'backgroundColor': colors['bg_color']}
        )

        return data.to_dict('records'), percentage_holdings_data, sector_weighting_data, dividend_stocks_percentage_data, portfolio_risk_data, portfolio_metrics_item1, portfolio_metrics_item2


@app.callback(
    Output('individual_stock_cards','children'),
    Output('store_stock_cards', 'data'),
    [
        Input('datastore', 'data'),
        Input('stocks_table', 'selected_rows')
    ],
    [
        State('store_stock_cards', 'data'),
        State('individual_stock_cards','children'),
    ]
)
def update_individual_stock_cards(store, selected_rows, store_stock_cards, cards):

    previous_cards_list = store_stock_cards['Cards']

    if len(selected_rows) == 0:
        symbols_selected=[]
    else:
        data = pd.read_json(store['data'])['Symbol']
        symbols_selected = data[data.index.isin(selected_rows)].values
        print(symbols_selected)

    if len(previous_cards_list) > len(symbols_selected):
        remove_card=[]
        to_be_removed = list(set(previous_cards_list) - set(symbols_selected))
        for i in range(len(cards)):
            if cards[i]['props']['id'] in to_be_removed:
                remove_card.append(cards[i])
        for i in remove_card:
            cards.remove(i)

    elif len(previous_cards_list) < len(symbols_selected):
        if len(symbols_selected)>1 and len(cards)==0:
            to_be_added=symbols_selected
        else:
            to_be_added = list(set(symbols_selected) - set(previous_cards_list))

        full_time_data = pd.read_csv(os.path.join(PATH_DATA,'time_frame_data.csv'), skiprows=[1])

        for i in range(len(to_be_added)):

            time_data = full_time_data.loc[:,["Datetime","{}.3".format(to_be_added[i])]]
            time_data.dropna(inplace=True)

            day_start = full_time_data.iloc[0]["{}".format(to_be_added[i])] #Nothing: open, .1: high, .2: low, .3: close
            day_end = time_data.iloc[-1]["{}.3".format(to_be_added[i])]

            indicator_fig = go.Figure(go.Indicator(
                mode="delta",
                value=day_end,
                delta={'reference': day_start, 'relative': True, 'valueformat': '.2%'}))
            indicator_fig.update_traces(delta_font={'size': 12})
            indicator_fig.update_layout(height=30, width=70)

            if day_end >= day_start:
                indicator_fig.update_traces(delta_increasing_color='green')
            elif day_end < day_start:
                indicator_fig.update_traces(delta_decreasing_color='red')

            line_chart_y_range_offset=(time_data["{}.3".format(to_be_added[i])].max()-time_data["{}.3".format(to_be_added[i])].min())/8
            line_chart = px.line(time_data, x="Datetime", y="{}.3".format(to_be_added[i]),
                            range_y=[time_data["{}.3".format(to_be_added[i])].min()-line_chart_y_range_offset, time_data["{}.3".format(to_be_added[i])].max()+line_chart_y_range_offset],
                            height=120)
            line_chart.update_layout(margin=dict(t=0, r=0, l=0, b=20),
                                                    paper_bgcolor='rgba(0,0,0,0)',
                                                    plot_bgcolor='rgba(0,0,0,0)',
                                                    yaxis=dict(
                                                        title=None,
                                                        showgrid=False,
                                                        showticklabels=False
                                                    ),
                                                    xaxis=dict(
                                                        title=None,
                                                        showgrid=False,
                                                        showticklabels=False
                                                    ))

            if day_end >= day_start:
                line_chart.update_traces(fill='tozeroy', line={'color': 'green'})
            elif day_end < day_start:
                line_chart.update_traces(fill='tozeroy',
                                         line={'color': 'red'})


            cards.append(
                dbc.Card(
                    id='{}'.format(to_be_added[i]),
                    children= [
                        dbc.CardImg(
                            src=app.get_asset_url('{}.png'.format(to_be_added[i])),
                            top=True,
                            style={'height': '4rem', 'width':'auto', 'margin-left': '5px'},
                        ),
                        dbc.CardBody([
                            dbc.Row([
                                dbc.Col([
                                    html.P("CHANGE (1D)", className="ml-3")
                                ], width={'size': 5, 'offset': 1}),

                                dbc.Col([
                                    dcc.Graph(id='indicator-graph', figure=indicator_fig,
                                              config={'displayModeBar': False},
                                              )
                                ], width={'size': 3, 'offset': 2})
                            ]),

                            dbc.Row([
                                dbc.Col([
                                    dcc.Graph(id='daily-line', figure=line_chart,
                                              config={'displayModeBar': False})
                                ], width=12)
                            ]),

                            dbc.Row([
                                dbc.Col([
                                    html.Div("Open", className="ml-5", style={'font-weight':'bold'}),
                                ], width=4),

                                dbc.Col([
                                    html.Div("Close",style={'font-weight':'bold'})
                                ], width=4)
                            ], justify="between"),

                            dbc.Row([
                                dbc.Col([
                                    dbc.Label(id='low-price', children= round(day_start,2),
                                              className="mt-2 bg-white p-1 border-top-0",
                                              style={'margin-left':'44px'}),
                                ], width=4),
                                dbc.Col([
                                    dbc.Label(id='high-price', children=round(day_end, 2),
                                              className="mt-2 bg-white p-1 border-top-0",
                                              style={'margin-left':'-2px'}),
                                ], width=4)
                            ], justify="between")
                        ],
                        style={'padding':'12px'}),
                    ],
                    style={"width": "334px", 'display': 'inline-block', 'margin-left': '6px', 'margin-top':'6px', 'margin-bottom':'6px'},
                )
            )

    return cards, {'Cards':symbols_selected}
