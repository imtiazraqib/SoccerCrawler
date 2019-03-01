# --------------------------------------------------------------------------------------------------------
# Soccer News Crawler
# Website Used: ESPN (http://www.espn.com/soccer/?src=com)
# January 4, 2019
# ------------------------------------------
# Authors: Imtiaz Raqib
# ------------------------------------------
# Language: Python with Beautifulsoup4 module
# --------------------------------------------------------------------------------------------------------

# IMPORTS ----------------------------------------------------
import requests
from bs4 import BeautifulSoup
# ------------------------------------------------------------

# Requesting connection to website and collecting content ----
page_link = 'http://www.espn.com/soccer/?src=com'
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")
# ------------------------------------------------------------

counter = 0

for sectag in page_content.find_all('section', {'class': 'headlineStack__listContainer'}):
    for ultag in sectag.find_all('ul', {'class': 'headlineStack__list'}):
        if (counter < 10):
            for litag in ultag.find_all('li'):
                counter = counter + 1
                print(str(counter) + ". " + litag.text + " - " + litag.find('a')['href'])
        
