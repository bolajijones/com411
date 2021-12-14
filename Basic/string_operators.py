#Read Bot Data
print(f"Please enter the number of lives")
number_of_lives = int(input())
print(f"Please enter the energy level")
energy_level = int(input())
print(f"Please enter the shield level")
shield_level = int(input())

# Display Bot Data
print(f"Lives:  {'♥' * number_of_lives}")
print(f"Energy: {'♦' * energy_level}")
print(f"Shield: {'♦' * shield_level}")
