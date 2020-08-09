class Pokemon:
    # Create a Pokemon. Give it a name, level, type, maximum health 
    # (determined by level), and if it's been knocked out.
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

    def attack(other_pokemon):
        other_pokemon.lose_health(damage)
        pass