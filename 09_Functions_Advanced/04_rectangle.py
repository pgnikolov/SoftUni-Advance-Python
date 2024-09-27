def rectangle(width, height):
    if  isinstance(width, int) and  isinstance(height, int):
        area = width * height
        perimeter = 2 * (width + height)
        return f"Rectangle area: {area}\nRectangle perimeter: {perimeter}"
    else:
        return "Enter valid values!"
    