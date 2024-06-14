import math


def bjm_round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier + 0.5) / multiplier


def bjm_round_down(number, decimals=0):
    """
    Special case for rounding where xxxx.5 is xxxx and not xxxx+1
    :param number: initial number
    :param decimals: number of decimals
    :return:
    """
    multiplier = 10 ** decimals
    return int(number * multiplier) / multiplier


def bjm_round_half_down(number, decimals=0):
    """
    Special case for rounding where xxxx.5 is xxxx and not xxxx+1
    :param number: initial number
    :param decimals: number of decimals
    :return:
    """
    multiplier = 10 ** decimals
    return math.ceil(number * multiplier - 0.5) / multiplier