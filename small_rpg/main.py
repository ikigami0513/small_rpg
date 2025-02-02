import sys
import os

# We dynamically add Elyria to the python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game import SmallRPG
from elyria import main

if __name__ == "__main__":
    small_rpg = SmallRPG()
    main(small_rpg)
