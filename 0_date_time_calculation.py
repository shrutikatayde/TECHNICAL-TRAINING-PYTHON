def time_in_h_m(h, m):

    hour_in_min = h * 60 + m

    total_hour = 24 * 60 - hour_in_min

    h_upd = int(total_hour / 60)
    m_upd = total_hour % 60

    return f"{h_upd} :: {m_upd}"


if __name__ == "__main__":
    h, m = map(int, input("Enter hour and minute: ").split())
    res = time_in_h_m(h, m)
    print(res)
