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

df = pd.read_csv('./data/hometowns.csv')
df['Region'] = df['birthplace'].str.split(',').str[1].str.strip()
df['City'] = df['birthplace'].str.split(',').str[0].str.strip()
df = df[df['Region'] == 'Canada']
print(df.shape)
print(df['City'])
provinces = [
  'ontario'
]
df['Province'] = 'Ontario'
df.loc[df['City'] == 'Montreal', 'Province'] = 'Quebec'
df.loc[df['City'] == 'Vancouver', 'Province'] = 'British Columbia'
df.loc[df['City'] == 'Saskatoon', 'Province'] = 'Saskatchewan'
place_df = None
for province in provinces:
  province_place = gpd.read_file(glob.glob(f'./maps/canada/province-places/{province}/*.shp')[0])
  province_place['province'] = province.title()
  # if (province == 'pennsylvania'):
  #   province_place["NAME"].to_csv('./pa-places.csv')
  if (place_df is None):
    place_df = province_place.copy()
  else:
    place_df=place_df.append(province_place)
canada_crs = gcrs.LambertConformal()
canada_extent = (-141,42,-53,83)
canada_provinces = gpd.read_file('./maps/canada/canada provinces/lpr_000b16a_e.shp')
# print(canada_provinces.crs)
# place_df['geometry'] = place_df['geometry'].centroid
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
ax.margins(0)
place_df = place_df[place_df['CATEGORY'] == 'Populated Place']
place_df = place_df.drop_duplicates(subset='GEONAME')
grouped_df = df.groupby(['City', 'Province'])['per', 'mp'].sum()
grouped_df['count'] = df.groupby(['City', 'Province'])['player'].count()
grouped_df = grouped_df.reset_index()
merged = place_df.merge(grouped_df, left_on=['GEONAME', 'province'], right_on=['City', 'Province'])
merged['geometry'] = merged['geometry'].to_crs(canada_provinces.crs).centroid
canada_provinces.plot(
  facecolor='lightgray',
  edgecolor='white',
  ax=ax,
)
merged.plot(
  ax=ax,
  marker='o',
  color='gray',
  alpha=0.5,
  markersize='mp',
)
# gplt.pointplot(
#   canada_places,
#   ax=ax,
#   # scale='mp',
#   # limits=(2,20),
#   color='gray',
#   alpha=0.5,
# )
plt.savefig('./output/canada.png')