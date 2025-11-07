from .entity import Entity

# --- 3. ITEM SUBCLASS ---
class Item(Entity):
    """Represents an item in the game, which can be consumable, equipment, or treasure."""
    def __init__(self, name, item_type, description, value=0):
        super().__init__(name)
        self.item_type = item_type  # e.g., 'Consumable', 'Weapon', 'Treasure'
        self.description = description
        self.value = value
        
    def use(self, target_character):
        """Placeholder method for item usage logic."""
        print(f"**Item Use:** {self.name} used on {target_character.name}.")
        # Subclasses (e.g., Potion, Sword) would override this with specific effects
        if self.item_type == 'Consumable':
            # After use, a consumable item might become inactive
            self.is_active = False 
        return True

    def __str__(self):
        return f"{self.name} ({self.item_type}): {self.description}"