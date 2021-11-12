from bigram_model import *

# disambiguation

class WordMap:
    """
    Word map is a list of sets.

    For example: After adding two seg_list into the word map named 'l': 

    ```
    ['他', '是', '研究生', '物', '的'],
    ['他', '是', '研究', '生物', '的']
    ```

    The word map might be like:

    ```
    l[/]: {'<BOS>'}
    l[0]: {'他'}
    l[1]: {'是'}
    l[2]: {'研究', '研究生'}
    l[3]: {}
    l[4]: {'生物'}
    l[5]: {'物'}
    l[6]: {'的'}
    l[/]: {'<EOS>'}
    ```
    """

    def __init__(self, s_len) -> None:
        self.l = []
        for i in range(s_len):
            self.l.append(list())
            # self.l.append(set())


    def add_to_word_map(self, seg_list):
        sentence_len = len("".join(seg_list))
        assert sentence_len == len(self.l)
        i = 0
        for seg in seg_list:
            if seg not in self.l[i]:
                self.l[i].append(seg)
            i += len(seg)
    

    def all_possible_combinations(self):
        def dfs(i, seg_list):
            if i == len(self.l):
                # yield 时注意拷贝列表
                yield seg_list + [EOS]
                return
            
            if len(self.l[i]) > 0:
                for w in self.l[i]:
                    seg_list.append(w)
                    yield from dfs(i + len(w), seg_list)
                    seg_list.pop()
            else:
                yield from dfs(i + 1, seg_list)
        
        return dfs(0, [BOS])


    def all_possible_combinations_with_probability(self, model):
        def dfs(i, seg_list, current_p):
            if i == len(self.l):
                yield {
                    "l": seg_list + [EOS],
                    "p": current_p * model.calc_probabilty((seg_list[-1], EOS), "ADD_ONE")
                }
                return
            
            if len(self.l[i]) > 0:
                for w in self.l[i]:
                    seg_list.append(w)
                    yield from dfs(i + len(w), seg_list, current_p * model.calc_probabilty((seg_list[-1], w), "ADD_ONE"))
                    seg_list.pop()
            else:
                yield from dfs(i + 1, seg_list, current_p)
        
        return dfs(0, [BOS], 1)

