import sys
import os
import tqdm
import requests
import urllib.request


# resolve args
def resolve_args():
    if len(sys.argv) < 2:
        print("No search keys specified")
        sys.exit(0)
    else:
        keys = []
        i = 1
        while i < len(sys.argv):
            keys.append(sys.argv[i])
            i += 1
        return keys


# process query
def build_url(keys):
    query_string = "+".join(keys)
    query_url = "https://www.torrentproject.se/?t=" + query_string
    return query_url


# fetch html from url and extract matching torrent_url
def get_torrent_from_query(query_url):
    url_req = urllib.request.Request(query_url, headers={"User-Agent": "Magic browser"})
    with urllib.request.urlopen(url_req) as f:
        response = f.read()
    raw = str(response, "utf-8")
    index = raw.find("<span><a href='/")
    if index != -1:
        index += 16
        torrent_identifier= ""
        while raw[index] != "/":
            torrent_identifier += raw[index]
            index += 1
        torrent_identifier = torrent_identifier.upper()
        print("torrent : " + torrent_identifier)
        prefix = "https://www.torrentproject.se/torrent/"
        torrent_url = prefix + torrent_identifier + ".torrent"
        print(torrent_url)

# execution flow of script
search_keys = resolve_args()
url = build_url(search_keys)
get_torrent_from_query(url)
