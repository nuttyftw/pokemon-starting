class Pokemon:
    # Create a Pokemon. Give it a name, level, type, maximum health determined by level), and if it's been knocked out.
    def __init__(self, name, type, level):
        self.name = name
        self.level = level
        self.type = type
        # Max helath is 5 times the pokemon's level.
        self.max_health = level * 5
        # Pokemon starts at max health.
        self.current_health = level * 5
        # Pokemon starts out conscious and in the fight
        self.knocked_out = False

    # Let's print out the pokemon's details.
    def __repr__(self):
        return "This Level {level} {name} has {health} hit points remaining. {name} is a {type}-type Pokemon.".format(level = self.level, name = self.name, health = self.current_health, type = self.type)

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

# Let's make three pokemon. One each of Fire, Grass, and Water.
# These are subclasses of Pokemon.
# By default, they will be at Level 5.
class Charmander(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Charmander", "Fire", level)

class Squirtle(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Squirtle", "Water", level)

class Bulbasaur(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Bulbasaur", "Grass", level)

class Trainer:
    # A Trainer has a name, a list of pokemon, and potions to heal their pokemon.
    # When the Trainer is created, the first pokemon in their list (number 0) is marked as active.
    def __init__(self, name, pokemon_list, number_of_potions):
        self.pokemons = pokemon_list
        self.name = name
        self.potions = number_of_potions
        self.current_pokemon = 0

    # Print out the details of a trainer.
    def __repr__(self):
        print("{name} has the following pokemon: ".format(name = self.name))
        for pokemon in self.pokemons:
            print(pokemon)
        return "{pokemon} is currently active.".format(pokemon = self.pokemons[self.current_pokemon].name)
    
    # A Trainer gives a potion to their pokemon.
    def use_potion(self):
        if self.potions > 0:
            self.pokemons[self.current_pokemon].gain_health(20)
            self.potions -= 1
            print("{name} just drank a potion. You know have {potions} left.".format(name = self.pokemons[self.current_pokemon].name, potions = self.potions))
        else:
            print("Oh no! You are out of potions!")

    # Attack a trainer
    def launch_attack(self, other_trainer):
        my_pokemon = self.pokemons[self.current_pokemon]
        enemy_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
        my_pokemon.attack(enemy_pokemon)

    # Switch pokemon
    def switch_pokemon(self, new_active):
        self.current_pokemon = new_active
        print("Go {name}, it's your turn!".format(name = self.pokemons[self.current_pokemon].name))

# Make a set of variables for the six pokemon.
poke_1 = Charmander()
poke_2 = Charmander()
poke_3 = Squirtle()
poke_4 = Squirtle()
poke_5 = Bulbasaur()
poke_6 = Bulbasaur()

# Make two trainers. Each has a list of pokemon, some potions, and a name.
trainer_1 = Trainer("Blaine", [poke_1, poke_2, poke_3], 4)
trainer_2 = Trainer("Misty", [poke_4, poke_5, poke_6], 6)

print(trainer_1)
print(trainer_2)