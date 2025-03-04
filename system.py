from amak import MAS

from entities import BoxEntity, RobotAgent

GRID_WIDTH = 100
GRID_HEIGHT = 50
CORRIDOR_WIDTH = 40


class TransporterRobotsMAS(MAS):
    def __init__(self, environment):
        super().__init__(environment)


# Room 1
ROOM1_WALL = (GRID_WIDTH // 2 - CORRIDOR_WIDTH // 2, 1, CORRIDOR_WIDTH, GRID_HEIGHT - 2)

# Room 2
VERTICAL_CENTER = GRID_HEIGHT // 2
ROOM2_WALL1 = (GRID_WIDTH // 2 - CORRIDOR_WIDTH // 2, 1, CORRIDOR_WIDTH, VERTICAL_CENTER - 1)
ROOM2_WALL2 = (GRID_WIDTH // 2 - CORRIDOR_WIDTH // 2, VERTICAL_CENTER + 2, CORRIDOR_WIDTH, GRID_HEIGHT // 2 - 3)
ROOM2_WALL3 = (GRID_WIDTH // 2 - CORRIDOR_WIDTH // 2, VERTICAL_CENTER, CORRIDOR_WIDTH // 2 - 1, 1)
ROOM2_WALL4 = (GRID_WIDTH // 2, VERTICAL_CENTER + 1, CORRIDOR_WIDTH // 2, 1)

PICKUP_RECT = (0, GRID_HEIGHT // 4, 5, GRID_HEIGHT // 2)
DROP_RECT = (GRID_WIDTH - 5, GRID_HEIGHT // 4, 5, GRID_HEIGHT // 2)


class TransporterRobotsEnvironment:
    def __init__(self, room=1):
        w, h = GRID_WIDTH, GRID_HEIGHT
        self.room = room
        self.grid = [[[] for x in range(w)] for y in range(h)]
        # Add boxes to grid
        for x in range(PICKUP_RECT[0], PICKUP_RECT[0] + PICKUP_RECT[2]):
            for y in range(PICKUP_RECT[1], PICKUP_RECT[1] + PICKUP_RECT[3]):
                self.grid[y][x].append(BoxEntity((x, y), self))

    def cycle(self):
        pass

    def render(self, display_surface):
        display_surface.fill((255, 255, 255))
        # draw a square in the middle
        if self.room == 1:
            display_surface.fill((0, 0, 0), (
                ROOM1_WALL[0] * 10, ROOM1_WALL[1] * 10, ROOM1_WALL[2] * 10, ROOM1_WALL[3] * 10))
        elif self.room == 2:
            display_surface.fill((0, 0, 0),
                                 (ROOM2_WALL1[0] * 10, ROOM2_WALL1[1] * 10, ROOM2_WALL1[2] * 10, ROOM2_WALL1[3] * 10))
            display_surface.fill((0, 0, 0),
                                 (ROOM2_WALL2[0] * 10, ROOM2_WALL2[1] * 10, ROOM2_WALL2[2] * 10, ROOM2_WALL2[3] * 10))
            display_surface.fill((0, 0, 0),
                                 (ROOM2_WALL3[0] * 10, ROOM2_WALL3[1] * 10, ROOM2_WALL3[2] * 10, ROOM2_WALL3[3] * 10))
            display_surface.fill((0, 0, 0),
                                 (ROOM2_WALL4[0] * 10, ROOM2_WALL4[1] * 10, ROOM2_WALL4[2] * 10, ROOM2_WALL4[3] * 10))

        # draw a surface for the DROP_RECT
        display_surface.fill((200, 200, 200),
                             (DROP_RECT[0] * 10, DROP_RECT[1] * 10, DROP_RECT[2] * 10, DROP_RECT[3] * 10))

        for x in range(0, len(self.grid[0])):
            for y in range(0, len(self.grid)):
                for e in self.grid[y][x]:
                    if isinstance(e, BoxEntity):
                        display_surface.blit(e.surface, e.rect)

    def is_on_grid_position_occupied_by_robot(self, position):
        cell = self.grid[position[1]][position[0]]
        for e in cell:
            if isinstance(e, RobotAgent):
                return True

    def is_on_grid_position_valid(self, position):
        if position is None:
            return False
        x, y = position
        return 0 <= position[0] < len(self.grid[0]) and 0 <= position[1] < len(self.grid)

    # Check if the position is inside the wall given as a parameter
    def is_on_grid_position_in_wall(self, position, wall):
        return (wall[0] <= position[0] < wall[0] + wall[2] and
                wall[1] <= position[1] < wall[1] + wall[3])

    # Check if the position is inside a wall of the current room
    def is_on_grid_position_wall(self, position):
        if self.room == 1:
            return self.is_on_grid_position_in_wall(position, ROOM1_WALL)
        elif self.room == 2:
            return self.is_on_grid_position_in_wall(position, ROOM2_WALL1) or \
                self.is_on_grid_position_in_wall(position, ROOM2_WALL2) or \
                self.is_on_grid_position_in_wall(position, ROOM2_WALL3) or \
                self.is_on_grid_position_in_wall(position, ROOM2_WALL4)

    def is_drop_zone(self, position):
        if not self.is_on_grid_position_valid(position):
            return False
        return DROP_RECT[0] <= position[0] < DROP_RECT[0] + DROP_RECT[2] and DROP_RECT[1] <= position[1] < DROP_RECT[
            1] + DROP_RECT[3]

    def get_box(self, position):
        if not self.is_on_grid_position_valid(position):
            return None
        cell = self.grid[position[1]][position[0]]
        for e in cell:
            if isinstance(e, BoxEntity):
                # Remove the box from the grid
                cell.remove(e)
                return e

    def remove_entity(self, entity):
        if not self.is_on_grid_position_valid(entity.on_grid_position):
            return
        self.grid[entity.on_grid_position[1]][entity.on_grid_position[0]].remove(entity)
