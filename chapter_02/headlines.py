#!/usr/bin/python2.7
# coding=utf-8

import feedparser
import sys
from flask import Flask, render_template


reload(sys)
sys.setdefaultencoding("utf8")


BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}


app = Flask(__name__)


@app.route("/")
@app.route("/<publication>")
def get_news(publication='bbc'):
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template('home.html', publication_name=publication.upper(), articles=feed['entries'])


if __name__ == "__main__":
    app.run(port=5000, debug=True)