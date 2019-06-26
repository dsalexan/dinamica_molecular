FEMTO = 10**-15  # SI femto < pico

ANGSTROM = 10**-10  # (A == 10**-10 m)
ATOMIC_MASS_UNIT = 1.66053906660 * 10**-27  # (u = 1.66 * 10**-27 kg)

DELTA_T = 2 * FEMTO  # s
K = 9 * 10**9  # N·m2/C2
R0 = 3.82 * ANGSTROM  # m 
U0 = 1.68 * 10**-21  # J

ARGON_RADIUS = 0.88 * ANGSTROM
ARGON_DIAMETER = ARGON_RADIUS * 2
ARGON_WEIGHT = 39.948 * ATOMIC_MASS_UNIT


def T(r):
    return float(r) * DELTA_T


def round(t):
    return int(t / DELTA_T)

