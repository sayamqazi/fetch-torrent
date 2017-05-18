import urllib
import urllib.request


class Feeder(object):

    def from_torrent_project(self, keys):
        query_string = "+".join(keys)
        query_url = "https://www.torrentproject.se/?t=" + query_string
        url_req = urllib.request.Request(query_url, headers={"User-Agent": "Magic browser"})
        with urllib.request.urlopen(url_req) as f:
            response = f.read()
        raw = str(response, "utf-8")
        index = raw.find("<span><a href='/")
        if index != -1:
            index += 16
            torrent_identifier = ""
            while raw[index] != "/":
                torrent_identifier += raw[index]
                index += 1
            torrent_identifier = torrent_identifier.upper()
            print("torrent : " + torrent_identifier)
            prefix = "https://www.torrentproject.se/torrent/"
            torrent_url = prefix + torrent_identifier + ".torrent"
            print(torrent_url)

    def from_1337x(self, keys):
        query_string = "+".join(keys)
        query_url = "https://www.1337x.to/search/" + query_string + "/1/"
        url_req = urllib.request.Request(query_url, headers={"User-Agent": "Magic browser"})
        with urllib.request.urlopen(url_req) as f:
            response = f.read()
        raw = str(response, "utf-8")
        index = raw.find("</a><a")
        torrent_page_url = ""
        if index != -1:
            index += 14
            while raw[index] != '"':
                torrent_page_url += raw[index]
                index += 1
            torrent_page_url = "https://www.1337x.to/" + torrent_page_url
            print("TORRENT PAGE : " + torrent_page_url)
            torrent_page_req = urllib.request.Request(torrent_page_url, headers={"User-Agent": "Magic browser"})
            with urllib.request.urlopen(torrent_page_req) as f:
                response = f.read()
            raw = str(response, "utf-8")
            index = raw.find('d" ta')
            torrent_url = ""
            if index != -1:
                index += 26
                while raw[index] != '"':
                    torrent_url += raw[index]
                    index += 1
                print("TORRENT : " + torrent_url)

    def from_yts(self, keys):
        query_string = "%20".join(keys)
        query_url = "https://www.yts.ag/browse-movies/" + query_string + "/all/all/0/latest"
        url_req = urllib.request.Request(query_url, headers={"User-Agent": "Magic browser"})
        with urllib.request.urlopen(url_req) as f:
            response = f.read()
        raw = str(response, "utf-8")
        index = raw.find("/torrent/")
        torrent_identifier = ""
        if index != -1:
            while raw[index] != '"':
                torrent_identifier += raw[index]
                index += 1
            torrent_url = "https://www.yts.ag" + torrent_identifier
            print("TORRENT 720p : " + torrent_url)
