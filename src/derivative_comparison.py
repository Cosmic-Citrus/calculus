import numpy as np
import matplotlib.pyplot as plt



def get_numerical_derivative_by_limit_difference(y, x):
	dy_dx = np.full(
		fill_value=0,
		shape=y.shape,
		dtype=float)
	## centered differences
	dx = x[2:] - x[:-2]
	dy = y[2:] - y[:-2]
	dy_dx[1:-1] = dy / dx
	## edge differences
	dy_dx[0] = (y[1] - y[0]) / (x[1] - x[0])
	dy_dx[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2])
	return dy_dx



if __name__ == "__main__":

	## y = f(x)
	x = np.linspace(
		0,
		2 * np.pi,
		100)
	f = lambda x : np.sin(x)
	y = f(x)

	## dy/dx = f'(x)
	fp = lambda x : np.cos(x) ## analytic
	dy_dx_by_analytic = fp(x) ## analytic
	dy_dx_by_numpy = np.gradient( ## numerical
		y,
		x)
	dy_dx_by_limit_diff = get_numerical_derivative_by_limit_difference( ## numerical
		y=y,
		x=x)
	absolute_error = np.abs(
		dy_dx_by_analytic - dy_dx_by_limit_diff)
	eps = 1e-6
	# relative_error = np.abs(
	# 	absolute_error / dy_dx_by_analytic)
	relative_error = np.abs(
		absolute_error / (dy_dx_by_analytic + eps))

	## tangent line at point (x0, y0) on y=f(x)
	x0 = np.pi / 3
	# x0 = 1
	# x0 = np.pi / 4
	# x0 = np.pi / 2
	y0 = f(x0)
	slope = np.interp(
		x0,
		x,
		# dy_dx_by_analytic,
		# dy_dx_by_numpy,
		dy_dx_by_limit_diff,
		) 
	x_tangent = np.linspace(
		x0 - 1, # min(x)
		x0 + 1, # max(x)
		10)
	y_tangent = slope * (x_tangent - x0) + y0

	## plot
	fig, (ax_top, ax_bottom) = plt.subplots(
		nrows=2,
		ncols=1,
		sharex=True,
		figsize=(11, 8))
	## y=f(x) vs x
	handle_by_y_of_x, = ax_top.plot(
		x,
		y,
		color="gray",
		label=r"$y=f(x)$",
		alpha=0.8,
		linestyle="-"
		)
	## y'=f'(x) is analytic
	## y'=f'(x) vs x
	handle_by_yp_of_x_analytic, = ax_top.plot(
		x,
		dy_dx_by_analytic,
		color="black",
		label=r"analytic $\frac{dy}{dx}=f^\prime(x)$",
		alpha=0.7,
		linestyle="--",
		)
	## y'=f'(x) is numerical (numpy)
	## y'=f'(x) vs x
	handle_by_yp_of_x_numpy, = ax_top.plot(
		x,
		dy_dx_by_numpy,
		color="steelblue",
		label=r"numerical $\frac{dy}{dx}=f^\prime(x)$" + "\n(numpy)",
		alpha=0.7,
		linestyle="-.",
		)
	## y'=f'(x) is numerical (limit difference)
	## y'=f'(x) vs x
	handle_by_yp_of_x_limit_diff, = ax_top.plot(
		x,
		dy_dx_by_limit_diff,
		color="crimson",
		label=r"numerical $\frac{dy}{dx}=f^\prime(x)$" + "\n(limit-difference)",
		alpha=0.7,
		linestyle=":",
		)
	## tangent line at point
	handle_by_tangent_line, = ax_top.plot(
		x_tangent,
		y_tangent,
		color="darkorange",
		label=r"tangent line at $(x_0, y_0)$",
		alpha=0.8,
		linestyle="-",
		)
	## point of tangency
	handle_by_tangency_point = ax_top.scatter(
		[x0],
		[y0],
		color="forestgreen",
		label=r"$(x_0, y_0)$",
		alpha=1,
		marker="o",
		s=25,
		)
	## absolute error
	ax_bottom.fill_between(
		x,
		np.full(
			fill_value=1e-6, ## avoid log(0)
			shape=absolute_error.shape,
			),
		absolute_error,
		color="purple",
		alpha=0.2,
		label="Absolute Error\n" + r"$|y^\prime_{analytic} - y^\prime_{numerical}|$",
		)
	ax_bottom.plot(
		x,
		absolute_error,
		color="purple",
		)
	## relative error
	ax_bottom.fill_between(
		x,
		np.full(
			fill_value=1e-6, ## avoid log(0)
			shape=relative_error.shape,
			),
		relative_error,
		color="goldenrod",
		alpha=0.2,
		label="Relative Error\n" + r"$|\frac{y^\prime_{analytic} - y^\prime_{numerical}}{y^\prime_{analytic}}|$", 
		)
	ax_bottom.plot(
		x,
		relative_error,
		color="goldenrod",
		)
	## format plot
	ax_top.set_ylabel(
		r"$y=f(x)$")
	ax_bottom.set_ylabel(
		"Error")
	ax_top.set_title(
		"Comparison of Numerical and Analytic Computation of Derivative")
	ax_bottom.set_ylim(
		bottom=0)
	for ax in (ax_top, ax_bottom):
		# ax.set_aspect(
		# 	"equal")
		ax.set_xlim([
			min(x),
			max(x),
			])
		ax.set_xlabel(
			r"$x$")
		ax.minorticks_on()
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