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
    title_node = page.query_selector('h1')
    entry['title'] = title_node.text_content().strip()
    # date
    entry['month'] = input('Month: ')
    entry['year'] = input('Year: ')
    # location
    continent = input('Continent: ')
    entry['continent'] = None if continent == '' else continent
    country = input('Country: ')
    entry['country'] = None if country == '' else country
    country = input('State: ')
    entry['state'] = None if state == '' else state
    city = input('City: ')
    entry['city'] = None if city == '' else city
    browser.close()

# save the data
with open('market.json', 'r') as f:
    data = json.load(f)

data.append(entry)

with open('market.json', 'w') as f:
    json.dump(data, f, indent=2)
