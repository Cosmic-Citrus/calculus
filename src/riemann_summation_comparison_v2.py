import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt


def get_parameters_by_left_riemann_summation(f, a, b, n, dx):
	x = np.linspace(
		a,
		b - dx,
		n)
	y = f(x)
	area_by_left_riemann_summation = np.sum(
		y * dx)
	label = "Left Riemann Sum\n" + r"$\sum_{i=0}^{n-1} f(x_i) \Delta x$" + r"$={:,.4}$".format(
		area_by_left_riemann_summation)
	return x, y, area_by_left_riemann_summation, label

def get_parameters_by_right_riemann_summation(f, a, b, n, dx):
	x = np.linspace(
		a + dx,
		b,
		n)
	y = f(x)
	area_by_right_riemann_summation = np.sum(
		y * dx)
	label = "Right Riemann Sum\n" + r"$\sum_{i=1}^{n} f(x_i) \Delta x$" + r"$={:,.4}$".format(
		area_by_right_riemann_summation)
	return x, y, area_by_right_riemann_summation, label

def get_parameters_by_midpoint_riemann_summation(f, a, b, n, dx):
	x = np.linspace(
		a + 0.5 * dx,
		b - 0.5 * dx,
		n)
	y = f(x)
	area_by_midpoint_riemann_summation = np.sum(
		y * dx)
	label = "Midpoint Riemann Sum\n" + r"$\sum_{i=0}^{n-1} f(\frac{x_i + x_{i+1}}{2}) \Delta x$" + r"$={:,.4}$".format(
		area_by_midpoint_riemann_summation)
	return x, y, area_by_midpoint_riemann_summation, label

if __name__ == "__main__":

	## y = f(x)
	x = np.linspace(
		0,
		2 * np.pi,
		100)
	f = lambda x : np.square(x)
	y = f(x)

	## sub-intervals
	a = x[0]
	b = x[-1]
	ns = np.logspace( ## 15 values :: 10^1, ..., 10^4
		1,
		4,
		15,
		dtype=int)
	dxs = (b - a) / ns

	## integral (exact value)
	area_by_exact_integral, _ = quad(
		f,
		a,
		b)

	## riemann summation (error of approximate value)
	left_error, right_error, midpoint_error = list(), list(), list()
	for n, dx in zip(ns, dxs):
		x_left, y_left, area_by_left_riemann_summation, left_label = get_parameters_by_left_riemann_summation(
			f=f,
			a=a,
			b=b,
			n=n,
			dx=dx)
		x_right, y_right, area_by_right_riemann_summation, right_label = get_parameters_by_right_riemann_summation(
			f=f,
			a=a,
			b=b,
			n=n,
			dx=dx)
		x_midpoint, y_midpoint, area_by_midpoint_riemann_summation, midpoint_label = get_parameters_by_midpoint_riemann_summation(
			f=f,
			a=a,
			b=b,
			n=n,
			dx=dx)
		absolute_error_by_left = np.abs(
			area_by_exact_integral - area_by_left_riemann_summation)
		absolute_error_by_right = np.abs(
			area_by_exact_integral - area_by_right_riemann_summation)
		absolute_error_by_midpoint = np.abs(
			area_by_exact_integral - area_by_midpoint_riemann_summation)
		relative_error_by_left = np.abs(
			absolute_error_by_left / area_by_exact_integral)
		relative_error_by_right = np.abs(
			absolute_error_by_right / area_by_exact_integral)
		relative_error_by_midpoint = np.abs(
			absolute_error_by_midpoint / area_by_exact_integral)
		left_error.append(
			(absolute_error_by_left, relative_error_by_left))
		right_error.append(
			(absolute_error_by_right, relative_error_by_right))
		midpoint_error.append(
			(absolute_error_by_midpoint, relative_error_by_midpoint))
	left_error = np.array(
		left_error)
	right_error = np.array(
		right_error)
	midpoint_error = np.array(
		midpoint_error)
	left_absolute_error = left_error[:, 0]
	left_relative_error = left_error[:, 1]
	right_absolute_error = right_error[:, 0]
	right_relative_error = right_error[:, 1]
	midpoint_absolute_error = midpoint_error[:, 0]
	midpoint_relative_error = midpoint_error[:, 1]

	## plot
	fig, ax = plt.subplots(
		figsize=(11, 8))
	ax.plot(
		ns,
		left_absolute_error,
		marker="o",
		color="steelblue",
		alpha=0.65,
		label="Absolute Error (left)\n" + r"$|\int_a^b f(x)dx - \sum_{i=0}^{n-1} f(x_i) \Delta x$|",
		linestyle="--",
		)
	# ax.plot(
	# 	ns,
	# 	left_relative_error,
	# 	marker="^",
	# 	color="steelblue",
	# 	alpha=0.65,
	# 	label="Relative Error (left)\n" + r"$|\frac{\int_a^b f(x)dx - \sum_{i=0}^{n-1} f(x_i) \Delta x}{\int_a^b f(x)dx}|$",
	# 	linestyle="--",
	# 	)
	ax.plot(
		ns,
		right_absolute_error,
		marker="o",
		color="crimson",
		alpha=0.65,
		label="Absolute Error (right)\n" + r"$|\int_a^b f(x)dx - \sum_{i=1}^{n} f(x_i) \Delta x$|",
		linestyle=":",
		)
	# ax.plot(
	# 	ns,
	# 	right_relative_error,
	# 	marker="^",
	# 	color="crimson",
	# 	alpha=0.65,
	# 	label="Relative Error (right)\n" + r"$|\frac{\int_a^b f(x)dx - \sum_{i=1}^{n} f(x_i) \Delta x}{\int_a^b f(x)dx}|$",
	# 	linestyle=":",
	# 	)
	ax.plot(
		ns,
		midpoint_absolute_error,
		marker="o",
		color="forestgreen",
		alpha=0.75,
		label="Absolute Error (midpoint)\n" + r"$|\int_a^b f(x)dx - \sum_{i=0}^{n-1} f(\frac{x_i + x_{i+1}}{2}) \Delta x$|",
		linestyle="-.",
		)
	# ax.plot(
	# 	ns,
	# 	midpoint_relative_error,
	# 	marker="^",
	# 	color="forestgreen",
	# 	alpha=0.75,
	# 	label="Relative Error (midpoint)\n" + r"$|\frac{\int_a^b f(x)dx - \sum_{i=0}^{n-1} f(\frac{x_i + x_{i+1}}{2}) \Delta x}{\int_a^b f(x)dx}|$",
	# 	linestyle="-.",
	# 	)
	ax.set_xscale(
		"log")
	ax.set_yscale(
		"log")
	ax.set_xlim([
		ns[0],
		ns[-1],
		])
	ax.set_xlabel(
		r"$n$ (number sub-intervals)")
	ax.set_ylabel(
		"Error")
	ax.set_title(
		"Error Analysis: Comparison of Riemann Summations")
	ax.grid(
		color="gray",
		linestyle=":",
		alpha=0.3)
	## format legend
	fig.subplots_adjust(
		bottom=0.25,
		hspace=0.3,
		)
	ncol = 3
	# leg = ax.legend(
	# 	loc="best",
	# 	ncol=ncol)
	leg = fig.legend(
		mode="expand",
		ncol=ncol,
		loc="lower center")
	## show or save
	plt.show()
	plt.close()

##