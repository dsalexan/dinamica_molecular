import numpy
from constants import DELTA_T as dT, K, U0, R0

# MATEMATICA

def distancia_euclidiana(a, b):
    return numpy.linalg.norm(a - b)


# FISICA

def potencial_eletrico(q, d):
    return K * q / d


def potencial_lennard_jones(d):
    # u0 * ((ro/r)**12 - 2(ro/r)**6)
    # truncado quando a distancia é maior que 2.5R0
    norm = numpy.linalg.norm(d)
    if norm > 2.5 * R0:
        return 0
    
    u = U0 * ( (R0/norm)**12 - 2*((R0/norm)**6) )
    return u * (d/norm)


def forca_classica(m, a):
    return m * a


def forca_em_funcao_do_potencial(dU, dr):
    return -dU / dr


# sendo dr = r_atual - d_ultimo_instante
def velocidade(dr):
    return dr / dT


def aceleracao(dr):
    return velocidade(dr) / dT
