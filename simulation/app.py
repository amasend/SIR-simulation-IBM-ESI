# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from simulation import container
from dash.dependencies import Input, Output, State

d = {'time': [], 'value': [], 'condition': []}
box = container.Container(size=20, population=0, time_to_live=0,
                          action_interval=0, move_dist_length=0)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('SIR simulation - IBM ESI',
            style={'textAlign': 'center'}),
    html.Div([
        html.H6('Simulation Set Up'),
        dcc.Input(id='population-amount',
                  type='number',
                  placeholder='population amount'),
        dcc.Input(id='susceptible-amount',
                  type='number',
                  placeholder='susceptible amount'),
        dcc.Input(id='infected-amount',
                  type='number',
                  placeholder='infected amount'),
        dcc.Input(id='recovered-amount',
                  type='number',
                  placeholder='recovered amount'),
        dcc.Input(id='dead-amount',
                  type='number',
                  placeholder='dead amount'),
    ]),
    html.Div([
        dcc.Input(id='infection-probability',
                  type='number',
                  placeholder='infection probability'),
        dcc.Input(id='recover-probability',
                  type='number',
                  placeholder='recover probability'),
        dcc.Input(id='dead-probability',
                  type='number',
                  placeholder='dead probability'),
        dcc.Input(id='infection-range',
                  type='number',
                  placeholder='infection-range'),
        dcc.Input(id='move-length',
                  type='number',
                  placeholder='move length'),
    ], style={'width': '80%', 'margin:': '0 auto'}),
    html.Div([
        html.Button('Start', id='start-button', n_clicks=0),
        html.Button('Stop', id='stop-button', n_clicks=0),
        html.Button('Reset', id='reset-button', n_clicks=0),
    ]),
    html.Div([
        dcc.Graph(id='live-population', style={
            'width': '80%', 'float': 'left'
        }),
        html.Table(id='current-population-amount', style={
            'width': '20%', 'float': 'left'
        })
    ]),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,
        n_intervals=0,
        disabled=True
    ),
    html.Div([
        dcc.Graph(id='move-population', style={
            'width': '50%', 'float': 'left'
        }),
        dcc.Graph(id='population-percent', style={
            'width': '50%', 'float': 'left'
        }),
    ])
])


@app.callback(Output('interval-component', 'disabled'),
              [Input('start-button', 'n_clicks'),
               Input('stop-button', 'n_clicks'),
               Input('reset-button', 'n_clicks')],
              [State('population-amount', 'value'),
               State('susceptible-amount', 'value'),
               State('infected-amount', 'value'),
               State('recovered-amount', 'value'),
               State('dead-amount', 'value'),
               State('infection-probability', 'value'),
               State('recover-probability', 'value'),
               State('dead-probability', 'value'),
               State('infection-range', 'value'),
               State('move-length', 'value'),
               ])
def simulation_controls(btn_start, btn_stop, btn_reset, population_amount, susceptible_amount, infected_amount,
                        recovered_amount, dead_amount, infection_probability, recover_probability,
                        dead_probability, infection_range, move_length):
    ctx = dash.callback_context

    if not ctx.triggered:
        button_id = 'No clicks yet'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'start-button':
        box.population = population_amount
        box.move_distance_length = move_length
        box.initial_set_up(number_of_susceptible=susceptible_amount,
                           number_of_infected=infected_amount,
                           number_of_recovered=recovered_amount,
                           number_of_dead=dead_amount,
                           infection_probability=infection_probability,
                           recover_probability=recover_probability,
                           dead_probability=dead_probability,
                           infection_range=infection_range)
        return False

    if button_id == 'stop-button':
        return True

    if button_id == 'reset-button':
        return False

    if box.count_infected() == 0:
        return True

    return True


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

    fig = px.line(df, x='time', y='value', color='condition',
                  color_discrete_map={
                      'susceptible': 'blue',
                      'infected': 'red',
                      'recovered': 'green',
                      'dead': 'gray'
                  })
    fig.update_layout({
        'title': {'text': 'Each group amount in given time of simulation',
                  'font': {'size': 30}},
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

    fig = px.scatter(df2, x='x', y='y', color='condition',
                     color_discrete_map={
                        'susceptible': 'blue',
                        'infected': 'red',
                        'recovered': 'green',
                        'dead': 'gray'
                     }, category_orders={'condition': ['susceptible', 'infected',
                                                       'recovered', 'dead']})
    fig.update_traces({
        'marker': {'size': 10}
    })
    fig.update_layout({
        'title': {'text': 'Population move', 'font': {'size': 30}},
        'xaxis': {'title': 'Width'},
        'yaxis': {'title': 'Height'},
        'autosize': False,
        'width': 600,
        'height': 600
    })
    print("Move")
    return fig


@app.callback(Output('population-percent', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_population_percent(n_intervals):
    percent = {'condition': [], 'percent_value': []}

    percent['condition'].append('susceptible')
    percent['percent_value'].append(box.count_susceptible())
    percent['condition'].append('infected')
    percent['percent_value'].append(box.count_infected())
    percent['condition'].append('recovered')
    percent['percent_value'].append(box.count_recovered())
    percent['condition'].append('dead')
    percent['percent_value'].append(box.count_dead())

    df = pd.DataFrame(data=percent)

    fig = px.pie(df, values='percent_value', names='condition', color='condition',
                 color_discrete_map={
                        'susceptible': 'blue',
                        'infected': 'red',
                        'recovered': 'green',
                        'dead': 'gray'
                 })
    fig.update_traces()
    fig.update_layout({
        'title': {'text': 'Percent of population in each group', 'font': {'size': 30}}
    })
    return fig


@app.callback(Output('current-population-amount', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_population_amount(n_intervals):
    return [html.Thead(html.Tr([html.Td('Condition'), html.Td('Amount')])),
            html.Tr([html.Td('Susceptible'), html.Td(box.count_susceptible())]),
            html.Tr([html.Td('Infected'), html.Td(box.count_infected())]),
            html.Tr([html.Td('Recovered'), html.Td(box.count_recovered())]),
            html.Tr([html.Td('Dead'), html.Td(box.count_dead())])]


if __name__ == '__main__':
    app.run_server(debug=True)
