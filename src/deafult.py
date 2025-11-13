import numpy as np
from src.config import TIME, STEP, SCALE, MOVE

def generate_base_signal() -> tuple[np.ndarray, np.ndarray]:

    t = np.arange(0, TIME, STEP)
    u = SCALE * np.sin(t) + MOVE
    return t, u
