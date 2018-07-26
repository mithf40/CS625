from hashlib import md5


def power(h, m):
    return md5(h.encode('utf-8') + m.encode('utf-8')).hexdigest()[:4]


def val(hl, m, hr):
    return power(hl, m), power(hr, m)


def AHash(hl, hr, M):
    message = list(map(''.join, zip(*[iter(M)] * 4)))
    for m in message:
        hl, hr = val(hl, m, hr)
        print hl, hr
        # print hr
    return hl + hr

hl1 = '0001'
hr1 = '630d'
m1 = '1c4e72f08a8078e1'



hl = '56fe'
hr = '03a8'
m = '3291388610185168'
# thanos = AHash('7575', 'a8a8', '7368617269666374')
# print thanos
print(AHash(hl, hr, m))

print(AHash(hl1, hr1, m1))
