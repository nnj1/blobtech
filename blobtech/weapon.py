# --- 3.2. WEAPON SUBCLASS ---

from .mergable_dict import MergeableDict
from .item import Item


class Weapon(Item):
    """Items equipped to increase a character's attack."""
    def __init__(self, name, description, value, attack_bonus=10, defense_bonus=0, resistance_bonus = MergeableDict({
            "poison":0,
            "burn": 0,
            "sleep": 0,
            "silence": 0,
            "blind": 0,
            "petrify": 0
        })):
        super().__init__(name, description, value)
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus
        self.resistance_bonus = resistance_bonus
        # Weapons don't usually have a 'use' method beyond being equipped.