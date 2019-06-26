from atom import Atom
from environment import Environment
from constants import round

def simulate(env, tI=0, tN=10):
    rI = round(tI)
    rN = round(tN)

    print('Simulation for {}, from {}s ({}) to {}s ({})'.format(env, tI, rI, tN, rN))
    for r in range(rI, rN):
        print(r)

E = Environment('A')
E.populate(1)

simulate(E)