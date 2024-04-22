import dash
from dash import dcc
# from dash_extensions.enrich import DashProxy
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

# Initialize Dash app
app = dash.Dash(__name__)

# External CSS
# external_stylesheets = ['/assets/styles.css']

# External sensor data
sensor_data = [1, 2, 3, 4, 5]  # Example data

# Layout
app.layout = html.Div([
    # Header
    html.Div([
        html.H1("Data Dashboard",style={'textAlign': 'center'})
    ]),

    # Main content
    html.Div([
        # Left column for External sensor data
        html.Div([
            html.H2("Sensor Data",style={'textAlign': 'center'}),
            dcc.Graph(
                id='sensor-graph',
                figure={
                    'data': [
                        go.Scatter(
                            x=list(range(len(sensor_data))),
                            y=sensor_data,
                            mode='lines+markers',
                            name='Sensor Data'
                        )
                    ],
                    'layout': go.Layout(
                        title='Sensor Data',
                        xaxis={'title': 'Time'},
                        yaxis={'title': 'Value'}
                    )
                },
                style={'display': 'flex', 'justifyContent': 'left', 'alignItems': 'left', 'height': '100vh'}
            )
        ], className='six columns'),  # Half of the row width

        html.Div(children=[
        html.Div([
        # Realtime Video Stream from External Notebook
        html.Div([
            html.H2("Video Stream", style={'textAlign': 'center','width': '50%' }),
            html.Iframe(src='http://external-notebook-url:port', width='600', height='500',
                       # style={'display': 'flex', 'justifyContent': 'center',  } 
                       )
        ], className='six columns'),  # Half of the row width
    ], className='row',style={'width': '50%', 'display': 'inline-block', 'justifyItems': 'center', 'alignSelf': 'center',}), 

    # Camera module with Realtime Stream
    html.Div([
        html.Div([
            html.H2(" Camera Output", style={'textAlign': 'center','width': '50%'}),
            html.Iframe(src='http://camera-stream-url:port', width='600', height='500',
            # style={'display': 'flex', 'justifyContent': 'center', , }
            )
            ], className='six columns'),
        ], className='row', style={'width': '50%', 'display': 'inline-block', 'justifyItems': 'center','alignSelf': 'auto', }),  # Half of the row width
        # middle portion
        ]) 
    ]),
    

# Empty Space or Additional Content
        html.Div([
            html.H2("Empty Space or Additional Content",
        style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'right', 'height': '100vh'})
        ], className='six columns'),  # Half of the row width
    
])

# replace 'http://external-notebook-url:port' and 'http://camera-stream-url:port' with the actual URLs where your video streams are hosted.

if __name__ == '__main__':
    app.run_server(debug=True)
