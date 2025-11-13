import numpy as np
from src.config import TIME, STEP, SCALE, MOVE


class SignalGenerator:
    """Generuje idealny sygnał bazowy u(t) = SCALE * sin(t) + MOVE."""

    def __init__(self, time=TIME, step=STEP, scale=SCALE, move=MOVE):
        self.time = time
        self.step = step
        self.scale = scale
        self.move = move

    def generate(self) -> tuple[np.ndarray, np.ndarray]:
        t = np.arange(0, self.time, self.step)
        u = self.scale * np.sin(t) + self.move
        return t, u
