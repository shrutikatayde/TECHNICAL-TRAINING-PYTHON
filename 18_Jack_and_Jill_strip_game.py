# FIRST APPROACH
# 23


def strip_game(N, jack_Strip, jill_Strip):
    jack_score = 0
    jill_score = 0

    for i in range(N):
        if i % 2 == 0:
            for x in range(N - 1):
                jack_score += jack_Strip[x]
        else:
            for c in range(N - 1):
                jill_score += jill_Strip[c]

    if jack_score > jill_score:
        print("jack win")
    elif jack_score == jill_score:
        print("Tie")
    else:
        print("jill win")


N = int(input())
jack_Strip = list(map(int, input().split()))
jill_Strip = list(map(int, input().split()))
jack_Strip.sort(reverse=True)
jill_Strip.sort(reverse=True)
strip_game(N, jack_Strip, jill_Strip)


# SECOND APPROACH

# N = int(input())
# jack_Strip = list(map(int, input().split()))
# jill_Strip = list(map(int, input().split()))
# jack = sum(jack_Strip)
# jill = sum(jill_Strip)
# # for i in range(N - 1):
# #     jack = jack_Strip[i] + jack_Strip[i + 1]
# #     jill = jill_Strip[i] + jill_Strip[i + 1]
#
# if jack > jill:
#     print("jack win")
# elif jack == jill:
#     print("Tie")
# else:
#     print("jill win")
