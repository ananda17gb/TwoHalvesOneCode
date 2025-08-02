def find_next_square(sq):
    if sq < 0:
        return -1  # Handle negative input
    sqrt = sq ** 0.5
    if sqrt.is_integer():  # More explicit than comparing to int(sqrt)
        return (int(sqrt) + 1) ** 2
    return -1

