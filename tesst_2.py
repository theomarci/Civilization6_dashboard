import dash
from dash import Dash, html, Output, Input, State, callback, dcc, ctx
import dash_ag_grid as dag

app = Dash(__name__)

# Column definitions
cities_columns = [
    {"field": "Name", "editable": True, "cellDataType": "text"},
    {"field": "Population", "editable": True, "cellDataType": "number"},
    {"field": "Truth", "editable": True, "cellEditor": "agSelectCellEditor", "cellEditorParams": {"values": ["True", "False"],}}
]

# Initial data
data = [
    {"Name": "Paris", "Population": 1},
    {"Name": "Nantes", "Population": 1},
]

app.layout = html.Div(
    [
        dcc.Store(
            id="cities_save",
            data=[],
            storage_type="session"
        ),
        dcc.Interval(
            id="Inter-val",
            interval=2000,
        ),
        dag.AgGrid(
            id="table_test",
            rowData=None,
            columnDefs=cities_columns,
        ),
        html.Button(
            id="button",
            children="J'aime le chocolat",
            n_clicks=0
        ),
        html.Button(
            id="Tiny_button",
            children="Sauvegaaaaaaaaaaarde",
            n_clicks=0
        ),
        html.Button(
            id="But on",
            children="Charge ment",
            n_clicks=0,
        )
    ]
)

# For the next time I need to test intervall to update automatically without push button
# when load or reload page, If data is none --> no update
# If there data saved in dcc<.store then data load from session storage
# interval_max must be define in 1 and interval count at 0 that load one time
# but after a moment fix in interval every modification made in the grid is saved in dcc.store session storage
#  The goal is to update data automatically without need to push button.

# _________________________________________________________ADD, SAVE, LOAD BUTTONS WORK _________________________________________________________________________  

# @callback(
#         Output("cities_save", "data"),
#         Input("Tiny_button", "n_clicks"),
#         State("table_test", "rowData"),
#         prevent_initial_call=True,
# )
# def save_data(n_clicks, data):
#     return data

# @callback(
#     Output("table_test", "rowData"),
#     Input("button", "n_clicks"),
#     Input("But on", "n_clicks"),
#     State("cities_save", "data"),
#     State("table_test", "rowData"),
#     prevent_initial_call=True
# )
# def add_row(n_clicks, n_clicks2, data, rowData):
#     print("aïe !")
#     if ctx.triggered_id == "button":
#             print("new row")
#             newRow = {
#                 "Name": "",
#                 "Population": 0
#             }
#             updatedRow = rowData + [newRow]
#             return updatedRow
#     elif ctx.triggered_id == "But on":
#          return data

# ___________________________________________________________________________________________________________________________________________________________________________

# Add row and retrieving data when the app is launch
@callback(
        Output("table_test", "rowData"),
        Input("button", "n_clicks"),
        State("table_test", "rowData"),
        State("cities_save", "data"),  
)
def interaction(n_clicks, data, citySaveData):   
    if ctx.triggered_id == None :
        return citySaveData
    elif ctx.triggered_id == "button":
        newRow = {
            "Name": "Paris" + " " + "Nantes",
            "Population": 0,
            "Truth": None,
        }
        updatedRow = data + [newRow]
        return updatedRow
# save data of my cities table automatically
@callback(
    Output("cities_save", "data"),
    Input("Inter-val", "n_intervals"),
    State("table_test", "rowData"),
    prevent_initial_call=True,
)
def save_data(n_intervals, data) :
    return data


if __name__ == "__main__":
    app.run(debug=True)