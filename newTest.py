# https://www.omi.me/blogs/api-guides/how-to-access-music-metadata-using-musicbrainz-api-in-python

import musicbrainzngs
import pprint

# Set the user agent for your application
musicbrainzngs.set_useragent("YourApplicationName", "0.1", "youremail@example.com")
 

# result = musicbrainzngs.search_artists(artist="Radiohead")

# # Display information about the first artist in the search result
# artist = result['artist-list'][0]
# print(f"Artist: {artist['name']}, ID: {artist['id']}")

# artist_id = artist['id']
# artist_data = musicbrainzngs.get_artist_by_id(artist_id, includes=["releases"])
# print(artist_data)

# Print album titles
# for release in artist_data['artist']['release-list']:
#    # pprint.pp(release)

#     print(f"Album: {release['title']}, ID: {release['id']}")


import musicbrainzngs
import pprint
# Set the user agent for your application
musicbrainzngs.set_useragent("YourApplicationName", "0.1", "youremail@example.com")

# Assume you have a release ID
release_id = "b7f998ec-32ca-43c7-a93e-d6d1456df45c"
release_data = musicbrainzngs.get_release_by_id(release_id, includes="recordings")
# pprint.pp(release_data)
# List tracks from the album+
for medium in release_data['release']['medium-list']:
    # pprint.pp(medium)
    for track in medium['track-list']:
        print(f"Track: {track['recording']['title']}")
