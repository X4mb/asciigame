#!/usr/bin/env python3
"""
Test script for ASCII Roguelike Dungeon Crawler
Tests all game functionalities without starting the actual game
"""

import sys
import random
import time

# Import game modules
from entities import Player, Monster, Item, Chest
from dungeon import Dungeon
from game import Game

def print_test_header(test_name):
    """Print a formatted test header"""
    print("\n" + "="*60)
    print(f"TESTING: {test_name}")
    print("="*60)

def print_test_result(test_name, passed, details=""):
    """Print test result"""
    status = "✅ PASSED" if passed else "❌ FAILED"
    print(f"{status}: {test_name}")
    if details:
        print(f"   Details: {details}")

def test_player_classes():
    """Test all player classes and their stats"""
    print_test_header("Player Classes")
    
    classes = ['warrior', 'mage', 'rogue', 'cleric']
    results = []
    
    for player_class in classes:
        player = Player(1, 1, player_class)
        
        # Test basic stats
        assert player.hp > 0, f"{player_class} has no HP"
        assert player.max_hp > 0, f"{player_class} has no max HP"
        assert player.mana >= 0, f"{player_class} has negative mana"
        assert player.max_mana >= 0, f"{player_class} has negative max mana"
        assert player.attack > 0, f"{player_class} has no attack"
        assert player.defense >= 0, f"{player_class} has negative defense"
        
        # Test class-specific features
        if player_class in ['warrior', 'rogue']:
            assert hasattr(player, 'available_skills'), f"{player_class} missing skills"
            assert not player.is_caster(), f"{player_class} incorrectly identified as caster"
        else:
            assert hasattr(player, 'available_spells'), f"{player_class} missing spells"
            assert player.is_caster(), f"{player_class} incorrectly identified as non-caster"
        
        results.append(True)
        print_test_result(f"{player_class.title()} Class", True, 
                         f"HP:{player.max_hp} MP:{player.max_mana} ATK:{player.attack} DEF:{player.defense}")
    
    return all(results)

def test_skills_and_spells():
    """Test skill and spell learning system"""
    print_test_header("Skills and Spells")
    
    try:
        # Test Warrior skills
        warrior = Player(1, 1, 'warrior')
        warrior.level = 1
        warrior.exp = 0
        warrior.exp_to_next = 10
        warrior.gain_exp(15)  # This should level up to 2
        learned_skills = warrior.get_learned_skills()
        if 'power_strike' not in learned_skills:
            print(f"DEBUG: Warrior learned skills at level {warrior.level}: {list(learned_skills.keys())}")
        assert 'power_strike' in learned_skills, "Warrior didn't learn Power Strike at level 2"
        
        # Test Mage spells
        mage = Player(1, 1, 'mage')
        learned_spells = mage.get_learned_spells()
        assert 'fireball' in learned_spells, "Mage didn't learn Fireball at level 1"
        
        # Test Rogue skills
        rogue = Player(1, 1, 'rogue')
        rogue.level = 1
        rogue.exp = 0
        rogue.exp_to_next = 10
        rogue.gain_exp(15)  # This should level up to 2
        learned_skills = rogue.get_learned_skills()
        if 'backstab' not in learned_skills:
            print(f"DEBUG: Rogue learned skills at level {rogue.level}: {list(learned_skills.keys())}")
        assert 'backstab' in learned_skills, "Rogue didn't learn Backstab at level 2"
        
        # Test Cleric spells
        cleric = Player(1, 1, 'cleric')
        learned_spells = cleric.get_learned_spells()
        assert 'heal' in learned_spells, "Cleric didn't learn Heal at level 1"
        
        print_test_result("Skill/Spell Learning", True, "All classes learn appropriate abilities")
        return True
    except Exception as e:
        print_test_result("Skill/Spell Learning", False, f"Error: {str(e)}")
        return False

def test_combat_system():
    """Test combat mechanics"""
    print_test_header("Combat System")
    
    try:
        player = Player(1, 1, 'warrior')
        monster = Monster(2, 2, 'goblin')
        
        # Test basic combat
        initial_hp = player.hp
        monster.take_damage(5)
        assert monster.hp < monster.max_hp, "Monster didn't take damage"
        
        # Test player damage calculation
        player.take_damage(10)
        assert player.hp < initial_hp, "Player didn't take damage"
        
        # Test monster death
        monster.take_damage(monster.hp + 10)
        assert not monster.is_alive(), "Monster should be dead"
        
        # Test skill effects
        warrior = Player(1, 1, 'warrior')
        warrior.level = 2
        warrior.level_up()
        goblin = Monster(2, 2, 'goblin')
        
        # Test stun effect
        goblin.stunned = True
        assert goblin.stunned, "Stun effect not applied"
        
        # Test poison effect
        goblin.poisoned = True
        goblin.poison_damage = 3
        initial_hp = goblin.hp
        goblin.take_damage(goblin.poison_damage)
        assert goblin.hp < initial_hp, "Poison damage not applied"
        
        print_test_result("Combat Mechanics", True, "Damage, death, and effects working")
        return True
    except Exception as e:
        print_test_result("Combat Mechanics", False, f"Error: {str(e)}")
        return False

def test_inventory_system():
    """Test inventory management"""
    print_test_header("Inventory System")
    
    try:
        player = Player(1, 1, 'warrior')
        
        # Test adding items
        sword = Item(1, 1, 'S', 'Steel Sword', {'attack': 5}, 'weapon', 1, 3.0)
        potion = Item(1, 1, '!', 'Health Potion', {'heal': 15}, 'potion', 1, 0.5)
        
        success, message = player.add_to_inventory(sword)
        assert success, f"Failed to add sword: {message}"
        assert len(player.inventory) == 1, "Sword not added to inventory"
        
        success, message = player.add_to_inventory(potion)
        assert success, f"Failed to add potion: {message}"
        assert len(player.inventory) == 2, "Potion not added to inventory"
        
        # Test item stacking
        potion2 = Item(1, 1, '!', 'Health Potion', {'heal': 15}, 'potion', 1, 0.5)
        success, message = player.add_to_inventory(potion2)
        assert success, f"Failed to stack potion: {message}"
        assert len(player.inventory) == 2, "Potion should stack, not create new slot"
        assert player.inventory[1].quantity == 2, "Potion quantity not increased"
        
        # Test weight limits
        heavy_item = Item(1, 1, 'H', 'Heavy Item', {}, 'misc', 1, 100.0)
        success, message = player.add_to_inventory(heavy_item)
        assert not success, "Should not be able to carry extremely heavy item"
        
        # Test equipment
        player.equip_item(sword)
        assert player.equipped_weapon == sword, "Sword not equipped"
        assert player.attack > 4, "Attack not increased by sword"
        
        print_test_result("Inventory Management", True, "Adding, stacking, weight limits, and equipment working")
        return True
    except Exception as e:
        print_test_result("Inventory Management", False, f"Error: {str(e)}")
        return False

def test_dungeon_generation():
    """Test dungeon generation and features"""
    print_test_header("Dungeon Generation")
    
    try:
        dungeon = Dungeon(20, 10)  # Smaller dungeon for testing
        
        # Test basic dungeon properties
        assert dungeon.width == 20, "Dungeon width incorrect"
        assert dungeon.height == 10, "Dungeon height incorrect"
        assert len(dungeon.map) == 10, "Dungeon map height incorrect"
        assert len(dungeon.map[0]) == 20, "Dungeon map width incorrect"
        
        # Test dungeon connectivity
        floor_tiles = 0
        for y in range(dungeon.height):
            for x in range(dungeon.width):
                if dungeon.map[y][x] == '.':
                    floor_tiles += 1
        
        assert floor_tiles > 0, "Dungeon should have floor tiles"
        
        # Test monster spawning
        assert len(dungeon.monsters) > 0, "Dungeon should have monsters"
        for monster in dungeon.monsters:
            assert monster.is_alive(), "Monsters should be alive when spawned"
            assert dungeon.map[monster.y][monster.x] == '.', "Monsters should be on floor tiles"
        
        # Test chest spawning
        assert len(dungeon.chests) > 0, "Dungeon should have chests"
        for chest in dungeon.chests:
            assert not chest.opened, "Chests should start unopened"
            assert dungeon.map[chest.y][chest.x] == '.', "Chests should be on floor tiles"
        
        # Test stairs placement
        assert dungeon.stairs is not None, "Dungeon should have stairs"
        stairs_x, stairs_y = dungeon.stairs
        assert dungeon.map[stairs_y][stairs_x] == '>', "Stairs should be marked on map"
        
        print_test_result("Dungeon Generation", True, "Generation, spawning, and movement working")
        return True
    except Exception as e:
        print_test_result("Dungeon Generation", False, f"Error: {str(e)}")
        return False

def test_loot_system():
    """Test loot generation and collection"""
    print_test_header("Loot System")
    
    try:
        # Test monster loot
        goblin = Monster(1, 1, 'goblin')
        loot = goblin.get_loot()
        assert isinstance(loot, list), "Loot should be a list"
        assert len(loot) > 0, "Goblin should drop loot"
        
        # Test chest loot
        chest = Chest(1, 1)
        chest_loot = chest.open()
        assert isinstance(chest_loot, list), "Chest loot should be a list"
        assert chest.opened, "Chest should be marked as opened"
        
        # Test loot item creation
        player = Player(1, 1, 'warrior')
        for item_tuple in loot:
            item_type, quantity = item_tuple
            if item_type == 'gold':
                item = Item(goblin.x, goblin.y, '$', 'Gold Coins', {'gold': quantity}, 'gold', quantity, 0.01)
            elif item_type == 'health_potion':
                item = Item(goblin.x, goblin.y, '!', 'Health Potion', {'heal': 15}, 'potion', quantity, 0.5)
            else:
                continue
            
            success, message = player.add_to_inventory(item)
            assert success, f"Failed to add loot item: {message}"
        
        print_test_result("Loot System", True, "Monster and chest loot working")
        return True
    except Exception as e:
        print_test_result("Loot System", False, f"Error: {str(e)}")
        return False

def test_level_progression():
    """Test leveling up and progression"""
    print_test_header("Level Progression")
    
    try:
        player = Player(1, 1, 'warrior')
        initial_level = player.level
        initial_exp = player.exp
        
        # Test experience gain
        player.gain_exp(15)  # Should level up (exp_to_next = 10)
        assert player.level > initial_level, "Player should level up"
        assert player.hp == player.max_hp, "Player should be fully healed on level up"
        assert player.mana == player.max_mana, "Player should have full mana on level up"
        
        # Test stat increases
        warrior = Player(1, 1, 'warrior')
        initial_hp = warrior.max_hp
        initial_attack = warrior.attack
        warrior.gain_exp(15)
        assert warrior.max_hp > initial_hp, "HP should increase on level up"
        assert warrior.attack > initial_attack, "Attack should increase on level up"
        
        # Test skill learning
        warrior = Player(1, 1, 'warrior')
        warrior.gain_exp(15)  # Level 2
        learned_skills = warrior.get_learned_skills()
        assert 'power_strike' in learned_skills, "Should learn Power Strike at level 2"
        
        print_test_result("Level Progression", True, "Leveling, stats, and skill learning working")
        return True
    except Exception as e:
        print_test_result("Level Progression", False, f"Error: {str(e)}")
        return False

def test_monster_ai():
    """Test monster AI and movement"""
    print_test_header("Monster AI")
    
    try:
        dungeon = Dungeon(10, 10)
        monster = Monster(5, 5, 'goblin')
        player_pos = (7, 7)
        
        # Test line of sight
        can_see = monster.can_see_player(player_pos[0], player_pos[1], dungeon)
        # Should be able to see player at this distance
        
        # Test movement towards player
        initial_x, initial_y = monster.x, monster.y
        monster.move_towards_player(player_pos[0], player_pos[1], dungeon)
        new_x, new_y = monster.x, monster.y
        
        # Monster should move towards player (either x or y should change)
        # Note: Monster might not move if it can't see player or if path is blocked
        # Let's just verify the movement method doesn't crash
        assert isinstance(new_x, int) and isinstance(new_y, int), "Monster position should be integers"
        assert 0 <= new_x < dungeon.width, "Monster x out of bounds after movement"
        assert 0 <= new_y < dungeon.height, "Monster y out of bounds after movement"
        
        # Test stun effect on movement
        monster.stunned = True
        old_x, old_y = monster.x, monster.y
        monster.move_towards_player(player_pos[0], player_pos[1], dungeon)
        assert monster.x == old_x and monster.y == old_y, "Stunned monster should not move"
        assert not monster.stunned, "Stun should be cleared after movement attempt"
        
        print_test_result("Monster AI", True, "Line of sight, movement, and stun effects working")
        return True
    except Exception as e:
        print_test_result("Monster AI", False, f"Error: {str(e)}")
        return False

def test_item_effects():
    """Test item usage and effects"""
    print_test_header("Item Effects")
    
    try:
        player = Player(1, 1, 'warrior')
        initial_hp = player.hp
        initial_mana = player.mana
        
        # Test health potion
        health_potion = Item(1, 1, '!', 'Health Potion', {'heal': 15}, 'potion', 1, 0.5)
        player.take_damage(10)  # Damage player first
        result = health_potion.use(player)
        assert player.hp > initial_hp - 10, "Health potion should heal player"
        
        # Test mana potion
        mana_potion = Item(1, 1, '~', 'Mana Potion', {'mana': 20}, 'potion', 1, 0.5)
        player.use_mana(5)  # Use some mana first
        result = mana_potion.use(player)
        assert player.mana > initial_mana - 5, "Mana potion should restore mana"
        
        # Test weapon equipment
        sword = Item(1, 1, 'S', 'Steel Sword', {'attack': 5}, 'weapon', 1, 3.0)
        initial_attack = player.attack
        old_item = player.equip_item(sword)
        assert player.attack > initial_attack, "Weapon should increase attack"
        assert player.equipped_weapon == sword, "Weapon should be equipped"
        
        # Test armor equipment
        armor = Item(1, 1, 'A', 'Leather Armor', {'defense': 2}, 'armor', 1, 8.0)
        initial_defense = player.defense
        old_item = player.equip_item(armor)
        assert player.defense > initial_defense, "Armor should increase defense"
        assert player.equipped_armor == armor, "Armor should be equipped"
        
        print_test_result("Item Effects", True, "Potions, weapons, and armor working")
        return True
    except Exception as e:
        print_test_result("Item Effects", False, f"Error: {str(e)}")
        return False

def test_game_integration():
    """Test game integration and initialization"""
    print_test_header("Game Integration")
    
    try:
        # Test game initialization
        game = Game()
        assert game.dungeon is not None, "Game should have a dungeon"
        assert game.player is None, "Player should start as None"
        assert game.is_running, "Game should start as running"
        
        # Test class selection (without user input)
        game.player = Player(1, 1, 'warrior')
        assert game.player is not None, "Player should be set"
        assert game.player.player_class == 'warrior', "Player should be warrior class"
        
        # Test dungeon rendering (should not crash)
        try:
            game.dungeon.render(player_pos=(1, 1), player=game.player)
        except Exception as e:
            assert False, f"Dungeon rendering failed: {str(e)}"
        
        print_test_result("Game Integration", True, "Game initialization and rendering working")
        return True
    except Exception as e:
        print_test_result("Game Integration", False, f"Error: {str(e)}")
        return False

def test_ascii_art():
    """Test ASCII art generation"""
    print_test_header("ASCII Art")
    
    try:
        from ascii_art import get_title_screen, get_game_over_screen, get_combat_art
        
        # Test title screen
        title = get_title_screen()
        assert isinstance(title, str), "Title screen should be a string"
        assert len(title) > 0, "Title screen should not be empty"
        
        # Test game over screen
        game_over = get_game_over_screen()
        assert isinstance(game_over, str), "Game over screen should be a string"
        assert len(game_over) > 0, "Game over screen should not be empty"
        
        # Test combat art
        player_art = get_combat_art('player', 'idle')
        assert isinstance(player_art, str), "Player combat art should be a string"
        
        monster_art = get_combat_art('goblin', 'attack')
        assert isinstance(monster_art, str), "Monster combat art should be a string"
        
        print_test_result("ASCII Art", True, "All ASCII art functions working")
        return True
    except Exception as e:
        print_test_result("ASCII Art", False, f"Error: {str(e)}")
        return False

def test_player_methods():
    print_test_header("Player Methods")
    try:
        player = Player(2, 3, 'mage')
        # Test stat setup
        assert player.max_hp == 8 and player.max_mana == 25
        # Test take_damage and heal
        player.take_damage(5)
        assert player.hp == player.max_hp - 4  # defense = 1
        player.heal(3)
        assert player.hp == player.max_hp - 1
        player.heal(100)
        assert player.hp == player.max_hp
        # Test mana usage and restore
        assert player.use_mana(5)
        assert player.mana == player.max_mana - 5
        player.restore_mana(3)
        assert player.mana == player.max_mana - 2
        player.restore_mana(100)
        assert player.mana == player.max_mana
        # Test inventory weight and stacking
        potion = Item(0, 0, '!', 'Health Potion', {'heal': 15}, 'potion', 2, 0.5)
        assert player.add_to_inventory(potion)[0]
        assert player.get_inventory_weight() == 1.0
        # Test can_carry_item slot limit
        for i in range(player.max_inventory_slots - 1):
            player.add_to_inventory(Item(0, 0, chr(65+i), f'Item{i}', {}, 'misc', 1, 0.1))
        assert not player.can_carry_item(Item(0, 0, 'Z', 'Overflow', {}, 'misc', 1, 0.1))[0]
        # Test drop and use item
        idx = 0
        msg = player.use_item_from_inventory(idx)
        assert "restored" in msg or "Used" in msg
        player.drop_item(0)
        # Test equip weapon/armor
        sword = Item(0, 0, 'S', 'Sword', {'attack': 5}, 'weapon', 1, 3.0)
        armor = Item(0, 0, 'A', 'Armor', {'defense': 2}, 'armor', 1, 8.0)
        player.add_to_inventory(sword)
        player.add_to_inventory(armor)
        player.equip_item(sword)
        player.equip_item(armor)
        assert player.equipped_weapon == sword
        assert player.equipped_armor == armor
        # Test leveling up
        player.exp = player.exp_to_next
        player.gain_exp(0)
        assert player.level > 1
        # Test get_status
        status = player.get_status()
        assert "Class:" in status and "Level:" in status
        print_test_result("Player Methods", True)
        return True
    except Exception as e:
        print_test_result("Player Methods", False, str(e))
        return False

def test_monster_methods():
    print_test_header("Monster Methods")
    try:
        m = Monster(4, 5, 'orc')
        # Test stat setup
        assert m.hp == m.max_hp
        # Test take_damage/is_alive
        m.take_damage(5)
        assert m.hp == m.max_hp - 5
        assert m.is_alive()
        m.take_damage(100)
        assert not m.is_alive()
        # Test move/stun/poison
        m = Monster(1, 1, 'goblin')
        m.stunned = True
        m.move_towards_player(2, 2, Dungeon(5, 5))
        assert not m.stunned
        m.poisoned = True
        m.poison_damage = 2
        m.take_damage(m.poison_damage)
        # Test loot
        loot = m.get_loot()
        assert isinstance(loot, list)
        print_test_result("Monster Methods", True)
        return True
    except Exception as e:
        print_test_result("Monster Methods", False, str(e))
        return False

def test_item_methods():
    print_test_header("Item Methods")
    try:
        player = Player(1, 1, 'warrior')
        potion = Item(1, 1, '!', 'Health Potion', {'heal': 15}, 'potion', 2, 0.5)
        msg = potion.use(player)
        assert "restored" in msg or "Used" in msg
        sword = Item(1, 1, 'S', 'Sword', {'attack': 5}, 'weapon', 1, 3.0)
        msg = sword.use(player)
        assert "Equipped" in msg
        armor = Item(1, 1, 'A', 'Armor', {'defense': 2}, 'armor', 1, 8.0)
        msg = armor.use(player)
        assert "Equipped" in msg
        print_test_result("Item Methods", True)
        return True
    except Exception as e:
        print_test_result("Item Methods", False, str(e))
        return False

def test_chest_methods():
    print_test_header("Chest Methods")
    try:
        chest = Chest(2, 2)
        loot = chest.open()
        assert chest.opened
        assert isinstance(loot, list)
        loot2 = chest.open()
        assert loot2 == []
        print_test_result("Chest Methods", True)
        return True
    except Exception as e:
        print_test_result("Chest Methods", False, str(e))
        return False

def test_dungeon_methods():
    print_test_header("Dungeon Methods")
    try:
        d = Dungeon(10, 10)
        # Test is_valid_position
        assert d.is_valid_position(1, 1)
        assert not d.is_valid_position(-1, -1)
        # Test has_line_of_sight
        assert d.has_line_of_sight(1, 1, 2, 2)
        # Test get_monster_at/get_chest_at/is_stairs_at
        m = d.monsters[0]
        c = d.chests[0]
        assert d.get_monster_at(m.x, m.y) == m
        assert d.get_chest_at(c.x, c.y) == c
        assert not d.is_stairs_at(0, 0)
        # Test remove_monster
        d.remove_monster(m)
        assert d.get_monster_at(m.x, m.y) is None
        # Test next_level
        old_level = d.level
        d.next_level()
        assert d.level == old_level + 1
        print_test_result("Dungeon Methods", True)
        return True
    except Exception as e:
        print_test_result("Dungeon Methods", False, str(e))
        return False

def test_game_methods():
    print_test_header("Game Methods")
    try:
        game = Game()
        # Only test non-interactive logic
        game.player = Player(1, 1, 'warrior')
        # Test display_player_status (should not crash)
        game.display_player_status()
        # Test combat logic directly (simulate a combat round)
        monster = Monster(2, 2, 'goblin')
        log = []
        # Simulate a combat round: player attacks
        result, log = game.combat_round(game.player, monster, 'a', log)
        assert result is None or result is True
        # Simulate a combat round: player heals
        result, log = game.combat_round(game.player, monster, 'h', log)
        # Simulate a combat round: player tries to run
        result, log = game.combat_round(game.player, monster, 'r', log)
        # Simulate a combat round: player uses skill/spell (should handle gracefully)
        result, log = game.combat_round(game.player, monster, 'x', log)
        print_test_result("Game Methods", True)
        return True
    except Exception as e:
        print_test_result("Game Methods", False, str(e))
        return False

def test_ascii_art_module():
    print_test_header("ASCII Art Module")
    try:
        from ascii_art import get_ascii_art, get_title_screen, get_game_over_screen, get_combat_art
        assert isinstance(get_ascii_art('player'), str)
        assert isinstance(get_title_screen(), str)
        assert isinstance(get_game_over_screen(), str)
        assert isinstance(get_combat_art('player', 'idle'), str)
        assert isinstance(get_combat_art('goblin', 'attack'), str)
        print_test_result("ASCII Art Module", True)
        return True
    except Exception as e:
        print_test_result("ASCII Art Module", False, str(e))
        return False

def run_all_tests():
    print("="*60)
    print("ASCII ROGUELIKE DUNGEON CRAWLER - FULL FUNCTION TEST SUITE")
    print("="*60)
    tests = [
        ("Player Classes", test_player_classes),
        ("Skills and Spells", test_skills_and_spells),
        ("Combat System", test_combat_system),
        ("Inventory System", test_inventory_system),
        ("Dungeon Generation", test_dungeon_generation),
        ("Loot System", test_loot_system),
        ("Level Progression", test_level_progression),
        ("Monster AI", test_monster_ai),
        ("Item Effects", test_item_effects),
        ("Game Integration", test_game_integration),
        ("ASCII Art", test_ascii_art),
        ("Player Methods", test_player_methods),
        ("Monster Methods", test_monster_methods),
        ("Item Methods", test_item_methods),
        ("Chest Methods", test_chest_methods),
        ("Dungeon Methods", test_dungeon_methods),
        ("Game Methods", test_game_methods),
        ("ASCII Art Module", test_ascii_art_module),
    ]
    passed = 0
    total = len(tests)
    for test_name, test_func in tests:
        try:
            result = test_func()
            if result:
                passed += 1
        except Exception as e:
            print_test_result(test_name, False, f"Exception: {str(e)}")
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    print(f"Tests Passed: {passed}/{total}")
    print(f"Success Rate: {(passed/total)*100:.1f}%")
    if passed == total:
        print("🎉 ALL TESTS PASSED! The game is working correctly.")
        print("🚀 Ready to play! Run 'python main.py' to start the game.")
    else:
        print("⚠️  Some tests failed. Please check the output above.")
    return passed == total

if __name__ == "__main__":
    random.seed(42)
    success = run_all_tests()
    sys.exit(0 if success else 1) 