def enough(cap, on, wait):
    return max(0, on + wait - cap)


def enough(cap, on, wait):
    total = on + wait
    return max(0, total - cap)
