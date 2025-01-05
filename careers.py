import json

from playwright.sync_api import sync_playwright

entry = {}

url = input('URL: ')
expected_prefix = 'https://www.reddit.com/r/technicalwriting/comments/'
if not url.startswith(expected_prefix):
    raise ValueError(f'URL must begin with {expected_prefix}')
tokens = url.split('/')
entry['post_id'] = tokens[6]
    
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url, wait_until='domcontentloaded')
    # title
    page.wait_for_selector('h1')
    title_node = page.query_selector('h1')
    entry['title'] = title_node.text_content().strip()
    # date
    entry['month'] = input('Month: ')
    entry['year'] = input('Year: ')
    # college
    college = input('College student (y, n): ')
    if college == 'y':
        degrees = input('Degree(s): ')
        entry['degrees'] = None if degrees == '' else degrees.split(',')
    # post-college
    else:
        entry['direction'] = input('Direction (in, out): ')
        if entry['direction'] == 'in':
            career = input('Current career: ')
            entry['career'] = None if career == '' else career
        else:
            career = input('Desired new career: ')
            entry['career'] = None if career == '' else career
    browser.close()

with open('careers.json', 'r') as f:
    data = json.load(f)

data.append(entry)

with open('careers.json', 'w') as f:
    json.dump(data, f, indent=2)
