from app import app
from functions import *


side_panel= dbc.Col(
    [
        html.P('Enter a New Transaction',style={'font-family': 'cursive','font-size': '17px', 'color':colors['text'], 'font-weight':'bold'}),
        html.P('Currency', style={'font-family': 'cursive', 'font-size': '15px', 'color': colors['text']}),
        dcc.RadioItems(
                    id='currency_radioItems',
                    options=[
                        {'label':'CAD', 'value':'CAD'},
                        {'label': 'USD', 'value':'USD'},
                    ],
                    value='CAD',
                    labelStyle={'display': 'inline-block', 'margin': '0 9px 0 0'},
                    style={'color':'#ffffff'}

                ),
        html.Br(),
        html.P('Transaction Type', style={'font-family': 'cursive','font-size': '15px', 'color':colors['text']}),

        dcc.Dropdown(
            id='transaction_type_dd',
            options=[
                {'label':'Deposit', 'value':'Deposit'},
                {'label': 'Withdrawal', 'value':'Withdrawal'},
                {'label':'Buy', 'value':'Buy'},
                {'label': 'Sell', 'value':'Sell'}
            ],
            placeholder='Select Transaction type',
            className='dropdown',
            style={'background-color': colors['bg_color']}
        ),
        html.Br(),
        #---------------------------------------for Deposit and Withdrawal---------------------------
        html.P(id='p_amount',children='Amount', style={'font-family': 'cursive', 'font-size': '15px', 'color': colors['text'],'display': 'none'}),
        dcc.Input(id='amount', type='number', className='inputs', style={'display': 'none'}),
        #-------------------------------------------for Buy and Sell---------------------------------
        html.Br(id='Br1', style={'display': 'none'}),
        html.Br(id='Br2', style={'display': 'none'}),
        html.P(id='p_exchange',children='Exchange', style={'font-family': 'cursive','font-size': '15px', 'color':colors['text'],'display': 'none'}),
        dcc.Dropdown(
            id='exchange_dd',
            options=[
                {'label':'TSX', 'value':'TSX'},
                {'label': 'TSXV', 'value':'TSXV'},
                {'label':'NYSE', 'value':'NYSE', 'disabled': True},
                {'label': 'NASDAQ', 'value':'NASDAQ', 'disabled': True}
            ],
            placeholder="Select an Exchange",
            className='dropdown',
            style={'display': 'none', 'background-color': colors['bg_color'], 'color':'#ffffff'}
        ),
        html.Br(id='Br3', style={'display': 'none'}),
        html.P(id='p_symbol',children='Ticker Symbol', style={'font-family': 'cursive','font-size': '15px', 'color':colors['text'], 'display': 'none'}),
        dcc.Dropdown(
            id='symbol_dd',
            options=[{'label':tsx_stocks.loc[i,'Company Name']+'('+tsx_stocks.loc[i,'Symbol']+')', 'value': i} for i in range(len(tsx_stocks))],
            placeholder="Select a Symbol",
            className='dropdown',
            style={'display': 'none', 'background-color': colors['bg_color']}
        ),
        html.Br(id='Br4', style={'display': 'none'}),

        html.P(id='p_QTY',children='Number of Shares', style={'font-family': 'cursive', 'font-size': '15px', 'color': colors['text'], 'display': 'none'}),
        dcc.Input(id='QTY', type='number', className='inputs',style={'display': 'none'}),
        html.Br(id='Br5', style={'display': 'none'}),
        html.Br(id='Br6', style={'display': 'none'}),

        html.P(id='p_PPS',children='Price Per Share', style={'font-family': 'cursive', 'font-size': '15px', 'color': colors['text'], 'display': 'none'}),
        dcc.Input(id='PPS', type='number', className='inputs', style={'display': 'none'}),
        html.Br(id='Br7', style={'display': 'none'}),
        html.Br(id='Br8', style={'display': 'none'}),

        html.P(id='p_risk', children='Risk',
               style={'font-family': 'cursive', 'font-size': '15px', 'color': colors['text'], 'display': 'none'}),
        dcc.Dropdown(
            id='risk_dd',
            options=[
                {'label': 'Low', 'value': 'Low'},
                {'label': 'Medium', 'value': 'Medium'},
                {'label': 'High', 'value': 'High'},
            ],
            placeholder="Select Risk level",
            className='dropdown',
            style={'display': 'none', 'background-color': colors['bg_color']}
        ),
        html.Br(id='Br9', style={'display': 'none'}),

        html.P(id='p_date',children='Date', style={'font-family': 'cursive', 'font-size': '15px', 'color': colors['text'],'display': 'none'}),
        dcc.DatePickerSingle(
            id='date_picker',
            min_date_allowed=datetime.date(1990, 1, 1),
            date=datetime.date.today(),
            with_portal=True,
            style={'display': 'none'}
        ),
        html.Br(id='Br10', style={'display': 'none'}),
        html.Br(id='Br11', style={'display': 'none'}),
        dbc.Button("Submit", id="submit", color="primary",block=True, style={'display': 'none'}),
    ],
    width=3,
    style={'max-width': '21%'},
    className='side_panel'
)


layout_transactions=html.Div(
    [
        dbc.Row(
            [
                side_panel,
                dbc.Col(
                    [
                        html.Div(
                            [
                                default_transactions_table
                            ],
                            style={'width':'100%', 'margin-left': '24px'}
                        ),
                        html.Div(id='hidden_div',style={'display':'none'})

                    ],
                    width=9,
                    style={'margin-top': '2rem'}
                ),
            ]
        ),
        dcc.Interval(id="interval2", interval=12000),
    ],
    id='transactions',
    style={'backgroundColor':colors['bg_color']}
)

#-----------------------------------------------callbacks------------------------------------
@app.callback(
    [
        Output('p_amount', 'style'),
        Output('amount', 'style'),
        Output('Br1', 'style'),
        Output('Br2','style'),
        Output('p_exchange','style'),
        Output('exchange_dd', 'style'),
        Output('Br3','style'),
        Output('p_symbol', 'style'),
        Output('symbol_dd','style'),
        Output('Br4', 'style'),
        Output('p_QTY','style'),
        Output('QTY','style'),
        Output('Br5', 'style'),
        Output('Br6', 'style'),
        Output('p_PPS','style'),
        Output('PPS','style'),
        Output('Br7', 'style'),
        Output('Br8', 'style'),
        Output('p_risk','style'),
        Output('risk_dd','style'),
        Output('Br9','style'),
        Output('p_date','style'),
        Output('date_picker','style'),
        Output('Br10', 'style'),
        Output('Br11', 'style'),
        Output('submit','style')
    ],
    [
        Input('transaction_type_dd', 'value')
    ]
)
def update_sidebar_layout(transaction_type):
    if transaction_type== 'Deposit' or transaction_type=='Withdrawal':
        return {'font-family': 'cursive', 'font-size': '15px', 'color': colors['text']}, {},{},{},{'display': 'none'},\
               {'display': 'none', 'background-color': colors['bg_color']},{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},\
               {'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},\
               {'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},\
               {'font-family': 'cursive', 'font-size': '15px', 'color': colors['text']}, {},{},{},{}
    elif transaction_type== 'Buy' or transaction_type=='Sell':
        return {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'font-family': 'cursive','font-size': '15px','color': colors['text']},\
        {'background-color': colors['bg_color']}, {}, {'font-family': 'cursive', 'font-size': '15px', 'color': colors['text']}, {'background-color': colors['bg_color']}, {}, {'font-family': 'cursive', 'font-size': '15px', 'color': colors['text']},\
        {}, {}, {}, {'font-family': 'cursive', 'font-size': '15px', 'color': colors['text']}, {}, {}, {}, {'font-family': 'cursive', 'font-size': '15px', 'color': colors['text']},\
        {'background-color': colors['bg_color']},{},{'font-family': 'cursive', 'font-size': '15px', 'color': colors['text']}, {}, {}, {}, {}

    else:
        return {'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none', 'background-color': colors['bg_color']},{'display': 'none'},{'display': 'none'},\
        {'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},\
        {'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'}, \
        {'display': 'none'}


@app.callback(
    [
        Output('symbol_dd', 'options'),
        Output('symbol_dd','disabled')
    ],
    [
        Input('exchange_dd', 'value'),

    ]
)
def select_symbols_list(exchange):
    if exchange == 'TSX':
        return [{'label':tsx_stocks.loc[i,'Company Name']+'('+tsx_stocks.loc[i,'Symbol']+')', 'value': i} for i in range(len(tsx_stocks))], False
    elif exchange == 'TSXV':
        return [{'label':tsxv_stocks.loc[i,'Company Name']+'('+tsxv_stocks.loc[i,'Symbol']+')', 'value': i} for i in range(len(tsxv_stocks))], False
    else:
        return [{'label': tsx_stocks.loc[i, 'Company Name'] + '(' + tsx_stocks.loc[i, 'Symbol'] + ')', 'value': i} for i in range(len(tsx_stocks))], True



@app.callback(
    Output('transactions_table','data'),
    [
        Input('submit','n_clicks')
    ],
    [
        State('currency_radioItems','value'),
        State('transaction_type_dd', 'value'),
        State('amount', 'value'),
        State('exchange_dd', 'value'),
        State('symbol_dd','value'),
        State('QTY','value'),
        State('PPS','value'),
        State('risk_dd','value'),
        State('date_picker','date')
    ]
)
def update_transactions_table(n_click, currency,transaction_type,deposit_withdrawal_amount, exchange, symbol_index, QTY, PPS, risk, date):
    if transaction_type== 'Deposit' or transaction_type=='Withdrawal':
        new_row = pd.DataFrame([[date, currency,transaction_type,None,None,None,None,None,deposit_withdrawal_amount,None]], columns=transactions_table_columns)
        new_row.to_csv(os.path.join(PATH_DATA, 'transactions.csv'), mode='a', header=False, index=False)
        full_data=pd.read_csv(os.path.join(PATH_DATA,'transactions.csv'))
        return full_data.to_dict('records')
    elif transaction_type == 'Buy' or transaction_type == 'Sell':
        if exchange == 'TSX':
            symbol=tsx_stocks.loc[symbol_index, 'Symbol']
            company_name=tsx_stocks.loc[symbol_index, 'Company Name']
            total_value=round(QTY*PPS,2)
        elif exchange == 'TSXV':
            symbol = tsxv_stocks.loc[symbol_index, 'Symbol']
            company_name = tsxv_stocks.loc[symbol_index, 'Company Name']
            total_value = round(QTY * PPS, 2)
        # ---------------calculations of transactions table---------
        new_row = pd.DataFrame([[date,currency,transaction_type,exchange, company_name, symbol,QTY,PPS,total_value,risk]], columns=transactions_table_columns)
        new_row.to_csv(os.path.join(PATH_DATA, 'transactions.csv'), mode='a', header=False, index=False)
        full_data = pd.read_csv(os.path.join(PATH_DATA, 'transactions.csv'))
        #----------------calculations of portfolio table------------
        # new_row = pd.DataFrame([[symbol, exchange, company_name, sector, company_name, symbol, QTY, PPS, total_value, risk]], columns=stocks_table_columns)
        # [ 'Symbol', 'Exchange', 'Company Name', 'Sector', 'QTY', 'Cost Per Share', 'Current Price', 'Book Value',
        #  'Market Value', 'Profit/Loss', '% Return']


        return full_data.to_dict('records')
    else:

        if 'transactions.csv' in os.listdir(PATH_DATA):
            return pd.read_csv(os.path.join(PATH_DATA, 'transactions.csv')).to_dict('records')
        else:
            pd.DataFrame(columns=transactions_table_columns).to_csv(os.path.join(PATH_DATA, 'transactions.csv'), index=False)
            return pd.read_csv(os.path.join(PATH_DATA, 'transactions.csv')).to_dict('records')



@app.callback(
    Output('hidden_div', 'style'),
    [
        Input('transactions_table','data')
    ],
    [
        State('transactions_table', 'data_previous')
    ]
)
def print_datatable_data(data_table, data_table_previous):

    if (data_table_previous != None) and (len(data_table_previous)> len(data_table)) and data_table != []:
        pd.DataFrame(data_table).to_csv(os.path.join(PATH_DATA, 'transactions.csv'),index=False)
    elif (data_table_previous != None) and (len(data_table_previous)> len(data_table)) and data_table == []:
        pd.DataFrame(columns=transactions_table_columns).to_csv(os.path.join(PATH_DATA, 'transactions.csv'), index=False)

    return {'display':'none'}