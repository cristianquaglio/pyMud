from models.player import Player
from app import App

p = Player('Aragorn', 'Elf', 'Wizard', 10)
print(p)
lang = App.get_language()
ds = App.get_db_params()
print(lang)
print(ds)
