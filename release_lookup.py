# made with ChatGPT's help
# 5/6/25 returns 5 matches and lets user select which release to 
#           search for details 

import musicbrainzngs
import json
import pprint


# set up user agaent
musicbrainzngs.set_useragent(
    "Music Lookup",
    "0.1", # version number
    "antkn33@gmail.com", 
)
musicbrainzngs.set_format(fmt='json')

search_artist = "Billy Cobham"
search_album = "Spectrum"
search_limit = "5"

def release_details(release):
    print(release['title'] + ": " + release['artist-credit'][0]['name'])
    release_date = release['release-events'][0].get('date', "Unknown Date") if 'release-events' in release and release['release-events'] else "Unknown Date"
    print(release['media'])
    print('Release Date: ' + release_date)
    print("MusicBrainz ID: " + release['id'])

def user_selection_search(release):
    user_release_id = release["id"]
    print(f"Looking up release ID: {user_release_id}")

    try:
        # This returns the release data directly (not wrapped in a 'release' key)
        release_data = musicbrainzngs.get_release_by_id(user_release_id, includes=["recordings"]+["artist-credits"])

       # pprint.pprint(release_data)  # For debug[""]

        # Directly use release_data (not release_data['release'])
        print(f"\nTitle: {release_data['title']}")
        media = release_data.get('media', [])
        if media:
            for disc in media:
                print(f"\nDisc format: {disc.get('format', 'Unknown')}")
                for track in disc.get('tracks', []):
                    print(f"  Track {track['number']}: {track['title']}")
                    print(["artist-credits"])
        else:
            print("No media info found.")

    except musicbrainzngs.WebServiceError as e:
        print(f"Web service error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

album_result = musicbrainzngs.search_releases(artist=search_artist, release=search_album, limit=search_limit)

match = 0 

for release in album_result['releases']:
    match += 1
    print(f"Match # {match}")
    release_details(release)
    # print(json.dumps(release, indent=4))  # Debugging: Print the release object
    print()

user_choice = input("Select a number to search: ")

try:
    selected_index = int(user_choice) - 1
    selected_release = album_result['releases'][selected_index]
    user_selection_search(selected_release)
except (IndexError, ValueError):
    print("Invalid selection. Please enter a number from the list.")


# user_selection_search(selected_release)

