# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import re

from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
from app import App


lang = App.get_language()
app_name = App.get_name()

style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})

msg_new_user = {
    'ES': 'Tienes una cuenta creada en ' + app_name + '?',
    'EN': 'Do you have an account in ?' + app_name + '?',
}
msg_email = {
    'ES': 'Ingresa tu e-mail:',
    'EN': 'Enter your e-mail:',
}


def validate_email(email):
    result = False
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if re.search(regex, email):
        result = True
    return result


def enter_email():
    question = [{
        'type': 'input',
        'name': 'email',
        'message': msg_email[lang],
        'validate': validate_email
    }, ]
    answer = prompt(question, style=style)
    return answer['email']


def validate_password():
    result = True
    return result


def validate_name():
    result = True
    return result


def is_user():
    question = [{
        'type': 'confirm',
        'name': 'new',
        'message': msg_new_user[lang],
        'default': False
    },]
    answer = prompt(question, style=style)
    return answer['new']


def create_account():
    if enter_email() is not None:
        enter_password()


def login_account():
    print('login_account')

# Main Loop --------------------------------------------
if is_user():
    login_account()
else:
    create_account()


def list_players():
    return True


def create_player():
    return True


def init_game():
    return True


def enter_password():
    return True






print('Hi, welcome to PyMud')

questions = [
    {
        'type': 'confirm',
        'name': 'new',
        'message': 'Are you new user?',
        'default': False
    },
    {
        'type': 'input',
        'name': 'email',
        'message': 'What\'s your email?',
        'validate': validate_email
    },
    {
        'type': 'password',
        'name': 'pass',
        'message': 'What\'s your password?',
        'validate': validate_password
    },
{
        'type': 'list',
        'name': 'race',
        'message': 'Choose your race:',
        'choices': ['Human', 'Elf', 'Dwarf', 'Drow', 'Orc'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'profession',
        'message': 'Choose a path:',
        'choices': ['Warrior', 'Wizard', 'Artisan'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'input',
        'name': 'name',
        'message': 'Choose a name for your player:',
        'validate': validate_name
    },
]

#answers = prompt(questions, style=style)
#print('User data:')
#pprint(answers)