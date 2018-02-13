# -*- coding: utf-8 -*-
import feedparser
from flask import Flask

app = Flask(__name__)

RSS_FEEDS = {"vesti": "http://www.vesti.ru/vesti.rss",
             "bbc": "http://feeds.bbci.co.uk/news/rss.xml",
             "cnn": "http://rss.cnn.com/rss/edition.rss",
             "fox": "http://feeds.foxnews.com/foxnews/latest",
             "iol": "http://www.iol.co.za/cmlink/1.640"}


@app.route("/")
@app.route("/<publication>")
def get_news(publication="vesti"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed["entries"][0]
    return """<html>
        <body>
            <h1> Новости </h1>
            <b>{0}</b> <br/>
            <i>{1}</i> <br/>
            <p>{2}</p> <br/>
        </body>""".format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))


if __name__ == "__main__":
    app.run(port=5000, debug=True)
