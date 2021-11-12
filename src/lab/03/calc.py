special_characters = set(list(
    "()[]+-*/<>|\\;:\"\'\,.?!@#$%^&~`\{\}（）【】《》，。？“”‘’；：——「」『』〔〕"
))

#包括部分特殊字符，在进行分词比对时将特殊字符排除，以免对结果产生一定的影响

def calc_hits(truth, result):
    # 传入分词得到的结果（列表），以及“正确分词”结果
    cut_truth = [item for item in truth if item not in special_characters]
    cut_result = [item for item in result if item not in special_characters]
    i = 0       # 指向 truth 中的 token
    j = 0       # 指向 result 中的 token
    l1 = 0      # i 所指向词串，对应在原句中的长度
    l2 = 0      # j 所指向词串，对应在原句中的长度
    hits = 0
    missmatches = set()
    while i < len(cut_truth) and j < len(cut_result):
        if l1 < l2:
            l1 += len(cut_truth[i])
            i += 1
        elif l1 > l2:
            l2 += len(cut_result[j])
            j += 1
        else: 
            if cut_truth[i] == cut_result[j]:
                hits += 1
            else:
                # 记录未匹配到的“新词”
                missmatches.add(cut_truth[i])
            l1 += len(cut_truth[i])
            i += 1
            l2 += len(cut_result[j])
            j += 1
    
    return hits, len(truth), len(result), missmatches


def calc_PRF(hits, truth_len, result_len):
    P = hits / result_len       # precision
    R = hits / truth_len        # recall
    F = (2 * P * R) / (P + R)   # F_1
    return P, R, F
