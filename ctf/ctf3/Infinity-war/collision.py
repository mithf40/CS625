from hashlib import md5

def foo(h, m):
    return md5(h.encode('utf-8') + m.encode('utf-8')).hexdigest()[:4]

hl = 'ffd6'
hr = '6287'
message = ''
for _ in range(4):
    found = False
    for i in xrange(2 ** 16):
        if found: break
        for j in xrange(2 ** 16):
            if found: break
            l = '{:04x}'.format(i)
            m = '{:04x}'.format(j)
            if foo(l, m) == hl:
                for k in xrange(2 ** 16):
                    r = '{:04x}'.format(k)
                    if foo(r, m) == hr:
                        found = True
                        message = m + message
                        hl = l
                        hr = r
                        break
print('message: {}, hl: {}, hr: {}'.format(message, hl, hr))