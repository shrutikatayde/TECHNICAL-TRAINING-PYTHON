# Q. 29

# N = int(input())
# x = int(N ** 0.5)
# count = 0
# for i in range(1,x, -1):  # n**0.5 means square-root of n --> if n=14 then SR -> int(3.74) + 1 = 3+1
#     if N % i == 0 and N // i != i:
#         count += 1
# print(count)

N = int(input())
count = 0
for i in range(N, 0, -1):
    if N % i == 0 and N // i != i:
        count += 1
print(count // 2)

# N = int(input())
# count = 0
# for i in range(1, 9 + 1):
#     if N % i == 0 and N // i != i:
#         count += 1
# print(count)
