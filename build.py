import datetime
import json

data = {}

with open('intro.md', 'r') as f:
    content = f.read()

with open('advancement.json', 'r') as f:
    data['advancement'] = json.load(f)

with open('demand.json', 'r') as f:
    data['demand'] = json.load(f)

data['entrances'] = {'misc': []}
with open('entrances.json', 'r') as f:
    data['entrances']['src'] = json.load(f)
for post in data['entrances']['src']:
    careers = post['careers']
    if careers is None:
        data['entrances']['misc'].append(post)
    else:
        for career in careers:
            if career not in data['entrances']:
                data['entrances'][career] = []
            data['entrances'][career].append(post)
del data['entrances']['src']

data['exits'] = {'misc': []}
with open('exits.json', 'r') as f:
    data['exits']['src'] = json.load(f)
for post in data['exits']['src']:
    careers = post['careers']
    if careers is None:
        data['exits']['misc'].append(post)
    else:
        for career in careers:
            if career not in data['exits']:
                data['exits'][career] = []
            data['exits'][career].append(post)
del data['exits']['src']

with open('interviews.json', 'r') as f:
    data['interviews'] = json.load(f)

with open('portfolios.json', 'r') as f:
    data['portfolios'] = json.load(f)

with open('resumes.json', 'r') as f:
    data['resumes'] = json.load(f)

with open('salaries.json', 'r') as f:
    data['salaries'] = json.load(f)

data['students'] = {'misc': []}
with open('students.json', 'r') as f:
    data['students']['src'] = json.load(f)
for post in data['students']['src']:
    degrees = post['degrees']
    if degrees is None:
        data['students']['misc'].append(post)
    else:
        for degree in degrees:
            if degree not in data['students']:
                data['students'][degree] = []
            data['students'][degree].append(post)
del data['students']['src']

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
    },
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
    # content += f'## {metadata[theme]["title"]}\n\n'
    content += f'<h2 id="{theme}>{metadata[theme]["title"]}</h2>\n\n'
    content += f'[Link to this section](#{theme})\n\n'
    content += f'{metadata[theme]["desc"]}\n\n'
    if theme == 'students':
        for degree in data['students']:
            if degree == 'misc':
                content += '### General and miscellaneous\n\n'
            else:
                content += f'### {degree.capitalize().replace("_", " ")}\n\n'
            for post in data['students'][degree]:
                post_id = post['post_id']
                title = post['title']
                date = datetime.datetime.fromisoformat(post['date']).strftime('%d %b %Y')
                content += f'* [{title}](https://reddit.com/r/technicalwriting/comments/{post_id}) ({date})\n'
            content += '\n'
    elif theme in ['entrances', 'exits']:
        for career in data[theme]:
            if career == 'misc':
                content += '### General and miscellaneous\n\n'
            else:
                content += f'### {career.capitalize().replace("_", " ")}\n\n'
            for post in data[theme][career]:
                post_id = post['post_id']
                title = post['title']
                date = datetime.datetime.fromisoformat(post['date']).strftime('%d %b %Y')
                content += f'* [{title}](https://reddit.com/r/technicalwriting/comments/{post_id}) ({date})\n'
            content += '\n'
    else:
        for post in data[theme]:
            post_id = post['post_id']
            title = post['title']
            date = datetime.datetime.fromisoformat(post['date']).strftime('%d %b %Y')
            content += f'* [{title}](https://reddit.com/r/technicalwriting/comments/{post_id}) ({date})\n'
        content += '\n'

print(content)
