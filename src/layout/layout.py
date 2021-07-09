import dash_core_components as dcc
import dash_html_components as html


class AppLayout:

    def __init__(self):

        pass

    @staticmethod
    def get(app_version):

        app_layout = html.Div(
            children=[
                html.Div(
                    className="app-card-external",
                    children=[
                        dcc.Markdown(f'# Time series data analysis and forecasting with Python - Dashboard v{app_version}'),
                        html.Div(
                            children=[
                                html.Div(
                                    className="app-card-internal-left",
                                    children=[
                                        html.Div(
                                            className="app-card-internal-left-top",
                                            children=[
                                                dcc.Tabs(
                                                    className='app-card-internal-left-tabs',
                                                    id='app-card-internal-left-tabs',
                                                    children=[
                                                        dcc.Tab(
                                                            label='Analysis',
                                                            value='tab-analysis',
                                                            className='custom-tab',
                                                            selected_className='custom-tab-selected',
                                                            style={
                                                                "background-color": "#eeeeee",
                                                                "border-right": "2px solid #d6d6d6",
                                                                "border-bottom": "2px solid #d6d6d6",
                                                                "font-family": "Helvetica, Calibri",
                                                                "padding-bottom": "15px",
                                                                "padding-top": "15px",
                                                                "text-align": "center"
                                                            },
                                                            selected_style={
                                                                "border-top": "0px",
                                                                "font-family": "Helvetica, Calibri",
                                                                "font-size": "1.5em",
                                                                "font-weight": "bold",
                                                                "padding-bottom": "10px",
                                                                "padding-top": "10px"
                                                            }
                                                        ),
                                                        dcc.Tab(
                                                            label='Forecasting',
                                                            value='tab-forecasting',
                                                            className='custom-tab',
                                                            selected_className='custom-tab-selected',
                                                            style={
                                                                "background-color": "#eeeeee",
                                                                "border-right": "2px solid #d6d6d6",
                                                                "border-bottom": "2px solid #d6d6d6",
                                                                "font-family": "Helvetica, Calibri",
                                                                "padding-bottom": "15px",
                                                                "padding-top": "15px",
                                                                "text-align": "center"
                                                            },
                                                            selected_style={
                                                                "border-top": "0px",
                                                                "font-family": "Helvetica, Calibri",
                                                                "font-size": "1.5em",
                                                                "font-weight": "bold",
                                                                "padding-bottom": "10px",
                                                                "padding-top": "10px"
                                                            }
                                                        )
                                                    ],
                                                    value='tab-analysis',
                                                    style={
                                                        'display': 'flex',
                                                        'flex-direction': 'row'
                                                    }
                                                ),
                                                html.Div(
                                                    className="app-card-internal-left-menu-item-title",
                                                    children=[dcc.Markdown('''## Mathematical tool''')]
                                                ),
                                                html.Div(
                                                    className="app-card-internal-left-menu-item-content-dropdown",
                                                    children=[
                                                        dcc.Dropdown(
                                                            id='mathematical-tool-dropdown',
                                                            style={'border-width': '2px'}
                                                        )
                                                    ]
                                                ),
                                                html.Div(
                                                    className="app-card-internal-left-menu-item-content-text",
                                                    children=[dcc.Markdown(id='mathematical-tool-explanation')]
                                                )
                                            ], style={'height': '50%'}
                                        ),
                                        html.Div(
                                            className="app-card-internal-left-bottom",
                                            children=[
                                                html.Div(
                                                    className="app-card-internal-left-menu-item-title",
                                                    children=[dcc.Markdown('''## Dataset''')]
                                                ),
                                                html.Div(
                                                    className="app-card-internal-left-menu-item-content-text",
                                                    children=[dcc.Markdown(id='dataset-explanation')]
                                                )
                                            ], style={'height': '50%'}
                                        )
                                    ],
                                    style={
                                        'display': 'flex',
                                        'flex-direction': 'column',
                                        'width': '40%',
                                        'vertical-align': 'middle'
                                    }
                                ),
                                html.Div(
                                    className="app-card-internal-right",
                                    children=[
                                        html.Div(
                                            className="app-card-internal-left-menu-item-title",
                                            children=[dcc.Markdown('''## Results figure''')]
                                        ),
                                        dcc.Graph(id="mathematical-tool-results-figure")
                                    ],
                                    style={
                                        'display': 'inline-block',
                                        'width': '60%',
                                        "vertical-align": "top"
                                    }
                                )
                            ],
                            style={'display': 'flex'}
                        )
                    ]
                )
            ]
        )

        return app_layout

    @staticmethod
    def get_analysis_dropdown_options():

        analysis_dropdown_options = [
            {'label': 'Augmented Dickey-Fuller Test', 'value': 'augmentedDickeyFullerTest'},
            {'label': 'Error-Trend-Seasonality (ETS) Decomposition', 'value': 'errorTrendSeasonalityDecomposition'},
            {'label': 'Exponentially Weighed Moving Average (EWMA)', 'value': 'exponentiallyWeightedMovingAverage'},
            {'label': 'Hodrick-Prescott Filter', 'value': 'hodrickPrescottFilter'},
            {'label': 'Simple Moving Average', 'value': 'simpleMovingAverage'},
        ]

        return analysis_dropdown_options

    @staticmethod
    def get_forecasting_dropdown_options():

        forecasting_dropdown_options = [
            {'label': "Double Exponential Smoothing (Holt's Method)", 'value': 'doubleExponentialSmoothing'},
            {'label': 'Simple Exponential Smoothing', 'value': 'simpleExponentialSmoothing'},
            {'label': "Triple Exponential Smoothing (Holt-Winters' Method)", 'value': 'tripleExponentialSmoothing'}
        ]

        return forecasting_dropdown_options
