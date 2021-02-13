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
import pyproj as proj

include_canada = False

df = pd.read_csv('./data/hometowns.csv')
# df = df[df['season'] > 1979]
# df2 = pd.read_csv('./data/hometowns-past.csv')
# df = df.append(df2)
# df.to_csv('./data/hometowns.csv', index=False)
print(df.shape)
# df = df[df['season'] == 2021]
df.loc[df['birthplace'] == 'Ventura, California', 'birthplace'] = 'San Buenaventura (Ventura), California'
df.loc[df['birthplace'] == 'Etiwanda, California', 'birthplace'] = 'Rancho Cucamonga, California'
df.loc[df['birthplace'] == 'Indianapolis, Indiana', 'birthplace'] = 'Indianapolis city (balance), Indiana'
df.loc[df['birthplace'] == 'North Tarrytown, New York', 'birthplace'] = 'Sleepy Hollow, New York'
df.loc[df['birthplace'] == 'Henrico, Virginia', 'birthplace'] = 'Richmond, Virginia'
df.loc[df['birthplace'] == 'Wynnewood, Pennsylvania', 'birthplace'] = 'Ardmore, Pennsylvania'
df.loc[df['birthplace'] == 'Chatsworth, California', 'birthplace'] = 'Los Angeles, California'
df.loc[df['birthplace'] == 'Harbor City, California', 'birthplace'] = 'Los Angeles, California'
df.loc[df['birthplace'] == 'Hollywood, California', 'birthplace'] = 'Los Angeles, California'
df.loc[df['birthplace'] == 'Greenbrae, California', 'birthplace'] = 'Kentfield, California'
df.loc[df['birthplace'] == 'Palos Verdes, California', 'birthplace'] = 'Palos Verdes Estates, California'
df.loc[df['birthplace'] == 'Laguna, California', 'birthplace'] = 'Elk Grove, California'
df.loc[df['birthplace'] == 'Northridge, California', 'birthplace'] = 'Los Angeles, California'
df.loc[df['birthplace'] == 'Tarzana, California', 'birthplace'] = 'Los Angeles, California'
df.loc[df['birthplace'] == 'San Pedro, California', 'birthplace'] = 'Los Angeles, California'
df.loc[df['birthplace'] == 'La Jolla, California', 'birthplace'] = 'San Diego, California'
df.loc[df['birthplace'] == 'Fort Ord, California', 'birthplace'] = 'Marina, California'
df.loc[df['birthplace'] == 'Chesterfield, Virginia', 'birthplace'] = 'Richmond, Virginia'
df.loc[df['birthplace'] == 'Edison, New Jersey', 'birthplace'] = 'Metuchen, New Jersey'
df.loc[df['birthplace'] == 'Cherry Hill, New Jersey', 'birthplace'] = 'Cherry Hill Mall, New Jersey'
df.loc[df['birthplace'] == 'Hillside, New Jersey', 'birthplace'] = 'Elizabeth, New Jersey'
df.loc[df['birthplace'] == 'Irvington, New Jersey', 'birthplace'] = 'Elizabeth, New Jersey'
df.loc[df['birthplace'] == 'Livingston, New Jersey', 'birthplace'] = 'Short Hills, New Jersey'
df.loc[df['birthplace'] == 'Millstone Township, New Jersey', 'birthplace'] = 'Millstone, New Jersey'
df.loc[df['birthplace'] == 'Orange, New Jersey', 'birthplace'] = 'East Orange, New Jersey'
df.loc[df['birthplace'] == 'West Orange, New Jersey', 'birthplace'] = 'East Orange, New Jersey'
df.loc[df['birthplace'] == 'Plainsboro, New Jersey', 'birthplace'] = 'Plainsboro Center, New Jersey'
df.loc[df['birthplace'] == 'Seacaucus, New Jersey', 'birthplace'] = 'Secaucus, New Jersey'
df.loc[df['birthplace'] == 'Teaneck, New Jersey', 'birthplace'] = 'Hackensack, New Jersey'
df.loc[df['birthplace'] == 'Willingboro, New Jersey', 'birthplace'] = 'Burlington, New Jersey'
df.loc[df['birthplace'] == 'Riverside, New Jersey', 'birthplace'] = 'Burlington, New Jersey'
df.loc[df['birthplace'] == 'Neptune, New Jersey', 'birthplace'] = 'Neptune City, New Jersey'
df.loc[df['birthplace'] == 'Kearney, New Jersey', 'birthplace'] = 'Kearny, New Jersey'
df.loc[df['birthplace'] == 'Maplewood, New Jersey', 'birthplace'] = 'East Orange, New Jersey'
df.loc[df['birthplace'] == 'Hamilton, Massachusetts', 'birthplace'] = 'Ipswich, Massachusetts'
df.loc[df['birthplace'] == 'Bernardston, Massachusetts', 'birthplace'] = 'Northfield, Massachusetts'
df.loc[df['birthplace'] == 'Roslindale, Massachusetts', 'birthplace'] = 'Boston, Massachusetts'
df.loc[df['birthplace'] == 'Roxbury, Massachusetts', 'birthplace'] = 'Boston, Massachusetts'
df.loc[df['birthplace'] == 'Weymouth, Massachusetts', 'birthplace'] = 'Weymouth Town, Massachusetts'
df.loc[df['birthplace'] == 'Winthrop, Massachusetts', 'birthplace'] = 'Winthrop Town, Massachusetts'
df.loc[df['birthplace'] == 'Nashville, Tennessee', 'birthplace'] = 'Nashville-Davidson metropolitan government (balance), Tennessee'
df.loc[df['birthplace'] == 'Antioch, Tennessee', 'birthplace'] = 'Nashville-Davidson metropolitan government (balance), Tennessee'
df.loc[df['birthplace'] == 'Mt. Juliet, Tennessee', 'birthplace'] = 'Mount Juliet, Tennessee'
df.loc[df['birthplace'] == 'Coffee County, Tennessee', 'birthplace'] = 'Manchester, Tennessee'
df.loc[df['birthplace'] == 'Coldwater, Tennessee', 'birthplace'] = 'Fayetteville, Tennessee'
df.loc[df['birthplace'] == 'Brooklyn, New York', 'birthplace'] = 'New York, New York'
df.loc[df['birthplace'] == 'Queens, New York', 'birthplace'] = 'New York, New York'
df.loc[df['birthplace'] == 'The Bronx, New York', 'birthplace'] = 'New York, New York'
df.loc[df['birthplace'] == 'Bronx, New York', 'birthplace'] = 'New York, New York'
df.loc[df['birthplace'] == 'Staten Island, New York', 'birthplace'] = 'New York, New York'
df.loc[df['birthplace'] == 'Harlem, New York', 'birthplace'] = 'New York, New York'
df.loc[df['birthplace'] == 'Queens Village, New York', 'birthplace'] = 'New York, New York'
df.loc[df['birthplace'] == 'Queensbridge, New York', 'birthplace'] = 'New York, New York'
df.loc[df['birthplace'] == 'Jamaica, New York', 'birthplace'] = 'New York, New York'
df.loc[df['birthplace'] == 'Rockaway, New York', 'birthplace'] = 'New York, New York'
df.loc[df['birthplace'] == 'Sunnyside, New York', 'birthplace'] = 'New York, New York'
df.loc[df['birthplace'] == 'Astoria, New York', 'birthplace'] = 'New York, New York'
df.loc[df['birthplace'] == 'Far Rockaway, New York', 'birthplace'] = 'New York, New York'
df.loc[df['birthplace'] == 'New York City, New York', 'birthplace'] = 'New York, New York'
df.loc[df['birthplace'] == 'Long Island City, New York', 'birthplace'] = 'New York, New York'
df.loc[df['birthplace'] == 'Flushing, New York', 'birthplace'] = 'New York, New York'
df.loc[df['birthplace'] == 'Richmond, New York', 'birthplace'] = 'New York, New York'
df.loc[df['birthplace'] == 'Elmhurst, New York', 'birthplace'] = 'New York, New York'
df.loc[df['birthplace'] == 'Glendale, New York', 'birthplace'] = 'New York, New York'
df.loc[df['birthplace'] == 'Amherst, New York', 'birthplace'] = 'Williamsville, New York'
df.loc[df['birthplace'] == 'Carmel, New York', 'birthplace'] = 'Mahopac, New York'
df.loc[df['birthplace'] == 'Cortlandt Manor, New York', 'birthplace'] = 'Peekskill, New York'
df.loc[df['birthplace'] == 'Lockwood, New York', 'birthplace'] = 'Spencer, New York'
df.loc[df['birthplace'] == 'Bayshore, New York', 'birthplace'] = 'Bay Shore, New York'
df.loc[df['birthplace'] == 'Southhampton, New York', 'birthplace'] = 'Southampton, New York'
df.loc[df['player_id'] == 'thomptr02', 'birthplace'] = 'Lithonia, Georgia'
df.loc[df['player_id'] == 'rowinji01', 'birthplace'] = 'Syosset, New York'
df.loc[df['player_id'] == 'mullajo01', 'birthplace'] = 'New York, New York'
df.loc[df['player_id'] == 'mahnkjo01', 'birthplace'] = 'West New York, New Jersey'
df.loc[df['player_id'] == 'hermabi01', 'birthplace'] = 'Dover, Ohio'
df.loc[df['player_id'] == 'kubiale01', 'birthplace'] = 'Toledo, Ohio'
df.loc[df['birthplace'] == 'York, Maine', 'birthplace'] = 'York Harbor, Maine'
df.loc[df['birthplace'] == 'North Hollywood, California', 'birthplace'] = 'Los Angeles, California'
df.loc[df['birthplace'] == 'Reseda, California', 'birthplace'] = 'Los Angeles, California'
df.loc[df['birthplace'] == 'Moon Township, Pennsylvania', 'birthplace'] = 'Pittsburgh, Pennsylvania'
df.loc[df['birthplace'] == 'Penn Hills, Pennsylvania', 'birthplace'] = 'Pittsburgh, Pennsylvania'
df.loc[df['birthplace'] == 'Holland, Pennsylvania', 'birthplace'] = 'Village Shires, Pennsylvania'
df.loc[df['birthplace'] == 'Orange County, California', 'birthplace'] = 'Yorba Linda, California'
df.loc[df['birthplace'] == 'Maui, Hawaii', 'birthplace'] = 'Kahului, Hawaii'
df.loc[df['birthplace'] == 'Daytona, Florida', 'birthplace'] = 'Daytona Beach, Florida'
df.loc[df['birthplace'] == 'Fort Walton, Florida', 'birthplace'] = 'Fort Walton Beach, Florida'
df.loc[df['birthplace'] == 'Ft. Lauderdale, Florida', 'birthplace'] = 'Fort Lauderdale, Florida'
df.loc[df['birthplace'] == 'Augusta, Georgia', 'birthplace'] = 'Augusta-Richmond County consolidated government (balance), Georgia'
df.loc[df['birthplace'] == 'Omaha, Georgia', 'birthplace'] = 'Lumpkin, Georgia'
df.loc[df['birthplace'] == 'Macon, Georgia', 'birthplace'] = 'Macon-Bibb County, Georgia'
df.loc[df['birthplace'] == 'Twiggs, Georgia', 'birthplace'] = 'Jeffersonville, Georgia'
df.loc[df['birthplace'] == 'Newman, Georgia', 'birthplace'] = 'Newnan, Georgia'
df.loc[df['birthplace'] == 'Dekalb, Illinois', 'birthplace'] = 'DeKalb, Illinois'
df.loc[df['birthplace'] == 'Mt. Vernon, Illinois', 'birthplace'] = 'Mount Vernon, Illinois'
df.loc[df['birthplace'] == 'Rosemond, Illinois', 'birthplace'] = 'Rosemont, Illinois'
df.loc[df['birthplace'] == 'East St. Louis, Missouri', 'birthplace'] = 'East St. Louis, Illinois'
df.loc[df['birthplace'] == 'Charlestown, Missouri', 'birthplace'] = 'Charleston, Missouri'
df.loc[df['birthplace'] == 'Lexington, Kentucky', 'birthplace'] = 'Lexington-Fayette, Kentucky'
df.loc[df['birthplace'] == 'Linwood, Michigan', 'birthplace'] = 'Auburn, Michigan'
df.loc[df['birthplace'] == 'Pleasant Grove, North Carolina', 'birthplace'] = 'Burlington, North Carolina'
df.loc[df['birthplace'] == 'Golden Valley, North Carolina', 'birthplace'] = 'Casar, North Carolina'
df.loc[df['birthplace'] == 'Hoke, North Carolina', 'birthplace'] = 'Raeford, North Carolina'
df.loc[df['birthplace'] == 'Lowlands, North Carolina', 'birthplace'] = 'Bayboro, North Carolina'
df.loc[df['birthplace'] == 'Sharps, Virginia', 'birthplace'] = 'Warsaw, Virginia'
df.loc[df['birthplace'] == 'Mayaguez, Puerto Rico', 'birthplace'] = 'Mayagüez, Puerto Rico'
df.loc[df['birthplace'] == 'Santurce, Puerto Rico', 'birthplace'] = 'San Juan, Puerto Rico'
df.loc[df['birthplace'] == 'Summerfield, Louisiana', 'birthplace'] = 'Bernice, Louisiana'
df.loc[df['birthplace'] == 'Sailes, Louisiana', 'birthplace'] = 'Bryceland, Louisiana'
df.loc[df['birthplace'] == 'Crenshaw, Alabama', 'birthplace'] = 'Brantley, Alabama'
df.loc[df['birthplace'] == 'Knoxville, Alabama', 'birthplace'] = 'Eutaw, Alabama'
df.loc[df['birthplace'] == 'Perry, Alabama', 'birthplace'] = 'Marion, Alabama'
df.loc[df['birthplace'] == 'Patton, Alabama', 'birthplace'] = 'Oakman, Alabama'
df.loc[df['birthplace'] == 'McGhee, Arkansas', 'birthplace'] = 'McGehee, Arkansas'
df.loc[df['birthplace'] == 'Osecola, Arkansas', 'birthplace'] = 'Osceola, Arkansas'
df.loc[df['birthplace'] == 'Plummerville, Arkansas', 'birthplace'] = 'Plumerville, Arkansas'
df.loc[df['birthplace'] == 'Havre De Grace, Maryland', 'birthplace'] = 'Havre de Grace, Maryland'
df.loc[df['birthplace'] == 'Ark City, Kansas', 'birthplace'] = 'Arkansas City, Kansas'
df.loc[df['birthplace'] == 'Yale, Kansas', 'birthplace'] = 'Frontenac, Kansas'
df.loc[df['birthplace'] == 'Culpepper, Virginia', 'birthplace'] = 'Culpeper, Virginia'
df.loc[df['birthplace'] == 'Amelia, Virginia', 'birthplace'] = 'Amelia Court House, Virginia'
df.loc[df['birthplace'] == 'LaGrange, Illinois', 'birthplace'] = 'La Grange, Illinois'
df.loc[df['birthplace'] == 'LaPorte, Indiana', 'birthplace'] = 'La Porte, Indiana'
df.loc[df['birthplace'] == 'Lacrosse, Wisconsin', 'birthplace'] = 'La Crosse, Wisconsin'
df.loc[df['birthplace'] == 'LaCrosse, Wisconsin', 'birthplace'] = 'La Crosse, Wisconsin'
df.loc[df['birthplace'] == 'Lafarge, Wisconsin', 'birthplace'] = 'La Farge, Wisconsin'
df.loc[df['birthplace'] == 'New Canaan, Connecticut', 'birthplace'] = 'Darien, Connecticut'
df.loc[df['birthplace'] == 'Monroe, Connecticut', 'birthplace'] = 'Trumbull, Connecticut'
df.loc[df['birthplace'] == 'Falls County, Texas', 'birthplace'] = 'Marlin, Texas'
df.loc[df['birthplace'] == 'Larue, Texas', 'birthplace'] = 'Poynor, Texas'
df.loc[df['birthplace'] == 'Edge, Texas', 'birthplace'] = 'Kurten, Texas'
df.loc[df['birthplace'] == 'El Mina, Texas', 'birthplace'] = 'New Waverly, Texas'
df.loc[df['birthplace'] == 'Harleton, Texas', 'birthplace'] = 'Nesbitt, Texas'
df.loc[df['birthplace'] == 'Hillister, Texas', 'birthplace'] = 'Woodville, Texas'
df.loc[df['birthplace'] == 'Lenoir County, North Carolina', 'birthplace'] = 'Kinston, North Carolina'
df.loc[df['birthplace'] == 'Madison County, Mississippi', 'birthplace'] = 'Canton, Mississippi'
df.loc[df['birthplace'] == 'Bethlehem, Mississippi', 'birthplace'] = 'Potts Camp, Mississippi'
df.loc[df['birthplace'] == 'Carrolton, Mississippi', 'birthplace'] = 'Carrollton, Mississippi'
df.loc[df['birthplace'] == 'Thornton, Mississippi', 'birthplace'] = 'Yazoo City, Mississippi'
df.loc[df['birthplace'] == 'Nansemond County, Virginia', 'birthplace'] = 'Suffolk, Virginia'
df.loc[df['birthplace'] == 'Williamsburg County, South Carolina', 'birthplace'] = 'Hemingway, South Carolina'
df.loc[df['birthplace'] == 'Plymouth, South Carolina', 'birthplace'] = 'Plymouth, North Carolina'
df.loc[df['birthplace'] == 'Ritter, South Carolina', 'birthplace'] = 'Walterboro, South Carolina'
df.loc[df['birthplace'] == 'Orefield, Pennsylvania', 'birthplace'] = 'Allentown, Pennsylvania'
df.loc[df['birthplace'] == 'West Baden, Indiana', 'birthplace'] = 'West Baden Springs, Indiana'
df.loc[df['birthplace'] == 'Weirsdale, Florida', 'birthplace'] = 'Lady Lake, Florida'
df.loc[df['birthplace'] == 'West Warwick, Rhode Island', 'birthplace'] = 'Warwick, Rhode Island'
df.loc[df['birthplace'] == 'North Providence, Rhode Island', 'birthplace'] = 'Providence, Rhode Island'
df.loc[df['birthplace'] == 'Berkley, West Virginia', 'birthplace'] = 'Beckley, West Virginia'
df.loc[df['birthplace'] == 'Charlestown, West Virginia', 'birthplace'] = 'Charleston, West Virginia'
df.loc[df['birthplace'] == 'Birmingham, Kentucky', 'birthplace'] = 'Grand Rivers, Kentucky'
df.loc[df['birthplace'] == 'Caldwell, Kentucky', 'birthplace'] = 'Princeton, Kentucky'
df.loc[df['birthplace'] == 'Henshaw, Kentucky', 'birthplace'] = 'Sturgis, Kentucky'
df.loc[df['birthplace'] == 'Neon, Kentucky', 'birthplace'] = 'Fleming-Neon, Kentucky'
df.loc[df['birthplace'] == 'Williamsport, Kentucky', 'birthplace'] = 'Paintsville, Kentucky'
df.loc[df['birthplace'] == 'Clemenceau, Arizona', 'birthplace'] = 'Cottonwood, Arizona'
df.loc[df['birthplace'] == 'Grand View, Iowa', 'birthplace'] = 'Grandview, Iowa'
df.loc[df['birthplace'] == 'Grant County, Indiana', 'birthplace'] = 'Fairmount, Indiana'
df.loc[df['birthplace'] == 'Greenville County, Virginia', 'birthplace'] = 'Emporia, Virginia'
df.loc[df['birthplace'] == 'Hico, Louisiana', 'birthplace'] = 'Dubach, Louisiana'
df.loc[df['birthplace'] == 'Hot Springs, Wyoming', 'birthplace'] = 'Thermopolis, Wyoming'
df['Region'] = df['birthplace'].str.split(',').str[1].str.strip()
df['City'] = df['birthplace'].str.split(',').str[0].str.strip()
df[df['Region'].isnull()].drop_duplicates(subset='player_id').to_csv('./no-region.csv')
print(df.head())


state_gdf = gpd.read_file("./maps/cb_2018_us_state_500k/cb_2018_us_state_500k.shp")
print(state_gdf.crs)
usa = gpd.read_file("./maps/cb_2019_us_county_500k/cb_2019_us_county_500k.shp")
# state_df = df.groupby('Region')[['per']].sum()
# state_df['count'] = df.groupby('Region')['player_id'].count()
# state_df = state_df.reset_index()
# merged = state_gdf.merge(state_df, left_on='NAME', right_on='Region')
# print(merged.columns)
# gplt.choropleth(
#   merged,
#   hue='count',
#   projection=gcrs.AlbersEqualArea()
# )
# plt.show()

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
print(len(states))
place_df = None
for state in states:
  state_place = gpd.read_file(glob.glob(f'./maps/state-places/{state[0]}/*.shp')[0])
  state_place['STATE'] = state[0].title()
  state_place['ABBR'] = state[1].upper()
  if (state[0] == 'dc'):
    state_place["STATE"] = 'District of Columbia'
  if (state[0] == 'louisiana'):
    state_place["NAME"].to_csv('./ny-places.csv')
  if (place_df is None):
    place_df = state_place.copy()
  else:
    place_df=place_df.append(state_place)
print(place_df.columns)
if (include_canada):
  province_gdf = gpd.read_file('./maps/canada/canada provinces/lpr_000b16a_e.shp')
  province_gdf['geometry'] = province_gdf['geometry'].to_crs(state_gdf.crs)
  state_gdf = state_gdf.append(province_gdf)
  provinces = [
    'ontario'
  ]
  canada_df = df[df['Region'] == 'Canada']
  canada_df['Region'] = 'Ontario'
  canada_df.loc[canada_df['City'] == 'Montreal', 'Region'] = 'Quebec'
  canada_df.loc[canada_df['City'] == 'Vancouver', 'Region'] = 'British Columbia'
  canada_df.loc[canada_df['City'] == 'Saskatoon', 'Region'] = 'Saskatchewan'
  print(canada_df['Region'])
  df = df.append(canada_df)
  for province in provinces:
    province_place = gpd.read_file(glob.glob(f'./maps/canada/province-places/{province}/*.shp')[0])
    province_place['STATE'] = province.title()
    # if (province == 'pennsylvania'):
    #   province_place["NAME"].to_csv('./pa-places.csv')
    province_place = province_place[province_place['CATEGORY'] == 'Populated Place']
    province_place = province_place.drop_duplicates(subset='GEONAME')
    province_place['NAME'] = province_place['GEONAME']
    place_df=place_df.append(province_place)
city_player_df = df.groupby(['City', 'Region'])[['per', 'mp']].sum()
city_player_df['count'] = df.groupby(['City', 'Region'])['player_id'].count()
city_player_df = city_player_df.reset_index()
city_player_df['City_State'] = city_player_df['City'] + ', ' + city_player_df['Region']
place_df['City_State'] = place_df['NAME'] + ', ' + place_df['STATE']
nonmatching = city_player_df[(city_player_df['Region'].isin(place_df['STATE'].unique())) & ~city_player_df['City_State'].str.strip().isin(place_df['City_State'])]
print(nonmatching.shape)
nonmatching.to_csv('./nonmatching.csv')
merged = place_df.merge(city_player_df, left_on=['NAME', 'STATE'], right_on=['City', 'Region'], how='inner')
print(merged['City'].unique())
merged['geometry']
crs = gcrs.AlbersEqualArea(central_longitude=-96, central_latitude=37.5)
# print(type(crs))
# print(crs.getParameterValues())
proj4 = '+proj=aea +lat_0=37.5 +lon_0=-96 +lat_1=20 +lat_2=50'
alaska_proj4 = '+proj=laea +lat_0=66 +lon_0=-153'
hawaii_proj4 = '+proj=laea +lat_0=20 +lon_0=-156'
pr_proj4 = '+proj=laea +lat_0=18 +lon_0=-66'
merged['geometry'] = merged['geometry'].to_crs(state_gdf.crs).centroid
# path = gplt.datasets.get_path("contiguous_usa")
# contiguous_usa = gpd.read_file(path)
# extent = contiguous_usa.total_bounds
extent = (-121, 25.25, -73, 49.5)
alaska_extent = (-173, 54, -130, 72)
alaska_crs = gcrs.LambertAzimuthalEqualArea(central_longitude=-153, central_latitude=66)
hawaii_extent = (-160, 18.75, -154, 22.5)
hawaii_crs = gcrs.LambertAzimuthalEqualArea(central_longitude=-156, central_latitude=20)
pr_extent = (-67.5, 17.9, -65, 18.6)
pr_crs = gcrs.LambertAzimuthalEqualArea(central_longitude=-66, central_latitude=18)
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1], projection=crs)
# state_gdf.apply(lambda x: ax.annotate(text=x['NAME'], xy=x['geometry'].representative_point().coords[0], ha='center'), axis=1)
ax.axis('off')
ax.margins(0)
alaska_ax = fig.add_axes([0.05, 0.05, 0.2, 0.2], projection=alaska_crs)
alaska_ax.axis('off')
alaska_ax.margins(0)
hawaii_ax = fig.add_axes([0.25, 0.05, 0.125, 0.125], projection=hawaii_crs)
hawaii_ax.axis('off')
hawaii_ax.margins(0)
pr_ax = fig.add_axes([0.9, 0.05, 0.075, 0.075], projection=pr_crs)
pr_ax.axis('off')
pr_ax.margins(0)
gplt.polyplot(
  state_gdf,
  ax=ax,
  linewidth=0.25,
  extent=extent,
  facecolor='whitesmoke',
  edgecolor='gray',
  projection=crs
)
gplt.pointplot(
  merged,
  ax=ax,
  scale='mp',
  limits=(2,25),
  color='gray',
  alpha=0.3,
  extent=extent,
  projection=crs
)
gplt.polyplot(
  state_gdf,
  ax=alaska_ax,
  projection=crs,
  linewidth=0.25,
  extent=alaska_extent,
  facecolor='whitesmoke',
  edgecolor='gray'
)
gplt.pointplot(
  merged,
  ax=alaska_ax,
  scale='mp',
  limits=(2,25),
  color='gray',
  alpha=0.5,
  extent=alaska_extent,
  projection=alaska_crs,
)
gplt.polyplot(
  state_gdf,
  ax=hawaii_ax,
  projection=crs,
  linewidth=0.25,
  extent=hawaii_extent,
  facecolor='whitesmoke',
  edgecolor='gray'
)
gplt.pointplot(
  merged,
  ax=hawaii_ax,
  scale='mp',
  limits=(2,25),
  color='gray',
  alpha=0.5,
  extent=hawaii_extent,
  projection=hawaii_crs,
)
gplt.polyplot(
  state_gdf,
  ax=pr_ax,
  projection=crs,
  linewidth=0.25,
  extent=pr_extent,
  facecolor='whitesmoke',
  edgecolor='gray'
)
gplt.pointplot(
  merged,
  ax=pr_ax,
  scale='mp',
  limits=(2,25),
  color='gray',
  alpha=0.5,
  extent=pr_extent,
  projection=pr_crs,
)
# proj = proj.Proj(state_gdf.crs)
# merged.to_crs('EPSG:4326')
# for index, row in merged.iterrows():
#   print(row['geometry'].coords[0])
#   xy = row['geometry'].coords[0]
#   print(xy)
#   ax.annotate(text='hi', xy=xy)
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
  ax.text(s=label, x=row['geometry'].representative_point().coords[0][0] + offset_x, y=row['geometry'].representative_point().coords[0][1] + offset_y, ha='center', va='center', fontsize=4, color='black')
state_gdf = state_gdf.to_crs(alaska_proj4)
for index, row in state_gdf[state_gdf['NAME'] == 'Alaska'].iterrows():
  alaska_ax.text(s='AK', x=row['geometry'].centroid.coords[0][0], y=row['geometry'].centroid.coords[0][1], ha='center', va='center', fontsize=4, color='black')
state_gdf = state_gdf.to_crs(hawaii_proj4)
for index, row in state_gdf[state_gdf['NAME'] == 'Hawaii'].iterrows():
  hawaii_ax.text(s='HI', x=row['geometry'].centroid.coords[0][0] + offset_x, y=row['geometry'].centroid.coords[0][1] + offset_y, ha='center', va='center', fontsize=4)
state_gdf = state_gdf.to_crs(pr_proj4)
for index, row in state_gdf[state_gdf['NAME'] == 'Puerto Rico'].iterrows():
  pr_ax.text(s='PR', x=row['geometry'].centroid.coords[0][0], y=row['geometry'].centroid.coords[0][1], ha='center', va='center', fontsize=4, color='black')
fig.suptitle('Where NBA Players Come From')
fig.text(
  s='Dot size represents total minutes played per birthplace',
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
plt.savefig('./output/Player Birthplace MP Point Plot All-Time.png', dpi=600)
plt.close()