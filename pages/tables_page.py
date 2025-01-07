import dash
from dash import Dash, html, dcc, callback, State, Input, Output, ctx
import dash_ag_grid as dag
import pandas as pd

dash.register_page(__name__)

# ________________________________________________________________________DATAFRAME_________________________________________________________________________________


genDf = pd.DataFrame()

cityDf = pd.DataFrame()

miliDf = pd.DataFrame()

wondersDf = pd.DataFrame()

# ________________________________________________________________________DEFINITION OF COLUMNS_________________________________________________________________________________

                                        # ----------GENERAL COLUMNS----------
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

                                        # ----------CITY COLUMNS----------
cities_columns = [
    {"field": "currentTurn"},
    {"field": "Name"},
    {"field": "foundationDate"},
    {"field": "Population"},
    {"field": "strategicRessources"},
    {"field": "luxuryRessources"}
]

                                        # ----------MILITARY COLUMNS----------

military_columns = [
    {"field": "Name"},
    {"field": "Type"},
    {"field": "Power"}
]

                                        # ----------WONDER COLUMNS----------

wonder_columns = [
    {"field": "Name"},
    {"field": "turnNumber"},
    {"field": "constructionDate"},
    {"field": "type"}
]

# ________________________________________________________________________LAYOUT_________________________________________________________________________________

layout = html.Div(
    [
        html.Div(
            [
                # Data save component
                dcc.Store(
                    id="memory_dash_AGrid_value"
                ),
                # Title
                html.H4(
                    children="The table page :"
                ),
                # Tables selection
                dcc.Tabs(
                    id='tabs',
                    value="general_table",
                    children=[
                        dcc.Tab(label="General table", value="genTable"),
                        dcc.Tab(label="Cities table", value="cityTab"),
                        dcc.Tab(label="military Table", value="miliTable"),
                        dcc.Tab(label="Wonders table", value="wondersTable")
                    ]
                ),
            ]
        ),
        html.Br(),
        # Display table
        html.Div(
            id="display_table"
            ),
    ]
)


# ________________________________________________________________________CALLBACK_________________________________________________________________________________

                                        # ----------TAB COMPONENT----------

@callback(
    Output("display_table", "children"),
    Input("tabs", "value"),
)
def display_table(value):
    if value == "genTable" :
        return  dag.AgGrid(
                id="display_general_table",
                rowData=genDf.to_dict("records"),
                columnDefs=general_columns,
                columnSize="sizeToFit",
                defaultColDef={
                                    "editable": True,
                                    "wrapHeaderText": True,
                                    "autoHeaderHeight": True,
                                },
                getRowId="params.data.currentTurn",
            ),
    elif value == "cityTab" :
        return html.Div(
            [
                dag.AgGrid(
                id="display_cities_table",
                rowData=cityDf.to_dict("records"),
                columnDefs=cities_columns,
                columnSize="sizeToFit",
                defaultColDef={
                    "editable": True,
                    "wrapHeaderText": True,
                    "autoHeaderHeight": True,
                },
                getRowId="params.data.currentTurn",
                persistence=True,
                persistence_type="session",
            ),
            html.Br(),
            # Add rows button
            html.Button(
                    id="add_row_button",
                    children="Add row",
                    n_clicks=0,
                ),
            ]
        ),
    elif value == "miliTable" :
        return dag.AgGrid(
            id="display_military_table",
            rowData=miliDf.to_dict("records"),
            columnDefs=military_columns,
            columnSize="sizeToFit",
            defaultColDef={
                "editable": True,
                "wrapHeaderText": True,
                "autoHeaderHeight": True,
            },
            getRowId="params.data.Name",
        ),
    elif value == "wondersTable" :
        return dag.AgGrid(
            id="display_wonders_table",
            rowData=wondersDf.to_dict("records"),
            columnDefs=wonder_columns,
            columnSize="sizeToFit",
            defaultColDef={
                "editable": True,
                "wrapHeaderText": True,
                "autoHeaderHeight": True,
            },
            getRowId="params.data.Name"
        ),

                                        # ----------ADD ROW BUTTON----------

@callback(
    Output("display_cities_table", "rowData"),
    Input("add_row_button", "n_clicks"),
    State("display_cities_table", "rowData"),
    prevent_initial_call=True,
)
def add_city_row(add, data) :
    if data is None :
        data=[]
    new_row = {
        "currentTurn": len(data)+1,
        "Name": "0",
        "foundationDate": "0",
        "Population": 0,
        "strategicRessources": "0",
        "luxuryRessources": "0",
    }
    updated_data = data + [new_row]
    return updated_data