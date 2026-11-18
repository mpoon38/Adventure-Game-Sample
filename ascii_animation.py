# ASCII Animation Demo
# --------------------
# How it works (like a flipbook!):
#   1. Draw each "frame" of the animation as a raw string.
#   2. Put the frames in a list.
#   3. Loop: clear the screen -> print a frame -> wait a little -> next frame.
#
# IMPORTANT: Run this in a real terminal (VS Code terminal, Terminal on Mac,
# Command Prompt on Windows). Clearing the screen does NOT work in IDLE.

import os
import time

os.system("")  # Turns on special screen codes in older Windows terminals


# ---------- Helper functions ----------

def clear():
    """Clear the screen and move the cursor back to the top-left corner."""
    print("\033[H\033[J", end="")


def animate(frames, loops=3, delay=0.3):
    """Play a list of frames over and over, like a flipbook."""
    for _ in range(loops):
        for frame in frames:
            clear()
            print(frame)
            time.sleep(delay)


def slide(art, distance=30, delay=0.08):
    """Move a picture across the screen by adding spaces in front of each line."""
    for x in range(distance):
        clear()
        for line in art.splitlines():
            print(" " * x + line)
        time.sleep(delay)


# ---------- Frames ----------
# TIP: Every frame should have the SAME number of lines,
#      and the parts that don't move should stay in the SAME columns.
#      Copy frame 1, then change only the moving part!

dino_closed = r"""
            ____
           / o  \______
          |    ________|
          |   |
   _______/   |
  /           |
 /_/|_|  |_|\_|
"""

dino_open = r"""
            ____
           / o  \______      ROAR!
          |     _______/
          |    \_______
   _______/   |
  /           |
 /_/|_|  |_|\_|
"""

sword_up = r"""
       |
       |
   O  -+-
  /|\_/
  / \
"""

sword_down = r"""


   O
  /|\_____)=====>
  / \
"""

# A 3-frame animation: a flag waving
flag_1 = r"""
  |~~~~~~~~~
  |~~~~~~~~~
  |
  |
"""

flag_2 = r"""
  |~~~~~~~~
  | ~~~~~~~~~
  |
  |
"""

flag_3 = r"""
  | ~~~~~~~~
  |~~~~~~~~
  |
  |
"""

# A small character for the slide() demo
runner = r"""
  O
 /|\
 / \
"""


# ---------- A tiny choose-your-own-adventure using the animations ----------

def game():
    clear()
    print("=== THE DINO VALLEY ===")
    print("You arrive at the castle. The flag is waving in the wind...")
    time.sleep(2)

    animate([flag_1, flag_2, flag_3], loops=4, delay=0.25)
    print("You walk into the valley behind the castle.")
    time.sleep(2)

    slide(runner, distance=25)
    print("Suddenly the ground shakes...")
    time.sleep(1.5)

    animate([dino_closed, dino_open], loops=4, delay=0.4)
    print("A T-Rex blocks the path!")

    choice = ""
    while choice not in ("1", "2"):
        choice = input("Do you (1) run away or (2) fight? ")

    if choice == "2":
        animate([sword_up, sword_down], loops=5, delay=0.2)
        print("You swing your sword bravely! The T-Rex runs away. You win!")
    else:
        slide(runner, distance=40, delay=0.04)
        print("You run as fast as you can and escape. Phew!")


game()
