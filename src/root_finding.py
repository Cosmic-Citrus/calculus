import numpy as np
from scipy.optimize import fsolve
import sympy


def get_root_by_bisection(f, a, b, tol=1e-6):

	def get_midpoint(a, b):
		midpoint = (a + b) / 2
		return midpoint

	while (b - a) / 2 > tol:
		midpoint = get_midpoint(
			a,
			b,
			)
		if f(midpoint) == 0:
			break
		else:
			if f(a) * f(midpoint) < 0:
				b = midpoint
			else:
				a = midpoint
	# midpoint = get_midpoint(
	# 	a,
	# 	b,
	# 	)
	return midpoint

def get_root_by_newton(f, fp, x0, tol=1e-6, number_maximum_iterations=100):
	xi = x0
	for it in range(number_maximum_iterations):
		y = f(xi)
		if abs(y) < tol:
			break
		dy_dx = fp(xi)
		if dy_dx == 0:
			break
		xi = xi - y / dy_dx
	return xi




if __name__ == "__main__":

	## define f(x) = 0 and f'(x) = d/dx f(x)
	## f(x) = 0 ==> x = root
	f = lambda x : np.square(x) - 2 ## f(x) = x^2 - 2 = 0
	fp = lambda x : 2 * x ## f'(x) = 2x
	# f = lambda x : np.exp(x) + x - 4
	# fp = lambda x : np.exp(x) + 1

	## define initial estimate of guess either directly or by interval
	## a < x0 < b ==> f(x0) = 0
	a = 0 
	b = 2
	# x0 = -1
	x0 = (a + b) / 2

	## get roots
	root_by_bisection = get_root_by_bisection(
		f=f,
		a=0,
		b=2,
		)
	root_by_newton = get_root_by_newton(
		f=f,
		fp=fp,
		x0=x0,
		)
	root_by_scipy, = fsolve(
		f,
		x0=x0)

	## print methods and corresponding roots
	print("\n .. root by bisection:\n{}\n".format(
		root_by_bisection))
	print("\n .. root by newton:\n{}\n".format(
		root_by_newton))
	print("\n .. root by scipy:\n{}\n".format(
		root_by_scipy))

	## ?
	## how to convert type <function> f into type <sympy.expression> lhs
	## ?

	## use sympy method
	x = sympy.Symbol(
		"x")
	lhs = x ** 2 - 2
	root_by_sympy = sympy.solve(
		lhs,
		x)

	## print sympy method
	print("\n .. root by sympy:\n{}\n".format(
		root_by_sympy))























##