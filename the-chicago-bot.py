
import tweepy as tp
import time
import os

# credentials to login to twitter api
consumer_key = 	'9MaX8WRnz1tWF5hGIlLs6gB81'
consumer_secret = 'fgAopYZmNEAz4hUntjXjtguoLr7fhzeyEN6DyZH95QLDyfXFpY'
access_token = 	'1013591445868105729-lkWKIeP1MRlwvVkUEbEWShLDTujDsG'
access_secret = 'ZJfbINiq1SogX3LxnYqWGU6HFhrvpusysr09khJXGbLUv'


# login into twitter api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

# iterates over pics in the folder
os.chdir('chicago')
for image in os.listdir('.'):
    api.update_with_media(image)
    time.sleep(10)
