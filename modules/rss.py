import feedparser
from PIL import Image
from bs4 import BeautifulSoup
import json



ONION_FEED = 'https://www.theonion.com/rss'


def get_onion_headlines():
  feed = feedparser.parse(ONION_FEED)
  return feed['entries']


def show_5_onion_headlines():
  feed_entries = get_onion_headlines()
  for entry in feed_entries[:5]:
    print(entry['title'])
    print(entry['published'])
    print(BeautifulSoup(entry['summary'], features='html.parser').get_text().replace('Read more...', ''))
    print(entry['link'])
    print()