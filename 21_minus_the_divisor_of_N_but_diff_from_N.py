# Q 28

# N = int(input())
# ct = 0
#
# for i in range(N):
#     if i % 2 == 0:
#         N = N - i
#         ct += 1
#
# print(ct)


def minus(N):
    val = 1
    for i in range(N - 1, 0, -1):
        if N % i == 0:
            val = i
            break
    return val


N = int(input())
ct = 0

while N != 0:
    res = minus(N)
    N = N - res
    ct += 1

print(ct)
