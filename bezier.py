from really_big_array import p
from math import lgamma, exp
from numpy import linspace, array


apply = lambda func,nArray : array(list(map(func, nArray)))

def nCk(n, k):
    """
    Returns the binomial coefficient C_{n,k}. This is a numeric approximation using the logarithm of the gamma function, so that it makes posible to calculate it for big values fo n and k.

    @n - scalar, should be an integer
    @k - array of integers

    Note that even for non integers, it may make sense to calculate the logarithmic gamma, althougt that's no longer a binomial coefficient.
    """
    lfact = lgamma(n + 1) - apply(lgamma, k + 1)- apply(lgamma, n - k + 1)
    return apply(exp, lfact)


nData = len(p)

t = linspace(0, 1, nData)
r = 1 - t
i = array(range(nData))
e = nData - i

B = nCk(nData, i) * pow (r, e) * pow(t, i) * p
B.tofile('bezier-coefs', sep=', ')
