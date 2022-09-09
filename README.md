# HackIOTA-GeoPandas-Draft
A primitive draft for utilizing GeoPandas using publicly available data as an example.
The practicality of using GeoPandas, to include surface areas or lines, as opposed to only points, remains to be seen or tested in later stages of development.
Interactive properties would be achieved by additionally using Folium.


GeoPandas is dependent on: 
numpy; pandas (version 1.0 or later) - shapely (interface to GEOS; version 1.7 or later) - fiona (interface to GDAL; version 1.8 or later) - pyproj (interface to PROJ; version 2.6.1 or later) - packaging
IMPORTANT: Testing discovered that shapely 1.7 and numpy 1.23 can cause issues when used together on these versions.

Further, optional dependencies are:
- pyogrio (optional; experimental alternative for fiona)
- rtree (optional; spatial index to improve performance and required for overlay operations; interface to libspatialindex)
- psycopg2 (optional; for PostGIS connection)
- GeoAlchemy2 (optional; for writing to PostGIS)
- geopy (optional; for geocoding)

