from pyvis.network import Network

def save_graph(G, out_html):
    net = Network(height="600px", width="100%", bgcolor="#222")
    net.from_nx(G)

    color_map = {
        "Place": "#FF6B6B",
        "Observation": "#4ECDC4",
        "HumanSignal": "#95E1D3"
    }

    for n in net.nodes:
        t = G.nodes[n["id"]].get("type", "")
        n["color"] = color_map.get(t, "#CCC")

    net.save_graph(out_html)
