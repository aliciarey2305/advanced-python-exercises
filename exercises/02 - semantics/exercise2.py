

def hailstone(n):
    hailstone_seq = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            hailstone_seq.append(n)
        else:
            n = 3 * n + 1
            hailstone_seq.append(n)
    return hailstone_seq

print(hailstone(27))

hailstone_dict = {n:len(hailstone(n)) for n in range(1,50)}


print(hailstone_dict)

hailstone_dict_million = {n:len(hailstone(n)) for n in range(1,1000000)}
hailstone_len_max = max(hailstone_dict_million.values())

hailstone_n_max = [key for (key, value) in hailstone_dict_million.items() if value == hailstone_len_max]

print(hailstone_n_max[0], hailstone_len_max, len(hailstone(hailstone_n_max[0])))