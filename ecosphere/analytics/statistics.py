from scipy.stats import pearsonr

def compute_correlation(daily_sentiment, ndvi):
    if len(daily_sentiment) < 3:
        return None
    corr, p = pearsonr([ndvi]*len(daily_sentiment),
                       daily_sentiment["AvgTone"])
    return corr, p
