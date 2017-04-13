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
    if info is None and i > 44757:
        print "Judgement:{} is not available".format(i)  # if there is no content in given URL

        """
            the URL is checked for every 1 hour whether content has been inserted into that particular URL or not
            (You can also change the sleep time to whatever you want to)
        """
        time.sleep(3600)
    elif info is None and i <= 44757:
        filename = 'Judgement\Judgement{}.txt'.format(i)
        with open(filename, 'a') as writer:
            # As there is no data present in the given URL
            writer.writelines("No CaseStudy Available for judgement: {}".format(i))
        # Value of index 'i' is incremented to traverse to the Next URL
        i += 1

    # The moment the content is inserted in the URL The content is parsed from the URL and is written to a TEXT file
    else:
        # A text file for the given URL is created in Data folder with name = Data1 or 2 or 3..(i.e. the value of i)
        filename = 'Judgement\Judgement{}.txt'.format(i)

        # finally the parsed text content from URL is written to a text file
        with open(filename, 'a') as writer:

            # unicode present in the file will be converted into string AS there is in judgement 4423
            writer.writelines(str(info.get_text().encode('utf-8')))

        # Value of index 'i' is incremented to traverse to the Next URL
        i += 1
