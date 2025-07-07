import sys
import msvcrt
import time
import os
from dungeon import Dungeon
from entities import Player, Item
from ascii_art import get_title_screen, get_game_over_screen, get_combat_art

class Game:
    def __init__(self):
        self.dungeon = Dungeon()
        self.player = None  # Will be set after class selection
        self.is_running = True
        self.last_move = (0, 0)  # Track last movement direction (dx, dy)

    def show_class_selection(self):
        """Show class selection menu"""
        os.system('cls')
        print("=" * 60)
        print("                           CHOOSE YOUR CLASS")
        print("=" * 60)
        print()
        print("Choose your class:")
        print("1. Warrior")
        print("   HP: 15, MP: 10, ATK: 4, DEF: 2")
        print("   Skills: Power Strike (L2), Shield Bash (L4), Battle Rage (L6)")
        print()
        print("2. Mage")
        print("   HP: 8, MP: 25, ATK: 2, DEF: 1")
        print("   Spells: Fireball (L1), Lightning (L3), Ice Storm (L5), Meteor (L7)")
        print()
        print("3. Rogue")
        print("   HP: 10, MP: 15, ATK: 3, DEF: 1")
        print("   Skills: Backstab (L2), Evasion (L4), Poison Strike (L6)")
        print()
        print("4. Cleric")
        print("   HP: 12, MP: 20, ATK: 2, DEF: 2")
        print("   Spells: Heal (L1), Smite (L3), Divine Protection (L5), Resurrection (L7)")
        print()
        print("Press 1-4 to select your class, or P to quit...")
        
        while True:
            key = msvcrt.getch().decode('utf-8').lower()
            if key == 'p':
                self.is_running = False
                break
            elif key == '1':
                self.player = Player(1, 1, 'warrior')
                break
            elif key == '2':
                self.player = Player(1, 1, 'mage')
                break
            elif key == '3':
                self.player = Player(1, 1, 'rogue')
                break
            elif key == '4':
                self.player = Player(1, 1, 'cleric')
                break

    def show_title_screen(self):
        os.system('cls')
        print(get_title_screen())
        print("Press any key to start...")
        msvcrt.getch()

    def show_game_over(self):
        os.system('cls')
        print(get_game_over_screen())
        time.sleep(2)

    def run(self):
        self.show_title_screen()
        self.show_class_selection()
        if self.player is None:  # Fallback in case class selection fails
            self.player = Player(1, 1, 'warrior')
        while self.is_running:
            self.dungeon.render(player_pos=(self.player.x, self.player.y), player=self.player)
            self.display_player_status()
            self.handle_input()

    def display_player_status(self):
        if self.player is None:
            return
        print(f"\n{self.player.get_status()}")
        print(f"Position: ({self.player.x}, {self.player.y})")
        print(f"Inventory: {len(self.player.inventory)} items")

    def show_inventory(self):
        """Display and manage inventory with WASD/F/Q list selection"""
        if self.player is None:
            return
        
        selected = 0
        mode = 'normal'  # 'normal' or 'drop'
        while True:
            os.system('cls')
            print("=" * 60)
            print("                              INVENTORY")
            print("=" * 60)
            current_weight = self.player.get_inventory_weight()
            print(f"Weight: {current_weight:.1f}/{self.player.max_weight} | Slots: {len(self.player.inventory)}/{self.player.max_inventory_slots}")
            print("-" * 60)
            if not self.player.inventory:
                print("\nYour inventory is empty!")
            else:
                for i, item in enumerate(self.player.inventory):
                    arrow = '→' if i == selected else ' '
                    equipped_marker = ""
                    if self.player.is_equipped(item):
                        equipped_marker = " [EQUIPPED]"
                    quantity_text = f" (x{item.quantity})" if item.quantity > 1 else ""
                    weight_text = f" [{item.get_total_weight():.1f}kg]"
                    print(f"{arrow} {item.name} ({item.char}){quantity_text}{weight_text}{equipped_marker}")
                    if item.effect:
                        if item.item_type == 'potion':
                            if 'heal' in item.effect:
                                print(f"   Restores {item.effect['heal']} HP")
                            elif 'mana' in item.effect:
                                print(f"   Restores {item.effect['mana']} MP")
                        elif item.item_type == 'weapon':
                            print(f"   Attack: +{item.effect['attack']}")
                        elif item.item_type == 'armor':
                            print(f"   Defense: +{item.effect['defense']}")
                        elif item.item_type == 'gold':
                            print(f"   Value: {item.effect['gold']} gold")
                    print()
            print("\nControls:")
            print("W/S: Move  F: " + ("Drop" if mode == 'drop' else "Use/Equip") + "  D: Drop mode  Q: Return  P: Quit")
            key = msvcrt.getch().decode('utf-8').lower()
            if key == 'p':
                self.is_running = False
                break
            elif key == 'q':
                break
            elif key == 'w' and self.player.inventory:
                selected = (selected - 1) % len(self.player.inventory)
            elif key == 's' and self.player.inventory:
                selected = (selected + 1) % len(self.player.inventory)
            elif key == 'd' and self.player.inventory:
                mode = 'drop' if mode == 'normal' else 'normal'
            elif key == 'f' and self.player.inventory:
                if mode == 'drop':
                    success, message = self.player.drop_item(selected)
                    print(f"\n{message}")
                    print("Press any key to continue...")
                    msvcrt.getch()
                    if selected >= len(self.player.inventory):
                        selected = max(0, len(self.player.inventory) - 1)
                    mode = 'normal'
                else:
                    result = self.player.use_item_from_inventory(selected)
                    print(f"\n{result}")
                    print("Press any key to continue...")
                    msvcrt.getch()
                    if selected >= len(self.player.inventory):
                        selected = max(0, len(self.player.inventory) - 1)

    def show_spells(self):
        """Display and cast spells (for casters) or skills (for non-casters)"""
        if self.player is None:
            return
            
        os.system('cls')
        print("=" * 60)
        if self.player.is_caster():
            print("                                SPELLS")
            print("=" * 60)
            
            learned_spells = self.player.get_learned_spells()
            if not learned_spells:
                print("\nYou haven't learned any spells yet!")
                print("Spells are unlocked as you level up.")
            else:
                for spell_key, spell_data in learned_spells.items():
                    can_cast = self.player.mana >= spell_data['mana_cost']
                    status = "✓" if can_cast else "✗"
                    print(f"{spell_key.upper()}: {spell_data['name']} ({spell_data['mana_cost']} MP) {status}")
                    print(f"   {spell_data['description']}")
                    print()
            
            # Show upcoming spells
            print("Upcoming spells:")
            for level, level_spells in self.player.available_spells.items():
                if level > self.player.level:
                    for spell_key, spell_data in level_spells.items():
                        print(f"   Level {level}: {spell_data['name']} - {spell_data['description']}")
        else:
            print("                                SKILLS")
            print("=" * 60)
            
            learned_skills = self.player.get_learned_skills()
            if not learned_skills:
                print("\nYou haven't learned any skills yet!")
                print("Skills are unlocked as you level up.")
            else:
                for skill_key, skill_data in learned_skills.items():
                    print(f"{skill_key.upper()}: {skill_data['name']}")
                    print(f"   {skill_data['description']}")
                    print()
            
            # Show upcoming skills
            print("Upcoming skills:")
            for level, level_skills in self.player.available_skills.items():
                if level > self.player.level:
                    for skill_key, skill_data in level_skills.items():
                        print(f"   Level {level}: {skill_data['name']} - {skill_data['description']}")
        
        print("\nControls:")
        if self.player.is_caster():
            learned_spells = self.player.get_learned_spells()
            if learned_spells:
                spell_keys = list(learned_spells.keys())
                for spell_key in spell_keys:
                    print(f"{spell_key.upper()}: Cast {learned_spells[spell_key]['name']}")
        else:
            learned_skills = self.player.get_learned_skills()
            if learned_skills:
                skill_keys = list(learned_skills.keys())
                for skill_key in skill_keys:
                    print(f"{skill_key.upper()}: Use {learned_skills[skill_key]['name']}")
        print("Q: Return  P: Quit")
        
        while True:
            key = msvcrt.getch().decode('utf-8').lower()
            if key == 'p':
                self.is_running = False
                break
            elif key == 'q':
                break
            elif self.player.is_caster():
                learned_spells = self.player.get_learned_spells()
                if key in learned_spells:
                    spell_data = learned_spells[key]
                    if self.player.mana >= spell_data['mana_cost']:
                        if 'heal' in spell_data:
                            self.player.heal(spell_data['heal'])
                            print(f"\nYou cast {spell_data['name']} and restored {spell_data['heal']} HP!")
                        else:
                            print(f"\nYou cast {spell_data['name']}!")
                    else:
                        print("\nNot enough mana!")
                    print("Press any key to continue...")
                    msvcrt.getch()
                    break
            else:
                learned_skills = self.player.get_learned_skills()
                if key in learned_skills:
                    print(f"\nYou prepare to use {learned_skills[key]['name']}!")
                    print("Press any key to continue...")
                    msvcrt.getch()
                    break

    def get_combat_spell_or_skill(self):
        """Get spell or skill selection during combat"""
        if self.player is None:
            return None
            
        if self.player.is_caster():
            learned_spells = self.player.get_learned_spells()
            if not learned_spells:
                return None
                
            os.system('cls')
            print("=" * 60)
            print("                            CAST SPELL")
            print("=" * 60)
            print()
            print(f"Your MP: {self.player.mana}/{self.player.max_mana}")
            print()
            
            for spell_key, spell_data in learned_spells.items():
                can_cast = self.player.mana >= spell_data['mana_cost']
                status = "✓" if can_cast else "✗"
                print(f"{spell_key.upper()}: {spell_data['name']} ({spell_data['mana_cost']} MP) {status}")
                print(f"   {spell_data['description']}")
                print()
            
            print("Controls:")
            spell_keys = list(learned_spells.keys())
            for spell_key in spell_keys:
                print(f"{spell_key.upper()}: {learned_spells[spell_key]['name']}")
            print("Q: Cancel")
            
            while True:
                key = msvcrt.getch().decode('utf-8').lower()
                if key == 'p':
                    self.is_running = False
                    return None
                elif key == 'q':
                    return None
                elif key in learned_spells:
                    return ('spell', key)
        else:
            learned_skills = self.player.get_learned_skills()
            if not learned_skills:
                return None
                
            os.system('cls')
            print("=" * 60)
            print("                            USE SKILL")
            print("=" * 60)
            print()
            print(f"Your HP: {self.player.hp}/{self.player.max_hp}")
            print()
            
            for skill_key, skill_data in learned_skills.items():
                print(f"{skill_key.upper()}: {skill_data['name']}")
                print(f"   {skill_data['description']}")
                print()
            
            print("Controls:")
            skill_keys = list(learned_skills.keys())
            for skill_key in skill_keys:
                print(f"{skill_key.upper()}: {learned_skills[skill_key]['name']}")
            print("Q: Cancel")
            
            while True:
                key = msvcrt.getch().decode('utf-8').lower()
                if key == 'p':
                    self.is_running = False
                    return None
                elif key == 'q':
                    return None
                elif key in learned_skills:
                    return ('skill', key)

    def get_monster_type(self, monster):
        """Get monster type for ASCII art"""
        if monster.name.lower() == 'goblin':
            return 'goblin'
        elif monster.name.lower() == 'orc':
            return 'orc'
        elif monster.name.lower() == 'troll':
            return 'troll'
        else:
            return 'monster'

    def display_combat_screen(self, monster, log, player_pose='idle', monster_pose='idle'):
        """Display the combat screen with ASCII art"""
        if self.player is None:
            return
            

            
        os.system('cls')
        
        # Get monster type for art
        monster_type = self.get_monster_type(monster)
        
        # Display combat interface
        print("=" * 80)
        print("                                    COMBAT")
        print("=" * 80)
        print()
        
        # Player and monster ASCII art side by side
        player_art = get_combat_art('player', player_pose) or ''
        monster_art = get_combat_art(monster_type, monster_pose) or ''
        
        player_lines = player_art.split('\n')
        monster_lines = monster_art.split('\n')
        
        # Display them side by side with more spacing
        max_lines = max(len(player_lines), len(monster_lines))
        for i in range(max_lines):
            player_line = player_lines[i] if i < len(player_lines) else ""
            monster_line = monster_lines[i] if i < len(monster_lines) else ""
            print(f"{player_line:<40} {monster_line}")
        
        print()
        print("-" * 80)
        print(f"Your HP: {self.player.hp}/{self.player.max_hp} | MP: {self.player.mana}/{self.player.max_mana}")
        print(f"{monster.name} HP: {monster.hp}/{monster.max_hp}")
        print()
        print("Battle Log:")
        for entry in log[-3:]:
            print(f"  {entry}")
        print()
        print("Choose action: [A]ttack  [H]eal  [R]un  [X]pell")
        print("(Press A/Enter to attack, H to heal, R to run, X for " + ("spells" if self.player.is_caster() else "skills") + ")")

    def combat_round(self, player, monster, action, log):
        if player is None:
            return None, log
            
        # Player's turn
        if action == 'a':
            # Show attack animation
            self.display_combat_screen(monster, log, 'attack', 'idle')
            time.sleep(0.5)
            
            damage_to_monster = max(1, player.attack - monster.defense)
            monster.take_damage(damage_to_monster)
            log.append(f"You hit {monster.name} for {damage_to_monster} damage!")
            
            # Show monster hurt animation
            self.display_combat_screen(monster, log, 'idle', 'hurt')
            time.sleep(0.5)
            
            if not monster.is_alive():
                log.append(f"You defeated the {monster.name}!")
                player.gain_exp(monster.exp_value)
                log.append(f"Gained {monster.exp_value} experience points!")
                
                # Show search message and loot
                self.display_combat_screen(monster, log, 'idle', 'hurt')
                print(f"\nYou search the {monster.name}'s remains...")
                time.sleep(1.0)
                
                # Generate loot
                loot = monster.get_loot()
                if loot:
                    print("You found:")
                    for item_tuple in loot:
                        item_type, quantity = item_tuple
                        # Create proper Item object from tuple
                        if item_type == 'gold':
                            item = Item(monster.x, monster.y, '$', 'Gold Coins', {'gold': quantity}, 'gold', quantity, 0.01)
                        elif item_type == 'health_potion':
                            item = Item(monster.x, monster.y, '!', 'Health Potion', {'heal': 15}, 'potion', quantity, 0.5)
                        elif item_type == 'mana_potion':
                            item = Item(monster.x, monster.y, '~', 'Mana Potion', {'mana': 20}, 'potion', quantity, 0.5)
                        elif item_type == 'sword':
                            item = Item(monster.x, monster.y, 'S', 'Steel Sword', {'attack': 5}, 'weapon', quantity, 3.0)
                        elif item_type == 'armor':
                            item = Item(monster.x, monster.y, 'A', 'Leather Armor', {'defense': 2}, 'armor', quantity, 8.0)
                        else:
                            continue  # Skip unknown item types
                        
                        success, message = player.add_to_inventory(item)
                        if success:
                            print(f"  - {item.name}")
                        else:
                            print(f"  - {item.name} (couldn't carry: {message})")
                else:
                    print("  Nothing of value.")
                
                print("\nPress any key to continue...")
                msvcrt.getch()
                
                if player.level > 1:
                    log.append(f"Level up! You are now level {player.level}!")
                return True, log
        elif action == 'h':
            if player.hp < player.max_hp:
                player.heal(5)
                log.append("You heal yourself for 5 HP!")
            else:
                log.append("You are already at full health!")
        elif action == 'x':
            # Cast spell or use skill
            result = self.get_combat_spell_or_skill()
            if result:
                action_type, key = result
                if action_type == 'spell':
                    learned_spells = player.get_learned_spells()
                    spell_data = learned_spells[key]
                    if player.mana >= spell_data['mana_cost']:
                        player.use_mana(spell_data['mana_cost'])
                        
                        if 'damage' in spell_data:
                            spell_damage = spell_data['damage']
                            monster.take_damage(spell_damage)
                            log.append(f"You cast {spell_data['name']} for {spell_damage} damage!")
                            if not monster.is_alive():
                                log.append(f"You defeated the {monster.name}!")
                                player.gain_exp(monster.exp_value)
                                log.append(f"Gained {monster.exp_value} experience points!")
                                return True, log
                        elif 'heal' in spell_data:
                            player.heal(spell_data['heal'])
                            log.append(f"You cast {spell_data['name']} and restored {spell_data['heal']} HP!")
                    else:
                        log.append("Not enough mana!")
                else: # action_type == 'skill'
                    learned_skills = player.get_learned_skills()
                    skill_data = learned_skills[key]
                    
                    # Apply skill effects
                    damage_dealt = 0
                    if 'damage' in skill_data:
                        damage_dealt = skill_data['damage']
                        monster.take_damage(damage_dealt)
                        log.append(f"You use {skill_data['name']} and deal {damage_dealt} damage!")
                    
                    # Handle special skill effects
                    if 'stun' in skill_data and skill_data['stun']:
                        # Stun effect (skip monster's next turn)
                        monster.stunned = True
                        log.append(f"The monster is stunned!")
                    
                    if 'self_heal' in skill_data:
                        heal_amount = skill_data['self_heal']
                        player.heal(heal_amount)
                        log.append(f"You heal {heal_amount} HP!")
                    
                    if 'dodge' in skill_data and skill_data['dodge']:
                        # Dodge effect (next attack will be dodged)
                        player.dodging = True
                        log.append(f"You prepare to dodge the next attack!")
                    
                    if 'poison' in skill_data:
                        poison_damage = skill_data['poison']
                        monster.poisoned = True
                        monster.poison_damage = poison_damage
                        log.append(f"The monster is poisoned!")
                    
                    if damage_dealt == 0 and not any(key in skill_data for key in ['stun', 'self_heal', 'dodge', 'poison']):
                        log.append(f"You use {skill_data['name']}!")
            else:
                log.append("You decide not to cast a spell or use a skill.")
        elif action == 'r':
            import random
            if random.random() < 0.5:
                log.append("You successfully ran away!")
                return 'run', log
            else:
                log.append("You failed to run away!")
        
        # Monster's turn
        if monster.is_alive():
            # Apply poison damage if monster is poisoned
            if monster.poisoned and monster.poison_damage > 0:
                monster.take_damage(monster.poison_damage)
                log.append(f"The monster takes {monster.poison_damage} poison damage!")
                monster.poison_damage -= 1
                if monster.poison_damage <= 0:
                    monster.poisoned = False
                    log.append("The poison wears off!")
            
            # Check if monster is stunned
            if monster.stunned:
                log.append("The monster is stunned and cannot attack!")
                monster.stunned = False
            else:
                # Check if player is dodging
                if player.dodging:
                    import random
                    if random.random() < 0.7:  # 70% chance to dodge
                        log.append("You successfully dodge the attack!")
                        player.dodging = False
                    else:
                        log.append("You fail to dodge the attack!")
                        player.dodging = False
                        # Calculate damage
                        damage = max(1, monster.attack - player.defense)
                        player.take_damage(damage)
                        log.append(f"The monster attacks for {damage} damage!")
                else:
                    # Normal attack
                    damage = max(1, monster.attack - player.defense)
                    player.take_damage(damage)
                    log.append(f"The monster attacks for {damage} damage!")
        
        if player.hp <= 0:
            log.append("You have been defeated!")
            return False, log
        return None, log

    def handle_combat(self, monster, monster_first=False):
        if self.player is None:
            return
        log = [f"You encounter a {monster.name}! ({monster.hp} HP, ATK {monster.attack}, DEF {monster.defense})"]
        if monster_first:
            # Monster gets first attack
            damage_to_player = max(1, monster.attack - self.player.defense)
            self.player.take_damage(damage_to_player)
            log.append(f"{monster.name} ambushes you for {damage_to_player} damage!")
            if self.player.hp <= 0:
                log.append("You have been defeated!")
                self.display_combat_screen(monster, log)
                self.is_running = False
                self.show_game_over()
                return
        while monster.is_alive() and self.player.hp > 0:
            self.display_combat_screen(monster, log)
            action = self.get_combat_action()
            result, log = self.combat_round(self.player, monster, action, log)
            if result == True:
                self.dungeon.remove_monster(monster)
                break
            elif result == False:
                self.is_running = False
                self.show_game_over()
                return
            elif result == 'run':
                print("\nYou escaped the fight!")
                print("Press any key to continue...")
                msvcrt.getch()
                break

    def get_combat_action(self):
        actions = [('Attack', 'a'), ('Heal', 'h'), ('Run', 'r')]
        # Add spell/skill if available
        if self.player:
            if self.player.is_caster():
                learned_spells = self.player.get_learned_spells()
                can_cast_any = any(self.player.mana >= spell_data['mana_cost'] for spell_data in learned_spells.values()) if learned_spells else False
                if learned_spells and can_cast_any:
                    actions.append(('Cast Spell', 'x'))
            else:
                learned_skills = self.player.get_learned_skills()
                if learned_skills:
                    actions.append(('Use Skill', 'x'))
        selected = 0
        while True:
            # Show action selection overlay
            print("\n" + "=" * 60)
            print("Choose your action:")
            for i, (label, _) in enumerate(actions):
                arrow = '→' if i == selected else ' '
                print(f"{arrow} {label}")
            print("\nControls: W/S = Move, F = Confirm, Q = Cancel")
            print("=" * 60)
            
            key = msvcrt.getch().decode('utf-8').lower()
            if key == 'p':
                self.is_running = False
                return None
            elif key == 'q':
                return None
            elif key == 'w':
                selected = (selected - 1) % len(actions)
                # Clear screen and redraw
                os.system('cls')
            elif key == 's':
                selected = (selected + 1) % len(actions)
                # Clear screen and redraw
                os.system('cls')
            elif key == 'f':
                return actions[selected][1]

    def handle_input(self):
        if self.player is None:
            return
            
        # Clear any buffered input to prevent combat keys from affecting movement
        while msvcrt.kbhit():
            msvcrt.getch()
            
        key = msvcrt.getch().decode('utf-8').lower()
        if key == 'p':
            self.is_running = False
            return
        elif key == 'i':
            self.show_inventory()
            return
        elif key == 'x':
            self.show_spells()
            return
        
        new_x, new_y = self.player.x, self.player.y
        dx, dy = 0, 0
        if key == 'w':
            new_y -= 1
            dy = -1
        elif key == 's':
            new_y += 1
            dy = 1
        elif key == 'a':
            new_x -= 1
            dx = -1
        elif key == 'd':
            new_x += 1
            dx = 1
        else:
            dx, dy = 0, 0
        self.last_move = (dx, dy)
        if (0 <= new_x < self.dungeon.width and
            0 <= new_y < self.dungeon.height and
            self.dungeon.map[new_y][new_x] != '#'):
            
            # Check for stairs
            if self.dungeon.is_stairs_at(new_x, new_y):
                print("\nYou descend to the next level...")
                print("Press any key to continue...")
                msvcrt.getch()
                self.player.x = 1
                self.player.y = 1
                self.dungeon.next_level()
                return
            
            # Check for chest
            chest = self.dungeon.get_chest_at(new_x, new_y)
            if chest:
                loot = chest.open()
                print(f"\nYou opened a treasure chest!")
                if loot:
                    for item in loot:
                        success, message = self.player.add_to_inventory(item)
                        if success:
                            print(f"Found {item.name}!")
                        else:
                            print(f"Couldn't carry {item.name}: {message}")
                else:
                    print("The chest was empty!")
                print("Press any key to continue...")
                msvcrt.getch()
                # Remove chest from the list so it disappears
                self.dungeon.chests.remove(chest)
                return
            
            # Check for monster
            monster = self.dungeon.get_monster_at(new_x, new_y)
            if monster:
                self.handle_combat(monster)
            else:
                self.player.x = new_x
                self.player.y = new_y
                # Move monsters after player moves
                self.monster_move_and_check_initiate()

    def monster_move_and_check_initiate(self):
        if self.player is None:
            return
        # Move monsters and check if any try to enter the player's square
        player_pos = (self.player.x, self.player.y)
        last_dx, last_dy = self.last_move
        attempted_attacks = []
        
        # Use the dungeon's move_monsters method which handles line of sight and move timing
        self.dungeon.move_monsters(player_pos, self.last_move)
        
        # Check if any monsters are now adjacent to the player and can attack
        for monster in self.dungeon.monsters:
            if not monster.is_alive():
                continue
            # Check if monster is adjacent to player
            dx = abs(monster.x - player_pos[0])
            dy = abs(monster.y - player_pos[1])
            if (dx <= 1 and dy <= 1) and (dx + dy > 0):  # Adjacent but not on same square
                # Determine if player moved away, sideways, or not
                # Opposite direction: player moved away from monster
                if (last_dx, last_dy) == (-(monster.x - player_pos[0]), -(monster.y - player_pos[1])):
                    continue  # Player dodged by moving away
                # Sideways: allow attack
                attempted_attacks.append(monster)
        
        # If any monster attempted to attack, initiate combat (monster first)
        for monster in attempted_attacks:
            self.handle_combat(monster, monster_first=True) 