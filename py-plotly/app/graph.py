import dash
import pandas as pd
import plotly.graph_objs as go
import flask

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

server = flask.Flask(__name__)  # define flask app.server

app = dash.Dash(
    __name__, external_stylesheets=external_stylesheets, server=server
)  # call flask server

# run following in command
# gunicorn graph:app.server -b :8000


df = pd.read_csv("graph_data.csv")


app.layout = dash.html.Div(
    [
        dash.dcc.Graph(
            id="life-exp-vs-gdp",
            figure={
                "data": [
                    go.Scatter(
                        x=df[df["continent"] == i]["gdp per capita"],
                        y=df[df["continent"] == i]["life expectancy"],
                        text=df[df["continent"] == i]["country"],
                        mode="markers",
                        opacity=0.7,
                        marker={"size": 15, "line": {"width": 0.5, "color": "white"}},
                        name=i,
                    )
                    for i in df.continent.unique()
                ],
                "layout": go.Layout(
                    xaxis={"type": "log", "title": "GDP Per Capita"},
                    yaxis={"title": "Life Expectancy"},
                    margin={"l": 40, "b": 40, "t": 10, "r": 10},
                    legend={"x": 0, "y": 1},
                    hovermode="closest",
                ),
            },
        )
    ]
)

# if __name__ == "__main__":
#     app.run_server(debug=True, port=8080)
