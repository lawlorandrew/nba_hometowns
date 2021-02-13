from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

seasons = range(1950, 1980)
df = pd.DataFrame()
for season in seasons:
  print(season)
  url = f'https://www.basketball-reference.com/leagues/NBA_{season}_advanced.html'
  req = requests.get(url)
  soup = BeautifulSoup(req.content, "html.parser")

  body = soup.find('tbody')
  if (body is not None):
    rows = body.find_all('tr', class_=lambda x: x == 'full_table')
    for row in rows:
      row_data = pd.Series()
      tds = row.find_all('td')
      for td in tds:
        row_data[td['data-stat']] = td.get_text()
        if (td['data-stat'] == 'player'):
          row_data['player_id'] = td['data-append-csv']
          link = td.find('a')
          href = link['href']
          row_data['href'] = href
      row_data['season'] = season
      df = df.append(row_data, ignore_index=True)
print(df['season'].unique())
# grouped_df = df.groupby(['player', 'player_id', 'href'])['ast_pct', 'blk_pct', 'bpm', 'bpm-dum', 'dbpm', 'drb_pct', 'dws', 'fg3a_per_fga_pct', 'fta_per_fga_pct', 'g', 'mp', 'obpm', 'orb_pct', 'ows', 'per', 'pos', 'stl_pct', 'team_id', 'tov_pct', 'trb_pct', 'ts_pct', 'usg_pct', 'vorp', 'ws', 'ws-dum', 'ws_per_48'].sum()
# grouped_df['seasons'] = df.groupby(['player', 'player_id', 'href'])['season'].apply(list)
# grouped_df = grouped_df.reset_index()
for href in df['href'].unique():
  linkUrl = f'https://www.basketball-reference.com/{href}'
  linkReq = requests.get(linkUrl)
  linkSoup = BeautifulSoup(linkReq.content, 'html.parser')
  span = linkSoup.find('span', { 'itemprop': 'birthPlace'})
  df.loc[df['href'] == href, 'birthplace'] = span.get_text().strip()[3:]
df.to_csv('./data/hometowns-past.csv', index=False)


