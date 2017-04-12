"""
    This is a Web scraper with Real Time MONITORING to get desired content from
    START LINK: http://judis.nic.in/supremecourt/imgst.aspx?filename=00001 to
    END LINK: http://judis.nic.in/supremecourt/imgst.aspx?filename=44756
"""

import requests  # install this module by the command: pip install requests in your command line
from bs4 import BeautifulSoup  # install this module by the command: pip install beautifulsoup4 in your command line
import time

i = 1  # Index local variable

"""
    This WHILE loop will scrape the textual data from the textarea of the URLs. 
    This will act lika a monitor to check the
    updated files in the next URL (if data is inserted)
"""
while True:

    # URL required
    url = 'http://judis.nic.in/supremecourt/imgst.aspx?filename={}'.format(i)
    response = requests.get(url)

    # <textarea>....content....</textarea>(from the present url) is assigned to 'html' variable
    html = response.content

    # parsing is done here to local variable soup
    soup = BeautifulSoup(html, 'lxml')

    # To find desired content from textarea, here id="txtqrydsp" is id the id of textarea
    info = soup.find(id="txtqrydsp")

    """
        If no content is included yet in the required field then NOT AVAILABLE message is printed and after 1 hour,
        it will again check for the content in the required field until it finds any content.
    """
    if info is None:
        print("Requested Page is not available")

        # it will go on sleep for 1 hour and check again the condition( you can change the update time if you want to)
        time.sleep(3600)

    # The moment the content is inserted in the URL The content is parsed from the URL and is written to a TEXT file
    else:

        # A text file for the given URL is created in Data folder with name = Data1 or 2 or 3...(i.e. the value of i)
        filename = 'Data\Data{}.txt'.format(i)

        # finally the parsed text content from URL is written to a text file
        with open(filename, 'a') as writer:
            writer.writelines(str(info.get_text()))

        # Value of index 'i' is incremented to traverse to the Next URL
        i += 1
