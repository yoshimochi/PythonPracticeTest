# ジェネレータ

# 通常の関数
def multpliter(values):
    ret = []
    for i in values:
        ret.append(2 ** i)
    return ret


values = [0, 1, 2, 3, 4, 5]
ret = multpliter(values)
print(ret)


# ジェネレーターで表すと

def multpliter2(values2):
    for i in values2:
        yield 2 ** i


values2 = [0, 1, 2, 3, 4, 5]
ret2 = multpliter2(values2)

for i in ret2:
    print(i)