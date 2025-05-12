import dash
from dash import dcc, html, dash_table
import plotly.express as px
import pandas as pd

def create_dashboard(correlated_events):
    # Flatten correlated events for visualization
    # For simplicity, we create a DataFrame with some summary information.
    data = []
    for event in correlated_events:
        threat = event["threat_event"]
        siem = event["siem_log"]
        record = {
            "Threat Indicator": threat.get("indicator", ""),
            "Threat Type": threat.get("type", ""),
            "Threat Source": threat.get("source", ""),
            "SIEM Activity": siem.get("activity", ""),
            "User": siem.get("user", ""),
            "Timestamp": siem.get("timestamp", "")
        }
        data.append(record)
    df = pd.DataFrame(data)
    
    app = dash.Dash(__name__)
    fig = px.scatter(df, x="Timestamp", y="Threat Indicator",
                     color="Threat Type",
                     title="Correlated Threat Events")
    
    app.layout = html.Div(children=[
        html.H1("Threat Intelligence Aggregation & Correlation Dashboard"),
        dash_table.DataTable(
            id='correlation-table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
            page_size=10,
        ),
        dcc.Graph(figure=fig)
    ])
    return app

if __name__ == '__main__':
    from correlation_engine import correlate_events
    from threat_feed_fetcher import fetch_threat_feed_data
    from siem_log_parser import parse_siem_logs
    threat_data = fetch_threat_feed_data("../data/threat_feeds.csv")
    siem_logs = parse_siem_logs("../data/siem_logs.csv")
    correlations = correlate_events(threat_data, siem_logs)
    app = create_dashboard(correlations)
    app.run_server(debug=True)
