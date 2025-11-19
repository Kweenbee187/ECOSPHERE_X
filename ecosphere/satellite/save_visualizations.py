import matplotlib.pyplot as plt

def save_ndvi_visualization(ndvi, ndwi, out_path):
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(ndvi, cmap="RdYlGn", vmin=-0.5, vmax=0.8)
    plt.colorbar(label="NDVI")

    plt.subplot(1, 2, 2)
    plt.imshow(ndwi, cmap="Blues", vmin=-0.5, vmax=0.5)
    plt.colorbar(label="NDWI")

    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close()
