import random

# Unicode symbols
weapons = {'stone': '✊', 'paper': '✋', 'scissors': '✌'}

print("Choose from: ✊ (stone), ✋ (paper), ✌ (scissors)")

# Get user input
a = input("Enter your weapon: ").strip().lower()

# Validate input
if a not in weapons:
  print("Invalid choice! Please select stone, paper, or scissors.")
  exit()
