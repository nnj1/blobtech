# --- 3.4. ARTIFACT SUBCLASS ---

from .item import Item


class Artifact(Item):
    """Unique, rare items providing permanent or passive bonuses."""
    def __init__(self, name, description, value, passive_bonus):
        super().__init__(name, description, value)
        self.passive_bonus = passive_bonus # Dictionary like {'max_hp': 10, 'magic_resist': 5}
        # Artifacts would require complex logic in Character class to apply bonuses