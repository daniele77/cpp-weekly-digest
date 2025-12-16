from datetime import datetime, timezone
from config import TIME_WINDOW, RSS_SOURCES
from fetchers.rss import fetch_rss
from fetchers.wg21 import fetch_wg21
from filters.authority import is_authoritative
from report.markdown import generate_report
import pathlib

def main():
    since = datetime.now(timezone.utc) - TIME_WINDOW
    items = []

    for name, url in RSS_SOURCES.items():
        entries = fetch_rss(url, since)
        for e in entries:
            if is_authoritative(e):
                e["source"] = name
                items.append(e)

    for e in fetch_wg21():
        e["source"] = "WG21 Papers"
        items.append(e)

    report = generate_report(items)

    output = pathlib.Path("weekly_report.md")
    output.write_text(report, encoding="utf-8")

if __name__ == "__main__":
    main()
