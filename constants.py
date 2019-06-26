DELTA_T = 2 * 10**-15  # s
K = 9 * 10**9  # N·m2/C2


def T(round):
    return round * DELTA_T


def round(t):
    return t / DELTA_T

