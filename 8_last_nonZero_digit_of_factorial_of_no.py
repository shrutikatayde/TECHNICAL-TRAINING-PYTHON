def fact(n):
    fact = 1
    arr = []
    for i in range(1, n + 1):
        fact *= i
    fact = str(fact)
    print(fact)
    for i in range(len(fact)):
        arr.append(fact[i])

    for i in range(len(arr) - 1, 0, -1):
        if arr[i] != "0":
            return arr[i]


n = int(input())
print(fact(n))
