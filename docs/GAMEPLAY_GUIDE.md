# ASCII Roguelike Dungeon Crawler - Gameplay Guide

Welcome to the ASCII Roguelike Dungeon Crawler! This guide will help you understand the game mechanics and become a successful dungeon explorer.

## 🎯 Getting Started

### Character Selection
Choose from four unique character classes, each with different strengths and playstyles:

#### 🗡️ Warrior
- **Stats**: High HP (15), Low MP (10), High Attack (4), Good Defense (2)
- **Playstyle**: Tank and spank - absorb damage and deal heavy melee damage
- **Skills**:
  - **Power Strike (L2)**: Deals 8 extra damage
  - **Shield Bash (L4)**: Deals 6 damage and may stun enemies
  - **Battle Rage (L6)**: Deals 12 damage and heals 5 HP
- **Best for**: Beginners, players who prefer straightforward combat

#### 🔥 Mage
- **Stats**: Low HP (8), High MP (25), Low Attack (2), Low Defense (1)
- **Playstyle**: Glass cannon - deal massive damage from afar
- **Spells**:
  - **Fireball (L1)**: Deals 8 damage (5 MP)
  - **Lightning (L3)**: Deals 12 damage (10 MP)
  - **Ice Storm (L5)**: Deals 18 damage (15 MP)
  - **Meteor (L7)**: Deals 25 damage (20 MP)
- **Best for**: Players who enjoy strategic spellcasting

#### 🥷 Rogue
- **Stats**: Medium HP (10), Medium MP (15), Good Attack (3), Low Defense (1)
- **Playstyle**: Hit and run - use agility and stealth abilities
- **Skills**:
  - **Backstab (L2)**: Deals 10 extra damage
  - **Evasion (L4)**: 70% chance to dodge next attack
  - **Poison Strike (L6)**: Deals 8 damage and poisons for 3 turns
- **Best for**: Players who enjoy tactical positioning and status effects

#### ⚜️ Cleric
- **Stats**: Medium HP (12), High MP (20), Low Attack (2), Good Defense (2)
- **Playstyle**: Support and sustain - heal yourself and deal divine damage
- **Spells**:
  - **Heal (L1)**: Restores 12 HP (6 MP)
  - **Smite (L3)**: Deals 10 damage (8 MP)
  - **Divine Protection (L5)**: Temporary defense boost (10 MP)
  - **Resurrection (L7)**: Revive with full HP (25 MP)
- **Best for**: Players who prefer support roles and sustainability

## 🎮 Basic Controls

### Movement
- **W**: Move up
- **A**: Move left
- **S**: Move down
- **D**: Move right

### Game Actions
- **I**: Open inventory
- **X**: Access spells/skills
- **P**: Quit game

### Combat Actions
- **A**: Attack
- **H**: Heal (restores 5 HP)
- **R**: Attempt to run away (50% success rate)
- **X**: Cast spell or use skill

### Inventory Management
- **W/S**: Navigate through items
- **F**: Use/equip selected item
- **D**: Toggle drop mode
- **Q**: Return to game

## 🗺️ Dungeon Exploration

### Map Symbols
- **@**: Your character
- **#**: Wall (impassable)
- **.**: Floor (walkable)
- **>**: Stairs to next level
- **C**: Treasure chest
- **g**: Goblin
- **o**: Orc
- **t**: Troll

### Dungeon Features
- **Procedural Generation**: Each level is uniquely generated
- **Scaling Difficulty**: Monsters and dungeons get harder each level
- **Connected Areas**: All floor tiles are connected via corridors
- **Strategic Placement**: Monsters and chests are placed intelligently

### Level Progression
- Find the stairs (>) to advance to the next level
- Each level increases in size and difficulty
- Monsters become stronger and more numerous
- Better loot becomes available

## ⚔️ Combat System

### Combat Mechanics
- **Turn-based**: You and monsters take turns
- **Damage Calculation**: `Damage = max(1, Attack - Defense)`
- **Line of Sight**: Monsters can only see you within 8 tiles
- **Movement**: Monsters move towards you when they can see you

### Combat Actions

#### Attack
- Basic melee attack
- Damage based on your attack vs monster defense
- Always hits (no accuracy system)

#### Heal
- Restores 5 HP instantly
- No cooldown or cost
- Cannot exceed maximum HP

#### Run Away
- 50% chance to escape combat
- If failed, you lose your turn
- Monster gets a free attack

#### Cast Spell/Use Skill
- Access your class-specific abilities
- Spells cost mana, skills are free
- Some abilities have special effects

### Special Effects

#### Stun
- Prevents monster from attacking next turn
- Applied by Shield Bash skill

#### Poison
- Deals damage over multiple turns
- Applied by Poison Strike skill
- Damage decreases each turn

#### Dodge
- 70% chance to avoid next attack
- Applied by Evasion skill
- Consumed when attacked

## 📦 Inventory System

### Weight Management
- **Maximum Weight**: 50.0 kg
- **Item Weight**: Each item has a weight value
- **Overweight**: Cannot pick up items if you exceed weight limit

### Inventory Slots
- **Maximum Slots**: 20 different item types
- **Stacking**: Similar items stack automatically
- **Slot Management**: Drop items to free up space

### Item Types

#### Weapons
- **Effect**: Increase attack power
- **Weight**: 3.0 kg
- **Examples**: Steel Sword (+5 attack)
- **Usage**: Automatically equipped when used

#### Armor
- **Effect**: Increase defense
- **Weight**: 8.0 kg
- **Examples**: Leather Armor (+2 defense)
- **Usage**: Automatically equipped when used

#### Potions
- **Effect**: Restore HP or MP
- **Weight**: 0.5 kg
- **Examples**: Health Potion (+15 HP), Mana Potion (+20 MP)
- **Usage**: Consumed when used

#### Gold
- **Effect**: Currency (not implemented in current version)
- **Weight**: 0.01 kg
- **Examples**: Gold Coins
- **Usage**: Collectible item

## 🎯 Strategy Tips

### General Tips
1. **Explore Thoroughly**: Check every corner for chests and monsters
2. **Manage Resources**: Don't waste potions on minor damage
3. **Level Up**: Gain experience by defeating monsters
4. **Equipment Priority**: Always equip better weapons and armor
5. **Know Your Class**: Use your class abilities effectively

### Class-Specific Strategies

#### Warrior
- **Tank Damage**: Use your high HP to absorb hits
- **Skill Timing**: Use Shield Bash to stun dangerous enemies
- **Battle Rage**: Save for tough fights to heal while dealing damage

#### Mage
- **Mana Management**: Don't waste spells on weak enemies
- **Kite Enemies**: Use spells from a distance
- **Spell Progression**: Save higher-level spells for stronger enemies

#### Rogue
- **Hit and Run**: Use Evasion before engaging tough enemies
- **Poison Strategy**: Apply poison and let it do damage over time
- **Positioning**: Use Backstab when possible for extra damage

#### Cleric
- **Heal Proactively**: Don't wait until you're low on HP
- **Divine Protection**: Use before engaging strong enemies
- **Sustain**: Your healing abilities let you fight longer

### Combat Strategies
1. **Assess Threats**: Check monster stats before engaging
2. **Use Abilities**: Don't forget your class skills/spells
3. **Manage HP**: Heal when below 50% HP
4. **Run When Necessary**: Don't be afraid to retreat
5. **Equipment**: Always use the best gear available

## 🏆 Progression Guide

### Early Game (Levels 1-3)
- **Focus**: Explore and gather basic equipment
- **Goals**: Find your first weapon and armor
- **Strategy**: Fight goblins and collect potions

### Mid Game (Levels 4-6)
- **Focus**: Level up and unlock new abilities
- **Goals**: Master your class abilities
- **Strategy**: Take on orcs and collect better loot

### Late Game (Levels 7+)
- **Focus**: Challenge trolls and find rare items
- **Goals**: Maximize your character's potential
- **Strategy**: Use all abilities strategically

## 🐛 Common Mistakes to Avoid

1. **Ignoring Inventory Weight**: Don't carry unnecessary items
2. **Wasting Abilities**: Save powerful spells/skills for tough fights
3. **Poor Positioning**: Don't get surrounded by monsters
4. **Ignoring Equipment**: Always use the best gear available
5. **Rushing**: Take your time to explore and plan

## 🎮 Advanced Techniques

### Monster AI Understanding
- Monsters move every 1-3 turns based on their speed
- They only move when they can see you
- Monsters will pursue you if you're within line of sight
- Use walls and corridors to control monster movement

### Resource Management
- **Potions**: Use health potions when below 30% HP
- **Mana**: For casters, keep some mana for emergency healing
- **Equipment**: Always carry backup weapons/armor
- **Weight**: Prioritize valuable items over heavy ones

### Level Progression
- **Experience**: Monsters give 5-20 XP based on difficulty
- **Leveling**: Each level requires more XP than the last
- **Abilities**: New skills/spells unlock at specific levels
- **Stats**: Your base stats increase with each level

---

**Remember**: The key to success is understanding your class, managing resources wisely, and adapting your strategy to each situation. Good luck, adventurer! 🗡️⚔️🛡️ 