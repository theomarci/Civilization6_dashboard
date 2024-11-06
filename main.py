from dash import Dash, html, dash_table, dcc
import pandas as pd

# Project's objective : Display a dashboard that show the progression during a Civilization 6 game from differents caracteristic.
# to create that, I must to define some steps that give me a way to follow.
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

# Step 3 : Initialize the app

app = Dash()

# Step 3 : Elaborate the dash Layout to organise the web page with html and dash components

app.layout = html.Div([
    html.Div([
        html.H1(children="Civilization 6 Dashboard")
    ])
])
# step 4 : write the callback that I need
# Step 5 : Define function update and other
# Step 6 : Launch the app

if __name__ == '__main__' :
    app.run(debug=True)