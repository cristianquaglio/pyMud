# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
import sys
import re
from app import App
from models.user import User
from models.player import Player

# Globals
if len(App.get_language()) is 0:
    sys.exit(1)
else:
    lang = App.get_language()
if len(App.get_name()) is 0:
    sys.exit(1)
else:
    app_name = App.get_name()

# Declarations
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

msg_password = {
    'ES': 'Ingresa tu clave (8 caracteres al menos):',
    'EN': 'Enter your password (8 characters at least):',
}

msg_account_failed = {
    'ES': 'Error creando la cuenta. Puede que ya exista el correo. Intenta nuevamente.',
    'EN': 'Error creating account. Maybe the account exists. Try again, please.',
}

msg_player_failed = {
    'ES': 'Error creando el jugador. Ya existe el nombre. Intenta nuevamente!',
    'EN': 'Error creating player. The name exists. Try again!',
}

msg_races = {
    'ES': 'Elige tu raza:',
    'EN': 'Choose your race:',
}

list_races = {
    'ES': ['Humano', 'Elfo', 'Drow', 'Enano', 'Orco'],
    'EN': ['Human', 'Elf', 'Drow', 'Dwarf', 'Orc'],
              }

msg_professions = {
    'ES': 'Elige tu profesión:',
    'EN': 'Choose your profession:',
}

list_professions = {
    'ES': ['Guerrero', 'Mago', 'Artesano'],
    'EN': ['Warrior', 'Wizard', 'Artisan'],
              }

msg_name_player = {
    'ES': 'Ingresa el nombre de tu personaje (sin espacios):',
    'EN': 'Enter player name (without spaces):',
}


def validate_email(email):
    result = False
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if re.search(regex, email):
        result = True
    return result


def validate_password(password):
    result = False
    regex = '^\w{8,}'
    if re.search(regex, password):
        result = True
    return result


def validate_name(name_player):
    result = False
    regex = '^[a-zA-Z]{2,16}$'
    if re.search(regex, name_player):
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


def enter_email():
    question = [{
        'type': 'input',
        'name': 'email',
        'message': msg_email[lang],
        'validate': validate_email
    }, ]
    answer = prompt(question, style=style)
    return answer['email']


def enter_password():
    question = [{
        'type': 'password',
        'name': 'pass',
        'message': msg_password[lang],
        'validate': validate_password
    }, ]
    answer = prompt(question, style=style)
    return answer['pass']


def create_account():
    result = False
    email = enter_email()
    if email is not None:
        password = enter_password()
        if password is not None:
            us = User(email, password)
            result = us.save()
    return result


def set_race():
    question = [{
        'type': 'list',
        'name': 'race',
        'message': msg_races[lang],
        'choices': list_races[lang],
    },]
    answer = prompt(question, style=style)
    return list_races[lang].index(answer['race']) + 1 # return index from selected value.


def set_profession():
    question = [{
        'type': 'list',
        'name': 'profession',
        'message': msg_professions[lang],
        'choices': list_professions[lang],
    },]
    answer = prompt(question, style=style)
    return list_professions[lang].index(answer['profession']) + 1  # return index from selected value.


def set_name_player():
    question = [{
        'type': 'input',
        'name': 'name_player',
        'message': msg_name_player[lang],
        'validate': validate_name
    },]
    answer = prompt(question, style=style)
    return answer['name_player']


def create_player():
    race = set_race()
    profession = set_profession()
    name_player = set_name_player()
    pl = Player(name_player, race, profession)
    return pl.save()


def init_game():
    return True


def login_account():
    print('login_account')

# Main Loop --------------------------------------------
if is_user():
    login_account()
else:
    account = False
    while account is False:
        account = create_account()
        if account:
            break
        else:
            print(msg_account_failed[lang])
    player = False
    while player is False:
        player = create_player()
        if player:
            break
        else:
            print(msg_player_failed[lang])
    init_game()


def list_players():
    return True
