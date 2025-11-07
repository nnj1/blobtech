import random

class BlobEngine:
    """Manages the turn-based combat flow."""
    def __init__(self, party, enemies, inventory=None):
        self.party = party
        self.enemies = enemies
        self.inventory = inventory if inventory is not None else []
        self.combat_active = True
        
    def start_battle(self):
        print("\n" + "="*20)
        print("=== BATTLE START ===")
        print("="*20)
        print(f"Your party (The Blob) faces: {', '.join(e.name for e in self.enemies)}")
        
        self.initiative_order = self.party + self.enemies
        random.shuffle(self.initiative_order)
        
        while self.combat_active:
            self.take_turn()
            self.check_combat_status()
            
    def take_turn(self):
        self.initiative_order = [c for c in self.initiative_order if c.is_active]
        
        if not self.initiative_order:
             return 

        current_character = self.initiative_order.pop(0) 
        
        print(f"\n--- {current_character.name}'s Turn ---")
        
        if current_character.is_player:
            self.handle_player_action(current_character)
        else:
            self.handle_enemy_action(current_character)
            
        self.initiative_order.append(current_character)

    def handle_player_action(self, actor):
        # Player action now uses the character's effective attack
        valid_targets = [e for e in self.enemies if e.is_alive]
        if not valid_targets: return
        target = valid_targets[0] 

        # Use effective attack value
        attack_value = actor.get_attack() 
        base_damage = random.randint(attack_value // 2, attack_value)
        
        damage_dealt = target.take_damage(base_damage)
        print(f"⚔️ {actor.name} attacks {target.name} for {damage_dealt} damage.")

    def handle_enemy_action(self, actor):
        valid_targets = [p for p in self.party if p.is_alive]
        if not valid_targets: return
            
        target = random.choice(valid_targets)
        
        base_damage = random.randint(actor.base_attack // 2, actor.base_attack)
        damage_dealt = target.take_damage(base_damage)
        print(f"💢 {actor.name} strikes {target.name} for {damage_dealt} damage.")

    def check_combat_status(self):
        party_alive = any(p.is_alive for p in self.party)
        enemies_alive = any(e.is_alive for e in self.enemies)
        
        if not party_alive:
            print("\n" + "="*20)
            print("❌ GAME OVER: Your party was wiped out.")
            print("="*20)
            self.combat_active = False
        elif not enemies_alive:
            print("\n" + "="*20)
            print("✅ VICTORY! All enemies have been defeated.")
            print("="*20)
            self.combat_active = False
        
        if self.combat_active:
            print("\n--- Current Status ---")
            for char in self.party:
                if char.is_alive:
                    print(char.get_status())