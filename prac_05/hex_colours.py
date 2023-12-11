"""
CP1404/CP5632 Practical
Hex Colours
"""

HEX_COLOURS = {"Black Coffee": "#3b2f2f", "Cadet Blue": "#53868b", "Carnelian": "	#b31b1b",
               "Celadon Green": "#2f847c", "Charcoal": "#36454f", "Crimson": "#dc143c",
               "Dark Orchid": "#68228b", "Dark Sea Green": "#698b69", "Eggplant": "#614051",
               "Eminence": "#6c3082"}

color = input("Enter color(With space): ").title()
while color != "":
    try:
        print(f"{color} is {HEX_COLOURS[color]}")
    except LookupError:
        print("Color hex code unavailable")
    color = input("Enter color(With space): ").title()
