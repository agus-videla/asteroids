from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self):
        super().__init__(self, x, y, SHOT_RADIUS)

