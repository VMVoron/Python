for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [0]*(2*10**5+1)
    max_possible_water = 0
    for i in range(n):
        x, p = map(int, input().split())
        a[x] = p
        max_possible_water += p
        if max_possible_water > m:
            print("0", end="")
            for j in range(i+1, n):
                input()
            break
    else:
        can_remove = [1]*n
        rain_left = max_possible_water
        for i in range(1, len(a)):
            rain_left -= a[i-1]
            if rain_left > m:
                can_remove[i-1] = 0
            rain_left = min(rain_left, max_possible_water)
        print("".join(map(str, can_remove)))
