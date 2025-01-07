from dash import Dash, html, dcc, callback, State, Input, Output, ctx
import dash_ag_grid as dag
import pandas as pd
import json


# This app will display a dashboard to analyse Civilization 6 game data of a player, that will help user to take decision or just for the fun.
# Main features : 
#         - multi pages
#         -save and load data
#         -editing rows
#         -selecting graph 
# When a user create a new save, there are no data in my tables. Therefore, user need to have the possibility to add or delete rows. Then, He write inside the cells values for 
# each columns. My data will be displayed on a graph fill by data's user.
# I think to create 3 differents tables :
#                                     - general
#                                     - city
#                                     - military

#  _____________________________________________________________TABLE OF CONTENT______________________________________________________________________________________

                                                                    # COLUMNS :
                                                                        # LINK :42
                                                                    # LAYOUT : 
                                                                        # LINK :85
                                                                    # CALLBACK :
                                                                        # LINK :181
                                                                            # add, delete, update :
                                                                                # LINK :185
                                                                            # data test :
                                                                                # LINK :224
                                                                            # download :
                                                                                # LINK :235

# _____________________________________________________________DASH___________________________________________________________________________________________________

# Initialize Dash app :

app = Dash()

df = pd.DataFrame()

# ____________________________________________________________COLUMNS_________________________________________________________________________________________________

# Here, I define the columns for my tables :

general_columns = [
    {"field": "currentTurn", "headerName": "Current Turn", "cellDataType": "number"},
    {"field": "currentDate", "headerName": "Current Date", "cellDataType": "text"},
    {"field": "currentMoney", "headerName": "Current Money", "cellDataType": "number"},
    {"field": "income/Turn", "headerName": "Income / Turn", "cellDataType": "number"},
    {"field": "currentFaith", "headerName": "Current Faith", "cellDataType": "number"},
    {"field": "faith/Turn", "headerName": "Faith / Turn", "cellDataType": "number"},
    {"field": "science/Turn", "headerName": "Science / Turn", "cellDataType": "number"},
    {"field": "culture/Turn", "headerName": "Culture / Turn", "cellDataType": "number"},
    {"field": "numberOfCity", "headerName": "Number of City", "cellDataType": "number"},
    {"field": "populationTotal", "headerName": "Population Total", "cellDataType": "number"},
    {"field": "renownedPerson", "headerName": "Renowned Person", "cellDataType": "number"},
    {"field": "numberOfWonder", "headerName": "Number of Wonder", "cellDataType": "number"},
    {"field": "militaryPower", "headerName": "Military Power", "cellDataType": "number"},
]

city_columns = [
    {"field": "Name"},
    {"field": "foundationDate"},
    {"field": "Number"},
    {"field": "strategicRessources"},
    {"field": "luxuryRessources"}
]

military_columns = [
    {"field": "Name"},
    {"field": "Type"},
    {"field": "Power"}
]

wonder_columns = [
    {"field": "turnNumber"},
    {"field": "Name"},
    {"field": "constructionDate"},
    {"field": "type"}
]

# _____________________________________________________________LAYOUT__________________________________________________________________________________________________

# LINK :1 

# In this phase, I build and organize my web pages.

app.layout = html.Div(
        [
            # main title
            html.Div(
                [
                    html.H1(
                children="Civilization 6 Dashboard :",
                style={
                    "textAlign": "center",
                    "color": "Red"
                }
            )
        ]
    ),
           # general table title and description
           html.Div(
            [
                html.Div(
                    [
                        html.H3(
                            children="General Table : ",
                            style={
                                "textAlign": "center",
                                "color": "Blue"
                            }
                        ),
                        html.P(
                            children="A short text"
                        )
                    ]
                ),
                html.Br(),
                # general table 
                html.Div(
                    [
                        dag.AgGrid(
                            id="gen_table",
                            rowData=df.to_dict("records"),
                            columnDefs=general_columns,
                            columnSize="sizeToFit",
                            defaultColDef={
                                "editable": True,
                                "wrapHeaderText": True,
                                "autoHeaderHeight": True,
                            },
                            csvExportParams={
                                "fileName": "Civilization6_data_save_V",
                            },
                            getRowId="params.data.currentTurn",
                        ),
                        html.Div(
                            [
                                html.Button(
                                    children="Add row", 
                                    id="add-row-button", 
                                    n_clicks=0
                                )
                            ]
                        ),
                        html.Br(),
                        # display data to test
                        html.Div(
                            [
                                html.Div(
                                    id="output"
                                )
                            ]
                        ),
                        html.Br(),
                        # Download button
                        html.Div(
                            [
                                html.Button(
                                    id="download_data",
                                    children="dowload data",
                                    n_clicks=0,
                                )
                            ]
                        ),
                        # Graph
                        html.Div(
                            [
                                # Columns selection
                                html.Div(
                                    [
                                        dcc.Dropdown(
                                            id="select_turn_or_date",
                                            options=[
                                                {"label": "Current Turn", "value": "currentTurn"},
                                                {"label": "Current Date", "value": "currentDate"},
                                            ],
                                        ),
                                        dcc.Dropdown(
                                            id="abscissa_columns_selected",
                                            options=[
                                                {"label": "Current money", "value": "currentMoney"},
                                                {"label": "Income / turn", "value": "income/Turn"},
                                                {"label": "Current Faith", "value": "currentFaith"},
                                                {"label": "Faith / turn", "value": "faith/Turn"},
                                                {"label": "Science / turn", "value": "science/Turn"},
                                                {"label": "Culture / turn", "value": "culture/Turn"},
                                                {"label": "Number of city", "value": "numberOfCity"},
                                                {"label": "Population total", "value": "populationTotal"},
                                                {"label": "Renowned person", "value": "renownedPerson"},
                                                {"label": "Number  of wonder", "value": "numberOfWonder"},
                                                {"label": "Military power", "value": "militaryPower"},
                                            ],
                                        ),
                                        html.Div(
                                            id="value_selected_output"
                                        ),
                                        html.Div(
                                            id="value_selected_output_2"
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)

# _____________________________________________________________CALLBACK__________________________________________________________________________________________________

# LINK :1

                # ----------------------------------------ADD,DELETE,UPDATE----------------------------------------

# callback that add, delete and update rows

@callback(
    Output("gen_table", "rowData"),
    Input("add-row-button", "n_clicks"),
    State("gen_table", "rowData"),
    prevent_initial_call=True,
)
def add_delete_rows(add, data):
    if ctx.triggered_id == "add-row-button":
        if data is None :
            data = []
        new_row = {
                    "currentTurn": len(data)+1,
                    "currentDate": "0",
                    "currentMoney": 0,
                    "income/Turn": 0,
                    "currentFaith": 0,
                    "faith/Turn": 0,
                    "science/Turn": 0,
                    "culture/Turn": 0,
                    "numberOfCity": 0,
                    "populationTotal": 0,
                    "renownedPerson": 0,
                    "numberOfWonder": 0,
                    "militaryPower": 0,
                }
        updated_data = data + [new_row]
        return updated_data

                # ----------------------------------------DATA TEST----------------------------------------

@callback(
        Output("output", "children"),
        Input("gen_table", "cellValueChanged"),
        Input("gen_table", "rowData"),
)
def update(cell_change, data) :
    return f"{data}"

                # ----------------------------------------EXPORT DATA----------------------------------------

@callback(
    Output("gen_table", "exportDataAsCsv"),
    Input("download_data", "n_clicks"),
)
def export_data(n_clicks):
    if n_clicks :
        return True
    return False

                # ----------------------------------------SELECT ORDINATE----------------------------------------

@callback(
    Output("value_selected_output", "children"),
    Input("select_turn_or_date", "value"),
    State("gen_table", "rowData"),
)
def select_value(ord, table) :
    print(ord)
    # ordinate
    ordinate_value = []
    for y in table :
        current_value = y[ord]
        ordinate_value.append(current_value)
    return f"You've selected {ord} and this is all values of this column {ordinate_value}"

                # ----------------------------------------SELECT ABSCISSA----------------------------------------

@callback(
    Output("value_selected_output_2", "children"),
    Input("abscissa_columns_selected", "value"),
    State("gen_table", "rowData"),
)
def select_abscissa(abs, table) :
    # abscissa
    abscissa_value = []
    for x in table :
        current_abs = x[abs]
        abscissa_value.append(current_abs)
    return f"You've selected {abs} and this is all values of this column {abscissa_value}"

# _____________________________________________________________RUN APP_________________________________________________________________________________________________

if __name__ == "__main__":
    app.run(debug=True)

# LINK :1