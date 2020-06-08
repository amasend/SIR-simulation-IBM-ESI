# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from simulation import container
from dash.dependencies import Input, Output

d = {'time': [], 'value': [], 'condition': []}


box = container.Container(size=20, population=200, time_to_live=10,
                          action_interval=1, move_dist_length=0.5)

box.initial_set_up(number_of_susceptible=110, number_of_infected=90,
                   number_of_recovered=0, number_of_dead=0,
                   infection_probability=0.4, recover_probability=0.005,
                   dead_probability=0.001, infection_range=1)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='live-population'),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,
        max_intervals=120,
        n_intervals=0
    ),
    dcc.Graph(id='move-population'),
])


# Multiple components can update everytime interval gets fired.
@app.callback(Output('live-population', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n_intervals):

    d['time'].append(n_intervals)
    d['value'].append(box.count_susceptible())
    d['condition'].append('susceptible')
    d['time'].append(n_intervals)
    d['value'].append(box.count_infected())
    d['condition'].append('infected')
    d['time'].append(n_intervals)
    d['value'].append(box.count_recovered())
    d['condition'].append('recovered')
    d['time'].append(n_intervals)
    d['value'].append(box.count_dead())
    d['condition'].append('dead')

    df = pd.DataFrame(data=d)

    box.simulation()

    fig = px.line(df, x='time', y='value', color='condition')
    fig.update_layout({
        'title': {'text': 'Each group amount in given time of simulation', 'font': {'size': 30}},
        'xaxis': {'title': 'Simulation time'},
        'yaxis': {'title': 'People amount'}
    })
    fig.update_traces({
        'marker': {'line': {'width': 26}}
    })
    return fig


@app.callback(Output('move-population', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_move(n_intervals):
    cords = {'x': [], 'y': [], 'condition': []}
    for element in box.object_list:
        cords['x'].append(element.x)
        cords['y'].append(element.y)
        cords['condition'].append(element.current_condition)

    df2 = pd.DataFrame(data=cords)

    fig = px.scatter(df2, x='x', y='y', color='condition')
    fig.update_traces({
        'marker': {'size': 12}
    })
    fig.update_layout({
        'title': {'text': 'Population move', 'font': {'size': 30}},
        'xaxis': {'title': 'Width', 'fixedrange': True},
        'yaxis': {'title': 'Height', 'fixedrange': True}
    })

    fig.for_each_trace(
        lambda trace: trace.update(marker_color='RoyalBlue') if trace.name == 'infected' else (),
    )

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
