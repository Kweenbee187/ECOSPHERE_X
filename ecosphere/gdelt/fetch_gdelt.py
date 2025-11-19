import pandas as pd
from ecosphere.config import GDELT_DATES

URL = "http://data.gdeltproject.org/events/{}.export.CSV.zip"

def fetch_gdelt(columns):
    dfs = []

    for d in GDELT_DATES:
        url = URL.format(d)
        try:
            df = pd.read_csv(url, sep='\t', names=columns,
                             compression="zip", low_memory=False)
            dfs.append(df)
        except Exception as e:
            print("Error fetching:", d, e)

    return pd.concat(dfs, ignore_index=True)
