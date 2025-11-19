import rasterio
from pystac_client import Client
import planetary_computer

from ecosphere.config import BBOX, DATE_RANGE, MAX_CLOUD_COVER


def fetch_best_item():
    catalog = Client.open(
        "https://planetarycomputer.microsoft.com/api/stac/v1",
        modifier=planetary_computer.sign_inplace
    )

    search = catalog.search(
        collections=["sentinel-2-l2a"],
        bbox=BBOX,
        datetime=DATE_RANGE,
        query={"eo:cloud_cover": {"lt": MAX_CLOUD_COVER}}
    )
    items = list(search.items())
    if not items:
        raise ValueError("No satellite scenes found.")

    return min(items, key=lambda x: x.properties.get("eo:cloud_cover", 100))


def download_band(item, band_name, output_path):
    signed = planetary_computer.sign(item.assets[band_name])
    with rasterio.open(signed.href) as src:
        data = src.read(1)
        profile = src.profile
    with rasterio.open(output_path, "w", **profile) as dst:
        dst.write(data, 1)
    return data, profile
