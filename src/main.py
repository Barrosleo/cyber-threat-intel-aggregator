from threat_feed_fetcher import fetch_threat_feed_data
from siem_log_parser import parse_siem_logs
from correlation_engine import correlate_events
from dashboard import create_dashboard
from report_generator import generate_report
import os

def main():
    # Ensure required directories
    os.makedirs("data", exist_ok=True)
    os.makedirs("docs", exist_ok=True)
    
    # Step 1: Fetch threat feed data (simulate or load from data folder)
    threat_data = fetch_threat_feed_data("data/threat_feeds.csv")
    print("Threat feed data loaded:", len(threat_data), "records")
    
    # Step 2: Parse internal SIEM logs
    siem_logs = parse_siem_logs("data/siem_logs.csv")
    print("SIEM logs loaded:", len(siem_logs), "records")
    
    # Step 3: Correlate threat intelligence with SIEM logs
    correlated_events = correlate_events(threat_data, siem_logs)
    print("Correlation complete. Correlated events found:", len(correlated_events))
    
    # Step 4: Generate a dashboard to visualize correlated incidents
    app = create_dashboard(correlated_events)
    # Run the dashboard server (for demo purpose, may block execution)
    app.run_server(debug=True)
    
    # Step 5: Generate an automated incident report with actionable insight
    report = generate_report(correlated_events)
    with open("docs/aggregated_report.json", "w") as f:
        f.write(report)
    print("Aggregated incident report generated.")

if __name__ == '__main__':
    main()
