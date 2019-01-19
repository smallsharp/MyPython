# 字典代替类swtich，if...else...


choice = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday'
}

now = choice.get(3, 'unknown')
print(now)


def getDay(id: int):
    choice = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday'
    }
    return choice.get(id)

print(getDay(0))
