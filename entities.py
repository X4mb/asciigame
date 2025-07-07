import random

class Entity:
    def __init__(self, x, y, char, name):
        self.x = x
        self.y = y
        self.char = char
        self.name = name

class Player(Entity):
    def __init__(self, x, y, player_class='warrior'):
        super().__init__(x, y, '@', 'Player')
        self.player_class = player_class
        self.level = 1
        self.exp = 0
        self.exp_to_next = 10
        self.learned_spells = set()  # Track which spells are learned
        self.learned_skills = set()  # Track which skills are learned
        self.available_spells = {}  # Spells that can be learned
        self.available_skills = {} # Skills that can be learned
        self.dodging = False
        self.max_weight = 50.0  # Maximum weight capacity
        self.max_inventory_slots = 20  # Maximum number of different items
        self.setup_class_stats()
        self.hp = self.max_hp
        self.mana = self.max_mana
        self.inventory = []
        self.equipped_weapon = None  # Track equipped weapon
        self.equipped_armor = None   # Track equipped armor
        self.unlock_all_skills_and_spells_for_level()

    def setup_class_stats(self):
        """Setup stats and spells/skills based on class"""
        if self.player_class == 'warrior':
            self.max_hp = 15
            self.max_mana = 0  # Warriors don't use mana
            self.max_stamina = 20  # Warriors have stamina
            self.stamina = 20
            self.attack = 4
            self.defense = 2
            self.available_skills = {
                2: {'power_strike': {'name': 'Power Strike', 'damage': 8, 'stamina_cost': 5, 'description': 'A powerful attack that deals extra damage'}},
                4: {'shield_bash': {'name': 'Shield Bash', 'damage': 6, 'stun': True, 'stamina_cost': 10, 'description': 'Bash with your shield, may stun the enemy'}},
                6: {'battle_rage': {'name': 'Battle Rage', 'damage': 12, 'self_heal': 5, 'stamina_cost': 15, 'description': 'Enter a rage, dealing damage and healing yourself'}}
            }
            self.dodge_chance = 0.0
        elif self.player_class == 'mage':
            self.max_hp = 8
            self.max_mana = 25
            self.max_stamina = 0  # Mages don't use stamina
            self.stamina = 0
            self.attack = 2
            self.defense = 1
            self.available_spells = {
                1: {'fireball': {'name': 'Fireball', 'damage': 8, 'mana_cost': 5, 'description': 'Deals 8 damage'}},
                3: {'lightning': {'name': 'Lightning', 'damage': 12, 'mana_cost': 10, 'description': 'Deals 12 damage'}},
                5: {'ice_storm': {'name': 'Ice Storm', 'damage': 18, 'mana_cost': 15, 'description': 'Deals 18 damage'}},
                7: {'meteor': {'name': 'Meteor', 'damage': 25, 'mana_cost': 25, 'description': 'Deals 25 damage'}}
            }
            self.dodge_chance = 0.0
        elif self.player_class == 'rogue':
            self.max_hp = 10
            self.max_mana = 0  # Rogues don't use mana
            self.max_stamina = 15  # Rogues have stamina
            self.stamina = 15
            self.attack = 3
            self.defense = 1
            self.available_skills = {
                2: {'backstab': {'name': 'Backstab', 'damage': 10, 'stamina_cost': 6, 'description': 'A precise strike that deals extra damage'}},
                4: {'evasion': {'name': 'Evasion', 'dodge': True, 'stamina_cost': 4, 'description': 'Attempt to dodge the next attack'}},
                6: {'poison_strike': {'name': 'Poison Strike', 'damage': 8, 'poison': 3, 'stamina_cost': 10, 'description': 'Strike with a poisoned weapon'}}
            }
            self.dodge_chance = 0.2  # 20% passive dodge chance
        elif self.player_class == 'cleric':
            self.max_hp = 12
            self.max_mana = 20
            self.max_stamina = 0  # Clerics don't use stamina
            self.stamina = 0
            self.attack = 2
            self.defense = 2
            self.available_spells = {
                1: {'heal': {'name': 'Heal', 'heal': 12, 'mana_cost': 6, 'description': 'Restores 12 HP'}},
                3: {'smite': {'name': 'Smite', 'damage': 10, 'mana_cost': 8, 'description': 'Deals 10 damage'}},
                5: {'divine_protection': {'name': 'Divine Protection', 'effect': 'shield', 'mana_cost': 10, 'description': 'Temporary defense boost'}},
                7: {'resurrection': {'name': 'Resurrection', 'effect': 'revive', 'mana_cost': 20, 'description': 'Revive with full HP'}}
            }
            self.dodge_chance = 0.0

    def take_damage(self, amount):
        actual_damage = max(1, amount - self.defense)
        self.hp = max(0, self.hp - actual_damage)
        return self.hp <= 0

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)

    def use_mana(self, amount):
        if self.mana >= amount:
            self.mana -= amount
            return True
        return False

    def restore_mana(self, amount):
        self.mana = min(self.max_mana, self.mana + amount)

    def use_stamina(self, amount):
        """Use stamina if available"""
        if self.stamina >= amount:
            self.stamina -= amount
            return True
        return False

    def restore_stamina(self, amount):
        """Restore stamina"""
        self.stamina = min(self.max_stamina, self.stamina + amount)

    def get_inventory_weight(self):
        """Calculate total weight of inventory"""
        return sum(item.get_total_weight() for item in self.inventory)

    def can_carry_item(self, item):
        """Check if player can carry this item"""
        current_weight = self.get_inventory_weight()
        new_weight = current_weight + item.get_total_weight()
        
        # Check weight limit
        if new_weight > self.max_weight:
            return False, f"Too heavy! ({new_weight:.1f}/{self.max_weight})"
        
        # Check if we need a new slot
        needs_new_slot = True
        for existing_item in self.inventory:
            if (existing_item.name == item.name and 
                existing_item.item_type == item.item_type and
                existing_item.effect == item.effect):
                needs_new_slot = False
                break
        
        if needs_new_slot and len(self.inventory) >= self.max_inventory_slots:
            return False, f"Inventory full! ({len(self.inventory)}/{self.max_inventory_slots} slots)"
        
        return True, "OK"

    def add_to_inventory(self, item):
        """Add item to inventory, stacking if possible"""
        can_carry, message = self.can_carry_item(item)
        if not can_carry:
            return False, message
            
        # Check if item can be stacked (potions, gold, etc.)
        if item.item_type in ['potion', 'gold', 'scroll']:
            # Look for existing stack of the same item
            for existing_item in self.inventory:
                if (existing_item.name == item.name and 
                    existing_item.item_type == item.item_type and
                    existing_item.effect == item.effect):
                    # Stack the items
                    existing_item.quantity += item.quantity
                    return True, f"Added to stack: {item.name} (x{existing_item.quantity})"
        # If no stack found or item can't be stacked, add as new item
        self.inventory.append(item)
        return True, f"Added: {item.name}"

    def remove_from_inventory(self, item):
        """Remove an item from inventory, handling stacks"""
        if item in self.inventory:
            if item.quantity > 1:
                item.quantity -= 1
                return True, f"Used one {item.name} (x{item.quantity} remaining)"
            else:
                self.inventory.remove(item)
                return True, f"Used last {item.name}"
        return False, "Item not found"

    def drop_item(self, item_index):
        """Drop an item from inventory"""
        if 0 <= item_index < len(self.inventory):
            item = self.inventory[item_index]
            if item.quantity > 1:
                item.quantity -= 1
                return True, f"Dropped one {item.name} (x{item.quantity} remaining)"
            else:
                self.inventory.remove(item)
                return True, f"Dropped {item.name}"
        return False, "Invalid item selection"

    def use_item_from_inventory(self, item_index):
        """Use an item from inventory by index, handling stacks"""
        if 0 <= item_index < len(self.inventory):
            item = self.inventory[item_index]
            result = item.use(self)
            
            # Remove one from stack if it's a consumable
            if item.item_type in ['potion', 'scroll']:
                self.remove_from_inventory(item)
            
            return result
        return "Invalid item selection"

    def equip_item(self, item):
        """Equip an item and return the old item if any"""
        if item.item_type == 'weapon':
            old_item = self.equipped_weapon
            self.equipped_weapon = item
            # Update attack stat
            self.attack = self.get_base_attack() + item.effect['attack']
            return old_item
        elif item.item_type == 'armor':
            old_item = self.equipped_armor
            self.equipped_armor = item
            # Update defense stat
            self.defense = self.get_base_defense() + item.effect['defense']
            return old_item
        return None

    def get_base_attack(self):
        """Get base attack without equipment"""
        if self.player_class == 'warrior':
            return 4 + (self.level - 1)  # Base + level gains
        elif self.player_class == 'mage':
            return 2 + (self.level - 1)
        elif self.player_class == 'rogue':
            return 3 + (self.level - 1)
        elif self.player_class == 'cleric':
            return 2 + (self.level - 1)
        return 2

    def get_base_defense(self):
        """Get base defense without equipment"""
        if self.player_class == 'warrior':
            return 2
        elif self.player_class == 'mage':
            return 1
        elif self.player_class == 'rogue':
            return 1
        elif self.player_class == 'cleric':
            return 2
        return 1

    def is_equipped(self, item):
        """Check if an item is currently equipped"""
        return (item == self.equipped_weapon or item == self.equipped_armor)

    def gain_exp(self, amount):
        self.exp += amount
        leveled_up = False
        while self.exp >= self.exp_to_next:
            self.level_up()
            leveled_up = True
        return leveled_up

    def unlock_all_skills_and_spells_for_level(self):
        """Unlock all skills and spells available at current level"""
        if self.player_class in ['mage', 'cleric']:
            for level, level_spells in self.available_spells.items():
                if level <= self.level:
                    for spell_key in level_spells.keys():
                        self.learned_spells.add(spell_key)
        if self.player_class in ['warrior', 'rogue']:
            for level, level_skills in self.available_skills.items():
                if level <= self.level:
                    for skill_key in level_skills.keys():
                        self.learned_skills.add(skill_key)

    def level_up(self):
        """Level up the player"""
        self.level += 1
        self.exp -= self.exp_to_next
        self.exp_to_next = self.level * 10
        
        # Increase stats based on class
        if self.player_class == 'warrior':
            self.max_hp += 3
            self.max_stamina += 2
            self.attack += 1
        elif self.player_class == 'mage':
            self.max_hp += 1
            self.max_mana += 3
            self.attack += 1
        elif self.player_class == 'rogue':
            self.max_hp += 2
            self.max_stamina += 2
            self.attack += 1
        elif self.player_class == 'cleric':
            self.max_hp += 2
            self.max_mana += 2
            self.attack += 1
        
        # Restore health and mana/stamina to full
        self.hp = self.max_hp
        if self.max_mana > 0:
            self.mana = self.max_mana
        if self.max_stamina > 0:
            self.stamina = self.max_stamina
        
        # Unlock new skills/spells
        self.unlock_all_skills_and_spells_for_level()
        return True

    def get_learned_spells(self):
        """Get dictionary of learned spells"""
        spells = {}
        if self.player_class in ['mage', 'cleric']:
            for level, level_spells in self.available_spells.items():
                if level <= self.level:
                    for spell_key, spell_data in level_spells.items():
                        if spell_key in self.learned_spells:
                            spells[spell_key] = spell_data
        return spells

    def get_learned_skills(self):
        """Get dictionary of learned skills"""
        skills = {}
        if self.player_class in ['warrior', 'rogue']:
            for level, level_skills in self.available_skills.items():
                if level <= self.level:
                    for skill_key, skill_data in level_skills.items():
                        if skill_key in self.learned_skills:  # Use learned_skills set
                            skills[skill_key] = skill_data
        return skills

    def is_caster(self):
        """Check if this class is a spellcaster"""
        return self.player_class in ['mage', 'cleric']

    def get_status(self):
        if self.max_stamina > 0:
            return f"Class: {self.player_class.title()} | HP: {self.hp}/{self.max_hp} | SP: {self.stamina}/{self.max_stamina} | Level: {self.level} | Exp: {self.exp}/{self.exp_to_next} | ATK: {self.attack} | DEF: {self.defense}"
        else:
            return f"Class: {self.player_class.title()} | HP: {self.hp}/{self.max_hp} | MP: {self.mana}/{self.max_mana} | Level: {self.level} | Exp: {self.exp}/{self.exp_to_next} | ATK: {self.attack} | DEF: {self.defense}"

class Monster:
    def __init__(self, x, y, monster_type):
        self.x = x
        self.y = y
        self.monster_type = monster_type
        self.stunned = False
        self.poisoned = False
        self.poison_damage = 0
        self.move_speed = 1
        self.move_counter = 0
        # Set stats based on monster type
        if monster_type == 'goblin':
            self.char = 'g'
            self.name = 'Goblin'
            self.hp = 8
            self.max_hp = 8
            self.attack = 3
            self.defense = 1
            self.speed = 1
            self.exp_value = 5
            self.loot_table = ['gold', 'health_potion', 'stamina_potion']
            self.move_speed = 1
        elif monster_type == 'orc':
            self.char = 'o'
            self.name = 'Orc'
            self.hp = 15
            self.max_hp = 15
            self.attack = 5
            self.defense = 2
            self.speed = 1
            self.exp_value = 10
            self.loot_table = ['gold', 'health_potion', 'mana_potion', 'stamina_potion']
            self.move_speed = 2
        elif monster_type == 'troll':
            self.char = 't'
            self.name = 'Troll'
            self.hp = 25
            self.max_hp = 25
            self.attack = 7
            self.defense = 3
            self.speed = 1
            self.exp_value = 20
            self.loot_table = ['gold', 'health_potion', 'mana_potion', 'stamina_potion', 'sword']
            self.move_speed = 3
        elif monster_type == 'dragon':
            self.char = 'D'
            self.name = 'Dragon'
            self.hp = 40  # Reduced from 50
            self.max_hp = 40  # Reduced from 50
            self.attack = 10  # Reduced from 12
            self.defense = 5
            self.speed = 1
            self.exp_value = 50
            self.loot_table = ['gold', 'health_potion', 'mana_potion', 'stamina_potion', 'sword', 'armor']
            self.move_speed = 1
        self.move_counter = 0

    def should_move(self):
        return self.move_counter >= self.move_speed

    def increment_move_counter(self):
        self.move_counter += 1

    def reset_move_counter(self):
        self.move_counter = 0

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0

    def move_towards_player(self, player_x, player_y, dungeon):
        """Move towards the player if they can see them"""
        if self.stunned:
            self.stunned = False
            return
            
        # Check if monster can see player (simple line of sight)
        if self.can_see_player(player_x, player_y, dungeon):
            # Calculate direction to player
            dx = 0
            dy = 0
            if player_x > self.x:
                dx = 1
            elif player_x < self.x:
                dx = -1
            if player_y > self.y:
                dy = 1
            elif player_y < self.y:
                dy = -1
            
            # Try to move in the calculated direction
            new_x = self.x + dx
            new_y = self.y + dy
            
            # Check if the new position is valid
            if dungeon.is_valid_position(new_x, new_y):
                self.x = new_x
                self.y = new_y

    def can_see_player(self, player_x, player_y, dungeon):
        """Simple line of sight check"""
        # Calculate distance
        distance = abs(player_x - self.x) + abs(player_y - self.y)
        if distance > 8:  # Can't see beyond 8 tiles
            return False
        
        # Simple line of sight (check if there's a clear path)
        dx = player_x - self.x
        dy = player_y - self.y
        
        # Check each tile along the path
        steps = max(abs(dx), abs(dy))
        if steps == 0:
            return True
            
        for i in range(1, steps + 1):
            check_x = self.x + (dx * i) // steps
            check_y = self.y + (dy * i) // steps
            if not dungeon.is_valid_position(check_x, check_y):
                return False
                
        return True

    def get_loot(self, player_class=None):
        """Generate loot based on loot table and player class"""
        import random
        if not self.loot_table:
            return []
        
        loot = []
        for item in self.loot_table:
            if item == 'gold':
                amount = random.randint(1, 5)
                loot.append(('gold', amount))
            elif item == 'health_potion':
                loot.append(('health_potion', 1))
            elif item == 'mana_potion':
                # Only give mana potions to casters
                if player_class in ['mage', 'cleric']:
                    loot.append(('mana_potion', 1))
            elif item == 'stamina_potion':
                # Only give stamina potions to non-casters
                if player_class in ['warrior', 'rogue']:
                    loot.append(('stamina_potion', 1))
            elif item == 'sword':
                loot.append(('sword', 1))
            elif item == 'armor':
                loot.append(('armor', 1))
        
        return loot

class Item(Entity):
    def __init__(self, x, y, char, name, effect=None, item_type='misc', quantity=1, weight=0.1):
        super().__init__(x, y, char, name)
        self.effect = effect
        self.item_type = item_type  # 'weapon', 'armor', 'potion', 'scroll', 'gold'
        self.quantity = quantity
        self.weight = weight  # Weight per unit

    def get_total_weight(self):
        """Get total weight of this item stack"""
        return self.weight * self.quantity

    def use(self, player):
        """Use the item on the player"""
        if not self.effect:
            return f"Used {self.name}"
            
        if self.item_type == 'potion':
            if 'heal' in self.effect:
                player.heal(self.effect['heal'])
                return f"Used {self.name} and restored {self.effect['heal']} HP!"
            elif 'mana' in self.effect:
                player.restore_mana(self.effect['mana'])
                return f"Used {self.name} and restored {self.effect['mana']} MP!"
            elif 'stamina' in self.effect:
                player.restore_stamina(self.effect['stamina'])
                return f"Used {self.name} and restored {self.effect['stamina']} SP!"
        elif self.item_type == 'weapon':
            old_item = player.equip_item(self)
            if old_item:
                return f"Equipped {self.name}! Replaced {old_item.name}. Attack: {player.attack}"
            else:
                return f"Equipped {self.name}! Attack: {player.attack}"
        elif self.item_type == 'armor':
            old_item = player.equip_item(self)
            if old_item:
                return f"Equipped {self.name}! Replaced {old_item.name}. Defense: {player.defense}"
            else:
                return f"Equipped {self.name}! Defense: {player.defense}"
        return f"Used {self.name}"

class Chest(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 'C', 'Treasure Chest')
        self.opened = False
        self.loot = []

    def generate_loot(self, player_class=None):
        """Generate random loot for the chest based on player class"""
        loot_options = [
            Item(self.x, self.y, '!', 'Health Potion', {'heal': 15}, 'potion'),
            Item(self.x, self.y, '~', 'Mana Potion', {'mana': 20}, 'potion'),
            Item(self.x, self.y, 'S', 'Steel Sword', {'attack': 5}, 'weapon'),
            Item(self.x, self.y, 'A', 'Leather Armor', {'defense': 2}, 'armor'),
            Item(self.x, self.y, '$', 'Gold Coins', {'gold': 50}, 'gold')
        ]
        
        # Add stamina potions for non-casters
        if player_class in ['warrior', 'rogue']:
            loot_options.append(Item(self.x, self.y, '&', 'Stamina Potion', {'stamina': 15}, 'potion'))
        
        # Filter out mana potions for non-casters
        if player_class in ['warrior', 'rogue']:
            loot_options = [item for item in loot_options if item.name != 'Mana Potion']
        
        # Filter out stamina potions for casters
        if player_class in ['mage', 'cleric']:
            loot_options = [item for item in loot_options if item.name != 'Stamina Potion']
        
        num_items = random.randint(1, 3)
        self.loot = random.sample(loot_options, min(num_items, len(loot_options)))
        return self.loot

    def open(self, player_class=None):
        if not self.opened:
            self.opened = True
            self.char = 'c'  # Opened chest
            return self.generate_loot(player_class)
        return [] 