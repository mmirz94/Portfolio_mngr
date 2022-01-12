import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import os
import numpy as np
import pandas as pd
import pathlib
import dash_table
import dash_charts
import plotly.express as px
import plotly.graph_objects as go
from dash.dash import no_update
import datetime
import yfinance as yf
import time
from dash_table.Format import Format, Group

#####################################
PATH = pathlib.Path(__file__).parent
PATH_DATA=os.path.join(PATH,"assets")
colors={
    'bg_color':'#383e45',
    'text':'#ffffff',
    'heading':'#0404cf'
}
########################################### defaults ###########################################
# stocks_table_columns=['Symbol', 'Exchange', 'Company Name', 'Sector', 'QTY', 'Cost Per Share', 'Current Price', 'Book Value', 'Market Value', 'Profit/Loss', '% Return']
stocks_table_columns = [
    {'id': 'Symbol','name': 'Symbol'},{'id': 'Exchange','name': 'Exchange'},{'id': 'Company Name','name': 'Company Name'}, {'id': 'Sector','name': 'Sector'},
    {'id': 'QTY','name': 'QTY',  'type': 'numeric', 'format': Format(precision=8, group=Group.yes, groups=3, group_delimiter=',',decimal_delimiter='.')},
    {'id': 'Cost Per Share', 'name': 'Cost Per Share', 'type': 'numeric', 'format': Format(precision=8, group=Group.yes, groups=3, group_delimiter=',', decimal_delimiter='.')},
    {'id': 'Current Price', 'name': 'Current Price', 'type': 'numeric', 'format': Format(precision=8, group=Group.yes, groups=3, group_delimiter=',', decimal_delimiter='.')},
    {'id': 'Book Value', 'name': 'Book Value', 'type': 'numeric', 'format': Format(precision=8, group=Group.yes, groups=3, group_delimiter=',', decimal_delimiter='.')},
    {'id': 'Market Value', 'name': 'Market Value', 'type': 'numeric', 'format': Format(precision=8, group=Group.yes, groups=3, group_delimiter=',', decimal_delimiter='.')},
    {'id': 'Profit/Loss', 'name': 'Profit/Loss', 'type': 'numeric', 'format': Format(precision=8, group=Group.yes, groups=3, group_delimiter=',', decimal_delimiter='.')},
    {'id': '% Return', 'name': '% Return', 'type': 'numeric', 'format': Format(precision=8, group=Group.yes, groups=3, group_delimiter=',', decimal_delimiter='.')},
]
transactions_table_columns=['Date', 'Currency', 'Transaction Type', 'Exchange', 'Company Name', 'Symbol', 'QTY', 'Cost Per Share', 'Total Amount', 'Risk']
tsx_stocks = pd.read_csv(os.path.join(PATH_DATA, 'TSX_Symbols.csv'))
tsxv_stocks = pd.read_csv(os.path.join(PATH_DATA,'TSXV_Symbols.csv'))

default_stocks_table= dash_table.DataTable(
                    id='stocks_table',
                    columns = stocks_table_columns,
                    sort_action="native",
                    sort_mode="multi",
                    row_selectable="multi",
                    row_deletable=False,
                    selected_rows=[0,1,2,3],
                    style_table={'height': '389px', 'overflowY': 'auto'},
                    style_header={'backgroundColor': colors['heading'], 'fontWeight': 'bold', 'font_family': 'cursive','font_size': '17px', 'textAlign': 'center', 'color':colors['text']},
                    style_data={'font_family': 'cursive', 'font_size': '14px', 'textAlign': 'center'},
                    # style_cell={'backgroundColor':colors['bg_color'], 'color':colors['text']}, #for dark cells
                    # style_cell_conditional=[
                        # {
                        #     'if': {'column_id': c},
                        #     'textAlign': 'left'
                        # } for c in ['#', 'Symbol', 'Exchange', 'Company name', 'Sector']
                    # ],

                    style_data_conditional=[
                        {
                            'if': {'row_index': 'odd'},
                            'backgroundColor': 'rgb(220,224,230)'
                        },
                        {
                            'if': {
                                'filter_query': '{Profit/Loss} > 0',
                                'column_id': 'Profit/Loss'
                            },
                            'color': '#40cc1d',
                        },
                        {
                            'if': {
                                'filter_query': '{Profit/Loss} < 0',
                                'column_id': 'Profit/Loss'
                            },
                            'color': '#f53936',
                        },

                        {
                            'if': {
                                'filter_query': '{% Return} > 0',
                                'column_id': '% Return'
                            },
                            'color': '#40cc1d',
                        },
                        {
                            'if': {
                                'filter_query': '{% Return} < 0',
                                'column_id': '% Return'
                            },
                            'color': '#f53936',
                        },

                        # {
                        #     'if': {
                        #         'filter_query': '{% Return} contains "▲"',
                        #         'column_id': '% Return'
                        #     },
                        #     'color': '#40cc1d',
                        # },
                        #
                        # {
                        #     'if': {
                        #         'filter_query': '{% Return} contains "▼"',
                        #         'column_id': '% Return'
                        #     },
                        #     'color': '#f53936',
                        # },
                    ],
                    )

default_transactions_table= dash_table.DataTable(
                    id='transactions_table',
                    columns = [{"name": i, "id": i} for i in transactions_table_columns],
                    sort_action="native",
                    sort_mode="multi",
                    row_deletable=True,
                    style_table={'height': '600px', 'overflowY': 'auto'},
                    # data=pd.read_csv(os.path.join(PATH_DATA, 'transactions.csv')).to_dict('records'),
                    style_header={'backgroundColor': colors['heading'], 'fontWeight': 'bold', 'font_family': 'cursive','font_size': '17px', 'textAlign': 'center', 'color':colors['text']},
                    style_data={'font_family': 'cursive', 'font_size': '14px', 'textAlign': 'center'},
                    # style_cell={'backgroundColor':colors['bg_color'], 'color':colors['text']}, #for dark cells
                    # style_cell_conditional=[
                        # {
                        #     'if': {'column_id': c},
                        #     'textAlign': 'left'
                        # } for c in ['#', 'Symbol', 'Exchange', 'Company name', 'Sector']
                    # ],

                    style_data_conditional=[
                        {
                            'if': {'row_index': 'odd'},
                            'backgroundColor': 'rgb(220,224,230)'
                        },

                    ],
                    )
########################################### functions ##########################################
def compute_dividend(symbol):
    dividends = yf.Ticker(symbol).dividends
    if len(dividends) != 0:
        dividends = dividends[-2:].reset_index()
        if dividends.loc[1, 'Date'] - dividends.loc[0, 'Date'] > datetime.timedelta(days=40):
            return dividends.loc[1, 'Dividends'] * 4
        else:
            return dividends.loc[1, 'Dividends'] * 12
    else:
        return 0
#------------------------------------------

