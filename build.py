import datetime
import json

data = {}

with open('intro.md', 'r') as f:
    data['content'] = f.read()
with open('advancement.json', 'r') as f:
    data['advancement'] = json.load(f)
with open('demand.json', 'r') as f:
    data['demand'] = json.load(f)
with open('entrances.json', 'r') as f:
    data['entrances'] = json.load(f)
with open('exits.json', 'r') as f:
    data['exits'] = json.load(f)
with open('interviews.json', 'r') as f:
    data['interviews'] = json.load(f)
with open('portfolios.json', 'r') as f:
    data['portfolios'] = json.load(f)
with open('resumes.json', 'r') as f:
    data['resumes'] = json.load(f)
with open('salaries.json', 'r') as f:
    data['salaries'] = json.load(f)
with open('students.json', 'r') as f:
    data['students'] = json.load(f)
with open('training.json', 'r') as f:
    data['training'] = json.load(f)

metadata = {
    'students': 'Education (internships, finding a job after graduating, whether Masters/PhDs are valuable, etc.)',
    'training': 'Training (certificates, books to read, etc.)',
    'resumes': 'Resumes',
    'portfolios': 'Portfolios',
    'interviews': 'Interviews',
    'salaries': 'Salaries',
    'entrances': 'Breaking into technical writing from a different field',
    'advancement': 'Advancement',
    'exits': 'Leaving technical writing and pursuing another career',
    'demand': 'Demand (state of the job market, what types of TW are in highest demand, etc.)'
}

for theme in data:
    content += f'## {theme.capitalize()}\n\n'
    for post in data[theme]:
        post_id = post['post_id']
        title = post['title']
        date = datetime.datetime(post['date']).strftime('%d %b %Y')
        content += f'* [{title}](https://reddit.com/r/technicalwriting/comments/{post_id}) ({date})\n'
