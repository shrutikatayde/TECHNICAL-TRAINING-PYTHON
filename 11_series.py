def series(N, a, b, c, d):
    arr_for_b = []
    arr_for_d = []

    # Generate the series for b and d
    for i in range(N):
        arr_for_b.append(b + i * a)
        arr_for_d.append(d + i * c)

    # Compare the elements in the series
    for i in range(N):
        for j in range(N):
            if arr_for_b[i] == arr_for_d[j]:
                return arr_for_b[i]


if __name__ == "__main__":
    N = int(input("Enter the value of N: "))
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))
    d = int(input("Enter the value of d: "))

    result = series(N, a, b, c, d)
    print(result)
