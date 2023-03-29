import sys
import subprocess

valid_websites = [
    'reddit.com',
    'stackoverflow.com',
    'stackexchange.com',
    'geeksforgeeks.org',
    'medium.com',
    'w3schools.com'
]

base_url = "https://www.google.com"

def create_filter():
    filter = '('
    for index, website in enumerate(valid_websites):
        filter += 'site: ' + website
        if index == len(valid_websites) - 1:
            filter += ')'
        else:
            filter += 'OR'
    return filter

def create_query():
    query = sys.argv[1:]
    return ' '.join(query)

def create_url():
    chrome_path = '/usr/bin/google-chrome-stable'
    
    if len(sys.argv[1:]) < 1:
        args = [chrome_path, "--disable-gpu", "--disable-software-rasterizer", "--remote-debugging-port=9222", base_url]
        subprocess.Popen(args, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    else:
        final_url = base_url + '/search?q=' + create_query() + create_filter()
        args = [chrome_path, "--disable-gpu", "--disable-software-rasterizer", "--remote-debugging-port=9222", final_url]
        subprocess.Popen(args, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

if __name__ == '__main__':
    create_url()
