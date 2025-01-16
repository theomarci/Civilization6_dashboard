import dash
from dash import Dash, html, dcc, callback, State, Input, Output, ctx
import dash_ag_grid as dag
import pandas as pd

app = Dash()

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
    {"field": "Id", "hide": True, "cellDataType": "number"},
    {"field": "currentTurn", "editable": True,"cellDataType": "number"},
    {"field": "Name", "editable": True, "cellDataType": "text"},
    {"field": "foundationDate", "editable": True, "cellDataType": "text"},
    {"field": "Population", "editable": True, "cellDataType": "number"},
]

                                        # ----------MILITARY COLUMNS----------

military_columns = [
    {"field": "Id", "hide": True, "cellDataType": "numer"},
    {"field": "Name", "editable": True, "cellDataType": "text"},
    {"field": "hireDate", "editable": True, "cellDataType": "text"},
    {"field": "Type", "editable": True, "cellDataType": "text"},
    {"field": "Power", "editable": True, "cellDataType": "number"}
]

                                        # ----------WONDER COLUMNS----------

wonder_columns = [
    {"field": "Id", "hide": True, "cellDataType": "number"},
    {"field": "Name", "editable": True, "cellDataType": "text"},
    {"field": "turnNumber", "editable": True, "cellDataType": "number"},
    {"field": "constructionDate", "editable": True, "cellDataType": "text"},
    {"field": "type", "editable": True, "cellDataType": "text"}
]

                                        # ----------WONDER COLUMNS----------

ressources_columns = [
    {"field": "Id", "hide": True, "cellDataType": "number"},
    {"field": "City", "editable": True, "cellDataType": "text"},
    {"field": "Type", "editable": True}
]

# ________________________________________________________________________LAYOUT_________________________________________________________________________________

app.layout = html.Div(
    [
        html.Div(
            [
                # ----------STORE DATA----------
                dcc.Store(
                    id="general_data_save",
                    data=[],
                    storage_type="session",
                ),
                dcc.Store(
                    id="cities_data_save",
                    data=[],
                    storage_type="session",
                ),
                dcc.Store(
                    id="military_data_save",
                    data=[],
                    storage_type="session",
                ),
                dcc.Store(
                    id="wonder_data_save",
                    data=[],
                    storage_type="session",
                ),
                # ----------TITLE----------
                dcc.Interval(
                    id="interval",
                    interval=2000,
                ),
                # ----------TITLE----------
                html.H4(
                    children="The table page :"
                ),
                # ----------TABLE SELECTION----------
                dcc.Tabs(
                    id='tabs',
                    value="tables",
                    children=[
                        # --> GENERAL TABLES TAB (the player'empire global overview)
                        dcc.Tab(
                                label="general_table",
                                children=[
                                    html.Div(
                                        [
                                            dag.AgGrid(
                                            id="display_general_table",
                                            rowData=None,
                                            columnDefs=general_columns,
                                            columnSize="sizeToFit",
                                            defaultColDef={
                                                            "editable": True,
                                                            "wrapHeaderText": True,
                                                            "autoHeaderHeight": True,
                                                        },
                                                    getRowId="params.data.currentTurn",
                                                ),
                                                html.Br(),
                                                html.Button(
                                                    id="general_button",
                                                    children="Add row",
                                                    n_clicks=0,
                                                )                                           
                                            ]
                                        )
                                    ]
                                ),
                        # --> CITIES TABLE TAB (list all player's empire cities with some details) 
                        dcc.Tab(
                            label="Cities table", 
                            children=[
                                html.Div(
                                    [
                                        dag.AgGrid(
                                            id="display_cities_table",
                                            rowData=None,
                                            columnDefs=cities_columns,
                                            columnSize="sizeToFit",
                                            persistence=True,
                                            persistence_type="session",
                                            persisted_props=["rowData"],
                                        ),
                                        html.Br(),
                                        html.Button(
                                            id="cities_button",
                                            children="Add new row",
                                            n_clicks=0,
                                        )
                                    ]
                                )
                            ]
                            ),
                        # --> MILITARY TABLE TAB (list all units withs details possessed by a player)
                        dcc.Tab(
                            label="military Table", 
                            children=[
                                html.Div(
                                    [
                                        dag.AgGrid(
                                            id="display_military_table",
                                            rowData=None,
                                            columnDefs=military_columns,
                                            columnSize="sizeToFit",
                                            defaultColDef={
                                                "wrapHeaderText": True,
                                                "autoHeaderHeight": True,
                                            },
                                            getRowId="params.data.Name",
                                        ),
                                        html.Br(),
                                        html.Button(
                                            id="military_button",
                                            children="Add row",
                                            n_clicks=0,
                                        ),
                                    ]
                                )
                            ]
                            ),
                        #  --> WONDERS TABLE TAB (list all wonders built by a player)
                        dcc.Tab(
                            label="Wonders table", 
                            children=[
                                html.Div(
                                    [
                                        dag.AgGrid(
                                            id="display_wonders_table",
                                            rowData=None,
                                            columnDefs=wonder_columns,
                                            columnSize="sizeToFit",
                                            defaultColDef={
                                                "editable": True,
                                                "wrapHeaderText": True,
                                                "autoHeaderHeight": True,
                                            },
                                            getRowId="params.data.Name"
                                        ),
                                        html.Br(),
                                        html.Button(
                                            id="wonder_button",
                                            children="Add row",
                                            n_clicks=0,
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
            ]
        ),
        html.Br(),
        # ----------DISPLAY TABLE----------
        html.Div(
            id="display_table"
            ),
        # ----------TEST DATA----------
        html.Div(id="output"),
    ]
)


# ________________________________________________________________________CALLBACK_________________________________________________________________________________

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                            # __________GENERAL TABLE__________

# ---------GENERAL OUTPUT CALLBACK----------
@callback(
        Output("display_general_table", "rowData"),
        Input("general_button", "n_clicks"),
        State("general_data_save", "data"),
        State("display_general_table", "rowData")
)
def generalOutput(clicks, data, rowData):
    # --> LOAD DATA : loading data from the session storage
    if ctx.triggered_id == None :
        return data
    # --> ADD NEW ROW : button that create on the grid a new row 
    elif ctx.triggered_id == "general_button":
        newRow = {
            "currentTurn": len(rowData)+1,
            "currentDate": None,
            "currentMoney": None,
            "income/Turn": None,
            "currentFaith": None,
            "faith/Turn": None,
            "science/Turn": None,
            "culture/Turn": None,
            "numberOfCity": None,
            "populationTotal": None,
            "renownedPerson": None,
            "numberOfWonder": None,
            "militaryPower": None,
        }
        updateRow = rowData + [newRow]
        return updateRow
    
# ---------GENERAL UPDATE DATA CALLBACK----------
 # --> Update data add in the grid to the session storage 
@callback(
        Output("general_data_save", "data"),
        Input("interval", "n_intervals"),
        State("display_general_table", "rowData"),
        prevent_initial_call=True,
)
def generalUpdate(interval, data):
    return data

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                             # __________CITIES TABLE__________

# ---------CTIES OUTPUT CALLBACK----------
@callback(
    Output("display_cities_table", "rowData"),
    Input("cities_button", "n_clicks"),
    State("display_cities_table", "rowData"),
    State("cities_data_save", "data"),
)
def citiesOutput(clicks, rowData, data) :
    # --> LOAD DATA : loading data from the session storage
    if ctx.triggered_id == None :
        return data
    # --> ADD NEW ROW : button that create on the grid a new row 
    elif ctx.triggered_id == "cities_button":
        newRow = {
            "Id": len(rowData)+1,
            "currentTurn": None,
            "Name": None,
            "foundationDate": None,
            "Population": None
        }
        updatedRow = rowData + [newRow]
        return updatedRow
    
# ---------CTIES UPDATE DATA CALLBACK----------
 # --> Update data add in the grid to the session storage 
@callback(
    Output("cities_data_save", "data"),
    Input("interval", "n_intervals"),
    State("display_cities_table", "rowData"),
    prevent_initial_call=True,
)
def citiesUpdate(intervals, data):
    return data

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                            # __________MILITARY TABLE__________

# ---------MILITARY OUTPUT CALLBACK----------
@callback(
    Output("display_military_table", "rowData"),
    Input("military_button", "n_clicks"),
    State("military_data_save", "data"),
    State("display_military_table", "rowData"),
)
def militaryOutput(clicks, data, rowData):
    # --> LOAD DATA : loading data from the session storage
    if ctx.triggered_id == None:
        return data
    # --> ADD NEW ROW : button that create on the grid a new row 
    elif ctx.triggered_id == "military_button":
        newRow = {
            "Id": len(rowData) + 1,
            "Name": None,
            "hireDate": None,
            "Type": None,
            "Power": None
        }
        updateRow = rowData + [newRow]
        return updateRow
    
 # ---------MILITARY UPDATE DATA CALLBACK----------   
  # --> Update data add in the grid to the session storage 
@callback(
    Output("military_data_save", "data"),
    Input("interval", "n_intervals"),
    State("display_military_table", "rowData"),
    prevent_initial_call=True,
)
def militaryUpdate(interval, data):
    return data

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                            # __________WONDER TABLE__________

# ---------WONDER OUTPUT CALLBACK----------
@callback(
    Output("display_wonders_table", "rowData"),
    Input("wonder_button", "n_clicks"),
    State("wonder_data_save", "data"),
    State("display_wonders_table", "rowData"),
)
def wonderOutput(clicks, data, rowData):
    # --> LOAD DATA : loading data from the session storage
    if ctx.triggered_id == None :
        return data
    # --> ADD NEW ROW : button that create on the grid a new row 
    elif ctx.triggered_id == "wonder_button":
        newRow = {
            "Id": len(rowData) + 1,
            "Name": None,
            "turnNumber": None,
            "constructionDate": None,
            "type": None
        }
        updateRow = rowData + [newRow]
        return updateRow
    
 # ---------WONDER UPDATE DATA CALLBACK---------- 
 # --> Update data add in the grid to the session storage 
@callback(
    Output("wonder_data_save", "data"),
    Input("interval", "n_intervals"),
    State("display_wonders_table", "rowData"),
    prevent_initial_call=True,
)
def wonderUpdate(interval, data):
    return data

# ________________________________________________________________________RUN APP_________________________________________________________________________________

if __name__ == "__main__" :
    app.run(debug=True)