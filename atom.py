import numpy
import uuid
from constants import T, round, DELTA_T as dt, ARGON_WEIGHT
from functions import potencial_lennard_jones, distancia_euclidiana


INFLUENCES = [
    'force'
]

def array(value):
    if isinstance(value, numpy.ndarray):
        return value
    elif isinstance(value, list):
        return numpy.array(value)
    else:
        a = numpy.empty(3)
        a.fill(value)
        return a

class Atom:
    def __init__(self, position=(0, 0, 0), mass=ARGON_WEIGHT, speed=0, acceleration=0, charge=0, environment=None):

        if environment is None:
            environment = []

        self.id = str(uuid.uuid1())

        self.environment = environment

        self._position = array(position)
        self._mass = mass
        self._speed = array(speed)
        self._acceleration = array(acceleration)
        self._charge = charge

        self._d_position = dict()
        self._d_speed = dict()
        self._d_acceleration = dict()
        self._d_charge = dict()

        self._d_intermolecular_interaction = dict()

        self._d_externals = dict()

        self.calculate(0)

    def __repr__(self):
        return '{} ({})'.format(self.id, self.environment)

    def snapshot(self, t=None, r=None):
        r = round(t) if t is not None else r
        return '{} (pos={}, vel={}, acc={})'.format(self.id, self.position(r=r), self.speed(r=r), self.acceleration(r=r))

    # getters

    def get_variable(self, variable, t=None, r=None):
        r = round(t) if t is not None else r

        return getattr(self, '_d_{}'.format(variable))[r]

    def position(self, t=None, r=None):
        return self.get_variable('position', t, r)

    def speed(self, t=None, r=None):
        return self.get_variable('speed', t, r)
        
    def acceleration(self, t=None, r=None):
        return self.get_variable('acceleration', t, r)
        
    def charge(self, t=None, r=None):
        return self.get_variable('charge', t, r)

    def intermolecular_interaction(self, t=None, r=None):
        return self.get_variable('intermolecular_interaction', t, r)

    def externals(self, t=None, r=None):
        r = round(t) if t is not None else r

        if r not in self._d_externals:
            return []
        return self._d_externals[r]

    # setters

    def influence(self, influence, source, t=None, r=None):
        r = round(t) if t is not None else r

        if influence not in INFLUENCES:
            raise NotImplementedError('Not implemented for influence "{}"'.format(influence))

        if self._d_externals[r] is None:
            self._d_externals[r] = dict()
        
        if self._d_externals[r][influence] is None:
            self._d_externals[r][influence] = []
        
        self._d_externals[r][influence].append(source)

    # functions

    def distance(self, other, t=None, r=None, norm=True):
        r = round(t) if t is not None else r

        return self.position(r=r) - other.position(r=r) if not norm else distancia_euclidiana(self.position(r=r), other.position(r=r))

    def calculate(self, t=None, r=None):
        t = round(t) if t is not None else r

        if t < 0:
            raise NotImplementedError('< 0 HAHA')

        externals = self.externals(r=t)

        m = self._mass

        if t == 0:
            r = self._position
            v = self._speed
            a = self._acceleration
            q = self._charge

            fi = array(0)
        else:
            ti = t - 1

            ri = self.position(r=t-1)
            vi = self.speed(r=t-1)
            ai = self.acceleration(r=t-1)
            qi = self.charge(r=t-1)

            '''
            acho que é a ideia aqui é:
                as forças intermoleculares - ??? - agem sobre a molecula
                força é massa vezes aceleração, então a força implica uma aceleracao
                a aceleracao implica uma velocidade
                que vai mudar a posicao da molecula
            '''

            # para ligar com as forças intermoleculares eu preciso criar uma mesh
            # com todos os campos em atuação no instante

            # na verdade seria um loop por todas as moleculas vizinhas, juntando os vetores de potencial elétrico?

            # isso ai

            fi = numpy.array([potencial_lennard_jones(self.distance(other, r=t-1, norm=False)) for other in self.environment if other.id != self.id])
            fi = numpy.sum(fi) if len(self.environment) > 0 else numpy.zeros(3)

            f = fi.copy()
            if 'force' in externals:
                fe = externals['force']
                f += numpy.sum(fe)

            # ok, mas e a carga??? 
            # argonio é um gas inerte, entao ignora isso

            a = f / m
            v = vi + a*dt
            r = ri + v*dt
            q = qi
        
        self._d_position[t] = r
        self._d_speed[t] = v
        self._d_acceleration[t] = a
        self._d_charge[t] = q

        self._d_intermolecular_interaction[t] = fi


