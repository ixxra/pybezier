from really_big_array import p

nData = len(p)

t = linspace(0, 1, nData)
r = 1 - t
i = array(range(0, nData + 1))
e = nData - i

B = pow (r, e) * pow(t, i) * p