ECOSPHERE_X/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── ecosphere/
│   ├── __init__.py
│   ├── config.py
│   │
│   ├── satellite/
│   │   ├── fetch_satellite.py
│   │   ├── compute_indices.py
│   │   └── save_visualizations.py
│   │
│   ├── gdelt/
│   │   ├── fetch_gdelt.py
│   │   ├── clean_gdelt.py
│   │   └── gdelt_utils.py
│   │
│   ├── knowledge_graph/
│   │   ├── build_graph.py
│   │   └── visualize_graph.py
│   │
│   ├── analytics/
│   │   ├── statistics.py
│   │   └── timeline.py
│   │
│   ├── agent/
│   │   └── decision_agent.py
│   │
│   └── pipeline.py
│
├── data/
│   ├── satellite/         # EMPTY: user will add data manually
│   ├── gdelt/
│   └── processed/
│
├── artifacts/
│   └── (empty - generated automatically)
│
└── notebooks/
    └── ecosphere_demo.ipynb    # You will manually add your Kaggle notebook
