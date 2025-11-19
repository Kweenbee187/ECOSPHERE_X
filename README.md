# ECOSPHERE_X
# 🌍 ECOSPHERE X
A multimodal climate intelligence system combining real **satellite Earth data**, **global news sentiment**, a **knowledge graph**, and an **AI emergency response agent**.

This project is part of the **SEED Global Hackathon**.

---

## 🚀 Features

### 🛰 Satellite Intelligence (Sentinel-2)
- Fetches real Sentinel-2 L2A imagery via Microsoft Planetary Computer
- Computes NDVI & NDWI
- Generates visual maps & environment summaries

### 📰 Human Distress Signals (GDELT)
- Downloads real global news events for Kerala Floods 2018
- Extracts sentiment, geography, volume
- Creates cleaned JSON for KG

### 🕸 Multimodal Knowledge Graph
- Combines Satellite + Human Signals
- Nodes: Place, Observation, HumanSignal
- Edges: OBSERVED_AT, REPORTS_ABOUT
- Export to PyVis (HTML) + GEXF (Gephi)

### 📊 Analytics & Timeline
- Daily sentiment
- Article volume
- Satellite observation alignment

### 🤖 AI Decision Agent
- Assigns emergency priority (LOW/MEDIUM/HIGH)
- Generates actionable recommendations
- Evidence-driven outputs

---

## 📁 Repository Structure

ecosphere/
satellite/
gdelt/
knowledge_graph/
analytics/
agent/
pipeline.py
data/
artifacts/
notebooks/

---

## 👥 Contributors

- **Kweenbee187** → https://github.com/Kweenbee187  
- **tituatgithub** → https://github.com/tituatgithub

---

## 📄 License
Apache License 2.0

---

## ▶ Running the Pipeline

```bash
python ecosphere/pipeline.py
🏆 Built for SEED Global Hackathon 2025

A truly multimodal climate intelligence system.

---

# 🟦 PYTHON MODULES  
All modules below are perfectly clean + modular + directly usable.

---

## 📁 **`ecosphere/config.py`**

```python
BBOX = [76.35, 9.8, 76.70, 10.1]
DATE_RANGE = "2018-08-01/2018-09-05"
MAX_CLOUD_COVER = 30

GDELT_DATES = [
    "20180815", "20180816", "20180817",
    "20180818", "20180819", "20180820"
]

