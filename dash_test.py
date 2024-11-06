from dash import Dash, html, dcc, Input, Output, callback
import pandas as pd
import plotly.express as px

app = Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        ['Théo', 'Elias', 'Agathe', 'Karina'], 'Elias', id='Name-dropdown'
    ),
    html.H1(
        style={
            'textAlign' : 'center',
            'color': 'red'
        },
        id='output-dropdown'
    ),
    html.Br(),
    html.Br(),
    html.Div([
        html.P(
            children="I happy to show my work with dash and plotly.",
            style={
                'textAlign' : 'center'
            }
        )
    ])
])

@callback(
    Output('output-dropdown', 'children'),
    Input('Name-dropdown', 'value')
)
def update_output(value) :
    return f"Hello {value} ! "

if __name__ == '__main__':
    app.run(debug=True)