import music

config = {
    'spotify_client_key': 'THE_SPOTIFY_CLIENT_KEY',
    'spotify_client_secret': 'THE_SPOTIFY_CLIENT_SECRET',
    'pandora_client_key': 'THE_PANDORA_CLIENT_KEY',
    'pandora_client_secret': 'THE_PANDORA_CLIENT_SECRET'
}

pandora = music.services.create('PANDORA', **config)
pandora.test_connection()

spotify = music.services.create('SPOTIFY', **config)
spotify.test_connection()

pandora2 = music.services.create('PANDORA', **config)
print(f'id(pandora) == id(pandora2): {id(pandora) == id(pandora2)}')

spotify2 = music.services.create('SPOTIFY', **config)
print(f'id(spotify) == id(spotify2):{id(spotify) == id(spotify2)}')
