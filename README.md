# ASCII Roguelike Dungeon Crawler

A classic roguelike dungeon crawler game built entirely in Python with ASCII graphics. Explore truly unique, procedurally generated dungeons, battle monsters (including bosses), collect loot, and level up your character across multiple classes.

![Game Screenshot](https://img.shields.io/badge/Game-ASCII%20Roguelike-blue)
![Python](https://img.shields.io/badge/Python-3.6+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🎮 Features

### Character Classes
- **Warrior**: High HP, strong melee combat with skills like Power Strike, Shield Bash, and Battle Rage
- **Mage**: Powerful spellcaster with Fireball, Lightning, Ice Storm, and Meteor spells
- **Rogue**: Stealthy fighter with Backstab, Evasion, Poison Strike, and a passive dodge ability
- **Cleric**: Support class with healing spells and divine magic (Heal, Smite, Divine Protection, Resurrection)

### Game Mechanics
- **Procedural Dungeon Generation**: Each level is generated randomly every time—no two runs are ever the same
- **Turn-based Combat**: Strategic battles with attacks, healing, running, skills, and spells
- **Inventory System**: Weight-based inventory with item stacking, equipment, and drop/use modes
- **Level Progression**: Gain experience, level up, and unlock new abilities for your class
- **Monster AI**: Enemies pursue the player with line-of-sight detection and pathfinding
- **Loot System**: Treasure chests and monster drops with weapons, armor, potions, gold, and more
- **Bosses**: Face the Dragon and other powerful foes with unique stats and loot

### Visual Features
- **ASCII Graphics**: Classic roguelike visuals with detailed combat and spell/skill animations
- **Dynamic UI**: Real-time status display, potion counters, and interactive menus
- **Combat Animations**: Visual feedback for attacks, spells, skills, and special effects

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- Windows (uses `msvcrt` for input handling)

### Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/ascii-roguelike.git
cd ascii-roguelike
```

2. Run the game:
```bash
python main.py
```

### Running Tests
The test suite is fully automated and non-interactive. It covers all game mechanics and disables all prompts during testing.
```bash
python test_game.py
```

## 🎯 How to Play

### Controls
- **W/A/S/D**: Move character
- **I**: Open inventory
- **X**: Access spells/skills
- **P**: Quit game

### Combat Controls
- **A**: Attack
- **H**: Heal (restores 5 HP or uses a potion if available)
- **R**: Attempt to run away
- **X**: Cast spell or use skill (if available)

### Inventory Management
- **W/S**: Navigate items
- **F**: Use/equip item
- **D**: Toggle drop mode
- **Q**: Return to game

## 🏗️ Project Structure

```
asciigame/
├── main.py              # Entry point
├── game.py              # Main game logic and UI
├── dungeon.py           # Dungeon generation and management
├── entities.py          # Player, monsters, items, and chests
├── ascii_art.py         # ASCII graphics and animations
├── test_game.py         # Comprehensive, non-interactive test suite
└── LICENSE              # MIT License
```

## 🎲 Game Systems

### Character Progression
Each class has unique progression paths:
- **Warrior**: Gains HP and attack power, learns combat skills
- **Mage**: Gains mana and learns powerful offensive spells
- **Rogue**: Gains HP and learns stealth/agility skills, with a passive dodge
- **Cleric**: Gains HP and mana, learns healing and divine spells

### Combat System
- Turn-based combat with multiple action options
- Damage calculation based on attack vs defense
- Special effects: stun, poison, dodge, healing
- Monster AI with line-of-sight detection and pursuit
- Boss monsters (e.g., Dragon) with unique stats and loot

### Dungeon Generation
- Procedural generation using cellular automata
- Dungeons are always unique—never cached or repeated
- Scaled difficulty with level progression
- Connected rooms and corridors
- Strategic placement of monsters, chests, and stairs

### Inventory & Items
- Weight-based carrying system
- Item stacking for consumables
- Equipment system for weapons and armor
- Various item types: weapons, armor, potions, gold, scrolls

## 🧪 Testing

The project includes a comprehensive, fully automated test suite covering:
- Character class functionality
- Combat mechanics (including skills, spells, and boss fights)
- Inventory management
- Dungeon generation (uniqueness and functionality)
- Loot systems
- Level progression
- Monster AI behavior
- UI and animation methods

**Test mode disables all interactive prompts.**

Run tests with:
```bash
python test_game.py
```

## 🛠️ Development

### Adding New Features
1. **New Character Classes**: Extend the `Player` class in `entities.py`
2. **New Monsters**: Add monster types to the `Monster` class
3. **New Items**: Create new item types in the `Item` class
4. **New Spells/Skills**: Add to the respective class definitions

### Code Style
- Follow Python PEP 8 conventions
- Add docstrings for all functions and classes
- Include comprehensive tests for new features

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📊 Game Statistics

- **Lines of Code**: ~2,000+
- **Character Classes**: 4
- **Monster Types**: 4 (Goblin, Orc, Troll, Dragon)
- **Item Types**: 5 (Weapons, Armor, Potions, Gold, Scrolls)
- **Spells/Skills**: 12+ total across all classes

---

**Enjoy your dungeon crawling adventure!** 🗡️⚔️🛡️ 