import feedparser
from datetime import datetime, timezone
from dateutil import parser

def fetch_rss(url, since):
    feed = feedparser.parse(url)
    entries = []

    for e in feed.entries:
        if not hasattr(e, "published"):
            continue

        published = parser.parse(e.published)
        if published < since:
            continue

        entries.append({
            "title": e.title,
            "link": e.link,
            "published": published,
            "author": getattr(e, "author", ""),
            "domain": feed.feed.get("link", "")
        })

    return entries
