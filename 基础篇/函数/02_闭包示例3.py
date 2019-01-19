from urllib.request import urlopen


def urltemplate(template):
    def opener(**kwargs):
        print(template.format_map(kwargs))
        return urlopen(template.format_map(kwargs))

    return opener


baidu = urltemplate('http://www.baidu.com?s={names}&f={fields}')
print(baidu(names='li', fields='kai'))

origin = 0


def factory(pos):
    def go(step):

        print(pos)
        # new_pos = pos + step
        # pos = new_pos
        # return new_pos

    return go


tour = factory(origin)
print(tour(10))
