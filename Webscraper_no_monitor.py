"""
    This is a basic Web scraper to get desired content from(WITHOUT MONITORING)
    START LINK: http://judis.nic.in/supremecourt/imgst.aspx?filename=00001 to
    END LINK: http://judis.nic.in/supremecourt/imgst.aspx?filename=44756
"""

import requests  # install this module by the command: pip install requests in your command line
from bs4 import BeautifulSoup  # install this module by the command: pip install beautifulsoup4 in your command line

# This FOR loop will scrape the textual data from the textarea of the given URLs ending from 1 to 44756...
for i in range(1, 44757):
    # URL required
    url = 'http://judis.nic.in/supremecourt/imgst.aspx?filename={}'.format(i)
    response = requests.get(url)

    # <textarea>....content....</textarea>(from the present url) is assigned to 'html' variable
    html = response.content

    # parsing is done here to local variable soup
    soup = BeautifulSoup(html, 'lxml')

    # To find desired content from textarea, here id="txtqrydsp" is id the id of textarea
    info = soup.find(id="txtqrydsp")

    # A text file for the given URL is created in Data folder with name = Data1 or 2 or 3...(i.e. the value of i)

    filename = 'Data\Data{}.txt'.format(i)

    # finally the parsed content from URL is written to text file
    with open(filename, 'a') as writer:
        writer.writelines(info)
