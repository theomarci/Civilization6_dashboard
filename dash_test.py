from dash import Dash, html, dash_table, dcc, callback, State, Input, Output
import dash_ag_grid as dag
import pandas as pd

# Project's objective : Display a dashboard that show the progression during a Civilization 6 game from differents caracteristic
# to create that, I must to define some steps that give me a way to follow
# I'll build several datasets

# ________________________________________________________________DICTIONNARIES____________________________________________________________________________

# Stept 1 : create dictionnaries, name the title for each columns but their are no values for the moment.

general_dict = {
    "Current turn" : [],
    "Money" : [],
    "Faith" : [],
    "Income / turn" : [],
    "Faith / turn" : [],
    "Science / turn" : [],
    "Culture / turn" : [],
    "Military power (sum of units power)" : [],
    "Renowned person" : [],
    "Number of city" : [],
    "Population total" : [],
    "Number of wonder" : []
}

city_dict = {
    "Name" : [],
    "Built (turn)" : [],
    "Population" : [],
    "Ressources" : [],
    "City's faith" : []
}

# ______________________________________________________________DATASET___________________________________________________________________________________

# Step 2 : Creation of the datasets (General and cities dataset)

general_df = pd.DataFrame(general_dict)

city_df = pd.DataFrame(city_dict)

# _____________________________________________________________DASH______________________________________________________________________________________

# I've decided to change the direction of my app after discovering AG Grid which can help me to build, edit, and delete table more easily
#  Initialization of my app

app = Dash(__name__)



# ----------------------------------------------------------LAYOUT---------------------------------------------------------------------------------------

# I create here the layout which organize my page with html call

app.layout = (
    html.Div([
        # main title
        html.Div([
            html.H1(
                children='Civilization 6 Dashboard :',
                style={
                    'textAlign': 'center',
                    'color': 'Red'
                }
            )
        ]),
        # general table
        html.Div([
            # text and introduction
            html.Div([
                html.H3(
                    children='General table : ', 
                    style={
                        'textAlign': 'center',
                        'color': 'blue'
                    }
                ),
                html.P(children='A short text')
            ]),
            # Table
            html.Div([
                dag.AgGrid(
                    id='gen_table',
                    rowData=general_df.to_dict("records"),
                    columnDefs=[
                        {"field" : i, 'editable': True} for i in general_df.columns
                    ]
                )
            ]),
            html.Br(),
            # add or delete row buttons
            html.Div([
                html.Button(children='Add row', id='add-row-button', n_clicks=0),
                html.Button(children='Delete row', id='delete-row-button', n_clicks=0)
            ])
        ])
    ])
)

# -------------------------------------------------------CALLBACK----------------------------------------------------------------------------------------------------------

if __name__ == '__main__' :
    app.run(debug=True)