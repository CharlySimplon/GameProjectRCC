def drink_potion(players_hp, max_players_hp, potion):
    if players_hp < max_players_hp -20:
        players_hp += 20
    else:
        players_hp = max_players_hp
    potion -= 1
    print(f'-------Vous avez maintenant {potion} potions')
    return print("+20 PV ========> ",players_hp)