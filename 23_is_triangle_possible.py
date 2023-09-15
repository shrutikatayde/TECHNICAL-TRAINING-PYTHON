def is_triangle_possible(n, m, k):
    T = (n * m) // k
    if T <= 0 or (n * m) % k != 0:
        return False
    return True


n, m, k = map(int, input().split())
res = is_triangle_possible(n, m, k)
if res:
    print("YES")
else:
    print("NO")
