import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from simulation import container
from prediction import api_handling
from dash.dependencies import Input, Output, State
from simulation import utils_parameters as up
from plotly.subplots import make_subplots


d = {'susceptible': [], 'infected': [], 'recovered': [], 'dead': [], 'time': [], 'r0': []}

old_amounts = {'susceptible': 0, 'dead': 0, 'recovered': 0, 'a_parameter': 0.0}

r0_parameters = [0.0]
q_parameters = [0.0]

box = container.Container(size=0, population=0, time_to_live=0,
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
                                          value=100)
                            ]),
                            html.Td([
                                html.Label('Container size', htmlFor='container-size'),
                                dcc.Input(id='container-size',
                                          type='number',
                                          placeholder='population amount',
                                          value=50)
                            ])
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
                html.Div([
                    html.Button('Start', id='start-button', n_clicks=0),
                    html.Button('Stop', id='stop-button', n_clicks=0),
                    html.Button('Continue', id='continue-button', n_clicks=0),
                    html.Button('Reset', id='reset-button', n_clicks=0),
                ], style={'display': 'flex', 'justify-content': 'center', 'paddingRight': '5px', 'marginTop': '10%'})
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
            ])
        ], style={'display': 'flex', 'justify-content': 'space-evenly'}),
        html.Div([dcc.Graph(id='live-population', style={'flex-grow': '0', 'width': '80%'}),
                  html.Table([
                      html.Thead(id='current-population-amount'),
                      html.Thead(id="additional-parameters")
                  ])
                  ], style={'marginTop': '20px', 'display': 'flex', 'justify-content': 'space-around'}),
        html.Div([
            dcc.Graph(id='move-population'),
            dcc.Graph(id='population-percent'),
        ], style={'display': 'flex', 'justify-content': 'space-evenly', 'marginTop': '20px'}),
        html.Div(dcc.Graph(id='real-data'), style={'width': '90%', 'margin': '20px auto'}),
        dcc.Store(id='simulation-data')
    ])


@app.callback(Output('inf-prob-value', 'children'),
              [Input('infection-probability', 'value')])
def display_infection_probability_slider_value(value):
    return value


@app.callback(Output('rec-prob-value', 'children'),
              [Input('recover-probability', 'value')])
def display_recover_probability_slider_value(value):
    return value


@app.callback(Output('dead-prob-value', 'children'),
              [Input('dead-probability', 'value')])
def display_dead_probability_slider_value(value):
    return value


@app.callback(Output('inf-range-value', 'children'),
              [Input('infection-range', 'value')])
def display_infection_range_slider_value(value):
    return value


@app.callback(Output('move-dist-value', 'children'),
              [Input('move-length', 'value')])
def display_move_length_slider_value(value):
    return value


@app.callback(Output('simulation-data', 'data'),
              [Input('interval-component', 'n_intervals')])
def simulation_begin(n_intervals: int) -> dict:
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
    "groups" in dictionary data structure.
    """

    data = {'individuals': [], 'groups': {'susceptible': 0, 'infected': 0,
                                          'recovered': 0, 'dead': 0}}

    for instance in box.object_list:
        data['individuals'].append({'x': instance.x, 'y': instance.y,
                                    'condition': instance.current_condition})

    data['groups'] = dict(susceptible=box.count_susceptible(), infected=box.count_infected(),
                          recovered=box.count_recovered(), dead=box.count_dead())

    box.simulation()

    return data


@app.callback([Output('interval-component', 'disabled'),
               Output('interval-component', 'n_intervals')],
              [Input('start-button', 'n_clicks'),
               Input('continue-button', 'n_clicks'),
               Input('stop-button', 'n_clicks'),
               Input('reset-button', 'n_clicks')],
              [State('population-amount', 'value'),
               State('container-size', 'value'),
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
                        population_amount: int, container_size: int, susceptible_amount: int,
                        infected_amount: int, recovered_amount: int, dead_amount: int,
                        infection_probability: float, recover_probability: float,
                        dead_probability: float, infection_range: float, move_length: float) -> list:
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
        container_size: int, required
            Dimension of container which contains all instances inside.
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
    Based on selected event return list where fist index is True or False for
    dcc.Interval object's attribute 'disabled'. If event is Stop, Reset
    returns True, if Start, Continue returns False. Second index is value
    for parmeter 'n_intervals' which stand for interval start value.
    """

    ctx = dash.callback_context

    if not ctx.triggered:
        button_id = 'No clicks yet'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'start-button':
        box.population = population_amount
        box.width = container_size
        box.height = container_size
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
        return [False, 0]

    if button_id == 'stop-button':
        return [True, d['time'][-1]]

    if button_id == 'continue-button':
        return [False, d['time'][-1] + 1]

    if button_id == 'reset-button':
        d['susceptible'].clear()
        d['infected'].clear()
        d['recovered'].clear()
        d['dead'].clear()
        d['time'].clear()
        d['r0'].clear()

        box.population = 0
        box.initial_set_up(0, 0, 0, 0, 0, 0, 0, 0)
        box.object_list.clear()

        r0_parameters.clear()
        q_parameters.clear()
        return [True, 0]

    return [True, 0]


@app.callback(Output('live-population', 'figure'),
              [Input('interval-component', 'n_intervals'),
               Input('simulation-data', 'data')])
def update_graph_live(n_intervals: int, simulation_data: dict) -> 'go.Scatter':
    """
    Function handling scatter graph for each individual instance move in
    grid.

    Parameters
    ----------
    n_intervals: int, required
        Number of passed intervals from begin of simulation. Generated
        with dash object dcc.Interval.
    simulation_data: dict, required
        Dictionary contain data of simulation.

    Returns
    -------
    Return plolty scatter chart with information of current amount of
    each group in simulation.
    """

    d['time'].append(n_intervals)
    d['susceptible'].append(simulation_data['groups']['susceptible'])
    d['infected'].append(simulation_data['groups']['infected'])
    d['dead'].append(simulation_data['groups']['dead'])
    d['recovered'].append(simulation_data['groups']['recovered'])

    if len(r0_parameters) > 0:
        d['r0'].append(sum(r0_parameters) / len(r0_parameters))
    else:
        d['r0'].append(0)

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(x=d['time'], y=d['susceptible'], name="susceptible", mode="lines", marker={'color': 'blue'}),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=d['time'], y=d['infected'], name="infected", mode="lines", marker={'color': 'red'}),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=d['time'], y=d['recovered'], name="recovered", mode="lines", marker={'color': 'green'}),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=d['time'], y=d['dead'], name="dead", mode="lines", marker={'color': 'gray'}),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=d['time'], y=d['r0'], name="R<sub>0</sub>", mode="lines",
                   marker={'color': 'gold'}, line={'dash': 'dash'}),
        secondary_y=True,
    )

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
    fig.update_yaxes(title_text="People amount", secondary_y=False)
    fig.update_yaxes(title_text="R<sub>0</sub> value", secondary_y=True)

    return fig


@app.callback(Output('move-population', 'figure'),
              [Input('interval-component', 'n_intervals'),
               Input('simulation-data', 'data')])
def update_graph_move(n_intervals: int, simulation_data: dict) -> 'px.scatter':
    """
    Function handling scatter graph for each individual instance move in
    grid.

    Parameters
    ---------
    n_intervals: int, required
        Number of passed intervals from begin of simulation. Generated
        with dash object dcc.Interval.
    simulation_data: dict, required
        Dictionary contain data of simulation.

    Returns
    -------
    Return plolty express scatter chart with placed instances in grid.
    """

    cords = {'x': [], 'y': [], 'condition': []}

    for element in simulation_data['individuals']:
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
    fig.for_each_trace(
        lambda trace: trace.update({'marker': {'symbol': 'circle-open-dot',
                                               'size': 20,
                                               'line': {'width': 2}}})
        if trace.name == "infected" else (),
    )
    return fig


@app.callback(Output('population-percent', 'figure'),
              [Input('interval-component', 'n_intervals'),
               Input('simulation-data', 'data')])
def update_population_percent(n_intervals: int, simulation_data: dict) -> 'px.pie':
    """
    Function handling pie chart with percent value of each group in population.

    Parameters
    ----------
    n_intervals: int, required
        Number of past intervals.
    simulation_data: dict, required
        Dictionary contain data of simulation..

    Returns
    -------
    Plotly express object pie chart.
    """

    data = simulation_data
    percent = {'condition': ['susceptible', 'infected', 'recovered', 'dead'],
               'percent_value': [data['groups']['susceptible'], data['groups']['infected'],
                                 data['groups']['recovered'], data['groups']['dead']]}

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
def update_population_amount(n_intervals: int, simulation_data: dict) -> list:
    """
    Function handling display html table with amount of each group.

    Parameters
    ----------
    n_intervals: int, required
        Number of past intervals.
    simulation_data: dict, required
        Dictionary contain data of simulation.

    Returns
    -------
    Html table base od bash html.Table object.
    """

    return [html.Tr([html.Th('Condition', colSpan=2), html.Th('Amount')]),
            html.Tr([html.Td('Susceptible', colSpan=2), html.Td(simulation_data['groups']['susceptible'])]),
            html.Tr([html.Td('Infected', colSpan=2), html.Td(simulation_data['groups']['infected'])]),
            html.Tr([html.Td('Recovered', colSpan=2), html.Td(simulation_data['groups']['recovered'])]),
            html.Tr([html.Td('Dead', colSpan=2), html.Td(simulation_data['groups']['dead'])])]


@app.callback(Output('additional-parameters', 'children'),
              [Input('interval-component', 'n_intervals'),
              Input('simulation-data', 'data')],
              [State('susceptible-amount', 'value')])
def parameter_update(n_intervals: int, simulation_data: dict, susceptible_amount: int) -> list:
    """
    Function handling display html table with additional parameters q and R0.

    Parameters
    ----------
    n_intervals: int, required
        Number of past intervals.
    simulation_data: dict, required
        Dictionary contain data of simulation.
    susceptible_amount: int, required
        Start number of susceptible.

    Returns
    -------
    Html table base od bash html.Table object with parameter q and R0.
    """

    if simulation_data['groups']['susceptible'] > 0 and simulation_data['groups']['infected'] > 0:
        r_parameter = up.compute_r_parameter(old_amounts['susceptible'],
                                             simulation_data['groups']['susceptible'],
                                             simulation_data['groups']['infected'])

        old_amounts['susceptible'] = simulation_data['groups']['susceptible']
    else:
        r_parameter = 0

    if simulation_data['groups']['infected'] > 0 and simulation_data['groups']['dead'] > 0 or \
            simulation_data['groups']['recovered'] > 0:
        a_parameter = up.compute_a_parameter(old_amounts['recovered'] + old_amounts['dead'],
                                             simulation_data['groups']['recovered'] +
                                             simulation_data['groups']['dead'],
                                             simulation_data['groups']['infected'])

        old_amounts['infected'] = simulation_data['groups']['infected']
        old_amounts['recovered'] = simulation_data['groups']['recovered']
        old_amounts['dead'] = simulation_data['groups']['dead']

        if a_parameter > 0:
            old_amounts['a_parameter'] = a_parameter

            q_parameters.append(up.compute_q_parameter(r_parameter, a_parameter))
            r0_parameters.append(up.compute_r0_parameter(r_parameter, a_parameter,
                                                         susceptible_amount))
        else:
            q_parameters.append(up.compute_q_parameter(r_parameter,
                                                       old_amounts['a_parameter']))
            r0_parameters.append(up.compute_r0_parameter(r_parameter,
                                                         old_amounts['a_parameter'],
                                                         susceptible_amount))

        q_parameter = sum(q_parameters) / len(q_parameters)
        q_parameter = round(q_parameter, 2)
        r_0 = sum(r0_parameters) / len(r0_parameters)
        r_0 = round(r_0, 2)

        # Note: Pandemic R0 parameter highlight
        if r_0 > 1.5:
            return [html.Tr([html.Th('Parameter'), html.Th('Mean'), html.Th('Current')]),
                    html.Tr([html.Td(['R', html.Sub('0')]), html.Td(r_0), html.Td(round(r0_parameters[-1], 2))],
                            style={'backgroundColor': 'red'}),
                    html.Tr([html.Td('q'), html.Td(q_parameter), html.Td(round(q_parameters[-1]))])]
        else:
            return [html.Tr([html.Th('Parameter'), html.Th('Mean'), html.Th('Current')]),
                    html.Tr([html.Td(['R', html.Sub('0')]), html.Td(r_0), html.Td(round(r0_parameters[-1], 2))]),
                    html.Tr([html.Td('q'), html.Td(q_parameter), html.Td(round(q_parameters[-1]))])]

    return [html.Tr([html.Th('Parameter'), html.Th('Mean'), html.Th('Current')]),
            html.Tr([html.Td(['R', html.Sub('0')]), html.Td(0), html.Td(0)]),
            html.Tr([html.Td('q'), html.Td(0), html.Td(0)])]


@app.callback(Output('real-data', 'figure'),
              [Input('simulation-data', 'data')])
def create_plot_with_real_data(data) -> 'px.line':
    """
    Function that get real data from https://covid19api.com and display it.
    Include attempt to implement machine learning prediction.

    Parameters
    ----------
    data: optional
        Input trigger for displaying plot.

    Returns
    -------
    Plotly express line chart.
    """

    country = 'Germany'
    total_data = api_handling.get_data_from_country(country)

    tab = {'date': [], 'amount': [], 'condition': []}

    for element in total_data:
        tab['date'].append(element['Date'])
        tab['amount'].append(element['Active'])
        tab['condition'].append('active')

    for element in total_data:
        tab['date'].append(element['Date'])
        tab['amount'].append(element['Recovered'])
        tab['condition'].append('recovered')

    for element in total_data:
        tab['date'].append(element['Date'])
        tab['amount'].append(element['Deaths'])
        tab['condition'].append('dead')

    for element in total_data:
        tab['date'].append(element['Date'])
        tab['amount'].append(element['Confirmed'])
        tab['condition'].append('confirmed')

    df = pd.DataFrame(data=tab)

    fig = px.line(df, x='date', y='amount', color='condition',
                  color_discrete_map={
                     'confirmed': 'gold',
                     'active': 'red',
                     'recovered': 'green',
                     'dead': 'gray'
                  }, category_orders={'condition': ['infected', 'recovered', 'dead']})

    fig.update_layout({'title': {'text': f'COVID-19 real data for {country}', 'font': {'size': 30}},
                       'template': 'plotly_dark'})

    # Note: Add prediction value based on machine learning model
    fig.add_scatter(y=[19256], x=['2020-06-18T00:00:00Z'],
                    marker={'size': 12},
                    name='prediction',
                    mode='markers+text',
                    text=['19256'],
                    textposition='top center')
    # -- end note

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
