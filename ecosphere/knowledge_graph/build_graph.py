import networkx as nx
from shapely.geometry import Point, box

def build_kg(ndvi_summary, human_clean, bbox):
    G = nx.Graph()

    G.add_node("kerala_region",
               type="Place",
               mean_ndvi=ndvi_summary["mean_ndvi"],
               mean_ndwi=ndvi_summary["mean_ndwi"],
               bounds=str(bbox))

    G.add_node("sentinel_obs_1",
               type="Observation",
               timestamp=ndvi_summary["observation_date"],
               ndvi=ndvi_summary["mean_ndvi"],
               ndwi=ndvi_summary["mean_ndwi"])

    G.add_edge("sentinel_obs_1", "kerala_region", relation="OBSERVED_AT")

    region = box(*bbox)

    for hs in human_clean:
        node = hs["id"]
        G.add_node(node, **hs, type="HumanSignal")

        p = Point(hs["lon"], hs["lat"])
        if region.contains(p):
            G.add_edge(node, "kerala_region", relation="REPORTS_ABOUT")

    return G
