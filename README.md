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


