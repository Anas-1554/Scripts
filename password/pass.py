import random
import pyperclip

def generate_random_string(length):

  characters = []
  for i in range(97, 123):
    characters.append(chr(i))
  for i in range(65, 91):
    characters.append(chr(i))
  for i in range(48, 58):
    characters.append(chr(i))
  characters.append('!')
  characters.append('@')
  characters.append('#')
  characters.append('$')
  characters.append('%')
  characters.append('^')
  characters.append('&')
  characters.append('*')
  characters.append('(')
  characters.append(')')
  characters.append('-')
  characters.append('_')
  characters.append('+')
  characters.append('=')
  characters.append('.')
  characters.append(',')
  characters.append(';')
  characters.append(':')
  characters.append('?')


  string = ''
  for i in range(length):
    string += characters[random.randint(0, len(characters) - 1)]

  string = string.replace(' ', '')

  pyperclip.copy(string)

  return string

if __name__ == '__main__':
  random_string = generate_random_string(12)

  print("This is your random password:")
  print(random_string)
