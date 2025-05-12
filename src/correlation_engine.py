import pandas as pd

def correlate_events(threat_df, siem_df):
    """
    A simple correlation engine that matches threat indicators
    with SIEM logs based on time proximity and user activity.
    
    For example:
    - If a threat feed record (e.g., a malicious IP) appears,
      check if any SIEM log from the same time window involves
      a user action that may be affected.
      
    This example will simulate basic matching by joining on a common column if available.
    """
    # For simplicity, simulate correlation by merging on approximate timestamps.
    # In practice, more advanced correlation logic would be applied.
    
    # Convert timestamps to datetime objects:
    threat_df['timestamp'] = pd.to_datetime(threat_df['timestamp'])
    siem_df['timestamp'] = pd.to_datetime(siem_df['timestamp'])
    
    # Simulate a correlation: Assume any SIEM log within 5 minutes after a threat feed is correlated.
    correlated = []
    for _, threat in threat_df.iterrows():
        window_start = threat['timestamp']
        window_end = window_start + pd.Timedelta(minutes=5)
        related_logs = siem_df[(siem_df['timestamp'] >= window_start) & (siem_df['timestamp'] <= window_end)]
        if not related_logs.empty:
            for _, log in related_logs.iterrows():
                correlation = {
                    "threat_event": threat.to_dict(),
                    "siem_log": log.to_dict()
                }
                correlated.append(correlation)
    return correlated

if __name__ == '__main__':
    import pandas as pd
    from threat_feed_fetcher import fetch_threat_feed_data
    from siem_log_parser import parse_siem_logs
    threat_data = fetch_threat_feed_data("../data/threat_feeds.csv")
    siem_logs = parse_siem_logs("../data/siem_logs.csv")
    correlations = correlate_events(threat_data, siem_logs)
    print("Correlated events:", correlations)
