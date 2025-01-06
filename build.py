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
    'students': {
        'title': 'Education',
        'desc': 'Internships, finding a job after graduating, whether Masters/PhDs are valuable, etc.'
    },
    'training': {
        'title': 'Training',
        'desc': 'Certificates, books to read, etc.'
    },
    'resumes': {
        'title': 'Resumes',
        'desc': 'What to include, getting feedback on your resume, etc.'
    },
    'portfolios': {
        'title': 'Portfolios',
        'desc': 'How to build a portfolio, where to host it, getting feedback on your portfolio, etc.'
    },
    'interviews': {
        'title': 'Interviews',
        'desc': 'How to ace the interview, what kinds of questions to ask, etc.'
    },
    'salaries': {
        'title': 'Salaries',
        'desc': 'Determining whether a salary is fair, asking for a raise, etc.'
    }
    'entrances': {
        'title': 'Transitions',
        'desc': 'Breaking into technical writing from a different field.'
    },
    'advancement': {
        'title': 'Advancement',
        'desc': 'You got the job (congrats). Next steps for growing your TW career.'
    },
    'exits': {
        'title': 'Exits',
        'desc': 'Leaving technical writing and pursuing another career.'
    },
    'demand': {
        'title': 'Demand',
        'desc': 'State of the TW job market, what types of TW specialties are in highest demand, which industries pay the most, etc.'
    }
}

for theme in metadata:
    content += f'## {metadata[theme]["title"]}\n\n'
    content += f'{metadata[theme]["desc"]\n\n'
    for post in data[theme]:
        post_id = post['post_id']
        title = post['title']
        date = datetime.datetime(post['date']).strftime('%d %b %Y')
        content += f'* [{title}](https://reddit.com/r/technicalwriting/comments/{post_id}) ({date})\n'
