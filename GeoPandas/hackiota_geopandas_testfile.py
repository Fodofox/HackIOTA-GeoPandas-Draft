### GeoPandas extends the datatypes used by pandas to allow spatial operations on geometric types.
### Geometric operations are performed by shapely. 
### Geopandas further depends on fiona for file access and matplotlib for plotting.
### The feasibility of GeoPandas with HackIOTA would still require testing in later stages of the project.
import geopandas as gpd
import matplotlib.pyplot as plt

### This file will generate two maps, as an example or basis of a possible implementation
###  to visualise data in fixed areas, additionally to just points, using Foilum to create interactive maps.
### Map Nr. 1 should give insight into a possible version of an air quality map, 
###  including critical points / points of interest.
### Map Nr. 2 will instead capture and display the temperature. Example temperatures have been
###  added manually below for convenience. The colours correspond to the temperature value.

# Importing ESRI Shapefiles for coordinates
districts = gpd.read_file(r'C:\GeoPandas\Shapefiles\districts.shp')
area_of_interest = gpd.read_file(r'C:\GeoPandas\Shapefiles\area_of_interest.shp')

# Uncomment to generate an additional, default map with only the area of interest:
# area_of_interest.plot() 

points_of_interest = gpd.read_file(r'C:\GeoPandas\Shapefiles\atms.shp')

# Example data - column gets created, in the 'districts', named temperature
districts.loc[0,'temperature'] = 22
districts.loc[1,'temperature'] = 17
districts.loc[2:3,'temperature'] = 24
districts.loc[4:5,'temperature'] = 20
districts.loc[6,'temperature'] = 19
districts.loc[7:8,'temperature'] = 18
districts.loc[9:10,'temperature'] = 21


# The following map does NOT use number data for the colour assignments, but the names
 # Plotting "Orange Map":
  #1 - District Layer
fig, ax = plt.subplots(figsize = (8,6))
districts = districts.to_crs(epsg = 32629) 
districts.plot(ax = ax, cmap = 'Oranges', edgecolor = 'black', column = 'district')
  #2 - Red Outline of Area of Interest in Center
area_of_interest = area_of_interest.to_crs(epsg = 32629) #converting to local coordinate system
area_of_interest.plot(ax = ax, color = 'none', edgecolor = 'red')
  #3 - Points of Importance/Interest
points_of_interest = points_of_interest.to_crs(32629) 
points_of_interest.plot(ax = ax, cmap = 'Oranges', markersize = 40, edgecolor = 'black')

# The following map uses the 'temperature' column to assign the colours
tempmap = districts
fig, ax = plt.subplots(figsize = (8,6))
tempmap.plot(ax = ax, cmap = 'coolwarm', edgecolor = 'black', column = 'temperature')


# Additional functions:

 # Example set operation: Intersection of Layers
 #districts_in_aoi = gpd.overlay(districts, area_of_interest, how = 'intersection')
 #districts_in_aoi.plot(edgecolor = 'red')

 # Calculating the areas of the intersected layer in square-kilometers
 #districts_in_aoi['area'] = districts_in_aoi.area/1000000

 # Exporting GeoPandas GeoDataFrames into an ESRI Shapefile
 #districts_in_aoi.to_file('districts_within_aoi.shp', driver = "ESRI Shapefile")