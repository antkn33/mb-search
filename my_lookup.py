import requests
import time
import json
import pprint

def lookup_album_musicians(album, artist):
    # Base URL for MusicBrainz API
    base_url = "https://musicbrainz.org/ws/2/"

    # Prepare search parameters for finding the release
    params = {
        "query": f'release:"{album}" AND artist:"{artist}"',
        "fmt": "json",
        "limit": 5
    }

    # search 
    headers = {"User-Agent": "PythonMusicLookupProject/1.0 (your_email@example.com)"}
    response = requests.get(base_url + "release", params=params, headers=headers)

     # Check if request was successful
    if response.status_code == 200:
        results = response.json()

        # If releases found, get the first one
        if results.get("releases") and len(results["releases"]) > 0:
            album_id = results["releases"][0]["id"]
            album_title = results["releases"][0]["title"]

            # print(json.dumps(results, indent=4))
            # print(album_title)
            # print(album_id)

            # Fetch detailed release information including relationships
            details_params = {"inc": "artist-credits", "fmt": "json"}
            details_url = f"{base_url}release/{album_id}"
            details_response = requests.get(details_url, params=details_params, headers=headers)
            pprint.pp(details_response.text)

lookup_album_musicians("spectrum", "billy cobham")