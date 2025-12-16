AUTHORITATIVE_DOMAINS = {
    "isocpp.org",
    "herbsutter.com",
    "open-std.org",
    "lwn.net",
    "sandordargo.com"
}

AUTHORITATIVE_AUTHORS = {
    "Herb Sutter",
    "Bjarne Stroustrup",
    "Nicolai Josuttis",
    "Jason Turner",
    "Andrei Alexandrescu",
    "Ville Voutilainen"
}

def is_authoritative(entry):
    domain = entry.get("domain", "")
    author = entry.get("author", "")

    return (
        domain in AUTHORITATIVE_DOMAINS or
        author in AUTHORITATIVE_AUTHORS
    )
