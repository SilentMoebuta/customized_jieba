import math
# 2.828
with open('jieba.dict.utf8', 'r', encoding='utf-8') as handle:
    text = handle.readlines()
with open('hmm_model.utf8', 'r', encoding='utf-8') as handle:
    model = handle.readlines()

bd = model[27].strip('\n').split(',')
bd = [x.split(':') for x in bd]
bd = dict(zip([x[0] for x in bd], [x[1] for x in bd]))
md = model[31].strip('\n').split(',')
md = [x.split(':') for x in md]
md = dict(zip([x[0] for x in md], [x[1] for x in md]))
ed = model[29].strip('\n').split(',')
ed = [x.split(':') for x in ed]
ed = dict(zip([x[0] for x in ed], [x[1] for x in ed]))
sd = model[33].strip('\n').split(',')
sd = [x.split(':') for x in sd]
sd = dict(zip([x[0] for x in sd], [x[1] for x in sd]))


def func(x):
    return int(math.sqrt(x))*10


def res_merge(ab):
    ab = sorted(ab, key=lambda x: x[0], reverse=True)
    res = [ab[0]]
    for i in range(1, len(ab)):
        if res[-1][0] == ab[i][0]:
            res[-1][1] += ab[i][1]
        else:
            res.append(ab[i])
    return res


text = [x.strip(' n\n').split(' ') for x in text]
word = []
for x in text:
    if len(x[0]) <= 4:
        word.append(x)
tk = [x[0] for x in word]
tv = [func(int(x[1])) for x in word]
B, M, E, S = [], [], [], []
for i in range(len(tk)):
    if len(tk[i]) == 1:
        S.append([tk[i], tv[i]])
    elif len(tk[i]) == 2:
        B.append([tk[i][0], tv[i]])
        E.append([tk[i][1], tv[i]])
    elif len(tk[i]) == 3:
        B.append([tk[i][0], tv[i]])
        M.append([tk[i][1], tv[i]])
        E.append([tk[i][2], tv[i]])
    else:
        B.append([tk[i][0], tv[i]])
        M.append([tk[i][1], tv[i]])
        M.append([tk[i][2], tv[i]])
        E.append([tk[i][3], tv[i]])
B = res_merge(B)
M = res_merge(M)
E = res_merge(E)
S = res_merge(S)
bs = sum([x[1] for x in B])
ms = sum([x[1] for x in M])
es = sum([x[1] for x in E])
ss = sum([x[1] for x in S])
B = [[x[0], round(math.log(x[1]/bs, 2.828), 6)] for x in B]
M = [[x[0], round(math.log(x[1]/ms, 2.828), 6)] for x in M]
E = [[x[0], round(math.log(x[1]/es, 2.828), 6)] for x in E]
S = [[x[0], round(math.log(x[1]/ss, 2.828), 6)] for x in S]
print(B[:5], len(B), bs)
print(M[:5], len(M), ms)
print(E[:5], len(E), es)
print(S[:5], len(S), ss)
for x in B:
    bd[x[0]] = str(x[1])
for x in M:
    md[x[0]] = str(x[1])
for x in E:
    ed[x[0]] = str(x[1])
for x in S:
    sd[x[0]] = str(x[1])

bd_s = ''
bd_k = list(bd.keys())
bd_v = list(bd.values())
for i in range(len(bd)):
    bd_s += bd_k[i]+':'+bd_v[i]+','
md_s = ''
md_k = list(md.keys())
md_v = list(md.values())
for i in range(len(md)):
    md_s += md_k[i]+':'+md_v[i]+','
ed_s = ''
ed_k = list(ed.keys())
ed_v = list(ed.values())
for i in range(len(ed)):
    ed_s += ed_k[i]+':'+ed_v[i]+','
sd_s = ''
sd_k = list(sd.keys())
sd_v = list(sd.values())
for i in range(len(sd)):
    sd_s += sd_k[i]+':'+sd_v[i]+','
model[27] = bd_s + '\n'
model[29] = md_s + '\n'
model[31] = ed_s + '\n'
model[33] = sd_s + '\n'

with open('hmm_model.utf8', 'w', encoding='utf-8') as handle:
    handle.writelines(model)
