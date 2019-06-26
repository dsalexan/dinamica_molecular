from constants import DELTA_T as dT, K


def potencial_eletrico(q, d):
    return K * q / d


def forca_classica(m, a):
    return m * a


def forca_em_funcao_do_potencial(dU, dr):
    return -dU / dr


# sendo dr = r_atual - d_ultimo_instante
def velocidade(dr):
    return dr / dT


def aceleracao(dr):
    return velocidade(dr) / dT
