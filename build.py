import json

with open('intro.md', 'r') as f:
    intro = f.read()
with open('advancement.json', 'r') as f:
    advancement = json.load(f)
with open('demand.json', 'r') as f:
    demand = json.load(f)
with open('entrances.json', 'r') as f:
    entrances = json.load(f)
with open('exits.json', 'r') as f:
    exits = json.load(f)
with open('interviews.json', 'r') as f:
    interviews = json.load(f)
with open('portfolios.json', 'r') as f:
    portfolios = json.load(f)
with open('resumes.json', 'r') as f:
    resumes = json.load(f)
with open('salaries.json', 'r') as f:
    salaries = json.load(f)
with open('students.json', 'r') as f:
    students = json.load(f)
with open('training.json', 'r') as f:
    training = json.load(f)
