from random import choice, random

from amak import AgentEntity, EnvironmentEntity


def grid_to_display_position(on_grid_position):
    return 5 + on_grid_position[0] * 10, 5 + on_grid_position[1] * 10


class RobotAgent(AgentEntity):
    def __init__(self, mas, on_grid_position):
        self.on_grid_position = on_grid_position
        self.held_box = None
        super().__init__(mas, grid_to_display_position(self.on_grid_position), "red")
        self.set_grid_position(on_grid_position)

    def set_grid_position(self, on_grid_position):
        g = self.amas.environment.grid[self.on_grid_position[1]][self.on_grid_position[0]]
        if self in g:
            g.remove(self)
        self.on_grid_position = on_grid_position
        self.set_position(grid_to_display_position(on_grid_position))
        self.amas.environment.grid[self.on_grid_position[1]][self.on_grid_position[0]].append(self)

    def move_randomly(self):
        new_position = None
        max_attempt = 10
        while max_attempt > 0 and (not self.amas.environment.is_on_grid_position_valid(
                new_position) or self.amas.environment.is_on_grid_position_occupied_by_robot(new_position)):
            direction = choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
            new_position = (self.on_grid_position[0] + direction[0], self.on_grid_position[1] + direction[1])
            max_attempt -= 1
        if max_attempt > 0:
            self.set_grid_position(new_position)

    def die(self):
        self.destroy()
        self.amas.environment.grid[self.on_grid_position[1]][self.on_grid_position[0]].remove(self)

    def try_to_take_box(self):
        if self.held_box is not None:
            return
        self.held_box = self.amas.environment.get_box(self.on_grid_position)
        if self.held_box:
            self.surface.fill("green", (2, 2, 6, 6))

    def drop_box(self):
        self.held_box = None
        self.surface.fill("red")

    def on_perceive(self):
        # Exercise: Implement the Robot perception
        pass

    def on_decide_and_act(self):
        # Exercise: Implement the Robot decision and action
        if self.held_box is None:
            self.try_to_take_box()
        else:
            if self.amas.environment.is_drop_zone(self.on_grid_position):
                self.drop_box()
        self.move_randomly()


class BoxEntity(EnvironmentEntity):
    def __init__(self, on_grid_position, environment):
        self.on_grid_position = on_grid_position
        self.environment = environment
        super().__init__(grid_to_display_position(self.on_grid_position), "green")
        self.set_grid_position(on_grid_position)

    def set_grid_position(self, on_grid_position):
        g = self.environment.grid[self.on_grid_position[1]][self.on_grid_position[0]]
        if self in g:
            g.remove(self)
        self.on_grid_position = on_grid_position
        self.set_position(grid_to_display_position(on_grid_position))
        self.environment.grid[self.on_grid_position[1]][self.on_grid_position[0]].append(self)
