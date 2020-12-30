# 3rd Party Imports
import requests

# Internal Imports
from core.crawler import *

def main():
    
    # PHASE 0: Initialization
    #New Session, you might want to reuse this later on
    s = requests.Session()
    
    CRWLER = Crawler(s)
    CRWLER.loadConfig()

    # PHASE 1: Initial Crawl
    CRWLER.AttemptCrawl()
    #print(CRWLER.links)

    # PHASE 2: GRAB
    CRWLER.Grab()

    # PHASE 3: COMPARE
    #CRWLER.Compare()

if __name__ == "__main__":
    main()