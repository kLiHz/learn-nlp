def insert(node, s):
    current = node
    for c in s:
        if c not in current['children'].keys():
            current['children'][c] = { 'c': c, 'children':dict(), 'cnt': 0 }
        current = current['children'][c]
    current['cnt'] += 1


def find(node, s):
    for c in s:
        if c in node['children'].keys():
            node = node['children'][c]
        else:
            return False
    return node['cnt'] > 0


def traverse(node, s=''):
    for key in node['children'].keys():
        s += node['children'][key]['c']
        yield from traverse(node['children'][key], s)
        s = s[:-1]
    if node['cnt'] > 0:
        yield s

