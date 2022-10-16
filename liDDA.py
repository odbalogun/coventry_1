def liDDA(a, b, c, d):
    P = []
    e = c-a
    f = d-b
    s = max(e, f)
    x, y = a, b

    for i in range(s):
        P.append((round(x), round(y)))
        x += e/s
        y += f/s
    print(P)
    # [(0, 1), (1, 2), (2, 2), (3, 2), (4, 3), (5, 4)]


liDDA(0, 1, 6, 4)
