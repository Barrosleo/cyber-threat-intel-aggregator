# cyber-threat-intel-aggregator

This project aggregates threat intelligence from open-source feeds and internal SIEM logs to detect potential compromise events. It normalizes, enriches, and correlates the data, visualizes correlated incidents using an interactive dashboard, and generates automated reports with actionable insights.

## Key Features
```
- Data ingestion from multiple threat feeds
- Normalization and enrichment of threat data and SIEM logs
- Event correlation using Python (Pandas, scikit‑learn)
- Interactive dashboards with Plotly Dash
- Automated reporting for actionable security insights
```
## Usage
1. Install dependencies:
```
pip install -r requirements.txt
```
2. Run the application:
```
python src/main.py
```

## Repository Structure
```
cyber-threat-intel-aggregator/
├── README.md
├── requirements.txt
├── docs/
│   └── aggregated_report.json
├── data/
│   ├── threat_feeds.csv
│   └── siem_logs.csv
└── src/
    ├── main.py
    ├── threat_feed_fetcher.py
    ├── siem_log_parser.py
    ├── correlation_engine.py
    ├── dashboard.py
    └── report_generator.py
```
