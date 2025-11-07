# --- 2. CHARACTER SUBCLASS ---

from .entity import Entity
from .mergable_dict import MergeableDict

class Character(Entity):
    """Represents a combat participant (Player or Enemy)."""
    def __init__(self, name, max_hp=100, attack=1, defense=1, resistance = MergeableDict({     
            "poison": 0.0,
            "burn": 0.0,
            "sleep": 0.0,
            "silence": 0.0,
            "blind": 0.0,
            "petrify": 0.0
        }), is_player=False):
        super().__init__(name) 
        
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.base_attack = attack    # Base stat
        self.base_defense = defense  # Base stat
        self.base_resistance = resistance # Base stat
        self.is_player = is_player
        self.is_alive = True
        self.ailments = MergeableDict({
            "poison": 0.0,
            "burn": 0.0,
            "sleep": 0.0,
            "silence": 0.0,
            "blind": 0.0,
            "petrify": 0.0
        })

        # Equipment slots for player party members
        self.equipment = {
            'equipped_weapon': None,
            'head': None,
            'chest': None,
            'arms': None,
            'legs': None
        }
    
    # --- New Methods for Gear Integration ---
    def get_attack(self):
        """Calculates effective attack including equipped weapon bonus."""
        effective_attack = self.base_attack
        if self.equipment['equipped_weapon']:
            effective_attack += self.equipment['equipped_weapon'].attack_bonus
        return effective_attack

    def get_defense(self):
        """Calculates effective defense including equipped armor bonus."""
        effective_defense = self.base_defense
        for key in self.equipment.keys():
            if self.equipment[key]:
                effective_defense += self.equipment[key].defense_bonus
        return effective_defense
    
    def get_resistance(self):
        """Calculates effective ailment resistance including equipped armor bonus."""
        effective_resistance = self.base_resistance
        for key in self.equipment.keys():
            if self.equipment[key]:
                effective_resistance += self.equipment[key].resistance_bonus
        return effective_resistance

    # --- Combat Methods ---
    def take_damage(self, damage, inflictions = MergeableDict({     
            "poison": 0.0,
            "burn": 0.0,
            "sleep": 0.0,
            "silence": 0.0,
            "blind": 0.0,
            "petrify": 0.0
        })):
        """Calculates and applies damage using effective defense."""
        damage_taken = max(0, damage - self.get_defense())
        self.current_hp -= damage_taken

        self.ailments += inflictions
        
        if self.current_hp <= 0:
            self.current_hp = 0
            self.is_alive = False
            self.is_active = False
            print(f"💀 {self.name} has been defeated!")
            
        return damage_taken

    def heal(self, amount):
        """Heals the character, respecting max HP."""
        if not self.is_alive:
            print(f"{self.name} is defeated and cannot be healed.")
            return 0
        
        pre_heal_hp = self.current_hp
        self.current_hp = min(self.max_hp, self.current_hp + amount)
        healed_amount = self.current_hp - pre_heal_hp
        return healed_amount

    def get_status(self):
        """Returns a string summary of the character's HP and effective stats."""
        return (f"[{self.name}] HP: {self.current_hp}/{self.max_hp} | "
                f"ATK: {self.get_attack()} (Base: {self.base_attack}) | "
                f"DEF: {self.get_defense()} (Base: {self.base_defense}) | "
                f"RES: {self.get_resistance()} (Base: {self.base_resistance})")