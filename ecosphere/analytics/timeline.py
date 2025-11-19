import matplotlib.pyplot as plt

def save_timeline(df, sat_date, out_path):
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(df["date"], df["avg_sentiment"], marker='o')
    plt.axvline(sat_date, color='cyan', linestyle='--')

    plt.subplot(1, 2, 2)
    plt.bar(df["date"], df["article_count"])

    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close()
