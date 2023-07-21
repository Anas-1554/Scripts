import random
import pyperclip
import os

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

    return string

def save_password(website_url, password, file_path):
    with open(file_path, 'a') as file:
        file.write(f"Website URL: {website_url}\n")
        file.write(f"Password: {password}\n\n")

if __name__ == '__main__':
    website_url = input("Please enter the website URL: ")
    length = 12
    use_custom_length = False

    prompt = input("Do you want to specify a custom password length? (y/n) ")
    if prompt.lower() == 'y':
        custom_length = input("Enter the desired password length: ")
        try:
            length = int(custom_length)
            use_custom_length = True
        except ValueError:
            print("Invalid input. Using default password length of 12 characters.")

    if use_custom_length:
        random_string = generate_random_string(length)
    else:
        random_string = generate_random_string(12)

    print("This is your random password:")
    print(random_string)

    pyperclip.copy(random_string)


    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "passwords.txt")
    save_password(website_url, random_string, file_path)
