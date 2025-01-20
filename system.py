from amak import MAS

from entities import BoxEntity, RobotAgent

GRID_WIDTH = 100
GRID_HEIGHT = 50
CORRIDOR_WIDTH = 10


class TransporterRobotsMAS(MAS):
    def __init__(self, environment):
        super().__init__(environment)


CORRIDOR_RECT = (GRID_WIDTH // 2 - CORRIDOR_WIDTH // 2, 1, CORRIDOR_WIDTH, GRID_HEIGHT-2)
PICKUP_RECT = (0, GRID_HEIGHT//4, 5, GRID_HEIGHT//2)
DROP_RECT = (GRID_WIDTH-5, GRID_HEIGHT//4, 5, GRID_HEIGHT//2)


class TransporterRobotsEnvironment:
    def __init__(self):
        w, h = GRID_WIDTH, GRID_HEIGHT
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
        display_surface.fill((0, 0, 0), (CORRIDOR_RECT[0] * 10, CORRIDOR_RECT[1] * 10, CORRIDOR_RECT[2] * 10, CORRIDOR_RECT[3] * 10))
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
        # check if position is in corridor rect
        if (CORRIDOR_RECT[0] <= x <= CORRIDOR_RECT[0] + CORRIDOR_RECT[2] and
                CORRIDOR_RECT[1] <= y <= CORRIDOR_RECT[1] + CORRIDOR_RECT[3]):
            return False
        return 0 <= position[0] < len(self.grid[0]) and 0 <= position[1] < len(self.grid)

    def is_drop_zone(self, position):
        if not self.is_on_grid_position_valid(position):
            return False
        return DROP_RECT[0] <= position[0] < DROP_RECT[0] + DROP_RECT[2] and DROP_RECT[1] <= position[1] < DROP_RECT[1] + DROP_RECT[3]

    def get_box(self, position):
        if not self.is_on_grid_position_valid(position):
            return None
        cell = self.grid[position[1]][position[0]]
        for e in cell:
            if isinstance(e, BoxEntity):
                #Remove the box from the grid
                cell.remove(e)
                return e
