def grocery_store(**kwargs):
    sorted_items = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    receipt = '\n'.join(f"{product}: {quantity}" for product, quantity in sorted_items)

    return receipt
