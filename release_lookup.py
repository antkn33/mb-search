import musicbrainzngs
import json
import pprint


# set up user agaent
musicbrainzngs.set_useragent(
    "Music Lookup",
    "0.1" # version number
    "antkn33@gmail.com", 
)
musicbrainzngs.set_format(fmt='json')

search_artist = "Fishbone"
search_album = "Truth and Soul"
search_limit = "10"

def release_details(release):
    print(release['title'] + ": " + release['artist-credit'][0]['name'])
    release_date = release['release-events'][0].get('date', "Unknown Date") if 'release-events' in release and release['release-events'] else "Unknown Date"
    print(release['media'])
    print('Release Date: ' + release_date)
    print("MusicBrainz ID: " + release['id'])

def user_selection_search(user_choice):
    user_release_id = release["id"]
    user_result = musicbrainzngs.get_release_by_id(user_release_id)
    #print(json.dumps(user_result, indent=4))
    pprint.pprint(user_result)
    pprint.pprint(user_result['media']['tracks'])

album_result = musicbrainzngs.search_releases(artist=search_artist, release=search_album, limit=search_limit)

print(search_artist + ' Discography')
print("____________")
#print(album_result
match = 0 

for release in album_result['releases']:
    match += 1
    print(f"Match # {match}")
    release_details(release)
    #print(json.dumps(release, indent=4))  # Debugging: Print the release object
    print()

user_choice = input("Select a number to search: ")
user_selection_search(user_choice)


