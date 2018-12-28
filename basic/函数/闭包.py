from urllib.request import urlopen


def urltemplate(template):
    def opener(**kwargs):
        print(template.format_map(kwargs))
        return urlopen(template.format_map(kwargs))

    return opener


baidu = urltemplate('http://www.baidu.com?s={names}&f={fields}')
print(baidu(names='li', fields='kai'))
