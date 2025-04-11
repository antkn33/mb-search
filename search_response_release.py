import requests

import json
import pprint

# base MB API URL
base_url = "https://musicbrainz.org/ws/2/"
# set up user agaent
useragent = "Music Lookup","0.1","antkn33@gmail.com"
params = {"fmt": "json", "limit": 5}


search_artist = "Fishbone"
search_album = "Truth and Soul"


def release_details(release):
    print(release['title'] + ": " + release['artist-credit'][0]['name'])
    release_date = release['release-events'][0].get('date', "Unknown Date") if 'release-events' in release and release['release-events'] else "Unknown Date"
    print(release['media'])
    print('Release Date: ' + release_date)
    print("MusicBrainz ID: " + release['id'])

# def user_selection_search(user_choice):
#     user_release_id = release["id"]
#     user_result = musicbrainzngs.get_release_by_id(user_release_id)
#     #print(json.dumps(user_result, indent=4))
#     pprint.pprint(user_result)
#     pprint.pprint(user_result['media']['tracks'])

album_search_result = base_url + "release/?query=" + search_album + " AND artist:" + search_artist

print(search_artist + ' Discography')
print("____________")
#print(album_result
match = 0 
print(album_search_result[0])
# for release in album_search_result:
#     match += 1
#     print(f"Match # {match}")
#     release_details(release)
#     #print(json.dumps(release, indent=4))  # Debugging: Print the release object
#     print()

#user_choice = input("Select a number to search: ")
#user_selection_search(user_choice)


