from blobtech.armor import Armor
from blobtech.artifact import Artifact
from blobtech.blobengine import BlobEngine
from blobtech.character import Character
from blobtech.consumable import Consumable
from blobtech.item import Item
from blobtech.weapon import Weapon

# --- Item Definitions ---
potion = Consumable("Slime Potion", "Restores moderate HP.", 5, "Heal", 40)

sword = Weapon("Goo-Slicer", "A sharp blade for slicing enemies.", 100, 15)

armor = Armor("Jelly Vest", "A resilient vest made of hardened slime.", 80, 8)

artifact = Artifact("Core of Glop", "A pulsing core that grants protection.", 500, {'defense': 5})

print("--- Item Showcase ---")
print(f"Item: {potion.name}, Type: Consumable (Heal: {potion.effect_value})")
print(f"Item: {sword.name}, Type: Weapon (ATK Bonus: +{sword.attack_bonus})")
print(f"Item: {armor.name}, Type: Armor (DEF Bonus: +{armor.defense_bonus})")
print("-" * 20)

# --- Character Setup (Equipping Items) ---
hero = Character("Goo-Knight", max_hp=100, attack=18, defense=5, is_player=True)
hero.equipment['equipped_weapon'] = sword # Equipping the Weapon
hero.equipment['chest'] = armor   # Equipping the Armor

mage = Character("Slime-Mage", max_hp=80, attack=25, defense=2, is_player=True)

party_members = [hero, mage]

# --- Initial State ---
print(hero.get_status())
print("-" * 20)

# --- Example Use (Pre-Battle) ---
# Take some damage
hero.current_hp = 50
print(f"Goo-Knight takes 50 damage! HP: {hero.current_hp}")

# Use Potion
potion.use(hero)

# Check status after use
print(f"Current Potion Status (Active): {potion.is_active}")
print(hero.get_status())
print("-" * 20)

# --- Define Enemies ---
enemy1 = Character("Goblin", max_hp=30, attack=10, defense=0)
enemies_to_fight = [enemy1]

# --- Run the Engine ---
game = BlobEngine(party_members, enemies_to_fight) 
game.start_battle()