def fill_the_box(*args):
    side1, side2, side3, *commands = args
    cube_size = side1 * side2 * side3
    cube_fill = 0
    for command in commands:
        if command == "Finish":
            break
        cube_fill += command
    if cube_size > cube_fill:
        return f"There is free space in the box. You could put {cube_size - cube_fill} more cubes."
    else:
        return f"No more free space! You have {cube_fill - cube_size} more cubes."