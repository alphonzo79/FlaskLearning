#!/usr/bin/python2.7
# coding=utf-8

import feedparser
from flask import Flask, render_template, request
import json
import sys
import urllib
import urllib2


reload(sys)
sys.setdefaultencoding("utf8")


BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}


app = Flask(__name__)


@app.route("/")
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEEDS:
        publication = "bbc"
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    weather = getWeather("83687")
    return render_template('home.html',
                           publication_name=publication.upper(),
                           articles=feed['entries'],
                           weather=weather)


def getWeather(query):
    api_url = """http://www.myweather2.com/developer/forecast.ashx?uac=CYiakGRSz-&temp_unit=f&output=json&query={0}"""
    query = urllib.quote(query)
    url = api_url.format(query)
    data = urllib2.urlopen(url).read()
    parsed = json.loads(data)
    weather = None

    if parsed.get('weather') and parsed.get('weather').get('curren_weather'):
        current = parsed.get('weather').get('curren_weather')
        weather = {'description': current[0]['weather_text'],
                   'temperature': current[0]['temp'],
                   'zip': query}

    return weather


if __name__ == "__main__":
    app.run(port=5000, debug=True)
