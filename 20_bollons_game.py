# Q17


def Ballon_game(N, K, arr):
    number_of_destroyed_grp = 0
    rounds = 0

    while number_of_destroyed_grp < K and (N - number_of_destroyed_grp) >= K:
        arr.sort(reverse=True)
        # print(arr)
        for i in range(K):
            arr[i] = arr[i] - 1
        rounds += 1
        # print(arr)
        for i in range(K):
            if arr[i] == 0:
                number_of_destroyed_grp += 1

        """print("DES GRP : ", number_of_destroyed_grp)
        print("Rounds", rounds)"""
    return rounds


if __name__ == "__main__":
    N = int(input())
    K = int(input())

    arr = []
    for i in range(N):
        arr.append(int(input()))
    res = Ballon_game(N, K, arr)
    print(res)
