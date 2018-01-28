"""
This Script Posts a new Judgement on the Website by using
wordpress_xmlrpc module in Python. It simply reads each file
one by one and post the content of that file in a new post
on the website.
"""
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost

count = 0
count_empty = 0

# authenticate (password and username is hidden)
wp_url = "https://legalwiki.in/xmlrpc.php"
wp_password = "*****"
wp_username = "******"
wp = Client(wp_url, wp_username, wp_password)

# range of text files scraped from html pages(present in the system)
for i in range(1, 37638):
    data_file = open('Judgment/Judgment_{}.txt'.format(i), 'r+')  # opens scraped text file in the system
    data = data_file.read()  # reads the scraped textual data

    # if data is empty in the file then will skip it.
    if bool(data) is False:
        count_empty += 1
        print('Judgment_{} is empty so skipped'.format(i))
        print 'Count of empty file is:', count_empty
        continue

    # will create a new post with the desired name and will copy the extracted data from the text file into the post.
    else:
        post = WordPressPost()
        post.title = 'Judgement: {}'.format(count)
        post.content = data  # writes the scraped data into the post
        post.post_status = 'publish'
        post.terms_names = {
            'post_tag': [],
            'category': ['SC_Judgment'],
        }
        wp.call(NewPost(post))
        print 'Wordpress judgment:', count
        print 'File_Judgment_:', i
        count += 1
print 'Count of empty file is:', count_empty
