# Changelog

All notable changes to the ASCII Roguelike Dungeon Crawler project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Cross-platform compatibility (Linux/Mac support)
- Save/load game functionality
- Additional monster types and bosses
- More character classes and races
- Enhanced UI/UX improvements
- Sound effects and music
- Modding support

## [1.0.0] - 2025-01-XX

### Added
- **Core Game Engine**: Complete roguelike game engine with turn-based gameplay
- **Character Classes**: Four unique classes (Warrior, Mage, Rogue, Cleric)
- **Procedural Dungeon Generation**: Cellular automata-based dungeon creation
- **Combat System**: Turn-based combat with multiple action options
- **Inventory System**: Weight-based inventory with item stacking
- **Level Progression**: Experience-based leveling with skill/spell unlocks
- **Monster AI**: Intelligent enemies with line-of-sight detection
- **Loot System**: Treasure chests and monster drops
- **ASCII Graphics**: Detailed ASCII art and combat animations
- **Comprehensive Test Suite**: Full test coverage for all game systems

### Features by Class

#### Warrior
- High HP and defense
- Skills: Power Strike (L2), Shield Bash (L4), Battle Rage (L6)
- Melee-focused combat abilities

#### Mage
- High mana pool
- Spells: Fireball (L1), Lightning (L3), Ice Storm (L5), Meteor (L7)
- Powerful offensive magic

#### Rogue
- Balanced stats
- Skills: Backstab (L2), Evasion (L4), Poison Strike (L6)
- Stealth and agility abilities

#### Cleric
- Support-focused
- Spells: Heal (L1), Smite (L3), Divine Protection (L5), Resurrection (L7)
- Healing and divine magic

### Game Mechanics
- **Dungeon Features**: Walls (#), floors (.), stairs (>), chests (C)
- **Monsters**: Goblins (g), Orcs (o), Trolls (t)
- **Items**: Weapons, armor, potions, gold, scrolls
- **Combat Effects**: Stun, poison, dodge, healing
- **Movement**: WASD controls with collision detection
- **UI**: Real-time status display and interactive menus

### Technical Features
- **Modular Architecture**: Clean separation of concerns
- **Extensible Design**: Easy to add new features
- **Comprehensive Testing**: Full test suite with 400+ lines of tests
- **Documentation**: Complete code documentation and user guides
- **Error Handling**: Robust error handling and edge case management

### Files Added
- `main.py`: Game entry point
- `game.py`: Main game logic and UI (721 lines)
- `dungeon.py`: Dungeon generation and management (290 lines)
- `entities.py`: Game entities (Player, Monster, Item, Chest) (507 lines)
- `ascii_art.py`: ASCII graphics and animations (311 lines)
- `test_game.py`: Comprehensive test suite (439 lines)
- `README.md`: Complete project documentation
- `CONTRIBUTING.md`: Contribution guidelines
- `CHANGELOG.md`: Version history
- `requirements.txt`: Dependencies (none required)
- `.gitignore`: Git ignore rules
- `LICENSE`: MIT License

### Known Issues
- Windows-only compatibility (uses msvcrt for input)
- No save/load functionality
- Limited monster variety
- No sound effects

### Future Enhancements
- Cross-platform support
- Save/load system
- Additional content (monsters, classes, items)
- Enhanced graphics and UI
- Multiplayer support
- Modding capabilities

---

## Version History Summary

### v1.0.0 (Current)
- Initial release with complete game functionality
- Four character classes with unique abilities
- Procedural dungeon generation
- Comprehensive combat and inventory systems
- Full test suite and documentation

---

**Note**: This changelog follows the [Keep a Changelog](https://keepachangelog.com/) format and uses [Semantic Versioning](https://semver.org/) for version numbers. 