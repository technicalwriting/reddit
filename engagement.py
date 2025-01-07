import json

from playwright.sync_api import sync_playwright

datasets = {}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    for dataset in ['students', 'entrances', 'exits', 'salaries', 'resumes', 'portfolios', 'interviews', 'advancement', 'training', 'demand']:
        file = f'{dataset}.json'
        with open(file, 'r') as f:
            datasets[dataset] = json.load(f)
        for index, post in enumerate(datasets[dataset]):
            if 'votes' in post and 'comments' in post:
                continue
            post_id = post['post_id']
            url = f'https://www.reddit.com/r/technicalwriting/comments/{post_id}'
            try:
                page.goto(url)
                input('Press Enter when the page is ready: ')
                votes = page.evaluate('document.querySelector("shreddit-post").getAttribute("score")').strip()
                comments = page.evaluate('document.querySelector("shreddit-post").getAttribute("comment-count")').strip()
                print(f'Votes: {votes}, Comments: {comments}')
                datasets[dataset][index]['votes'] = votes
                datasets[dataset][index]['comments'] = comments
            except Exception as e:
                print(f'Exception: {e}')
                continue
            with open(file, 'w') as f:
                json.dump(datasets[dataset], f, indent=2)
