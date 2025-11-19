# 🌍 ECOSPHERE X

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Sentinel-2](https://img.shields.io/badge/Sentinel--2-L2A-green)](https://sentinel.esa.int/)
[![GDELT](https://img.shields.io/badge/GDELT-News%20API-orange)](https://www.gdeltproject.org/)

**A multimodal climate intelligence system combining real satellite Earth observation data, global news sentiment analysis, knowledge graphs, and AI-powered emergency response.**

> 🏆 Built for the **SEED Global Hackathon**

![ECOSPHERE X Banner](https://via.placeholder.com/1200x300/1a1a2e/16213e?text=ECOSPHERE+X+%7C+Climate+Intelligence+System)

---

## 🎯 Overview

ECOSPHERE X bridges the gap between **satellite observations** and **human signals** to provide comprehensive climate disaster intelligence. By fusing remote sensing data with real-time news sentiment, the system creates a holistic view of environmental emergencies and generates AI-driven response recommendations.

### Case Study: Kerala Floods 2018
This implementation focuses on the devastating Kerala floods of 2018, demonstrating how multimodal data fusion can enhance disaster response capabilities.

---

## ✨ Key Features

### 🛰️ **Satellite Intelligence Module**
Powered by Sentinel-2 L2A imagery via Microsoft Planetary Computer
- **Real-time data acquisition** from Sentinel-2 satellites
- **Environmental indices calculation**:
  - NDVI (Normalized Difference Vegetation Index)
  - NDWI (Normalized Difference Water Index)
- **Visual mapping** with geospatial overlays
- **Automated environment summaries** for rapid assessment

### 📰 **Human Distress Signal Processing**
Leveraging GDELT Global Database of Events, Language, and Tone
- **News event extraction** from global sources
- **Sentiment analysis** of disaster-related articles
- **Geographic tagging** of reported incidents
- **Temporal tracking** of event evolution
- **Cleaned JSON exports** for knowledge graph integration

### 🕸️ **Multimodal Knowledge Graph**
Unified representation of satellite and human intelligence
- **Entity types**:
  - `Place` - Geographic locations
  - `Observation` - Satellite measurements
  - `HumanSignal` - News reports and sentiment
- **Relationship types**:
  - `OBSERVED_AT` - Satellite → Location
  - `REPORTS_ABOUT` - News → Location
- **Export formats**:
  - PyVis interactive HTML visualization
  - GEXF format for Gephi analysis

### 📊 **Advanced Analytics & Timeline**
Real-time monitoring and historical analysis
- **Daily sentiment trends** across news sources
- **Article volume tracking** by date and location
- **Satellite-news alignment** correlation
- **Multi-dimensional dashboards**

### 📈 **Emergency Response Analytics**
Intelligent decision support system
- **Priority classification**: LOW / MEDIUM / HIGH based on data thresholds
- **Context-aware recommendations** from multimodal data analysis
- **Evidence-driven outputs** with source attribution
- **Actionable response strategies** based on patterns

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      ECOSPHERE X Pipeline                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  📡 Sentinel-2        📰 GDELT           📊 Analytics       │
│  Satellite Data       News Events        Decision Engine    │
│       │                   │                    │            │
│       ├───────────────────┼────────────────────┤            │
│       │                   │                    │            │
│       ▼                   ▼                    ▼            │
│  ┌──────────────────────────────────────────────────┐      │
│  │         Multimodal Knowledge Graph               │      │
│  │  Nodes: Place, Observation, HumanSignal         │      │
│  │  Edges: OBSERVED_AT, REPORTS_ABOUT              │      │
│  └──────────────────────────────────────────────────┘      │
│                          │                                  │
│                          ▼                                  │
│               📊 Emergency Response Reports                 │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 📂 Repository Structure

```
ECOSPHERE_X/
├── ecosphere/
│   ├── satellite/              # Sentinel-2 data processing
│   │   ├── fetcher.py         # Satellite imagery acquisition
│   │   ├── indices.py         # NDVI/NDWI computation
│   │   └── visualizer.py      # Mapping and visualization
│   ├── gdelt/                 # GDELT news processing
│   │   ├── scraper.py         # News event extraction
│   │   ├── sentiment.py       # Sentiment analysis
│   │   └── exporter.py        # JSON export utilities
│   ├── knowledge_graph/       # Graph construction
│   │   ├── builder.py         # KG creation logic
│   │   ├── exporter.py        # PyVis/GEXF export
│   │   └── schema.py          # Graph schema definitions
│   ├── analytics/             # Data analysis
│   │   ├── timeline.py        # Temporal analysis
│   │   ├── sentiment.py       # Sentiment metrics
│   │   └── correlation.py     # Cross-modal alignment
│   └── agent/                 # Analytics & reporting
│       ├── classifier.py      # Priority assignment
│       ├── recommender.py     # Action generation
│       └── reporter.py        # Report generation
├── pipeline.py                # End-to-end orchestration
├── data/                      # Input data storage
│   ├── raw/                   # Raw satellite/news data
│   └── processed/             # Cleaned datasets
├── artifacts/                 # Generated outputs
│   ├── graphs/                # KG visualizations
│   ├── maps/                  # Satellite maps
│   └── reports/               # Emergency reports
├── notebooks/                 # Jupyter exploration
│   ├── EDA.ipynb             # Exploratory analysis
│   └── Demo.ipynb            # System demonstration
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Microsoft Planetary Computer API access
- GDELT API access (free)

### Installation

```bash
# Clone the repository
git clone https://github.com/Kweenbee187/ECOSPHERE_X.git
cd ECOSPHERE_X

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory:

```env
PLANETARY_COMPUTER_KEY=your_api_key_here
GDELT_API_KEY=your_gdelt_key_here  # Optional
```

### Quick Start

```bash
# Run the complete pipeline
python pipeline.py --location "Kerala, India" --date "2018-08-15"

# Or run individual modules
python -m ecosphere.satellite.fetcher --coords 10.8505 76.2711
python -m ecosphere.gdelt.scraper --query "Kerala floods 2018"
python -m ecosphere.agent.classifier --input artifacts/knowledge_graph.json
```

---

## 📊 Sample Outputs

### Knowledge Graph Visualization
Interactive graph showing connections between satellite observations and news reports.

### Emergency Response Report
```
PRIORITY: HIGH
CONFIDENCE: 0.92

EVIDENCE:
- Satellite NDWI increased by 45% (flood indicator)
- 127 distress-related news articles in 24h
- Sentiment score: -0.78 (highly negative)

RECOMMENDATIONS:
1. Deploy emergency response teams to affected areas
2. Establish temporary shelters in elevated regions
3. Coordinate with local authorities for evacuation
4. Monitor water levels via satellite for 72h
```

---

## 🔬 Technical Stack

| Component | Technology |
|-----------|------------|
| Satellite Data | Sentinel-2 L2A via Microsoft Planetary Computer |
| News Intelligence | GDELT Project API |
| Knowledge Graph | NetworkX, PyVis, GEXF |
| Analytics | Pandas, NumPy, Matplotlib |
| Geospatial | Rasterio, GeoPandas, Folium |
| Sentiment | VADER, TextBlob |

---

## 🎓 Use Cases

- **Disaster Response Planning** - Real-time emergency prioritization
- **Climate Research** - Multi-source environmental analysis
- **Policy Making** - Evidence-based decision support
- **NGO Operations** - Resource allocation optimization
- **Insurance Assessment** - Risk evaluation with ground truth

---

## 🗺️ Roadmap

- [ ] Real-time streaming pipeline
- [ ] Additional satellite data sources (Landsat, MODIS)
- [ ] Predictive modeling for disaster forecasting
- [ ] Mobile app for field responders
- [ ] Integration with emergency management systems
- [ ] Multi-language news sentiment analysis

---

## 🤝 Contributors

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Kweenbee187">
        <img src="https://github.com/Kweenbee187.png?size=100" width="100px;" alt=""/>
        <br />
        <sub><b>@Kweenbee187</b></sub>
      </a>
      <br />
      <sub></sub>
    </td>
    <td align="center">
      <a href="https://github.com/tituatgithub">
        <img src="https://github.com/tituatgithub.png?size=100" width="100px;" alt=""/>
        <br />
        <sub><b>@tituatgithub</b></sub>
      </a>
      <br />
      <sub></sub>
    </td>
  </tr>
</table>

---

## 📄 License

This project is licensed under the **Apache License 2.0** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **SEED Global Hackathon** for the opportunity
- **Microsoft Planetary Computer** for satellite data access
- **GDELT Project** for global news event data
- **ESA Copernicus Programme** for Sentinel-2 mission
- Kerala disaster response teams who inspired this work

---

## 📮 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/Kweenbee187/ECOSPHERE_X/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Kweenbee187/ECOSPHERE_X/discussions)

---

<div align="center">

**🌍 Making climate intelligence accessible for better disaster response**

[![Star this repo](https://img.shields.io/github/stars/Kweenbee187/ECOSPHERE_X?style=social)](https://github.com/Kweenbee187/ECOSPHERE_X)

</div>
