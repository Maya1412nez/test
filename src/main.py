a = [90,6,600]

if len(a) > 0:
    m, n = a[0], None
    for i in range(len(a)):
        if not n and a[i] < m:
            n = a[i]
        if a[i] > m:
            n = m
            m = a[i]
        if n:
            if n < a[i] < m:
                n = a[i]
        if i == len(a) - 1 and not n:
            n = m
    print(n)
else:
    print('[dfnbn ghbrfksdfnmcz')

# for i in range(len(a)):
#     if not n and a[i] > m:
#         n = a[i]
#         print(i)
#     if a[i] < m:
#         n, m = m, a[i]
#     if n:
#         if n > a[i] > m:
#             n = a[i]
#     if i == len(a) - 1 and not n:
#         n = m
# print(n)


"""
if len(a) > 0:
    m, n = a[0], None
    for i in range(len(a)):
        if a[i] is int or a[i] is float:
            if not n and a[i] < m:
                n = a[i]
            if a[i] > m:
                n = m
                m = a[i]
            if n:
                if n < a[i] < m:
                    n = a[i]
            if i == len(a) - 1 and not n:
                n = m
    print(n)
else:
    print('nope')
"""
