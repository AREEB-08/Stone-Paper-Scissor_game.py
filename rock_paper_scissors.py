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

# Computer choice
choices = list(weapons.keys())
b = random.choice(choices)
print(f"Computer chose {weapons[b]} ({b})")

# Game logic
if a == b:
    print("It's a draw!")
elif (a == 'stone' and b == 'scissors') or (a == 'paper' and b == 'stone') or (a == 'scissors' and b == 'paper'):
    print("You win!")
else:
    print("Computer wins!")
