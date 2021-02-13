import geoplot as gplt
import geopandas as gpd
import geoplot.crs as gcrs
import imageio
import pandas as pd
import pathlib
import matplotlib.pyplot as plt
import mapclassify as mc
import numpy as np
import glob

states = [
  ('alabama', 'al'),
  ('alaska', 'ak'),
  ('arizona', 'az'),
  ('arkansas', 'ar'),
  ('california', 'ca'),
  ('colorado', 'co'),
  ('connecticut', 'ct'),
  ('dc', 'dc'),
  ('delaware', 'de'),
  ('florida', 'fl'),
  ('georgia', 'ga'),
  ('hawaii', 'hi'),
  ('idaho', 'id'),
  ('illinois', 'il'),
  ('indiana', 'in'),
  ('iowa', 'ia'),
  ('kansas', 'ks'),
  ('kentucky', 'ky'),
  ('louisiana', 'la'),
  ('maine', 'me'),
  ('maryland', 'md'),
  ('massachusetts', 'ma'),
  ('michigan', 'mi'),
  ('minnesota', 'mn'),
  ('mississippi', 'ms'),
  ('missouri', 'mo'),
  ('montana', 'mt'),
  ('nebraska', 'ne'),
  ('nevada', 'nv'),
  ('new hampshire', 'nh'),
  ('new jersey', 'nj'),
  ('new mexico', 'nm'),
  ('new york', 'ny'),
  ('north carolina', 'nc'),
  ('north dakota', 'nd'),
  ('ohio', 'oh'),
  ('oklahoma', 'ok'),
  ('oregon', 'or'),
  ('pennsylvania', 'pa'),
  ('puerto rico', 'pr'),
  ('rhode island', 'ri'),
  ('south carolina', 'sc'),
  ('south dakota', 'sd'),
  ('tennessee', 'tn'),
  ('texas', 'tx'),
  ('utah', 'ut'),
  ('vermont', 'vt'),
  ('virginia', 'va'),
  ('washington', 'wa'),
  ('west virginia', 'wv'),
  ('wisconsin', 'wi'),
  ('wyoming', 'wy'),
]

df = pd.read_csv('./data/hometowns.csv')
state_pops = pd.read_csv('./data/populations.csv', delimiter='	')
state_pops['pop'] = state_pops['2019'].str.replace(',', '').astype(float)
print(state_pops.head())
state_gdf = gpd.read_file("./maps/cb_2018_us_state_500k/cb_2018_us_state_500k.shp")
usa = gpd.read_file("./maps/cb_2019_us_county_500k/cb_2019_us_county_500k.shp")
df = df[~df['player'].isin(['bitadgo01', 'tsakaja01', 'tskitni01'])]
df['Region'] = df['birthplace'].str.split(',').str[1].str.strip()
df['City'] = df['birthplace'].str.split(',').str[0].str.strip()
state_df = df.groupby('Region')[['per', 'mp']].sum()
state_df['count'] = df.groupby('Region')['player_id'].count()
state_df = state_df.reset_index()
print(state_gdf.head())
crs = gcrs.AlbersEqualArea(central_longitude=-96, central_latitude=37.5)
extent = (-121, 25.25, -73, 49.5)
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1], projection=crs)
ax.axis('off')
# gplt.polyplot(
#   state_gdf,
#   ax=ax,
#   projection=crs,
#   linewidth=0.25,
#   extent=extent,
#   edgecolor='white',
#   facecolor='lightgray',
# )
ax.margins(0)
alaska_extent = (-173, 54, -130, 72)
alaska_crs = gcrs.LambertAzimuthalEqualArea(central_longitude=-153, central_latitude=66)
hawaii_extent = (-160, 18.75, -154, 22.5)
hawaii_crs = gcrs.LambertAzimuthalEqualArea(central_longitude=-156, central_latitude=20)
pr_extent = (-67.5, 17.9, -65, 18.6)
pr_crs = gcrs.LambertAzimuthalEqualArea(central_longitude=-66, central_latitude=18)
alaska_ax = fig.add_axes([0.05, 0.05, 0.2, 0.2], projection=alaska_crs)
alaska_ax.axis('off')
alaska_ax.margins(0)
hawaii_ax = fig.add_axes([0.25, 0.05, 0.125, 0.125], projection=hawaii_crs)
hawaii_ax.axis('off')
hawaii_ax.margins(0)
pr_ax = fig.add_axes([0.9, 0.05, 0.075, 0.075], projection=pr_crs)
pr_ax.axis('off')
pr_ax.margins(0)
state_df = state_pops.merge(state_df, left_on='State', right_on='Region', how='left')
state_df['count'] = state_df['count'].fillna(0)
state_df['per'] = state_df['per'].fillna(0)
state_df['mp'] = state_df['mp'].fillna(0)
merged = state_gdf.merge(state_df, left_on='NAME', right_on='State')
# print(state_df[state_df['Region'] == 'New Hampshire'])
# print(state_df[~state_df['Region'].isin(merged['NAME'])]['Region'])
merged['per_capita_mp'] = merged['mp'] / merged['pop']
print(merged.columns)
scheme = mc.Quantiles(merged['per_capita_mp'], k=30)
gplt.choropleth(
  merged,
  ax=ax,
  hue='per_capita_mp',
  edgecolor='gray',
  projection=crs,
  cmap='Reds',
  extent=extent,
  linewidth=.25,
  scheme=scheme,
)
gplt.choropleth(
  merged,
  ax=hawaii_ax,
  hue='per_capita_mp',
  edgecolor='gray',
  projection=hawaii_crs,
  cmap='Reds',
  extent=hawaii_extent,
  linewidth=.25,
  scheme=scheme,
)
gplt.choropleth(
  merged,
  ax=pr_ax,
  hue='per_capita_mp',
  edgecolor='gray',
  projection=pr_crs,
  cmap='Reds',
  extent=pr_extent,
  linewidth=.25,
  scheme=scheme,
)
gplt.choropleth(
  merged,
  ax=alaska_ax,
  hue='per_capita_mp',
  edgecolor='gray',
  projection=alaska_crs,
  cmap='Reds',
  extent=alaska_extent,
  linewidth=.25,
  scheme=scheme,
)
proj4 = '+proj=aea +lat_0=37.5 +lon_0=-96 +lat_1=20 +lat_2=50'
alaska_proj4 = '+proj=laea +lat_0=66 +lon_0=-153'
hawaii_proj4 = '+proj=laea +lat_0=20 +lon_0=-156'
pr_proj4 = '+proj=laea +lat_0=18 +lon_0=-66'
state_gdf = state_gdf.to_crs(proj4)
# merged = merged.to_crs(proj4)
for index, row in state_gdf[~state_gdf['NAME'].isin(['Alaska', 'Hawaii', 'Puerto Rico'])].iterrows():
  if (row['NAME'] == 'District of Columbia'):
    label = 'DC'
  else:
    offset_x = 0
    offset_y = 0
    if (row['NAME'] == 'Maryland'):
      offset_x = 1000
      offset_y = 50000
    matching_state = [x for x in states if x[0].title() == row['NAME']]
    if (len(matching_state) == 1):
      label = matching_state[0][1].upper()
  ax.text(s=label, x=row['geometry'].representative_point().coords[0][0] + offset_x, y=row['geometry'].representative_point().coords[0][1] + offset_y, ha='center', va='center', fontsize=4)
state_gdf = state_gdf.to_crs(alaska_proj4)
for index, row in state_gdf[state_gdf['NAME'] == 'Alaska'].iterrows():
  alaska_ax.text(s='AK', x=row['geometry'].centroid.coords[0][0], y=row['geometry'].centroid.coords[0][1], ha='center', va='center', fontsize=4)
state_gdf = state_gdf.to_crs(hawaii_proj4)
for index, row in state_gdf[state_gdf['NAME'] == 'Hawaii'].iterrows():
  hawaii_ax.text(s='HI', x=row['geometry'].centroid.coords[0][0] + offset_x, y=row['geometry'].centroid.coords[0][1] + offset_y, ha='center', va='center', fontsize=4)
state_gdf = state_gdf.to_crs(pr_proj4)
for index, row in state_gdf[state_gdf['NAME'] == 'Puerto Rico'].iterrows():
  pr_ax.text(s='PR', x=row['geometry'].centroid.coords[0][0], y=row['geometry'].centroid.coords[0][1], ha='center', va='center', fontsize=4)
fig.suptitle('Where NBA Players Come From')
fig.text(
  s='Color represents total minutes played per capita',
  x=0.5,
  y=0.93,
  ha='center',
  va='top',
  fontsize=6,
)
fig.text(
  s='American-born players only, All NBA Seasons (1949-50 to 2020-2021)',
  x=0.5,
  y=0.91,
  ha='center',
  va='top',
  fontsize=6,
)
fig.text(
  s='Plot: @lawlorpalooza, Data: Basketball Reference, Shapefiles: US Census',
  x=0.01,
  y=0.01,
  ha='left',
  va='bottom',
  fontsize=6,
)
plt.savefig('./output/NBA Player Birthplace State Choropleth.png', dpi=800)
plt.close()