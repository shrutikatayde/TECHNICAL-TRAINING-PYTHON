# Input : 1 15
# output : 22 :: 45


def time_in_h_m(h, m):

    hour_in_min = h * 60 + m

    if h > 24:
        total_hour = 24 - h

        h_upd = int(total_hour)  # converted into hour
        m_upd = m  # converted into

    else:
        total_hour = 24 * 60 - hour_in_min

        h_upd = int(total_hour / 60)  # converted into hour
        m_upd = total_hour % 60  # converted into

    return f"{h_upd} :: {m_upd}"

    #     ANOTHER APPROACH

    # if h > 24:
    #     h = h - 24
    #     print("-", h, "::", m)
    # else:
    #     h = 24 - h
    #     if m != 0:
    #         m = 60 - m
    #         h -= 1
    #     print(h, "::", m)


if __name__ == "__main__":
    h = int(input())
    m = int(input())
    res = time_in_h_m(h, m)
    # print(res)
