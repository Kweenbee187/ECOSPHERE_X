def run_agent(mean_ndwi, mean_ndvi, mean_tone, neg_count, total_articles):
    priority = "LOW"
    reason = "Normal conditions"
    actions = []

    if mean_ndwi > 0.2 and mean_tone < -3:
        priority = "HIGH"
        reason = "High water + negative sentiment"
        actions = ["Deploy response teams", "Activate monitoring"]
    elif mean_ndvi < 0.3 and neg_count > 10:
        priority = "MEDIUM"
        reason = "Vegetation stress + many negative reports"
        actions = ["Monitor areas", "Prepare resources"]
    elif mean_tone < -2:
        priority = "MEDIUM"
        reason = "Negative sentiment spike"
        actions = ["Increase media monitoring"]

    return {
        "priority": priority,
        "reason": reason,
        "actions": actions
    }
