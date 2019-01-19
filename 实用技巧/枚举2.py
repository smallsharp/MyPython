from enum import IntEnum, unique


@unique
class VIP(IntEnum):
    YELLOW = 1
    # GREEN = 1 # ValueError: duplicate values found in <enum 'VIP'>: GREEN -> YELLOW

    BLACK = 'black'  # ValueError: invalid literal for int() with base 10: 'black'


print(VIP.BLACK.value)
