import random 
import string 
from decouple import config


def generate_shareable_link():
    
    letters = string.ascii_letters
    numbers = string.digits

    acceptable_characters = letters + numbers
    generated_link = "".join(random.choice(acceptable_characters) for i in range(12))

    if config("MODE") == 'dev':
        return f'http://127.0.0.1/photo/{generated_link}'
    else:
        return f'http://https://project-storybook.herokuapp.com/photo/{generated_link}'
