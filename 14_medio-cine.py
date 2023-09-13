N, L = map(int, input().split())
arr = list(map(int, input(f"Enter age of {N} humans : ").split()[:N]))
n1 = N // L
n2 = N % L

print(n1 + n2, "Days")

# or
# if n1!= 0:
#     print(n1 + n2, "Days")
# else:
#     print(n1, "Days")
