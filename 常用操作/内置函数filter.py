values = [1, 3, 6, '-', 2, 'N/A', 10, 8, 11, 'N']


def is_int(value):
    try:
        x = int(value)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)
