# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from simulation import container
from dash.dependencies import Input, Output, State
import json


d = {'time': [], 'value': [], 'condition': []}

old_amounts = {'susceptible': 0, 'dead': 0, 'recovered': 0}

box = container.Container(size=20, population=0, time_to_live=0,
                          action_interval=0, move_dist_length=0)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
        dcc.Interval(
            id='interval-component',
            interval=1*1000,
            n_intervals=0,
            disabled=True
        ),
        html.H1('SIR simulation - IBM ESI',
                style={'textAlign': 'center', 'border': '', 'padding': '10px'}),
        html.Div([
            html.Div([
                html.H6('Simulation Set Up'),
                html.Table([
                        html.Tr([
                            html.Td([
                                html.Label('Population', htmlFor='population-amount'),
                                dcc.Input(id='population-amount',
                                          type='number',
                                          placeholder='population amount',
                                          value=100, style={'width': '468px'})
                            ], colSpan=2)
                        ]),
                        html.Tr([
                            html.Td([
                                html.Label('Susceptible amount', htmlFor='susceptible-amount'),
                                dcc.Input(id='susceptible-amount',
                                          type='number',
                                          placeholder='susceptible amount',
                                          value=90)
                            ]),
                            html.Td([
                                html.Label('Infected amount', htmlFor='infected-amount'),
                                dcc.Input(id='infected-amount',
                                          type='number',
                                          placeholder='infected amount',
                                          value=10)
                            ])
                        ]),
                        html.Tr([
                            html.Td([
                                html.Label('Recovered amount', htmlFor='recovered-amount'),
                                dcc.Input(id='recovered-amount',
                                          type='number',
                                          placeholder='recovered amount',
                                          value=0),
                            ]),
                            html.Td([
                                html.Label('Dead amount', htmlFor='dead-amount'),
                                dcc.Input(id='dead-amount',
                                          type='number',
                                          placeholder='dead amount',
                                          value=0),
                            ])
                        ]),
                    ], id='configuration-table'),
            ]),
            html.Div([
                    html.Table([
                        html.Tr([
                            html.Td([
                                html.Label('Infection probability', htmlFor='infection-probability'),
                                dcc.Slider(id='infection-probability',
                                           min=0,
                                           max=1,
                                           step=0.1,
                                           value=0.4,
                                           marks={
                                                 0: {'label': '0'},
                                                 1: {'label': '1'}
                                           })
                            ], style={'width': '80%'}),
                            html.Td([
                                html.P('0.000', id='inf-prob-value')
                            ]),
                        ]),
                        html.Tr([
                            html.Td([
                                html.Label('Recover probability', htmlFor='recover-probability'),
                                dcc.Slider(id='recover-probability',
                                           min=0,
                                           max=0.5,
                                           step=0.001,
                                           value=0.005,
                                           marks={
                                               0: {'label': '0'},
                                               0.5: {'label': '0.5'}
                                           })
                            ]),
                            html.Td([
                                html.P('0', id='rec-prob-value')
                            ]),
                        ]),
                        html.Tr([
                            html.Td([
                                html.Label('Dead probability', htmlFor='dead-probability'),
                                dcc.Slider(id='dead-probability',
                                           min=0,
                                           max=0.5,
                                           step=0.001,
                                           value=0.001,
                                           marks={
                                               0: {'label': '0'},
                                               0.5: {'label': '0.5'}
                                           })
                            ]),
                            html.Td([
                                html.P('0', id='dead-prob-value')
                            ]),
                        ]),
                        html.Tr([
                            html.Td([
                                html.Label('Infection range', htmlFor='infection-range'),
                                dcc.Slider(id='infection-range',
                                           min=0,
                                           max=1,
                                           step=0.1,
                                           value=1,
                                           marks={
                                               0: {'label': '0'},
                                               1: {'label': '1'}
                                           })
                            ]),
                            html.Td([
                                html.P('0', id='inf-range-value')
                            ]),
                        ]),
                        html.Tr([
                            html.Td([
                                html.Label('Move length', htmlFor='move-length'),
                                dcc.Slider(id='move-length',
                                           min=0,
                                           max=1,
                                           step=0.1,
                                           value=0.5,
                                           marks={
                                               0: {'label': '0'},
                                               1: {'label': '1'}
                                           })
                            ]),
                            html.Td([
                                html.P('0', id='move-dist-value')
                            ]),
                        ])
                    ], style={'width': '468px'}),
                    html.Div([
                        html.Button('Start', id='start-button', n_clicks=0),
                        html.Button('Stop', id='stop-button', n_clicks=0),
                        html.Button('Continue', id='continue-button', n_clicks=0),
                        html.Button('Reset', id='reset-button', n_clicks=0),
                    ], style={'display': 'flex', 'justify-content': 'center', 'padding': '5px'})

            ])
        ], style={'display': 'flex', 'justify-content': 'space-evenly'}),
        html.Div([
            html.Div([
                html.Table(id='current-population-amount', style={
                })
            ]),
            html.Div(
                html.Table(id='additional-parameters')),
        ], style={'display': 'flex', 'justify-content': 'space-evenly'}),



        html.Div(
            dcc.Graph(id='live-population'), style={'marginTop': '20px'}),
        html.Div([
            dcc.Graph(id='move-population'),
            dcc.Graph(id='population-percent'),
        ], style={'display': 'flex', 'justify-content': 'space-evenly', 'marginTop': '20px'}),
        dcc.Store(id='simulation-data')
    ])


@app.callback(Output('inf-prob-value', 'children'),
              [Input('infection-probability', 'value')])
def update_slider(value):
    return value


@app.callback(Output('rec-prob-value', 'children'),
              [Input('recover-probability', 'value')])
def update_slider(value):
    return value


@app.callback(Output('dead-prob-value', 'children'),
              [Input('dead-probability', 'value')])
def update_slider(value):
    return value


@app.callback(Output('inf-range-value', 'children'),
              [Input('infection-range', 'value')])
def update_slider(value):
    return value


@app.callback(Output('move-dist-value', 'children'),
              [Input('move-length', 'value')])
def update_slider(value):
    return value


@app.callback(Output('simulation-data', 'data'),
              [Input('interval-component', 'n_intervals')])
def simulation_begin(n_intervals: int) -> json:
    """
    Function than handling generate simulation data end execute
    Container.simulation() method in every second of simulation.

    Parameters
    ---------
    n_intervals: int, required
        Number of passed intervals from begin of simulation. Generated
        with dash object dcc.Interval.

    Returns
    -------
    Function return Container.object_list each instance x, y and condition
    parameters in key "individuals" and each population group amount in key
    "groups" in JSON format.
    """

    data = {'individuals': [], 'groups': {'susceptible': 0, 'infected': 0,
                                          'recovered': 0, 'dead': 0}}

    for instance in box.object_list:
        data['individuals'].append({'x': instance.x, 'y': instance.y,
                                    'condition': instance.current_condition})

    data['groups'] = dict(susceptible=box.count_susceptible(), infected=box.count_infected(),
                          recovered=box.count_recovered(), dead=box.count_dead())

    box.simulation()

    return json.dumps(data)


@app.callback(Output('interval-component', 'disabled'),
              [Input('start-button', 'n_clicks'),
               Input('continue-button', 'n_clicks'),
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
def simulation_controls(btn_start: int, btn_continue: int, btn_stop: int, btn_reset: int,
                        population_amount: int, susceptible_amount: int, infected_amount: int,
                        recovered_amount: int, dead_amount: int, infection_probability: float,
                        recover_probability: float, dead_probability: float, infection_range: float,
                        move_length: float) -> bool:
    """
    Function handling simulation events like start, stop, continue, reset.

    Parameters
    ----------
        btn_start: int, required
            Clicks amount of button for start simulation event.
        btn_continue: int, required
            Clicks amount of button for continue simulation event.
        btn_stop: int, required
            Clicks amount of button for stop simulation event.
        btn_reset: int, required
            Clicks amount of button for reset simulation event.
        population_amount: int, required
            This parameters store amount of max count of population based objects.
        susceptible_amount: int, required
            Amount of susceptible instances to place in container.
        infected_amount: int, required
            Amount of infected instances to place in container.
        recovered_amount: int, required
            Amount of infected instances to place in container.
        dead_amount: int, required
            Amount of dead instances to place in container.
        infection_probability: float, required
            Instance probability to get infected.
        recover_probability: float, required
            Instance probability to get recovered.
        dead_probability: float, required
            Instance probability to die.
        infection_range: float, required
            Area in witch infected instance can infect susceptible instances.
        move_length: float, required
            Length in which instances inside container could move.

    Returns
    -------
    Based on selected event return True or False for dcc.Interval object's attribute
    'disabled'. If event is Stop, Reset returns True, if Start, Continue returns
    False.
    """

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
        old_amounts['susceptible'] = susceptible_amount
        old_amounts['recovered'] = recovered_amount
        old_amounts['dead'] = dead_amount
        return False

    if button_id == 'stop-button' or box.count_infected() <= 0:
        return True

    if button_id == 'continue-button':
        return False

    if button_id == 'reset-button':
        d['condition'] = []
        d['time'] = []
        d['value'] = []

        box.population = 0
        box.initial_set_up(0, 0, 0, 0, 0, 0, 0, 0)
        box.object_list = []

        return True

    return True


@app.callback(Output('live-population', 'figure'),
              [Input('interval-component', 'n_intervals'),
               Input('simulation-data', 'data')])
def update_graph_live(n_intervals: int, json_data: json) -> 'plotly_express.line':
    """
    Function handling scatter graph for each individual instance move in
    grid.

    Parameters
    ----------
    n_intervals: int, required
        Number of passed intervals from begin of simulation. Generated
        with dash object dcc.Interval.
    json_data: json, required
        JSON contain data of simulation.

    Returns
    -------
    Return plolty express line chart with information of current amount of
    each group in simulation.
    """

    data = json.loads(json_data)

    d['time'].append(n_intervals)
    d['value'].append(data['groups']['susceptible'])
    d['condition'].append('susceptible')
    d['time'].append(n_intervals)
    d['value'].append(data['groups']['infected'])
    d['condition'].append('infected')
    d['time'].append(n_intervals)
    d['value'].append(data['groups']['recovered'])
    d['condition'].append('recovered')
    d['time'].append(n_intervals)
    d['value'].append(data['groups']['dead'])
    d['condition'].append('dead')

    df = pd.DataFrame(data=d)

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
        'yaxis': {'title': 'People amount'},
        'template': 'plotly_dark'
    })
    fig.update_traces({
        'marker': {'line': {'width': 26}}
    })

    return fig


@app.callback(Output('move-population', 'figure'),
              [Input('interval-component', 'n_intervals'),
               Input('simulation-data', 'data')])
def update_graph_move(n_intervals: int, json_data: json) -> 'plotly.express.scatter':
    """
    Function handling scatter graph for each individual instance move in
    grid.

    Parameters
    ---------
    n_intervals: int, required
        Number of passed intervals from begin of simulation. Generated
        with dash object dcc.Interval.
    json_data: json, required
        JSON contain data of simulation.

    Returns
    -------
    Return plolty express scatter chart with placed instances in grid.
    """

    data = json.loads(json_data)
    cords = {'x': [], 'y': [], 'condition': []}

    for element in data['individuals']:
        cords['x'].append(element['x'])
        cords['y'].append(element['y'])
        cords['condition'].append(element['condition'])

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
        'width': 800,
        'height': 800,
        'template': 'plotly_dark'
    })

    return fig


@app.callback(Output('population-percent', 'figure'),
              [Input('interval-component', 'n_intervals'),
               Input('simulation-data', 'data')])
def update_population_percent(n_intervals: int, json_data: json) -> 'plotly.express.pie':
    """
    Function handling pie chart with percent value of each group in population.

    Parameters
    ----------
    n_intervals: int, required
        Number of past intervals.
    json_data: json, required
        JSON contain data of simulation.
        
    Returns
    -------
    Plotly express object pie chart.
    """

    data = json.loads(json_data)
    percent = {'condition': [], 'percent_value': []}

    percent['condition'].append('susceptible')
    percent['percent_value'].append(data['groups']['susceptible'])
    percent['condition'].append('infected')
    percent['percent_value'].append(data['groups']['infected'])
    percent['condition'].append('recovered')
    percent['percent_value'].append(data['groups']['recovered'])
    percent['condition'].append('dead')
    percent['percent_value'].append(data['groups']['dead'])

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
        'title': {'text': 'Percent of population in each group', 'font': {'size': 30}},
        'template': 'plotly_dark'
    })
    return fig


@app.callback(Output('current-population-amount', 'children'),
              [Input('interval-component', 'n_intervals'),
               Input('simulation-data', 'data')])
def update_population_amount(n_intervals: int, json_data) -> 'html table':
    """
    Function handling display html table with amount of each group.

    Parameters
    ----------
    n_intervals: int, required
        Number of past intervals.
    json_data: json, required
        JSON contain data of simulation.

    Returns
    -------
    Html table base od bash html.Table object.
    """

    data = json.loads(json_data)
    return [html.Thead(html.Tr([html.Td('Condition'), html.Td('Amount')])),
            html.Tr([html.Td('Susceptible'), html.Td(data['groups']['susceptible'])]),
            html.Tr([html.Td('Infected'), html.Td(data['groups']['infected'])]),
            html.Tr([html.Td('Recovered'), html.Td(data['groups']['recovered'])]),
            html.Tr([html.Td('Dead'), html.Td(data['groups']['dead'])])]


@app.callback(Output('additional-parameters', 'children'),
              [Input('interval-component', 'n_intervals'),
              Input('simulation-data', 'data')],
              [State('susceptible-amount', 'value')])
def parameter_update(n_intervals: int, json_data: json, susceptible_amount: int) -> 'html table':
    """
    Function handling display html table with additional parameters q and R0.

    Parameters
    ----------
    n_intervals: int, required
        Number of past intervals.
    json_data: json, required
        JSON contain data of simulation.
    susceptible_amount: int, required
        Start number of susceptible.

    Returns
    -------
    Html table base od bash html.Table object with parameter q and R0.
    """

    data = json.loads(json_data)
    change_susceptible = data['groups']['susceptible'] - old_amounts['susceptible']
    change_d = abs(old_amounts['dead'] - data['groups']['dead'])
    change_r = abs(old_amounts['recovered'] - data['groups']['recovered'])
    change_removed = change_d + change_r
    r_parameter = 0
    a_parameter = 1
    q_parameter = 0
    r_0 = 0

    if data['groups']['susceptible'] > 0 and data['groups']['infected'] > 0:
        r_parameter = -change_susceptible / (data['groups']['susceptible'] * data['groups']['infected'])

    if data['groups']['infected'] > 0 and data['groups']['dead'] > 0 and data['groups']['recovered'] > 0:
        a_parameter = change_removed * (1 / data['groups']['infected'] * (data['groups']['dead'] +
                                                                          data['groups']['recovered']))

    if a_parameter > 0:
        q_parameter = r_parameter / a_parameter
        r_0 = (r_parameter * susceptible_amount) / a_parameter

    q_parameter = round(q_parameter, 2)
    r_0 = round(r_0, 2)

    old_amounts['susceptible'] = data['groups']['susceptible']
    old_amounts['dead'] = data['groups']['dead']
    old_amounts['recovered'] = data['groups']['recovered']

    # Note: Pandemic R0 parameter highlight
    if r_0 > 1.5:
        table = [html.Thead(html.Tr([html.Td('Parameter'), html.Td('Value')])),
                 html.Tr([html.Td('R'), html.Td(r_0)], style={'backgroundColor': 'red'}),
                 html.Tr([html.Td('q'), html.Td(q_parameter)])]
    else:
        table = [html.Thead(html.Tr([html.Td('Parameter'), html.Td('Value')])),
                 html.Tr([html.Td('R'), html.Td(r_0)]),
                 html.Tr([html.Td('q'), html.Td(q_parameter)])]

    return table


if __name__ == '__main__':
    app.run_server(debug=True)
