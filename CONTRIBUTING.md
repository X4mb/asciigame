# Contributing to ASCII Roguelike Dungeon Crawler

Thank you for your interest in contributing to the ASCII Roguelike Dungeon Crawler! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Types of Contributions

We welcome various types of contributions:

- **Bug Reports**: Report issues you encounter while playing
- **Feature Requests**: Suggest new features or improvements
- **Code Contributions**: Submit code for new features or bug fixes
- **Documentation**: Improve or add documentation
- **Testing**: Help test the game and improve test coverage

### Getting Started

1. **Fork the Repository**
   ```bash
   git clone https://github.com/yourusername/ascii-roguelike.git
   cd ascii-roguelike
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Follow the coding standards below
   - Add tests for new features
   - Update documentation as needed

4. **Test Your Changes**
   ```bash
   python test_game.py
   ```

5. **Commit Your Changes**
   ```bash
   git commit -m "Add: brief description of your changes"
   ```

6. **Push and Create a Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

## 📋 Coding Standards

### Python Style Guide
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use meaningful variable and function names
- Keep functions focused and under 50 lines when possible
- Add type hints where appropriate

### Code Documentation
- Add docstrings to all functions and classes
- Use clear, descriptive comments for complex logic
- Update README.md for new features

### Testing Requirements
- Add tests for all new functionality
- Ensure existing tests still pass
- Aim for good test coverage

## 🎮 Game Design Guidelines

### Adding New Character Classes
When adding a new character class:

1. **Update `entities.py`**:
   - Add class stats in `setup_class_stats()`
   - Define available skills/spells
   - Set appropriate base stats

2. **Update `game.py`**:
   - Add class to selection menu
   - Update class-specific UI elements

3. **Add Tests**:
   - Test class creation and stats
   - Test skill/spell learning
   - Test progression

### Adding New Monsters
When adding new monster types:

1. **Update `entities.py`**:
   - Add monster type in `Monster.__init__()`
   - Set appropriate stats and loot table
   - Define movement speed

2. **Update `ascii_art.py`**:
   - Add ASCII art for the monster
   - Include combat animations

3. **Update `dungeon.py`**:
   - Add to monster spawn list

### Adding New Items
When adding new item types:

1. **Update `entities.py`**:
   - Add item type in `Item` class
   - Define use effects
   - Set appropriate weight

2. **Update Loot Tables**:
   - Add to monster loot tables
   - Add to chest generation

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Description**: Clear description of the issue
2. **Steps to Reproduce**: Step-by-step instructions
3. **Expected Behavior**: What should happen
4. **Actual Behavior**: What actually happens
5. **Environment**: Python version, OS, etc.
6. **Screenshots**: If applicable

## 💡 Feature Requests

When suggesting features:

1. **Clear Description**: Explain the feature in detail
2. **Use Case**: Why this feature would be useful
3. **Implementation Ideas**: How it might be implemented
4. **Priority**: How important this feature is

## 🧪 Testing Guidelines

### Running Tests
```bash
python test_game.py
```

### Writing Tests
- Test both positive and negative cases
- Test edge cases and error conditions
- Use descriptive test names
- Keep tests focused and independent

### Test Structure
```python
def test_feature_name():
    """Test description of what is being tested"""
    # Setup
    # Action
    # Assert
```

## 📝 Commit Message Guidelines

Use clear, descriptive commit messages:

- **Format**: `Type: brief description`
- **Types**: Add, Fix, Update, Remove, Refactor, Test, Docs
- **Examples**:
  - `Add: new warrior skill - Battle Rage`
  - `Fix: inventory weight calculation bug`
  - `Update: improve dungeon generation algorithm`
  - `Docs: add contributing guidelines`

## 🔄 Pull Request Process

1. **Title**: Clear, descriptive title
2. **Description**: Detailed description of changes
3. **Testing**: Confirm all tests pass
4. **Documentation**: Update docs if needed
5. **Review**: Address any review comments

## 📋 Issue Templates

### Bug Report Template
```markdown
**Bug Description**
Brief description of the bug

**Steps to Reproduce**
1. Step 1
2. Step 2
3. Step 3

**Expected Behavior**
What should happen

**Actual Behavior**
What actually happens

**Environment**
- Python Version:
- OS:
- Game Version:

**Additional Information**
Any other relevant information
```

### Feature Request Template
```markdown
**Feature Description**
Detailed description of the requested feature

**Use Case**
Why this feature would be useful

**Implementation Ideas**
How this might be implemented

**Priority**
High/Medium/Low

**Additional Information**
Any other relevant information
```

## 🏆 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

## 📞 Getting Help

If you need help contributing:

1. **Check Documentation**: Read the README and code comments
2. **Search Issues**: Look for similar issues or discussions
3. **Ask Questions**: Open an issue with your question
4. **Join Discussions**: Participate in project discussions

## 🎯 Current Priorities

- [ ] Cross-platform compatibility (Linux/Mac)
- [ ] Save/load game functionality
- [ ] Additional monster types
- [ ] More character classes
- [ ] Enhanced UI/UX
- [ ] Performance optimizations

Thank you for contributing to the ASCII Roguelike Dungeon Crawler! 🗡️⚔️🛡️ 