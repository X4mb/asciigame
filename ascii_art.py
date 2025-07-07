def get_ascii_art(name):
    """Return ASCII art for entities/items"""
    art = {
        'player': '''
    @
   /|\\
   / \\
        ''',
        'monster': '''
    M
   /|\\
   / \\
        ''',
        'treasure': '''
    $
   /|\\
   / \\
        ''',
        'wall': '''
  ####
  ####
  ####
        '''
    }
    return art.get(name.lower(), '?')

def get_combat_art(entity_type, pose='idle'):
    """Return ASCII art for combat animations"""
    if entity_type == 'player':
        if pose == 'idle':
            return '''
      @
     /|\\
    / | \\
   /  |  \\
  /   |   \\
 /    |    \\
/     |     \\
     / \\
    /   \\
   /     \\
  /       \\
 /         \\
/           \\
        '''
        elif pose == 'attack':
            return '''
      @
     /|\\
    / | \\
   /  |  \\
  /   |   \\
 /    |    \\
/     |     \\
     / \\
    /   \\
   /     \\
  /       \\
 /         \\
/           \\
   >>>>>>>>>>>>
        '''
        elif pose == 'hurt':
            return '''
      @
     /|\\
    / | \\
   /  |  \\
  /   |   \\
 /    |    \\
/     |     \\
     / \\
    /   \\
   /     \\
  /       \\
 /         \\
/           \\
     OUCH!
        '''
    elif entity_type == 'goblin':
        if pose == 'idle':
            return '''
      g
     /|\\
    / | \\
   /  |  \\
  /   |   \\
 /    |    \\
/     |     \\
     / \\
    /   \\
   /     \\
  /       \\
 /         \\
/           \\
        '''
        elif pose == 'attack':
            return '''
      g
     /|\\
    / | \\
   /  |  \\
  /   |   \\
 /    |    \\
/     |     \\
     / \\
    /   \\
   /     \\
  /       \\
 /         \\
/           \\
   <<<<<<<<<<<<
        '''
        elif pose == 'hurt':
            return '''
      g
     /|\\
    / | \\
   /  |  \\
  /   |   \\
 /    |    \\
/     |     \\
     / \\
    /   \\
   /     \\
  /       \\
 /         \\
/           \\
     GRR!
        '''
    elif entity_type == 'orc':
        if pose == 'idle':
            return '''
      O
     /|\\
    / | \\
   /  |  \\
  /   |   \\
 /    |    \\
/     |     \\
     / \\
    /   \\
   /     \\
  /       \\
 /         \\
/           \\
        '''
        elif pose == 'attack':
            return '''
      O
     /|\\
    / | \\
   /  |  \\
  /   |   \\
 /    |    \\
/     |     \\
     / \\
    /   \\
   /     \\
  /       \\
 /         \\
/           \\
   <<<<<<<<<<<<
        '''
        elif pose == 'hurt':
            return '''
      O
     /|\\
    / | \\
   /  |  \\
  /   |   \\
 /    |    \\
/     |     \\
     / \\
    /   \\
   /     \\
  /       \\
 /         \\
/           \\
     RAA!
        '''
    elif entity_type == 'troll':
        if pose == 'idle':
            return '''
      T
     /|\\
    / | \\
   /  |  \\
  /   |   \\
 /    |    \\
/     |     \\
     / \\
    /   \\
   /     \\
  /       \\
 /         \\
/           \\
        '''
        elif pose == 'attack':
            return '''
      T
     /|\\
    / | \\
   /  |  \\
  /   |   \\
 /    |    \\
/     |     \\
     / \\
    /   \\
   /     \\
  /       \\
 /         \\
/           \\
   <<<<<<<<<<<<
        '''
        elif pose == 'hurt':
            return '''
      T
     /|\\
    / | \\
   /  |  \\
  /   |   \\
 /    |    \\
/     |     \\
     / \\
    /   \\
   /     \\
  /       \\
 /         \\
/           \\
     GRR!
        '''
    else:  # Default monster
        if pose == 'idle':
            return '''
      M
     /|\\
    / | \\
   /  |  \\
  /   |   \\
 /    |    \\
/     |     \\
     / \\
    /   \\
   /     \\
  /       \\
 /         \\
/           \\
        '''
        elif pose == 'attack':
            return '''
      M
     /|\\
    / | \\
   /  |  \\
  /   |   \\
 /    |    \\
/     |     \\
     / \\
    /   \\
   /     \\
  /       \\
 /         \\
/           \\
   <<<<<<<<<<<<
        '''
        elif pose == 'hurt':
            return '''
      M
     /|\\
    / | \\
   /  |  \\
  /   |   \\
 /    |    \\
/     |     \\
     / \\
    /   \\
   /     \\
  /       \\
 /         \\
/           \\
     OOF!
        '''

def get_animation_frames(name):
    """Return a list of ASCII frames for a given spell or skill animation name."""
    # Example animations for demonstration
    animations = {
        'fireball': [
            r"   *   ",
            r"  ***  ",
            r" ***** ",
            r"*******",
            r"  ***  ",
            r"   *   "
        ],
        'lightning': [
            r"   /  ",
            r"  /   ",
            r" /    ",
            r"/     ",
            r"  /   ",
            r" /    "
        ],
        'heal': [
            r"  +  ",
            r" +++ ",
            r"  +  "
        ],
        'power_strike': [
            r"  /|  ",
            r" / |  ",
            r"/  |  ",
            r"   |  "
        ],
        'shield_bash': [
            r" [===] ",
            r"  | |  ",
            r" [===] "
        ],
        'backstab': [
            r"  >---> ",
            r"   >--->",
            r"    >--->"
        ],
        'evasion': [
            r"  \\  ",
            r"   \\ ",
            r"    \\"],
        'poison_strike': [
            r" ~~~  ",
            r"~ ~ ~ ",
            r" ~~~  "
        ],
        'battle_rage': [
            r" !!!  ",
            r"!!!!! ",
            r" !!!  "
        ],
        'smite': [
            r"  |  ",
            r" /|\ ",
            r"  |  "
        ],
        'ice_storm': [
            r"  *  ",
            r" * * ",
            r"  *  "
        ],
        'meteor': [
            r"  o  ",
            r" ooo ",
            r"  o  "
        ],
        'divine_protection': [
            r"  ()  ",
            r" (  ) ",
            r"  ()  "
        ],
        'resurrection': [
            r"  ^  ",
            r" / \\",
            r"/   \\"
        ]
    }
    return animations.get(name, [r" * "])

def get_title_screen():
    return r'''
    ╔════════════════════════════════════════════════════════════════════════════╗
    ║                        ASCII DUNGEON CRAWLER                             ║
    ║                                                                          ║
    ║  @ = Player    # = Wall    . = Floor                                     ║
    ║  g = Goblin    o = Orc     t = Troll                                     ║
    ║  C = Chest     > = Stairs                                                ║
    ║                                                                          ║
    ║  Controls:                                                               ║
    ║    W/A/S/D - Move                                                        ║
    ║    P - Quit      I - Inventory      X - Spells/Skills                    ║
    ║                                                                          ║
    ║  Press any key to start...                                               ║
    ╚════════════════════════════════════════════════════════════════════════════╝
'''

def get_game_over_screen():
    """Return ASCII art game over screen"""
    return '''
    ╔══════════════════════════════════════════════════════════╗
    ║                        GAME OVER                         ║
    ║                                                          ║
    ║                    Thanks for playing!                   ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    ''' 