# https://www.omi.me/blogs/api-guides/how-to-access-music-metadata-using-musicbrainz-api-in-python

import musicbrainzngs
import pprint

# Set the user agent for your application
musicbrainzngs.set_useragent("YourApplicationName", "0.1", "youremail@example.com")

# Assume you have a release ID
release_id = "b2784fc1-283f-4af7-8dc6-5061764e7076"
release_data = musicbrainzngs.get_release_by_id(release_id, includes=["recordings", "recording-level-rels", "work-level-rels",
    "artist-rels", "work-rels"])

# List tracks from the album+
for medium in release_data['release']['medium-list']:
    # pprint.pp(medium)
    for track in medium['track-list']:
        print(f"Track {track['number']}: {track['recording']['title']}")
        try:
            for artist in track['recording']['artist-relation-list']:
                if artist['type'] == 'instrument':
                    for intrustment in artist['attribute-list']:
                        print(f"\t{artist['artist']['name']}: {intrustment}")                    
                        # print(f" \t\t{intrustment}")
        except:
            print("info not available")

