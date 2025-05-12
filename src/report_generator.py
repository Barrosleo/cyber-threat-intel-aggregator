import json
from datetime import datetime

def generate_report(correlated_events):
    """
    Generates a JSON report summarizing:
    - Total correlated events
    - Details of each correlation (threat event and matching SIEM log)
    - Timestamp of report generation
    """
    report = {
        "report_generated": datetime.now().isoformat(),
        "total_correlated_events": len(correlated_events),
        "correlated_details": correlated_events
    }
    return json.dumps(report, indent=4)

if __name__ == '__main__':
    from correlation_engine import correlate_events
    from threat_feed_fetcher import fetch_threat_feed_data
    from siem_log_parser import parse_siem_logs
    threat_data = fetch_threat_feed_data("../data/threat_feeds.csv")
    siem_logs = parse_siem_logs("../data/siem_logs.csv")
    correlations = correlate_events(threat_data, siem_logs)
    report = generate_report(correlations)
    print(report)
