import datetime
from sgs import get_serie 
from dash import Dash, html, dcc, dash_table, Output, Input
import dash_bootstrap_components as dbc
import dash_ag_grid as dag

app = Dash(__name__,
        serve_locally=False,
        compress=False)

columnDefs = [
    {"headerName": "Data", "field": "data", "type": "dateColumn", "filter": "agDateColumnFilter", "sortable": True, "resizable": True, "width": 150},
    {"headerName": "Valor", "field": "valor", "type": "numberColumn", "filter": "agNumberColumnFilter", "sortable": True, "resizable": True, "width": 150}
]

layout=[
    html.H1("Plotly dash deployed on AWS Lambda"),
    html.Div("This is a simple Dash application running on AWS Lambda."),
    html.Div([
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='serie_name',
                    options=[
                        {'label': 'CDI (%a.d.)', 'value': '12'},
                        {'label': 'CDI (%a.a.)', 'value': '4392'},
                        {'label': 'Salário mínimo', 'value': '1619'},
                        {'label': 'SELIC meta (%a.a.)', 'value': '432'},
                        {'label': 'IPCA', 'value': '433'},
                        {'label': 'INCC (%a.m)', 'value': '192'}
                    ],
                    value='12'
                ),
            width=6),
            dbc.Col(
                dcc.DatePickerRange(
                    id='date-picker-range',
                    start_date=datetime.date.today().strftime('%Y-01-01'),
                    end_date=datetime.date.today().strftime('%Y-%m-%d'),
                    display_format='DD/MM/YYYY'
                ),
            width=6),
        ])
    ]),
    dag.AgGrid(
        id='table',
        className="ag-theme-alpine-dark",
        defaultColDef={"filter": True},
        columnDefs=columnDefs,
        columnSize="sizeToFit",
        dashGridOptions={"animateRows": False},
        style={"height": 400, "width": "70%",  "margin": "auto"},
    ),
    dbc.Row([
        dbc.Col(html.Div([
            dash_table.DataTable(
                fixed_rows={'headers': True},
                style_table={'height': '300px', 'width': '50%', 'overflowY': 'auto'},
                style_cell_conditional=[
                    {'if': {'column_id': 'data'},
                        'width': '130px'},
                ])
            ]), md=4
        ),
    ], justify="center")

]
@app.callback(
    Output('table', 'rowData'),
    [Input('serie_name', 'value'),
    Input('date-picker-range', 'start_date'),
    Input('date-picker-range', 'end_date')])
def update_table(serie_code, start_date, end_date):
    ts = get_serie(serie_code, start_date, end_date)
    return ts.to_dict(orient='records')

app.layout = layout

if __name__ == "__main__":
    app.run(debug=True)