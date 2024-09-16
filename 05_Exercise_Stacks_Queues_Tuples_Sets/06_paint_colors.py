from collections import deque

substrings = deque(input().split())

color_combinations = {
    "valid_colors": ("red", "yellow", "blue", "orange", "purple", "green"),
    "secondary_colors": {
        "orange": ("red", "yellow"),
        "purple": ("red", "blue"),
        "green": ("yellow", "blue")
    }
}

output_colors = []

while substrings:
    end_part = ""
    if len(substrings) > 1:
        end_part = substrings.pop()
    start_part = substrings.popleft()

    for combined_color in (start_part + end_part, end_part + start_part):
        if combined_color in color_combinations["valid_colors"]:
            output_colors.append(combined_color)
            break
    else:
        for part in (start_part[:-1], end_part[:-1]):
            if part:
                substrings.insert(len(substrings) // 2, part)

for secondary, required in color_combinations["secondary_colors"].items():
    if any(comp not in output_colors and secondary in output_colors for comp in required):
        output_colors.remove(secondary)

print(output_colors)
