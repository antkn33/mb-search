import musicbrainzngs
import json


# set up user agaent
musicbrainzngs.set_useragent(
    "Music Lookup",
    "0.1" # version number
    "antkn33@gmail.com", 
)
musicbrainzngs.set_format(fmt='json')

search_artist = "Billy Cobham"
search_album = "Spectrum"
search_limit = "5"

def release_details(release):
    print(release['title'] + ": " + release['artist-credit'][0]['name'])
    release_date = release['release-events'][0].get('date', "Unknown Date") if 'release-events' in release and release['release-events'] else "Unknown Date"
    print('Release Date: ' + release_date)
    print("MusicBrainz ID: " + release['id'])



album_result = musicbrainzngs.search_releases(artist=search_artist, release=search_album, limit=search_limit)

print(search_artist + ' Discography')
print("____________")
#print(album_result
choice = 0 

for release in album_result['releases']:
    choice += 1
    print(f"Match # {choice}")
    #print(json.dumps(release, indent=4))  # Debugging: Print the release object
    release_details(release)
    print()

#choice = input("Select a number to search")


