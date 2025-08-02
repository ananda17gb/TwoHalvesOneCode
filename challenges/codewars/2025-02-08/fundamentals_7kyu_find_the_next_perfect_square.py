def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    sqrt = sq ** 0.5
    if (sqrt == int(sqrt)):
        return (int(sqrt)+1)**2
    return -1

