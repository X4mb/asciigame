# ASCII Dungeon Crawler

![Game Screenshot](https://img.shields.io/badge/Game-ASCII%20Roguelike-blue)
![Python](https://img.shields.io/badge/Python-3.6+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)


### Prerequisites
- Python 3.6 or higher
- Windows (uses `msvcrt` for input handling)

### Installation
1. Clone the repository:
```bash
git clone https://github.com/x4mb/ascii-roguelike.git
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

## How to Play

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


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Game Statistics

- **Lines of Code**: ~2,000+
- **Character Classes**: 4
- **Monster Types**: 4 (Goblin, Orc, Troll, Dragon)
- **Item Types**: 5 (Weapons, Armor, Potions, Gold, Scrolls)
- **Spells/Skills**: 12+ total across all classes

---
