def printer_error(s):
    bad_count = 0
    for i in s:
        if i > "m":
            bad_count += 1
    return f"{bad_count}/{len(s)}"
