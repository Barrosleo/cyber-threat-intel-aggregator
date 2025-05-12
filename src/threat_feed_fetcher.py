import pandas as pd

def fetch_threat_feed_data(filepath):
    """
    Loads threat feed data from a CSV.
    In a real implementation, this could use APIs to fetch live data.
    """
    try:
        df = pd.read_csv(filepath)
        return df
    except Exception as e:
        print(f"Error fetching threat feed data: {e}")
        return pd.DataFrame()

if __name__ == '__main__':
    data = fetch_threat_feed_data("../data/threat_feeds.csv")
    print(data.head())
