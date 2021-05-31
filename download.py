from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

key = 'bf1d2b88b7f0d4c92b8b8a4acd2f0546'
secret = 'b5f8cd0ad507a982'
wait_time = 1

animal_name = sys.argv[1]
savedir = './' + animal_name

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text=animal_name,
    per_page=400,
    madia='photos',
    sort='relevance',
    safe_search=1,
    extras='url_q, licence'
)

photos = result['photos']

for i,photo in enumerate(photos['photo']):
    url_q=photo['url_q']
    filepath=savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath):
        continue
    urlretrieve(url_q,filepath)
    time.sleep(1)
