# Q4

N, k = map(int, input().split())
arr = list(map(int, input().split()[:N]))
mx = -682368
for i in range(N):
    pizza_bob_can_eat = [arr[i]]
    diff_ele_count = 1

    for j in range(i + 1, N - 1):
        if arr[j] in pizza_bob_can_eat:
            pizza_bob_can_eat.append(arr[j])
        else:
            if diff_ele_count < k - 1:
                pizza_bob_can_eat.append(arr[j])
                diff_ele_count += 1
            else:
                ln = len(pizza_bob_can_eat)
                if mx < ln:
                    mx = ln
                break

    # print(pizza_bob_can_eat)
print(mx)
