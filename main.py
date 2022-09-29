import requests
r =requests.get('https://paul.flowics.com/paul/public/polls/13619/62d1a9579bdf4d570350c09c?profile=interactive')
total = 0

for p in r.json().get('polls')[0].get('items'):
  print('{} votos {}'.format(p.get('name'), p.get('results').get('count')))
  total +=  p.get('results').get('count')
print('######')

for p in r.json().get('polls')[0].get('items'):
  print('{} %{}'.format(p.get('name'), p.get('results').get('count')/total*100))