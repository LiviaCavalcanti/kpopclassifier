import spotipy
import sys
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

my_id = '655e62800e724511b9a6f74b1bfa635f'
secret_key = '9e1f1feb45874771b24d1d10d19e87bd'

artist_names = ["BTS", "AOA", "SHINee", "Girls' Generation", "Red Velvet", "Wanna One", "iKON", "GFRIEND", "BIGBANG"]

client_credentials_manager = SpotifyClientCredentials(client_id = my_id, client_secret = secret_key)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artists_list = []

for a in artist_names:
    results = spotify.search(q='artist:' + a, type='artist')
    items = results['artists']['items']
    artist = items[0]
    artists_list.append([artist["name"], artist["followers"]["total"]])

data = pd.DataFrame(artists_list, columns = ["name", "followers"])

print(data)

data.to_csv('../data/name_and_followers_kpop.csv')