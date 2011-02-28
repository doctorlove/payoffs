#####################
# By Fran Buontempo #
#####################

import pylab as p

def long_put(E):
	S = [E*t/10.0 for t in range(0,21)]
	P = map( lambda x : max(E-x, 0), S )
	return S,P

def short_put(E):
	S, P = long_put(E)
	return S,[-1.0*p for p in P]

def long_call(E):
	S = [E*t/10.0 for t in range(0,21)]
	P = map( lambda x : max(x-E, 0), S )
	return S,P

def short_call(E):
	S, P = long_call(E)
	return S,[-1.0*p for p in P]


if __name__ == "__main__":
	S1, P1 = long_call(30)
	S2, P2 = short_put(30)
	p.plot(S1,P1,'r-')
	p.plot(S2,P2,'b-')
	p.show()

