import numpy
from atom import Atom
from constants import ANGSTROM, ARGON_DIAMETER

class Environment:
    def __init__(self, name, dimensions=None):
        if dimensions is None:
            dimensions = numpy.array([[numpy.inf] * 3])

        self.name = name
        self.population = []
        self.__population_index = dict()

        self.dimensions = dimensions

    def __len__(self):
        return len(self.population)

    def __iter__(self):
        for x in self.population:
            yield x

    def __repr__(self):
        return '{} ({})'.format(self.name, len(self))

    def __str__(self):
        return repr(self)

    @property
    def infinite_box(self):
        return numpy.inf in self.dimensions

    def position_helper(self, directive):
        r = numpy.array((0, 0, 0))

        dimensions = self.dimensions
        if self.infinite_box:
            dimensions = numpy.array((5, 5, 5)) * ANGSTROM  # mais ou menos uns 100 atomos de argonio

        if directive == 'randomize':
            r = numpy.random.rand(1, 3)
            r = numpy.multiply(r, dimensions)
        elif directive == 'impenetrability':
            raise NotImplementedError('"Impenetrability" directive for populate function is not implemented')

        return r

    def populate(self, N, position=None):
        if N is None:
            raise NotImplementedError("Not implemented empty population")

        for i in range(N):
            r = self.position_helper(position)

            x = Atom(position=r, environment=self)
            self.__population_index[x.id] = x
