def sort_array(source_array):
    odds = iter(sorted(x for x in source_array if x % 2 != 0))
    return [next(odds) if x % 2 != 0 else x for x in source_array]
        
