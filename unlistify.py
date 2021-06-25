def unlistify(some_list):
    """
    Takes a given list and removes the element that's a list at the end of some_list
    """
    new_list = []
    for item in some_list:
        new_list += item
    return new_list
