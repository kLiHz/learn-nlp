import my_trie as trie

root = { 'c': '', 'children':dict(), 'cnt': 0 }

trie.insert(root, 'apple')
trie.insert(root, 'loop')
trie.insert(root, 'app')

test_cases = [
    ('a', False),
    ('ap', False),
    ('app', True),
    ('appl', False),
    ('apple', True),
    ('l', False),
    ('lo', False),
    ('loo', False),
    ('loop', True),
    ('loopa', False),
    ('loopan', False)
]

for t in test_cases:
    print(t[0], '\tExpected: ', t[1], '\tGot: ', trie.find(root, t[0]))

print('All words:')

trie.traverse(root)
