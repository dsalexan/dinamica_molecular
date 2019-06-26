from atom import Atom
from environment import Environment
from constants import round, T

from dev import timer

def simulate(env, t=None, r=None):
    r = r if r is not None else (round(t[0]), round(t[1]))
    t = t if t is not None else (T(r[0]), T(r[1]))
    
    msg = 'Simulation for {}, from {}s ({}) to {}s ({})'.format(env, t[0], r[0], t[1], r[1])
    print(msg)
    with timer() as elapsed_sim:
        for r in range(r[0], r[1]):
            t = T(r)

            print('{}'.format(r))
            
            with timer() as elapsed_loop:
                for x in env:
                    with timer() as elapsed_calc:
                        x.calculate(r=r)
                        
                        print('    {:180}'.format(x.snapshot(r=r)), end='')
                        print('{:.7f}ms'.format(elapsed_calc() / 1000))

                print('{:184}'.format('{} ({}s)'.format(r, t)), end='')
                print('total: {:.7f}ms'.format(elapsed_loop() / 1000))
    
    print('\n', end='')
    print('ENDED {:178}'.format(msg), end='')
    print('sim: {:.7f}ms'.format(elapsed_sim() / 1000))
        

E = Environment('A')
E.populate(2, position='randomize')

simulate(E, r=(0, 100))