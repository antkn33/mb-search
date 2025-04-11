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

search_artist = "Billy Cobham"
search_album = "Spectrum"
search_limit = "5"

def recording_details(recording):
    print(recording['title'] + ": " + recording['artist-credit'][0]['name'])
    recording_date = recording['recording-events'][0].get('date', "Unknown Date") if 'recording-events' in recording and recording['recording-events'] else "Unknown Date"
    print('recording Date: ' + recording_date)
    print("MusicBrainz ID: " + recording['id'])

def user_selection_search(user_choice):
    user_recording_id = recording["id"]
    user_result = musicbrainzngs.get_recording_by_id(user_recording_id)
    print(json.dumps(user_result, indent=4))
    #pprint.pprint(user_result)

album_result = musicbrainzngs.search_recordings(artist=search_artist, recording=search_album, limit=search_limit)

print(search_artist + ' Discography')
print("____________")
#print(album_result
match = 0 

for recording in album_result['recordings']:
    match += 1
    print(f"Match # {match}")
    recording_details(recording)
    #print(json.dumps(recording, indent=4))  # Debugging: Print the recording object
    print()

user_choice = input("Select a number to search: ")
user_selection_search(user_choice)


