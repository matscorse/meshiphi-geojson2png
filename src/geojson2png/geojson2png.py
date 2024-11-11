import geopandas as gpd
import matplotlib.pyplot as plt


_XSIZE = 40
_YSIZE = 30


df = gpd.read_file('amsr_southern_SDA.vessel.geojson')

bounds = df.geometry.total_bounds

fig, ax = plt.subplots(figsize = (_XSIZE,_YSIZE))

df.to_crs(epsg=4326).plot(column='SIC', ax=ax, edgecolor='grey', linewidth=0.5, cmap = 'coolwarm')

df.to_crs(epsg=4326).plot(column='land', ax=ax, edgecolor='brown', linewidth=0.5, cmap = 'copper')

plt.savefig('amsr_southern_SDA.vessel.geojson.png', dpi=180)
