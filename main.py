from models.player import Player
import config

p = Player('Aragorn', 'Elf', 'Wizard', 10)
print(p)
lang = config.read_language()
print(lang['language'])
