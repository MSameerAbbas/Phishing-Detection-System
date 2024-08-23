import os
import sys

import requests


# Use 'demo' mode just to try api4ai for free. Free demo is rate limited.
# For more details visit:
#   https://api4.ai
#
# Use 'rapidapi' if you want to try api4ai via RapidAPI marketplace.
# For more details visit:
#   https://rapidapi.com/api4ai-api4ai-default/api/brand-recognition/details
MODE = 'demo'


# Your RapidAPI key. Fill this variable with the proper value if you want
# to try api4ai via RapidAPI marketplace.
RAPIDAPI_KEY = ''


OPTIONS = {
    'demo': {
        'url': 'https://demo.api4ai.cloud/brand-det/v2/results?detailed=True',
        'headers': {'A4A-CLIENT-APP-ID': 'sample'}
    },
    'rapidapi': {
        'url': 'https://brand-recognition.p.rapidapi.com/v2/results?detailed=True',
        'headers': {'X-RapidAPI-Key': RAPIDAPI_KEY}
    }
}


def detect_logo(image):
    if '://' in image:
        # POST image via URL.
        response = requests.post(
            OPTIONS[MODE]['url'],
            headers=OPTIONS[MODE]['headers'],
            data={'url': image})
    else:
        # POST image as file.
        with open(image, 'rb') as image_file:
            response = requests.post(
                OPTIONS[MODE]['url'],
                headers=OPTIONS[MODE]['headers'],
                files={'image': (os.path.basename(image), image_file)}
            )

    # Parse response and print recognized brands.
    brands = response.json()['results'][0]['entities'][0]['array']

    return [b['name'] for b in brands]
