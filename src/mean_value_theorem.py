from root_finding import get_root_by_bisection, get_root_by_newton
import numpy as np
import matplotlib.pyplot as plt





if __name__ == "__main__":

	# f = lambda x : np.square(x) - 2 ## f(x) = x^2 - 2 = 0
	# fp = lambda x : 2 * x ## f'(x) = 2x
	# fpp = lambda x : 2 ## f''(x) = 2
	f = lambda x : x ** 3 - 3 * x ** 2 + 2
	fp = lambda x : 3 * x ** 2 - 6 * x
	fpp = lambda x : 6 * x - 6
	x = np.linspace(
		-1,
		3,
		100)
	y = f(x)
	yp = fp(x)
	ypp = fpp(x)
	xa = 0
	xb = 2.5
	ya = f(xa)
	yb = f(xb)
	slope = (yb - ya) / (xb - xa)
	mod_fp = lambda x : fp(x) - slope

	## get root by bisection
	xc = get_root_by_bisection(
		mod_fp,
		xa,
		xb)
	## ...
	## OR
	## ...
	## get root by newton
	x0 = (xa + xb) / 2
	xc = get_root_by_newton(
		mod_fp,
		fpp,
		x0)
	## y=f(x) ==> yc = f(xc)
	yc = f(xc)

	## plot
	fig, ax = plt.subplots(
		figsize=(9, 6))
	# ax.set_aspect(
	# 	"equal")
	ax.plot(
		x,
		y,
		color="black",
		alpha=1,
		label=r"$y=f(x)$",
		linestyle="-",
		)
	# ax.plot(
	# 	x,
	# 	yp,
	# 	color="goldenrod",
	# 	alpha=0.8,
	# 	label=r"$y^\prime=f^\prime(x)$",
	# 	linestyle="-.",
	# 	)
	# ax.plot(
	# 	x,
	# 	ypp,
	# 	color="gray",
	# 	alpha=0.8,
	# 	label=r"$y^{\prime\prime}=f^{\prime\prime}(x)$",
	# 	linestyle=":",
	# 	)
	ax.scatter(
		[xa, xb],
		[ya, yb],
		color="crimson",
		label=r"$a={:,.4}$".format(float(xa)) + "\n" + r"$b={:,.4}$".format(float(xb)) + "\n" + r"slope$={:,.4}$".format(float(slope)),
		)
	ax.plot(
		[xa, xb],
		[ya, yb],
		color="crimson",
		label=r"$y - y_1 = m(x - x_1)$" + "\nAverage Rate of Change\n(secant line)",
		linestyle=":",
		)
	xca = xc - 0.5
	xcb = xc + 0.5
	ax.plot(
		[xca, xcb],
		[yc - 0.5 * slope, yc + 0.5 * slope],
		color="forestgreen",
		label=r"$y^\prime=f^\prime(x)$" + "\nInstantaneous Rate of Change\n(tangent line)",
		linestyle="-",
		)
	ax.scatter(
		[xc],
		[yc],
		color="limegreen",
		label=r"$c={:,.4}$".format(xc) + "\n" + r"$f^\prime(c)={:,.4}$".format(fp(xc)),
		)
	## format plot
	ax.set_xlim([
		x[0],
		x[-1],
		])
	ax.set_xlabel(
		r"$x$")
	ax.set_ylabel(
		r"$y=f(x)$")
	ax.set_title(
		r"Mean Value Theorem: $f^\prime(c)=\frac{f(b)-f(a)}{b-a}$")
	ax.minorticks_on()
	ax.grid(
		color="gray",
		linestyle=":",
		alpha=0.3)
	## format legend
	fig.subplots_adjust(
		bottom=0.3,
		)
	ncol = 3
	# leg = ax.legend(
	# 	loc="best",
	# 	ncol=ncol)
	leg = fig.legend(
		mode="expand",
		ncol=ncol,
		loc="lower center",
		# title=,
		)
	## show or save
	plt.show()
	plt.close()

##