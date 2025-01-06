import json

from playwright.sync_api import sync_playwright

def exists(post_id, dataset):
    for post in dataset:
        if post_id == post['post_id']:
            print('Post already exists in this dataset')
            return True
    return False

with open('students.json', 'r') as f:
    students = json.load(f)
with open('entrances.json', 'r') as f:
    entrances = json.load(f)
with open('exits.json', 'r') as f:
    exits = json.load(f)
with open('salaries.json', 'r') as f:
    salaries = json.load(f)
with open('resumes.json', 'r') as f:
    resumes = json.load(f)
with open('portfolios.json', 'r') as f:
    portfolios = json.load(f)
with open('interviews.json', 'r') as f:
    interviews = json.load(f)
with open('advancement.json', 'r') as f:
    advancement = json.load(f)
with open('training.json', 'r') as f:
    training = json.load(f)
with open('demand.json', 'r') as f:
    demand = json.load(f)

more_posts = True

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
        print('a - Students')
        print('b - Entrance')
        print('c - Exit')
        print('d - Salaries')
        print('e - Resumes')
        print('f - Portfolios')
        print('g - Interviews')
        print('h - Advancement')
        print('i - Training')
        print('j - Demand')
        print()
        post_type = input('> Select a post type: ')
        # Manually enter different data depending on the post type
        if post_type == 'a':  # new grads
            if exists(post_id, students):
                continue
            degrees = input('> Degree(s): ')
            degrees = None if degrees == '' else degrees.split(',')
            new_post['degrees'] = degrees
            students.append(new_post)
            with open('students.json', 'w') as f:
                json.dump(students, f, indent=2)
        elif post_type == 'b':  # entrances
            if exists(post_id, entrances):
                continue
            careers = input('> Past career(s): ')
            careers = None if careers == '' else careers.split(',')
            new_post['careers'] = careers
            entrances.append(new_post)
            with open('entrances.json', 'w') as f:
                json.dump(entrances, f, indent=2)
        elif post_type == 'c':  # exits
            careers = input('> Desired new career(s): ')
            if exists(post_id, exits):
                continue
            careers = None if careers == '' else careers.split(',')
            new_post['careers'] = careers
            exits.append(new_post)
            with open('exits.json', 'w') as f:
                json.dump(exits, f, indent=2)
        elif post_type == 'd':  # salaries
            if exists(post_id, salaries):
                continue
            salaries.append(new_post)
            with open('salaries.json', 'w') as f:
                json.dump(salaries, f, indent=2)
        elif post_type == 'e':  # resumes
            if exists(post_id, resumes):
                continue
            resumes.append(new_post)
            with open('resumes.json', 'w') as f:
                json.dump(resumes, f, indent=2)
        elif post_type == 'f':  # portfolios
            if exists(post_id, portfolios):
                continue
            portfolios.append(new_post)
            with open('portfolios.json', 'w') as f:
                json.dump(portfolios, f, indent=2)
        elif post_type == 'g':  # interviews
            if exists(post_id, interviews):
                continue
            interviews.append(new_post)
            with open('interviews.json', 'w') as f:
                json.dump(interviews, f, indent=2)
        elif post_type == 'h':  # advancement
            if exists(post_id, advancement):
                continue
            advancement.append(new_post)
            with open('advancement.json', 'w') as f:
                json.dump(advancement, f, indent=2)
        elif post_type == 'i':  # training
            if exists(post_id, training):
                continue
            training.append(new_post)
            with open('training.json', 'w') as f:
                json.dump(training, f, indent=2)
        elif post_type == 'j':  # demand
            if exists(post_id, demand):
                continue
            demand.append(new_post)
            with open('demand.json', 'w') as f:
                json.dump(demand, f, indent=2)
        # Determine if there's more data to be entered
        more_posts = input('> More data (y/n) [y]: ')
        more_posts = 'y' if more_posts == '' else more_posts
        more_posts = True if more_posts == 'y' else False
    browser.close()
