import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_wg21():
    resp = requests.get("https://www.open-std.org/jtc1/sc22/wg21/docs/papers/")
    soup = BeautifulSoup(resp.text, "html.parser")

    results = []
    for link in soup.select("a"):
        href = link.get("href", "")
        if href.startswith("p") and href.endswith(".pdf"):
            results.append({
                "title": link.text.strip(),
                "link": "https://www.open-std.org/jtc1/sc22/wg21/docs/papers/" + href,
                "published": datetime.utcnow(),
                "author": "WG21",
                "domain": "open-std.org"
            })

    return results
