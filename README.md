# ASCII Roguelike Dungeon Crawler

A classic roguelike dungeon crawler game built entirely in Python with ASCII graphics. Explore procedurally generated dungeons, battle monsters, collect loot, and level up your character across multiple classes.

![Game Screenshot](https://img.shields.io/badge/Game-ASCII%20Roguelike-blue)
![Python](https://img.shields.io/badge/Python-3.6+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🎮 Features

### Character Classes
- **Warrior**: High HP, strong melee combat with skills like Power Strike and Shield Bash
- **Mage**: Powerful spellcaster with Fireball, Lightning, Ice Storm, and Meteor spells
- **Rogue**: Stealthy fighter with Backstab, Evasion, and Poison Strike abilities
- **Cleric**: Support class with healing spells and divine magic

### Game Mechanics
- **Procedural Dungeon Generation**: Each level is uniquely generated using cellular automata
- **Turn-based Combat**: Strategic battles with multiple action options
- **Inventory System**: Weight-based inventory with item stacking and equipment
- **Level Progression**: Gain experience, level up, and unlock new abilities
- **Monster AI**: Intelligent enemies that pursue the player with line-of-sight detection
- **Loot System**: Treasure chests and monster drops with various item types

### Visual Features
- **ASCII Graphics**: Classic roguelike visuals with detailed combat animations
- **Dynamic UI**: Real-time status display and interactive menus
- **Combat Animations**: Visual feedback for attacks, damage, and special effects

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
- **H**: Heal (restores 5 HP)
- **R**: Attempt to run away
- **X**: Cast spell or use skill

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
├── test_game.py         # Comprehensive test suite
└── LICENSE              # MIT License
```

## 🎲 Game Systems

### Character Progression
Each class has unique progression paths:
- **Warrior**: Gains HP and attack power, learns combat skills
- **Mage**: Gains mana and learns powerful offensive spells
- **Rogue**: Gains HP and learns stealth/agility skills
- **Cleric**: Gains HP and mana, learns healing and divine spells

### Combat System
- Turn-based combat with multiple action options
- Damage calculation based on attack vs defense
- Special effects: stun, poison, dodge, healing
- Monster AI with line-of-sight detection and pursuit

### Dungeon Generation
- Procedural generation using cellular automata
- Scaled difficulty with level progression
- Connected rooms and corridors
- Strategic placement of monsters, chests, and stairs

### Inventory & Items
- Weight-based carrying system
- Item stacking for consumables
- Equipment system for weapons and armor
- Various item types: weapons, armor, potions, gold

## 🧪 Testing

The project includes a comprehensive test suite covering:
- Character class functionality
- Combat mechanics
- Inventory management
- Dungeon generation
- Loot systems
- Level progression
- Monster AI behavior

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

## 🎯 Future Enhancements

- [ ] Save/load game functionality
- [ ] More character classes and races
- [ ] Additional monster types and bosses
- [ ] Magic items and enchantments
- [ ] Multiplayer support
- [ ] Sound effects and music
- [ ] Cross-platform compatibility
- [ ] Modding support

## 📊 Game Statistics

- **Lines of Code**: ~2,000+
- **Character Classes**: 4
- **Monster Types**: 3 (Goblin, Orc, Troll)
- **Item Types**: 5 (Weapons, Armor, Potions, Gold, Scrolls)
- **Spells/Skills**: 12 total across all classes

## 🏆 Acknowledgments

- Inspired by classic roguelike games like NetHack and Rogue
- Built with pure Python for maximum accessibility
- ASCII art created for immersive retro gaming experience

---

**Enjoy your dungeon crawling adventure!** 🗡️⚔️🛡️ 