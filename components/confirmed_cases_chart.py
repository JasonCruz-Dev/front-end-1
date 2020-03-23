import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.settings import TIME_URL


def confirmed_cases_chart(state=None) -> go.Figure:
    """Bar chart data for the selected state.

    :params state: get the time series data for a particular state for confirmed, deaths, and recovered. If None, the whole US.
    """

    df = pd.read_csv(TIME_URL)
    df = df[df["Country/Region"] == "US"]
    # "Let it go, let it go" - Princess Elsa
    df = df[~df["Province/State"].str.contains("Princess")]
    df = df.drop(columns=["Lat", "Long", "Province/State", "Country/Region"])
    df = df.sum(axis=0).to_frame().reset_index()
    df["index"] = pd.to_datetime(df["index"])
    df = df.rename(columns={"index": "Date", 0: "Confirmed Cases"})
    df = df[30:]

    fig = px.line(df, x="Date", y="Confirmed Cases")
    fig.update_layout(
        margin={"r": 10, "t": 40, "l": 0, "b": 0},
        template="plotly_dark",
        title="U.S. Confirmed Cases",
        xaxis_title=None,
        yaxis_title=None,
        showlegend=False,
    )

    # card = dbc.Card(dbc.CardBody(dcc.Graph(figure=fig, style={"height": "20vh"})))
    # return card
    return fig