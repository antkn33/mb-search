import requests
import time

def lookup_album_musicians(album_name, artist_name=None):
    """
    Look up musicians for a specific album using MusicBrainz API.
    
    :param album_name: Name of the album to search
    :param artist_name: Optional artist name to narrow the search
    :return: Dictionary of album and musician information
    """
    # Base URL for MusicBrainz API
    base_url = "https://musicbrainz.org/ws/2/"
    
    # Prepare search parameters for finding the release
    params = {
        "query": f'release:"{album_name}" AND artist:',
        "fmt": "json",
        "limit": 5
    }
    
    # Add artist to search if provided
    if artist_name:
        params["query"] += f' AND artist:"{artist_name}"'
    
    # Search for the album
    headers = {"User-Agent": "PythonMusicLookupProject/1.0 (your_email@example.com)"}
    response = requests.get(base_url + "release", params=params, headers=headers)
    
    # Check if request was successful
    if response.status_code == 200:
        results = response.json()
        
        # If releases found, get the first one
        if results.get("releases") and len(results["releases"]) > 0:
            album_id = results["releases"][0]["id"]
            album_title = results["releases"][0]["title"]
            
            # Wait to respect rate limiting
            time.sleep(1)
            
            # Fetch detailed release information including relationships
            details_params = {"inc": "artist-credits+recordings+recording-level-rels", "fmt": "json"}
            details_url = f"{base_url}release/{album_id}"
            details_response = requests.get(details_url, params=details_params, headers=headers)
            
            if details_response.status_code == 200:
                album_details = details_response.json()
                
                # Get main artist credits
                main_artists = []
                for artist_credit in album_details.get("artist-credit", []):
                    if "artist" in artist_credit:
                        main_artists.append(artist_credit["artist"]["name"])
                
                # Get track musicians if available
                musicians = set()
                for medium in album_details.get("media", []):
                    for track in medium.get("tracks", []):
                        if "recording" in track:
                            # Add musicians from track level
                            for rel in track["recording"].get("relations", []):
                                if rel.get("type") == "performer" and "artist" in rel:
                                    musicians.add(rel["artist"]["name"])
                
                return {
                    "album_name": album_title,
                    "main_artists": main_artists,
                    "musicians": list(musicians) if musicians else main_artists
                }
            else:
                print(f"Failed to get details: {details_response.status_code}")
        else:
            print("No releases found matching the criteria")
    else:
        print(f"Search failed: {response.status_code}")
    
    return None

# Example usage
def main():
    album = "Kind of Blue"
    artist = "Miles Davis"
    print(f"Looking up '{album}' by {artist}...")
    result = lookup_album_musicians(album, artist)
    
    if result:
        print(f"\nAlbum: {result['album_name']}")
        print("\nMain Artists:")
        for artist in result['main_artists']:
            print(f"- {artist}")
        
        if result['musicians'] != result['main_artists']:
            print("\nMusicians:")
            for musician in result['musicians']:
                print(f"- {musician}")
    else:
        print("Album not found or error occurred.")

if __name__ == "__main__":
    main()
