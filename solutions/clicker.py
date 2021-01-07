# Example Clicker Game
import os

# Title screen UwU
print("Clicker Game UwU")
input("Press Enter to Start\n> ")

# Game powered on or off
game = True
score = 0
multiplier = 1
# Function that clears screen, optional
def clear():
  os.system("clear")
# Repeats while game = True
while game:
  clear()
  print("Score:", score, "| Power:", multiplier)
  text = input("> ")
  # Upgrade
  if text == "up":
    # Checks to make sure you have enough points to upgrade
    if score >= multiplier * 2:
      # Takes points from score
      score -= multiplier * 2
      # Increases multiplier
      multiplier += 1
  # If the person just presses enter
  elif text == "":
    # Increases score
    score += multiplier