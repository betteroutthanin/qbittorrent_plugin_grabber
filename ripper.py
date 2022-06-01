from requests_html import HTMLSession
from bs4 import BeautifulSoup
import wget


linuxLocation = "~/.local/share/qBittorrent/nova3/engines/"
gitHubURL = "https://github.com/qbittorrent/search-plugins/wiki/Unofficial-search-plugins"

def Ripper():
    session = HTMLSession()
    dataFeed = session.get(gitHubURL)
    dataFeed.html.render()
        
    soup = BeautifulSoup(dataFeed.content, 'html.parser') 

    # Just find the tables.  The first one will contain the gold    
    tables = soup.body.findAll('table')
    publicTable = tables[0]

    trs = publicTable.findAll('tr')     

    for tr in trs:
        tds = tr.findAll('td')        
        if len(tds) == 0:
            continue

        link = tds[4].find('a')['href']
        wget.download(link)
    
