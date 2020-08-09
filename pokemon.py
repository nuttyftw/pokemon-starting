class Pokemon:
    # Create a Pokemon. Give it a name, level, type, maximum health determined by level), and if it's been knocked out.
    def __init__(self, name, level, type, max_health, current_health, knocked_out):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = max_health
        self.current_health = current_health
        self.knocked_out = knocked_out

    # Deduct health when a pokemon takes damage.
    def lose_heatlh(self, damage):
        self.current_health -= damage
        # Check to see if the damage knocks out the pokemon.
        if self.current_health <= 0:
            self.current_health = 0
            self.knock_out()
        else:
            print("{name} now has {current_health} out of {max_health} health.".format(name = self.name, current_health = self.current_health, max_health = self.max_health))
    
    # Add health when a pokemon is healed.
    def gain_health(self, healing):
        # Check to see if the damage revives the pokemon
        if self.current_health == 0:
            self.revive()
        self.current_health += healing
        print("{name} now has {current_health} out of {max_health} health.".format(name = self.name, current_health = self.current_health, max_health = self.max_health))

    # Statement for an unconscious pokemon.
    def knock_out(self):
        self.knocked_out = True
        print("Oh no! {name} has been knocked out!".format(name = self.name))

    # State for reviving a pokemon.
    def revive(self):
        self.knocked_out = False
        print("Yay! {name} has been revived and is back in the fight!".format(name = self.name))

    def attack(self, other_pokemon):
        damage = self.level
        # If the attacking pokemon has advantage based on type, it deals damage equals to double it's level.
        if (self.type == "Fire" and other_pokemon.type == "Grass") or (self.type == "Water" and other_pokemon.type == "Fire") or (self.type == "Grass" and other_pokemon.type == "Water"):
            damage = damage * 2
            other_pokemon.lose_health(damage)
            print("{attacker_name} attakced {defense_name} for " + damage + " damage.".format(attacker_name = self.name, defense_name = other_pokemon.name))
            print("It's super effective!")
        # If the attacking pokemon has disadvantage based on type, it deals damage equal to one half it's level.
        if (self.type == "Grass" and other_pokemon.type == "Fire") or (self.type == "Fire" and other_pokemon.type == "Water") or (self.type == "Water" and other_pokemon.type == "Grass"):
            damage = damage / 2
            other_pokemon.lose_health(damage)
            print("{attacker_name} attakced {defense_name} for " + damage + " damage.".format(attacker_name = self.name, defense_name = other_pokemon.name))
            print("It's not very effective!")
        # If the attacking pokemon has neither advantage or disadvantage on type, it deals damage equal to it's level.
        if (self.type == other_pokemon.type):
            other_pokemon.lost_health(damage)
            print("{attacker_name} attakced {defense_name} for " + damage + " damage.".format(attacker_name = self.name, defense_name = other_pokemon.name))

class Trainer:
    # A Trainer has a name, a list of pokemon, and potions to heal their pokemon.
    # When the Trainer is created, the first pokemon in their list (number 0) is marked as active.
    def __init__(self, pokemon_list, name, number_of_potions):
        self.pokemons = pokemon_list
        self.name = name
        self.potions = number_of_potions
        self.current_pokemon = 0