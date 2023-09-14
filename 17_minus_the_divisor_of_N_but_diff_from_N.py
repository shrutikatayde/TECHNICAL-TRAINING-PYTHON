N = int(input())
ct = 0
d
for i in range(N):
    if i % 2 == 0:
        N = N - i
        ct += 1

print(ct)
