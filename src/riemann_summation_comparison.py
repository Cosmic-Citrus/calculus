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
	n = 10
	dx = (b - a) / n

	## integral (exact value)
	area_by_exact_integral, _ = quad(
		f,
		a,
		b)

	## riemann summation (approximate value)
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

	## plot
	fig, (ax_top, ax_middle, ax_bottom) = plt.subplots(
		nrows=3,
		ncols=1,
		sharex=True,
		figsize=(11, 8))
	for ax, side, xx, yy, area, align, facecolor, label in zip((ax_top, ax_middle, ax_bottom), ("left", "right", "midpoint"), (x_left, x_right, x_midpoint), (y_left, y_right, y_midpoint), (area_by_left_riemann_summation, area_by_right_riemann_summation, area_by_midpoint_riemann_summation), ("edge", "edge", "center"), ("darkorange", "forestgreen", "crimson"), (left_label, right_label, midpoint_label)):
		# ax.set_aspect(
		# 	"equal")
		if side == "right":
			xxx = xx - dx
		else:
			xxx = xx
		ax.bar(
			xxx,
			yy,
			width=dx,
			align=align,
			color=facecolor,
			edgecolor=facecolor,
			alpha=0.3,
			label=label,
			)
		ax.scatter(
			xx,
			yy,
			marker="o",
			color=facecolor,
			)
		ax.plot(
			x,
			y,
			color="black")
		ax.text(
			0.05,
			0.85,
			"{} Riemann Sum".format(
				side.title()),
			horizontalalignment="left",
			verticalalignment="top",
			transform=ax.transAxes,
			)
	ax_top.plot(
		list(),
		list(),
		color="black",
		# marker=".",
		linestyle="-",
		label=r"$y=f(x)$"
		)
	ax_top.scatter(
		list(),
		list(),
		color="none",
		label=r"$\int_a^b f(x)dx =$" + r"${:,.4}$".format(
			area_by_exact_integral),
		)
	## format plot
	for ax in (ax_top, ax_middle, ax_bottom):
		ax.set_ylabel(
			r"$y=f(x)$")
		ax.set_xlim([
			min(x),
			max(x),
			])
		ax.minorticks_on()
		ax.grid(
			color="gray",
			linestyle=":",
			alpha=0.3)
	ax_bottom.set_xlabel(
		r"$x$")
	ax_top.set_title(
		"Comparison of Riemann Summation Approximations")
	## format legend
	fig.subplots_adjust(
		bottom=0.25,
		hspace=0.3,
		)
	ncol = 5
	# leg = ax.legend(
	# 	loc="best",
	# 	ncol=ncol)
	leg = fig.legend(
		mode="expand",
		ncol=ncol,
		loc="lower center",
		# title="${:,}$ sub-intervals from $a={:,.4}$ to $b={:,.4}$".format(
		# 	n,
		# 	float(a),
		# 	float(b),
		# 	),
		title=r"${:,}$ sub-intervals from $a=0$ to $b=2\pi$".format(
			n,
			),
		)
	## show or save
	plt.show()
	plt.close()

##