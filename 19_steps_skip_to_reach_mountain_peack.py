# RECURSION CONCEPT
# Q7
# def rec(i):
#     if i == 1:
#         print(i)
#         return
#     rec(i - 1)
#     print(i)   ---> PRINT 1 2 3 WHY ? ---->>>> BECAUSE IS IS PRINTING AFTER THE RECURSION CALL
#
# print(rec(3))


def count_the_ways_to_climb(N, I, X):

    Ways = [0] * (N + 1)

    Ways[I] = 1
    for i in range(I, N + 1):
        if Ways[I] == 0:
            continue
        for j in range(1, X + 1):
            if i + j <= N:
                Ways[i + j] += Ways[i]

    return Ways[N]


N = int(input())
I = int(input())
X = int(input())
Ways = count_the_ways_to_climb(N, I, X)
print(Ways)


# def count_the_ways_to_climb(N, I, X):
#
#     Ways = 0
#     if I == N:
#         return 1
#     if N < I:
#         return 0
#
#     for i in range(1, X + 1):
#         Ways += count_the_ways_to_climb(N, I + i, X)
#
#     return Ways
#
#
# N = int(input())
# I = int(input())
# X = int(input())
# Ways = count_the_ways_to_climb(N, I, X)
# print(Ways)
