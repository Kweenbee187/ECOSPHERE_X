import pandas as pd

def clean_gdelt(df, bbox):
    df = df[
        (df["ActionGeo_FullName"].str.contains("Kerala", na=False, case=False)) |
        (
            (df["ActionGeo_Lat"] >= bbox[1]) &
            (df["ActionGeo_Lat"] <= bbox[3]) &
            (df["ActionGeo_Long"] >= bbox[0]) &
            (df["ActionGeo_Long"] <= bbox[2])
        )
    ]

    df = df[[
        "GLOBALEVENTID", "SQLDATE", "AvgTone", "NumArticles",
        "ActionGeo_Lat", "ActionGeo_Long", "ActionGeo_FullName", "SOURCEURL"
    ]].dropna(subset=["ActionGeo_Lat", "ActionGeo_Long", "AvgTone"])

    return df
