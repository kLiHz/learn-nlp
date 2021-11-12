from word_map import WordMap

cut1 = ['他', '是', '研究生', '物', '的']
cut2 = ['他', '是', '研究', '生物', '的']

m = WordMap(len("".join(cut1)))

m.add_to_word_map(cut1)
m.add_to_word_map(cut2)

print(m.l)

for l in m.all_possible_combinations():
    print(l)
