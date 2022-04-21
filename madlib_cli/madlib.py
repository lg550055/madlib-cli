import re

def read_template(path):
  try:
    with open(path) as file:
      return file.read()
  except FileNotFoundError as err:
    raise err

def parse_template(text):
  parts = re.findall(r'{(.*?)}', text)
  stripped = re.sub(r'{(.*?)}','{}', text)
  return stripped, tuple(parts)

def merge(stripped, parts):
  return stripped.format(*parts)

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
  stripped, parts = parse_template(s)
  words = []
  for p in parts:
    words.append(input(f'Please enter a {p}: '))
  print('Here is the story you created\n')
  story = merge(stripped, words)
  print(story)
  print('\nCheers!')
