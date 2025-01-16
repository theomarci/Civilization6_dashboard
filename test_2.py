import dash
from dash import Dash, html, Output, Input, State, callback, dcc, ctx
import dash_ag_grid as dag

app = Dash(__name__)

# Column definitions
cities_columns = [
    {"field": "Name", "editable": True, "cellDataType": "text"},
    {"field": "Population", "editable": True, "cellDataType": "number"},
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
            storage_type="session"
        ),
        dag.AgGrid(
            id="table_test",
            rowData=[],
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

@callback(
        Output("cities_save", "data"),
        Input("Tiny_button", "n_clicks"),
        State("table_test", "rowData"),
        prevent_initial_call=True,
)
def save_data(n_clicks, data):
    return data

@callback(
    Output("table_test", "rowData"),
    Input("button", "n_clicks"),
    Input("But on", "n_clicks"),
    State("cities_save", "data"),
    State("table_test", "rowData"),
    prevent_initial_call=True
)
def add_row(n_clicks, n_clicks2, data, rowData):
    print("aïe !")
    if ctx.triggered_id == "button":
            print("new row")
            newRow = {
                "Name": "",
                "Population": 0
            }
            updatedRow = rowData + [newRow]
            return updatedRow
    elif ctx.triggered_id == "But on":
         return data

if __name__ == "__main__":
    app.run(debug=True)