import pandas as pd
import spotipy
import config
# To access authorised Spotify data
from spotipy.oauth2 import SpotifyClientCredentials

client_id = config.client_id
client_secret = config.secret_key

client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret)
# spotify object to access API
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
name = input("Enter Artist Name: ")  # chosen artist
result = sp.search(name)  # search query
artist_uri = next(
    (
        row['uri']
        for row in result['tracks']['items'][0]['artists']
        if name.lower() in row['name'].lower()
    ),
    '',
)

# Pull all of the artist's albums
sp_albums = sp.artist_albums(artist_uri, album_type='album')
# Store artist's albums' names' and uris in separate lists

album_names = []
album_uris = []
for i in range(len(sp_albums['items'])):
    album_names.append(sp_albums['items'][i]['name'])
    album_uris.append(sp_albums['items'][i]['uri'])


def albumSongs(uri):
    album = uri  # assign album uri to a_name
    spotify_albums[album] = {
        'album': [],
        'track_number': [],
        'id': [],
        'name': [],
        'uri': [],
    }

    tracks = sp.album_tracks(album)  # pull data on album tracks
    for n in range(len(tracks['items'])):  # for each song track
        # append album name tracked via album_count
        spotify_albums[album]['album'].append(album_names[album_count])
        spotify_albums[album]['track_number'].append(
            tracks['items'][n]['track_number'])
        spotify_albums[album]['id'].append(tracks['items'][n]['id'])
        spotify_albums[album]['name'].append(tracks['items'][n]['name'])
        spotify_albums[album]['uri'].append(tracks['items'][n]['uri'])


spotify_albums = {}
for i in album_uris:
    albumSongs(i)


def popularity(album):
    spotify_albums[album]['popularity'] = []
    for track in spotify_albums[album]['uri']:
        pop = sp.track(track)
        spotify_albums[album]['popularity'].append(pop['popularity'])


for i in spotify_albums:
    popularity(i)

dic_df = {'name': [], 'popularity': []}
for album in spotify_albums:
    for feature in ['name', 'popularity']:
        dic_df[feature].extend(spotify_albums[album][feature])

df = pd.DataFrame.from_dict(dic_df)

final_df = df.sort_values('popularity', ascending=False)
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(final_df)
