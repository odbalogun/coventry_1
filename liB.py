def liB(a, b, c, d):
    P = []
    e = c-a
    f = d-b
    g = 2*f - e
    y = b

    for x in range(a, c+1):
        P.append((x, y))
        if (g > 0):
            y += 1
            g = g - 2*e  # -6
        g = g + 2*f  # 6
    print(P)
    # [(0, 1), (1, 1), (2, 2), (3, 2), (4, 3), (5, 3), (6, 4)]


liB(0, 1, 6, 4)
