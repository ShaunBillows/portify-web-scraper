import pymongo
from pymongo import MongoClient
import os 
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

connection_string = os.getenv('connection_string')
playlist_name = input('Playlist name : ')
username = input('Portify username : ')

def insert_playlist(playlist):
    """Connects to a MongoDB database and appends a playlist to the user document.

    Args: 
        username (string): The username corresponding to a document.
        playlist (list): The playlist to be appended to the users playlists.
        name (string): The name of the playlist to be inserted.

    Returns:
        response (string): HTTP response object from PyMongo. 
    """

    try: 
        client = pymongo.MongoClient(connection_string, tls=True, tlsAllowInvalidCertificates=True)
        print("Connection successful.")
        db = client.portify
        collection = db.users
    except: 
        print("Failed to connect to db")
    
    try:
        user = collection.find_one({"username": username})
        user['playlists'].append({'name': playlist_name, 'playlist': playlist})
        if user["playlists"]:
            result = collection.replace_one({"username":username}, user)
            print(result)

    except Exception as e: 
        print("Failed update document.")
        print(e)
