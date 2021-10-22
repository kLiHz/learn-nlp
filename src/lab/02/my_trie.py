def insert(node, s):
    current = node
    for c in s:
        if c not in current:
            current[c] = dict()
        current = current[c]
    current['end'] = True


def find(node, s):
    for c in s:
        if c not in node:
            return False
        node = node[c]
    return 'end' in node


def traverse(node, s=''):
    for key in node.keys():
        if key == 'end':
            continue
        s += key
        yield from traverse(node[key], s)
        s = s[:-1]
    if 'end' in node:
        yield s

