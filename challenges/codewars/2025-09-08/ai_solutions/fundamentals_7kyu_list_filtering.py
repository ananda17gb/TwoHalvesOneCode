# it change the parameter from l to lst

def filter_list(lst):
    return [x for x in lst if isinstance(x, int)]

def filter_list(lst):
    return [x for x in lst if type(x) is int]

def filter_list(lst):
    return list(filter(lambda x: isinstance(x, int), lst))

def filter_list(lst):
    return [x for x in lst if isinstance(x, int) and x >= 0]
