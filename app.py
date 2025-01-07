import dash
from dash import Dash, html, dcc, callback, State, Input, Output, ctx
import dash_ag_grid as dag
import pandas as pd

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True)

# ________________________________________________________________________LAYOUT_________________________________________________________________________________

app.layout = html.Div(
    [
        html.Div(
            [
                html.H1(
                    children="The civilization 6 Dashboard",
                ),
                html.Div(
                    [
                        dcc.Link(
                            children=html.Div(
                                [
                                    f"{page['name']}" 
                                    
                                ]
                            ),
                            href=page["relative_path"]
                        ) for page in dash.page_registry.values()
                    ]
                )   
            ]
        ),
        dash.page_container
    ]
)

# ________________________________________________________________________CALLBACK_________________________________________________________________________________

# ________________________________________________________________________RUN APP_________________________________________________________________________________

if __name__ == "__main__" :
    app.run(debug=True)