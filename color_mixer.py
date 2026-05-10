"""

Mallory Rich 
IS 303

Color Mixer
Tells the user what color they get by mixing two primary colors

INPUTS
- color 1
- color 2

PROCESSES
- Red+blue=purple, red+yellow=orange, blue+yellow=green
- same+same=that color
- invalid colors rejected

OUTPUTS
- color 1
- color 2
- color 3

"""

#INPUTS
color_1 = input("Pick one primary color to mix with (red, yellow, blue): ").lower()
color_2 = input("Pick a second primary color to mix with (red, yellow, blue): ").lower()

#INPUT VALIDATION
is_valid = True

if not (color_1 == "red" or color_1 == "yellow" or color_1 == "blue") or not (color_2 == "red" or color_2 == "yellow" or color_2 == "blue"):
    print("You have entered an invalid color. Please enter red, yellow, or blue.")
    is_valid = False

#PROCESSES
if color_1 == "red":
    if color_2 == "red":
        color_3 = "red"
    elif color_2 == "yellow":
        color_3 = "orange"
    elif color_2 == "blue":
        color_3 = "purple"
elif color_1 == "yellow":
    if color_2 == "red":
        color_3 = "orange"
    elif color_2 == "yellow":
        color_3 = "yellow"
    elif color_2 == "blue":
        color_3 = "green"
elif color_1 == "blue":
    if color_2 == "red":
        color_3 = "purple"
    elif color_2 == "yellow":
        color_3 = "green"
    elif color_2 == "blue":
        color_3 = "blue"

#OUTPUTS
if is_valid:
    print(f"You get {color_3} when you mix {color_1} amd {color_2}.")