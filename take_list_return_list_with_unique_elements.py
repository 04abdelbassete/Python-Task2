def unique(taken_list:list):
    ''' taking a list and returning a list with unique elements '''
    unique_list = []
    for item in taken_list:
        if item in unique_list:
            continue
        unique_list.append(item)
    return unique_list
