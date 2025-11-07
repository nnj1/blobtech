# --- 3.3. ARMOR SUBCLASS ---

from .item import Item
from .mergable_dict import MergeableDict

class Armor(Item):
    """Items equipped to increase a character's defense."""
    def __init__(self, name, description, value=100, defense_bonus=0, resistance_bonus = MergeableDict({
            "poison": .1,
            "burn": .1,
            "sleep": .1,
            "silence": .1,
            "blind": .1,
            "petrify": .1
        })):
        super().__init__(name, description, value)
        self.defense_bonus = defense_bonus # for raw defense
        self.resistance_bonus = resistance_bonus # for resisting ailments