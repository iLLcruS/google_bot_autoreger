import random
import string


def generate_random_first_name():
    first_names = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer', 'Michael', 'Linda', 'William',
                   'Elizabeth']
    return random.choice(first_names)

def generate_random_last_name():
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez',
                  'Martinez']
    return random.choice(last_names)

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def generate_random_email():
    domain = 'gmail.com'
    name_part = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
    return f"{name_part}@{domain}"