from typing import Iterable, Any, List


def unique_in_order(sequence: Iterable[Any]) -> List[Any]:
    result = []
    last_seen = object()  # A sentinel value that won't appear in the sequence
    for item in sequence:
        if item != last_seen:
            result.append(item)
            last_seen = item
    return result


###
from itertools import groupby


def unique_in_order(sequence):
    return [key for key, _ in groupby(sequence)]


###
def unique_in_order(sequence):
    if not sequence:  # Handle empty sequence immediately
        return []

    result = [sequence[0]]  # Start with the first element
    for item in sequence[1:]:  # Iterate from the second element onward
        if item != result[-1]:  # Compare with the last added element
            result.append(item)
    return result
