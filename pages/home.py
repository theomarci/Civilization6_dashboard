import dash
from dash import Dash, html, dcc, callback, State, Input, Output, ctx
import dash_ag_grid as dag
import pandas as pd

dash.register_page(__name__, path="/")

# ________________________________________________________________________LAYOUT_________________________________________________________________________________

layout = html.Div (
    [
        html.H1(
            children="I'm the Home page !"
        )
    ]
)

# ________________________________________________________________________CALLBACK_________________________________________________________________________________