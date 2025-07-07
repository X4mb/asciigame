import random
import os
from entities import Monster, Chest, Item

class Dungeon:
    def __init__(self, width=40, height=20):
        self.base_width = width
        self.base_height = height
        self.width = width
        self.height = height
        self.map = []  # 2D list for dungeon layout
        self.monsters = []  # List of monsters in the dungeon
        self.chests = []  # List of chests in the dungeon
        self.stairs = None  # Position of stairs to next level
        self.level = 1
        self.generate()

    def generate(self):
        # Use different seed for each level to ensure variety
        random.seed(42 + self.level)
        # Scale dungeon size with level
        self.width = self.base_width + (self.level - 1) * 4
        self.height = self.base_height + (self.level - 1) * 2
        # Initialize with walls
        self.map = [['#' for _ in range(self.width)] for _ in range(self.height)]
        # Generate rooms using cellular automata for more organic feel
        self.generate_rooms()
        # Ensure starting position (1,1) is always a floor
        self.map[1][1] = '.'
        # Ensure connectivity
        self.ensure_connectivity()
        # Add stairs to next level
        self.add_stairs()
        # Spawn monsters and chests
        self.spawn_monsters()
        self.spawn_chests()

    def generate_rooms(self):
        """Generate rooms using cellular automata for more organic feel"""
        # Create some initial random floor tiles
        for _ in range(self.width * self.height // 4):
            x = random.randint(1, self.width - 2)
            y = random.randint(1, self.height - 2)
            self.map[y][x] = '.'
        
        # Apply cellular automata rules
        for _ in range(3):
            new_map = [row[:] for row in self.map]
            for y in range(1, self.height - 1):
                for x in range(1, self.width - 1):
                    neighbors = 0
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            if dx == 0 and dy == 0:
                                continue
                            if 0 <= y + dy < self.height and 0 <= x + dx < self.width:
                                if self.map[y + dy][x + dx] == '.':
                                    neighbors += 1
                    
                    if self.map[y][x] == '#':
                        if neighbors >= 4:
                            new_map[y][x] = '.'
                    else:
                        if neighbors < 2:
                            new_map[y][x] = '#'
            
            self.map = new_map

    def ensure_connectivity(self):
        """Ensure all floor tiles are connected"""
        # Find all floor tiles
        floor_tiles = []
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] == '.':
                    floor_tiles.append((x, y))
        
        if not floor_tiles:
            return
        
        # Start from (1,1) and connect to all other floor tiles
        start = (1, 1)
        connected = {start}
        to_connect = set(floor_tiles) - connected
        
        while to_connect:
            # Find closest unconnected tile
            closest = min(to_connect, key=lambda pos: abs(pos[0] - start[0]) + abs(pos[1] - start[1]))
            
            # Create path to closest tile
            self.create_path(start, closest)
            connected.add(closest)
            to_connect.remove(closest)

    def create_path(self, start, end):
        """Create a path between two points"""
        x1, y1 = start
        x2, y2 = end
        
        # Create L-shaped path
        if random.random() < 0.5:
            # Horizontal then vertical
            for x in range(min(x1, x2), max(x1, x2) + 1):
                if 0 <= x < self.width and 0 <= y1 < self.height:
                    self.map[y1][x] = '.'
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if 0 <= x2 < self.width and 0 <= y < self.height:
                    self.map[y][x2] = '.'
        else:
            # Vertical then horizontal
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if 0 <= x1 < self.width and 0 <= y < self.height:
                    self.map[y][x1] = '.'
            for x in range(min(x1, x2), max(x1, x2) + 1):
                if 0 <= x < self.width and 0 <= y2 < self.height:
                    self.map[y2][x] = '.'

    def add_stairs(self):
        """Add stairs to the furthest room from start"""
        floor_tiles = []
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] == '.' and (x, y) != (1, 1):
                    floor_tiles.append((x, y))
        
        if floor_tiles:
            # Find furthest tile from start
            furthest = max(floor_tiles, key=lambda pos: abs(pos[0] - 1) + abs(pos[1] - 1))
            self.stairs = furthest
            self.map[furthest[1]][furthest[0]] = '>'

    def spawn_monsters(self):
        """Spawn monsters in the dungeon"""
        # Spawn 5-8 monsters
        num_monsters = random.randint(5, 8)
        occupied_positions = set()  # Track occupied positions to prevent overlap
        
        for _ in range(num_monsters):
            # Find a random floor tile that's not occupied
            floor_tiles = []
            for y in range(self.height):
                for x in range(self.width):
                    if (self.map[y][x] == '.' and 
                        (x, y) != (1, 1) and 
                        (x, y) not in occupied_positions):
                        floor_tiles.append((x, y))
            
            if floor_tiles:
                x, y = random.choice(floor_tiles)
                occupied_positions.add((x, y))  # Mark as occupied
                
                # Choose monster type
                monster_types = ['goblin', 'orc', 'troll']
                monster_type = random.choice(monster_types)
                
                monster = Monster(x, y, monster_type)
                self.monsters.append(monster)

    def spawn_chests(self):
        """Spawn treasure chests in the dungeon"""
        num_chests = random.randint(2, 4)
        occupied_positions = set()
        
        # Get all monster positions
        for monster in self.monsters:
            occupied_positions.add((monster.x, monster.y))
        
        for _ in range(num_chests):
            # Find a random floor tile that's not occupied
            floor_tiles = []
            for y in range(self.height):
                for x in range(self.width):
                    if (self.map[y][x] == '.' and 
                        (x, y) != (1, 1) and 
                        (x, y) not in occupied_positions):
                        floor_tiles.append((x, y))
            
            if floor_tiles:
                x, y = random.choice(floor_tiles)
                occupied_positions.add((x, y))  # Mark as occupied
                chest = Chest(x, y)
                self.chests.append(chest)

    def move_monsters(self, player_pos, player_last_move=(0,0)):
        for monster in self.monsters:
            if monster.is_alive():
                monster.increment_move_counter()
                if monster.should_move():
                    monster.move_towards_player(player_pos[0], player_pos[1], self)
                    monster.reset_move_counter()

    def is_valid_position(self, x, y):
        """Check if a position is valid for movement"""
        return (0 <= x < self.width and 
                0 <= y < self.height and 
                self.map[y][x] == '.')

    def has_line_of_sight(self, x1, y1, x2, y2):
        """Check if there's a clear line of sight between two points"""
        # Use Bresenham's line algorithm to check for walls
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        x, y = x1, y1
        n = 1 + dx + dy
        x_inc = 1 if x2 > x1 else -1
        y_inc = 1 if y2 > y1 else -1
        error = dx - dy
        dx *= 2
        dy *= 2

        for _ in range(n):
            # Check if current position is a wall
            if self.map[y][x] == '#':
                return False
            
            # If we've reached the target, we have line of sight
            if x == x2 and y == y2:
                return True
            
            if error > 0:
                x += x_inc
                error -= dy
            else:
                y += y_inc
                error += dx
        
        return True

    def get_monster_at(self, x, y):
        """Get monster at specific coordinates"""
        for monster in self.monsters:
            if monster.x == x and monster.y == y and monster.is_alive():
                return monster
        return None

    def get_chest_at(self, x, y):
        """Get chest at specific coordinates"""
        for chest in self.chests:
            if chest.x == x and chest.y == y and not chest.opened:
                return chest
        return None

    def is_stairs_at(self, x, y):
        """Check if stairs are at specific coordinates"""
        return self.stairs and (x, y) == self.stairs

    def remove_monster(self, monster):
        """Remove a dead monster from the list"""
        if monster in self.monsters:
            self.monsters.remove(monster)

    def next_level(self):
        """Generate the next level of the dungeon, scaling up size"""
        self.level += 1
        self.monsters.clear()
        self.chests.clear()
        self.stairs = None
        self.generate()

    def render(self, player_pos=None, visible=None, player=None):
        # Clear screen using Windows-compatible method
        os.system('cls')
        
        # Create a display map that includes monsters and chests
        display_map = [row[:] for row in self.map]
        
        # Add monsters to display map
        for monster in self.monsters:
            if monster.is_alive():
                display_map[monster.y][monster.x] = monster.char
        
        # Add chests to display map
        for chest in self.chests:
            display_map[chest.y][chest.x] = chest.char
        
        # Render the dungeon
        for y in range(self.height):
            for x in range(self.width):
                if player_pos and (x, y) == player_pos:
                    print('@', end='')
                else:
                    print(display_map[y][x], end='')
            print()  # New line after each row
        
        print(f"\nLevel: {self.level} | Player position: {player_pos}")
        if player:
            print("Controls: WASD to move, P to quit, I for inventory, X for " + ("spells" if player.is_caster() else "skills"))
        else:
            print("Controls: WASD to move, P to quit, I for inventory, X for spells/skills")
        print("Monsters: g=Goblin, o=Orc, t=Troll | C=Chest, >=Stairs") 