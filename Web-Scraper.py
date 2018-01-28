"""
This Script is for the employer for whom I interned for.
It reads the new data on the link and post it on the
employer's Website. It directly reads the content of the
New Link (if any) and post it on the Website directly.
"""
import os
import inspect
import requests
from bs4 import BeautifulSoup
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost

# To check the Path of the script
path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))  # script directory

# To Fetch the last updated values of i and count from input text files.
# i (Unique URL index for every Link we have to scrape content from)
try:
    my_i = open('{}\Value_of_i(URL index).txt'.format(path), 'r+')
    data_i = my_i.read()
    i = int(data_i)
    my_i.close()
except IOError:
    i = 0
# count (Count of Post that is to be posted on our WebSite)
try:
    my_count = open('{}\Value_of_Count(Count of Post).txt'.format(path), 'r+')
    data_count = my_count.read()
    count = int(data_count)
    my_count.close()
except IOError:
    count = 0

while True:
    url = 'http://judis.nic.in/supremecourt/imgst.aspx?filename={}'.format(i)
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'lxml')
    info = soup.find(id="txtqrydsp")

    if info is None:
        with open('{}\Log.txt'.format(path), 'w+') as writer:
            writer.writelines('Judgement :{} is not created yet\n'.format(count))
            writer.writelines("Url: 'http://judis.nic.in/supremecourt/imgst.aspx?filename={}' is empty\n\n".format(i))
            writer.writelines('MESSAGE: Will Check Again Tomorrow\n')
            writer.writelines('(count)Count of File is:{}\n'.format(count))
            writer.writelines('(i)Link index is:{}\n\n'.format(i))
            writer.writelines('REMINDER: The value of (count) and (i) will be updated automatically now in the '
                              'input text files.\n')
        writer.close()
        break
    else:
        value = str(info.get_text().encode('utf-8'))
        # authenticate(Password & Username is hidden)
        wp_url = "https://legalwiki.in/xmlrpc.php"
        wp_password = "******"
        wp_username = "******"
        wp = Client(wp_url, wp_username, wp_password)
        # Making a new post
        post = WordPressPost()
        post.title = 'Judgement: {}'.format(count)
        post.content = value
        post.post_status = 'publish'
        post.terms_names = {
            'post_tag': [],
            'category': ['SC_Judgment'],
        }
        wp.call(NewPost(post))
        with open('{}\Log.txt'.format(path), 'w+') as writer:
            writer.writelines('Post = Judgement: {} has been posted at the following LINK'.format(count))
            writer.writelines('http://legalwiki.in/category/sc_judgment/')
            writer.writelines('URL of content: http://judis.nic.in/supremecourt/imgst.aspx?filename={}\n'.format(i))
        writer.close()
        i += 1
        count += 1

        # To update the values of i and count in input text file.
        filename_1 = '{}\Value_of_i(URL index).txt'.format(path)
        with open(filename_1, 'w+') as writer:
            writer.writelines(str(i))
        writer.close()
        filename_2 = '{}\Value_of_Count(Count of Post).txt'.format(path)
        with open(filename_2, 'w+') as writer:
            writer.writelines(str(count))
        writer.close()
print path
os.system("notepad.exe {}\Log.txt".format(path))
os.system("notepad.exe {}\Value_of_i(URL index).txt".format(path))
os.system("notepad.exe {}\Value_of_Count(Count of Post).txt".format(path))
