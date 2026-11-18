import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys
from pathlib import Path
rng = np.random.default_rng(12)


project_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(project_root))

from src.conway_functions import update_square_board

# Initialize board
board_size = 30  
number_of_generations = 100

board = np.zeros(board_size**2)


indices = rng.choice(board_size**2, size=250, replace=False)

board[indices] = 1

board = board.reshape((board_size, board_size))

fig, ax = plt.subplots()
img = ax.imshow(board, cmap="gray_r", vmin=0, vmax=1)

ax.set_title("Generation 0")

def animate(generation):
    global board

    board = update_square_board(board)

    img.set_data(board)
    ax.set_title(f"Generation {generation + 1}")

    return img,

ani = FuncAnimation(fig, animate, frames=number_of_generations, interval=1000, repeat=False)

plt.show()
