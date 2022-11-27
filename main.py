from src.scraper import get_beatport_url, scrape_beatport
from src.spotify import spotify
from time import sleep
from src.utils import print_table
from src.db import insert_playlist

def app(): 
    tracks = spotify().get_tracks()

    for i, track in enumerate(tracks):

        try:
            url = get_beatport_url(f'beatport {track["name"]} {track["artist"]}', track["name"])
            genre = scrape_beatport(url)
            track['genre'] = genre
            track['url'] = url
            print(f'{i}: {track["name"]}, {track["artist"]}, {track["genre"]}, {track["url"]}')
            sleep(3) 
        except:
            print(f'\n Error{i}: {track["name"]}, {track["artist"]}\n')
            track['genre'] = "None found"
            track['url'] = "None found"

    print_table(tracks)
    insert_playlist(tracks)

if __name__ == "__main__":
    app()
