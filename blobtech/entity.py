import random

# --- 1. BASE ENTITY CLASS ---

class Entity:
    """The base class for all objects in the game world."""
    def __init__(self, name):
        self.name = name
        # is_active can be used to track if an item is available, 
        # a character is alive, or a trap is disarmed.
        self.is_active = True 
        
    def __repr__(self):
        return self.name