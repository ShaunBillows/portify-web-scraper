import requests

spotify_user_id = input("Enter Spotify user id  : ")
playlist_uri = input("Enter Spotify playlist uri : ")
spotify_token = input("Enter Spotify auth token : ")

class spotify:
    
    def __init__(self):
        self.spotify_token = spotify_token
        self.spotify_user_id = spotify_user_id
        self.playlist_uri = playlist_uri

    def get_tracks(self):
        """Connects to Spotify's API and retrieves the tracks information of a playlist.

        Args: 
            spotify_token (string): Spotify auth token for an account.
            spotify_user_id (string): Spotify account username.
            playlist_uri (string): The unique URI of the playlists without the 'spotify:playlist:' part.

        Returns:
            tracks (list): Returns a list of track objects, each with the following keys: name, artist, uri.
        """
        
        try: 
            tracks = []
            offset = 0

            while offset <= len(tracks):

                query = f"https://api.spotify.com/v1/playlists/{playlist_uri}/tracks?offset={offset}"

                response = requests.get(query, headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {spotify_token}",
                })

                response_json = response.json()

                for track in response_json["items"]:

                    tracks.append({
                        "name": track["track"]["name"],
                        "artist": track["track"]["artists"][0]["name"],
                        "uri": track["track"]["uri"]
                    })

                offset += 100

            return tracks

        except:
            print("An error occured retrieving the playlist.")
