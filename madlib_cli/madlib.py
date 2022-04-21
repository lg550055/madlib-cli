import re

def read_template(path):
  try:
    with open(path) as file:
      return file.read()
  except FileNotFoundError as err:
    raise err

def parse_template(text):
  p = re.findall(r'\{\w+\}', text)
  parts = [re.sub(r'[\{\}]','', e) for e in p]
  stp = re.sub(r'\{\w+\}','{}', text)
  return stp, tuple(parts)

def merge(stp, parts):
  return stp.format(*parts)

def intro():
  print('''
    Welcome!
    This is a Madlib game
    We'll aks you to provide a few nouns, verbs, adjectives..
    Then we'll show you the story you created!
    Enjoy!
  ''')

if __name__ == "__main__":
  intro()
  s = read_template('assets/vgame.txt')
  stp, parts = parse_template(s)
  print(parts)
  w = []
  for p in parts:
    w.append(input(f'Please enter an {p}: '))
  print('Here is the story you created\n')
  story = merge(stp, w)
  print(story)
  print('\nCheers!')