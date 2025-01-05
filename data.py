import json

from playwright.sync_api import sync_playwright

with open('students.json', 'r') as f:
    students = json.load(f)
with open('entrances.json', 'r') as f:
    entrances = json.load(f)
with open('exits.json', 'r') as f:
    exits = json.load(f)
with open('markets.json', 'r') as f:
    markets = json.load(f)
with open('resumes.json', 'r') as f:
    resumes = json.load(f)
with open('portfolios.json', 'r') as f:
    portfolios = json.load(f)

more_posts = True

def exists(post_id, dataset):
    for post in dataset:
        if post_id == post['post_id']:
            print('Post already exists in this dataset')
            return True
    return False
        

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    while more_posts:
        new_post = {}
        # Extract the post ID from the URL
        url = input('URL: ')
        expected_prefix = 'https://www.reddit.com/r/technicalwriting/comments/'
        if not url.startswith(expected_prefix):
            print(f'URL must begin with {expected_prefix}')
            continue
        tokens = url.split('/')
        post_id = tokens[6]
        new_post['post_id'] = post_id
        # Scrape the post title and date from the web
        try:
            page.goto(url)
            input('> Press Enter when the page is ready: ')
            title = page.evaluate('document.querySelector("h1").textContent').strip()
            new_post['title'] = title
            date = page.evaluate('document.querySelector("shreddit-post time").getAttribute("datetime")')
            new_post['date'] = date
        except Exception as e:
            print(e)
            continue
        # Get the post type
        print('Post types:')
        print()
        print('1 - New Grads')
        print('2 - Entrance')
        print('3 - Exit')
        print('4 - Markets')
        print('5 - Resumes')
        print('6 - Portfolios')
        print()
        post_type = input('> Select a post type: ')
        # Manually enter different data depending on the post type
        if post_type == '1':  # new grads
            if exists(post_id, students):
                continue
            degrees = input('> Degree(s): ')
            degrees = None if degrees == '' else degrees.split(',')
            new_post['degrees'] = degrees
            students.append(new_post)
            with open('students.json', 'w') as f:
                json.dump(students, f, indent=2)
        elif post_type == '2':  # entrances
            if exists(post_id, entrances):
                continue
            careers = input('> Past career(s): ')
            careers = None if careers == '' else careers.split(',')
            new_post['careers'] = careers
            entrances.append(new_post)
            with open('entrances.json', 'w') as f:
                json.dump(entrances, f, indent=2)
        elif post_type == '3':  # exits
            careers = input('> Desired new career(s): ')
            if exists(post_id, exits):
                continue
            careers = None if careers == '' else careers.split(',')
            new_post['careers'] = careers
            exits.append(new_post)
            with open('exits.json', 'w') as f:
                json.dump(exits, f, indent=2)
        elif post_type == '4':  # markets
            if exists(post_id, markets):
                continue
            continent = input('Continent: ')
            continent = None if continent == '' else continent
            new_post['continent'] = continent
            country = input('Country: ')
            country = None if country == '' else country
            new_post['country'] = country
            state = input('State: ')
            state = None if state == '' else state
            new_post['state'] = state
            city = input('City: ')
            city = None if city == '' else city
            new_post['city'] = city
            markets.append(new_post)
            with open('markets.json', 'w') as f:
                json.dump(markets, f, indent=2)
        elif post_type == '5':  # resumes
            if exists(post_id, resumes):
                continue
            resumes.append(new_post)
            with open('resumes.json', 'w') as f:
                json.dump(resumes, f, indent=2)
        elif post_type == '6':  # portfolios
            if exists(post_id, portfolios):
                continue
            portfolios.append(new_post)
            with open('portfolios.json', 'w') as f:
                json.dump(portfolios, f, indent=2)
        # Determine if there's more data to be entered
        more_posts = input('> More data (y/n) [y]: ')
        more_posts = 'y' if more_posts == '' else more_posts
        more_posts = True if more_posts == 'y' else False
    browser.close()
