def commands(command, value, file):
    result = []
    if command == 'filter':
        result = list(filter(lambda val: value in val, file))
    if command == 'map':
        result = list(map(lambda val: val.split()[int(value)], file))
    if command == 'unique':
        result = list(set(file))
    if command == 'sort':
        if value == 'desc':
            result = sorted(file, reverse=True)
        elif value == 'asc':
            result = sorted(file)
    if command == 'limit':
        result = list(file)[:int(value)]
    return result


# x = [
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3]
# ]
#
# '''
# 1 2 3
# 1 2 3
# 1 2 3
# '''