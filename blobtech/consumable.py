# --- 3.1. CONSUMABLE SUBCLASS ---

from .item import Item


class Consumable(Item):
    """Items that are used once and removed, providing an immediate effect."""
    def __init__(self, name, description, value, effect_type, effect_value):
        super().__init__(name, description, value)
        self.effect_type = effect_type  # e.g., 'Heal', 'Restore Mana', 'Buff'
        self.effect_value = effect_value

    def use(self, target_character):
        """Applies the consumable's effect to a character."""
        if self.effect_type == 'Heal':
            healed = target_character.heal(self.effect_value)
            print(f"✨ {self.name} used on {target_character.name}, restoring {healed} HP.")
        else:
            print(f"⚠️ {self.name} effect '{self.effect_type}' not yet implemented.")
            return False # Item not consumed if effect fails
        
        self.is_active = False # Consumable is used up
        return True