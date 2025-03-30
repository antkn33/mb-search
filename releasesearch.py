#!/usr/bin/env python
"""A simple script that searches for a release in the MusicBrainz
database and prints out a few details about the first 5 matching release.

    $ ./releasesearch.py "the beatles" revolver
    Revolver, by The Beatles
    Released 1966-08-08 (Official)
    MusicBrainz ID: b4b04cbf-118a-3944-9545-38a0a88ff1a2
"""
from __future__ import print_function
from __future__ import unicode_literals
import musicbrainzngs
import sys

musicbrainzngs.set_useragent(
    "python-musicbrainzngs-example",
    "0.1",
    "https://github.com/alastair/python-musicbrainzngs/",
)

def show_release_details(rel):
    """Print some details about a release dictionary to stdout.
    """
    # "artist-credit-phrase" is a flat string of the credited artists
    # joined with " + " or whatever is given by the server.
    # You can also work with the "artist-credit" list manually.
    # print(rel)
    print("{}, by {}".format(rel['title'], rel["artist-credit-phrase"], rel))
    if 'date' in rel:
        print("Released {} ({})".format(rel['date'], rel['status']))
     #print(rel['tracks'])
    print("MusicBrainz ID: {}".format(rel['id']))

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) != 2:
        sys.exit("usage: {} ARTIST ALBUM".format(sys.argv[0]))
    artist, album = args

    # Keyword arguments to the "search_*" functions limit keywords to
    # specific fields. The "limit" keyword argument is special (like as
    # "offset", not shown here) and specifies the number of results to
    # return.
    result = musicbrainzngs.search_releases(artist=artist, release=album,
                                            limit=5)
    # On success, result is a dictionary with a single key:
    # "release-list", which is a list of dictionaries.
    #print(result['release-list'])
    if not result['release-list']:
        sys.exit("no release found")
    for (idx, release) in enumerate(result['release-list']):
        print("match #{}:".format(idx+1))
        show_release_details(release)
        print()







'''
# Example output
match #1:
Spectrum, by Billy Cobham
Released 2002 (Official)
MusicBrainz ID: 935b193a-b1fa-4ccd-92f0-afe68f3ba64c

==========

# All output
match #5:
{'id': 'b2784fc1-283f-4af7-8dc6-5061764e7076', 'ext:score': '100', 'title': 'Spectrum',
 'status': 'Official', 'text-representation': {'language': 'eng', 'script': 'Latn'}, 
 'artist-credit': [{'name': 'Billy Cobham', 'artist': {'id': '255497f8-26fb-4044-b97e-d4787d5974f6', 
 'name': 'Billy Cobham', 'sort-name': 'Cobham, Billy'}}], 'release-group': {'id': '30074be9-33ed-3b40-998d-ae60ef0ff0b9', 
 'type': 'Album', 'title': 'Spectrum', 'primary-type': 'Album'}, 'date': '1973-10-01', 'country': 'US', 
 'release-event-list': [{'date': '1973-10-01', 'area': {'id': '489ce91b-6658-3307-9877-795b68554c98', 
 'name': 'United States', 'sort-name': 'United States', 'iso-3166-1-code-list': ['US']}}], 
 'label-info-list': [{'catalog-number': 'SD 7268', 'label': {'id': '50c384a2-0b44-401b-b893-8181173339c7', 'name': 'Atlantic'}}], 
 'medium-list': [{'format': 'Vinyl', 'disc-list': [], 'disc-count': 0, 'track-list': [], 'track-count': 6}], 'medium-track-count': 6,
   'medium-count': 1, 'tag-list': [], 'artist-credit-phrase': 'Billy Cobham'}
MusicBrainz ID: b2784fc1-283f-4af7-8dc6-5061764e7076

'''

