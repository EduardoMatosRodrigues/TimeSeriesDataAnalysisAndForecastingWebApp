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
                                                html.Div(
                                                    className="app-card-internal-left-menu-item-title",
                                                    children=[dcc.Markdown('''## Mathematical tool''')]
                                                ),
                                                html.Div(
                                                    className="app-card-internal-left-menu-item-content-dropdown",
                                                    children=[
                                                        dcc.Dropdown(
                                                            id='mathematical-tool-dropdown',
                                                            options=[
                                                                {'label': 'Hodrick-Prescott filter', 'value': 'hodrickPrescottFilter'},
                                                                {'label': 'ETS decomposition', 'value': 'errorTrendSeasonalityDecomposition'},
                                                                {'label': 'SMA', 'value': 'simpleMovingAverage'},
                                                                {'label': 'EWMA', 'value': 'exponentiallyWeightedMovingAverage'}
                                                            ],
                                                            value='hodrickPrescottFilter',
                                                            style={'border-width': '2.5px'}
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
                                        'width': '35%',
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
                                        'width': '65%',
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
