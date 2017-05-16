# fetch-torrent
A python script to find torrents on popular sites with given search keywords at a set time interval and add them to your favorite client automaticaly.

**Project is in development right now. So everything below is what it will be when it gets completed**
Right now if you run the script it will find torrent on https://torrentproject.se and just output the torrent url.
### Supported Torrent Sites

1. https://extratorrent.cc
2. https://rar.bg
3. https://yts.ag
4. https://extratorrent.cc

### Requirements

In order to run this script you must have `python 3.x` installed on your system.

### Usage tutorial

1. Download the `fetch-torrent.py` file `fetch-torrent/source` direcotry.
2. Open up your Shell on linux or CMD on windows.
3. Navigate to where the file is located.
4. run following command

    `python fetch-torrent.py d:/torrent_downloads Moana 720p`
5. Script will try to find torrents that have 'Moana' and '720p' in their names.
6. If it finds some matching torrent it will automaticaly download the torrent to `d:/torrent_downloads` then add that torrent to utorrent.
7. if the downlaod path does not exists it will exit with appropriate error.
