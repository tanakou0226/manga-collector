import tweepy
import urllib.request
import re
import os
from dotenv import load_dotenv
load_dotenv()

CONSUMER_KEY = os.environ['ConsumerKey']
CONSUMER_SECRET = os.environ['ConsumerSecret']
ACCESS_TOKEN = os.environ['AccessToken']
ACCESS_SECRET = os.environ['AccessTokenSecret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

#キーワードで検索
def log(user_name, count, id): #user_name アカウントのID 取得ツイート数 ツイートのID
    result_url = []
    for i in range(0, 3):
        results = api.user_timeline(screen_name=user_name, count=count, max_id=id)
        id = results[-1].id
        for result in results:
            if 'media' in result.entities:
                judg = 'RT @' in result.text
                if judg == False:  #RTを含まない
                    for media in result.extended_entities['media']:
                        result_url.append(media['media_url'])
    return result_url

def extract_pic_file(image_url):
    m = re.search(r"(([A-Za-z0-9]|_)+\.(png|jpg))", image_url)
    if m:
        name = 'images/' + m.group(0)
    else:
        name = 'images/None.png'

    return name

def save_image(url, name):
    count = 1
    for image_url in url:
        file_name = extract_pic_file(image_url)
        urllib.request.urlretrieve(image_url, file_name)
        count += 1

def fast(user_name):
    results = api.user_timeline(screen_name=user_name, count="1")
    for result in results:
        id = result.id
    return id

def start():
    count = 100
    user_name = input("IDを入力>>")
    id = fast(user_name)
    url = log(user_name, count, id - 1)
    save_image(url, user_name)

if __name__ == "__main__":
    start()