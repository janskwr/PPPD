def merge(x, y):
    u = []
    v = []
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                u.append(i)
                v.append(j)
    return [u, v]


def merge_sprytny(x, y):
    x.sort()
    y.sort()
    u = []
    v = []
    pointer_x = 0
    pointer_y = 0
    assert len(x) > 0 and len(y) > 0
    while pointer_x < len(x) and pointer_y < len(y):
        if x[pointer_x] < y[pointer_y]:
            pointer_x += 1
            continue
        if y[pointer_y] < x[pointer_x]:
            pointer_y += 1
            continue
        start_x = pointer_x
        start_y = pointer_y
        while pointer_x < len(x) and x[start_x] == x[pointer_x]:
            pointer_x += 1
        while pointer_y < len(y) and y[start_y] == y[pointer_y]:
            pointer_y += 1
        end_x = pointer_x
        end_y = pointer_y
        for index_x in range(start_x, end_x):
            for index_y in range(start_y, end_y):
                u.append(index_x)
                v.append(index_y)
    return [u, v]


def main():
    x = [1, 3, 3, 5, 6]
    y = [1, 2, 3, 4, 5, 5]
