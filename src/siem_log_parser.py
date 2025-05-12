import pandas as pd

def parse_siem_logs(filepath):
    """
    Loads SIEM log data from a CSV file.
    """
    try:
        df = pd.read_csv(filepath)
        return df
    except Exception as e:
        print(f"Error parsing SIEM logs: {e}")
        return pd.DataFrame()

if __name__ == '__main__':
    logs = parse_siem_logs("../data/siem_logs.csv")
    print(logs.head())
