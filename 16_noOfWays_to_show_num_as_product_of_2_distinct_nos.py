# Q. 29

N = int(input())
count = 0
for i in range(
    1, int(N ** 0.5) + 1
):  # n**0.5 means square-root of n --> if n=14 then SR -> int(3.74) + 1 = 3+1
    if N % i == 0 and N // i != i:
        count += 1
print(count)
