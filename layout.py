from dash import dash_table
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State 
import dash_bootstrap_components as dbc

from app import app

import openfda 

df = openfda.get_data(None)

df = df[["medical_specialty","medical_specialty_description","device_class","product_code", "device_name"]]
df.sort_values(by=["medical_specialty","device_class","product_code"], inplace=True, ascending=True)

specialty_list = df["medical_specialty_description"].unique().tolist()


options = [{"label":x, "value":x} for x in specialty_list]
print(options)

filter_row =  dbc.Row(
    [
        dbc.Col(
            html.Label("Medical Specialty"), 
            width=3, 
            style={"text-align":"left", "padding-right":0}
        ),

        dbc.Col(
            dcc.Dropdown(
                id="medical_specialty",
                options=options, 
                value=None,
                style={"text-align":"centre"}
            ),
            width=6, 
            style={"text-align":"centre", "padding-right":0}
        ),
    ]
)


data_table = dash_table.DataTable(
    id='output_table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
    page_size=10,
    filter_action="native",
    sort_action="native",
    sort_mode="multi",
    page_action="native",
    style_cell={
        'whiteSpace': 'normal',
        'height': 'auto',
        'textAlign': 'right',
        'padding': '10px'
    },
    style_as_list_view=True,
    style_header={'backgroundColor': 'azure', 'fontWeight': 'bold'},
)


table_row = dbc.Row(
    [
        dbc.Col(dcc.Loading(
            type="default",
            children=data_table)
        ), 
    ], align="center", style={"margin-bottom": "10px"},
)

main = dbc.Card(
    [
        dbc.CardHeader(
            filter_row
        ),
        dbc.CardBody(
            data_table
        ), 
    ],
    outline=True
)


@app.callback(
    Output("output_table", "data"),
    Output("output_table", "columns"),
    Input("medical_specialty", "value")
)
def update_output_div(specialty):

    df = openfda.get_data(specialty)

    df = df[["medical_specialty","medical_specialty_description","device_class","product_code", "device_name"]]
    df.sort_values(by=["medical_specialty","device_class","product_code"], inplace=True, ascending=True)
    
    return df.to_dict('records'), [{"name": i, "id": i} for i in df.columns]