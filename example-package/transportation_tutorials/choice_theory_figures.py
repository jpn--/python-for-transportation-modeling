import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xmle
import sys
print("""Note: figures labeled 'interactive' will not actually be interactive unless they are 
created in a live Jupyter notebook. If you're viewing this as a page on the course 
static website, you'll be able to see the default figures but not change the sliders.""", file=sys.stderr)

from . import data as exampledata

data2 = pd.read_csv(exampledata("data2_ca.csv"))

diffs2 = pd.DataFrame(
    [
        dict(obs=1, choice="bus", timediff=10, costdiff=-10),
        dict(obs=2, choice="car", timediff=9, costdiff=-2),
    ]
)

diffs9 = pd.DataFrame(
    [
        dict(obs=1, choice="car", timediff=9, costdiff=-7),
        dict(obs=2, choice="bus", timediff=-8, costdiff=-5),
        dict(obs=3, choice="bus", timediff=4, costdiff=-6),
        dict(obs=4, choice="bus", timediff=-7, costdiff=-2),
        dict(obs=5, choice="car", timediff=2, costdiff=0),
        dict(obs=6, choice="bus", timediff=1, costdiff=-5),
        dict(obs=7, choice="car", timediff=-3, costdiff=4),
        dict(obs=8, choice="bus", timediff=-2, costdiff=-7),
        dict(obs=9, choice="car", timediff=5, costdiff=0),
    ]
)

diffs19 = pd.DataFrame([
    dict(obs= 1, choice='car', timediff= 9, costdiff=-7),
    dict(obs= 2, choice='bus', timediff=-8, costdiff=-5),
    dict(obs= 3, choice='bus', timediff= 4, costdiff=-6),
    dict(obs= 4, choice='bus', timediff=-7, costdiff=-2),
    dict(obs= 5, choice='bus', timediff= 2, costdiff= 0),
    dict(obs= 6, choice='bus', timediff= 1, costdiff=-5),
    dict(obs= 7, choice='car', timediff=-3, costdiff= 4),
    dict(obs= 8, choice='car', timediff=-2, costdiff=-7),
    dict(obs= 9, choice='car', timediff= 5, costdiff= 0),
    dict(obs=10, choice='car', timediff= 7, costdiff=-6),
    dict(obs=11, choice='car', timediff= 8, costdiff=-7),
    dict(obs=12, choice='car', timediff=-5, costdiff=-3),
    dict(obs=13, choice='car', timediff= 3, costdiff=-8),
    dict(obs=14, choice='bus', timediff=-9, costdiff=-1),
    dict(obs=15, choice='car', timediff= 1, costdiff= 0),
    dict(obs=16, choice='bus', timediff= 0, costdiff=-9),
    dict(obs=17, choice='car', timediff=-5, costdiff= 5),
    dict(obs=18, choice='car', timediff=-5, costdiff=-5),
    dict(obs=19, choice='car', timediff= 7, costdiff= 1),
])


def figure_two_observations(*ignored_arguments):
    fig, axs = plt.subplots(1, 2, sharey=True, figsize=(5, 3))
    fig.set_tight_layout(True)
    for obs, ax in zip([1, 2], axs):
        for (ch, mo), gg in data2.query(f"obs=={obs}").groupby(["chosen", "mode"]):
            marker = "o" if ch else "x"
            color = "r" if mo == "bus" else "b"
            ax.scatter(gg.time, gg.cost, label=(ch, mo), marker=marker, color=color)
            ax.annotate(
                mo,
                (gg.time, gg.cost),
                textcoords="offset points",
                xytext=(0, 10),
                ha="center",
            )
            ax.annotate(
                ch,
                (gg.time, gg.cost),
                textcoords="offset points",
                xytext=(0, -15),
                ha="center",
            )
        ax.set_xlabel("Time")
        ax.set_ylabel("Cost")
        ax.set_title(f"Observation {obs}")
        ax.set_ylim(8, 22)
        ax.set_xlim(8, 22)
    axs[0].arrow(11.5, 18.5, 7, -7, head_width=0.5, color="k")
    axs[0].text(14.5, 14.5, "Better", rotation=-45)
    axs[1].arrow(19.75, 14.1, -6, 1.6, head_width=0.5, color="k")
    axs[1].text(16, 15, "Better", rotation=-15)
    return xmle.Show(fig)


def figure_four_fields(funcs):
    assert len(funcs) == 4
    space = np.linspace(8, 22)
    grid = np.meshgrid(space, space)
    fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
    axs = axs.ravel()
    for n, (label, func) in enumerate(funcs.items()):
        field = func(grid[0], grid[1])
        cf = axs[n].contourf(space, space, field, levels=11)
        label = label.replace("beta time", r"$\beta_{time}$")
        label = label.replace("beta cost", r"$\beta_{cost}$")
        axs[n].set_title(label, fontsize=8 )
        if n > 1: axs[n].set_xlabel("Time")
        if not n % 2: axs[n].set_ylabel("Cost")
    return xmle.Show(fig)


def figure_two_observations_on_field(beta_time=-0.18, beta_cost=-0.1):
    space = np.linspace(8, 22)
    grid = np.meshgrid(space, space)
    field = grid[0] * beta_time + grid[1] * beta_cost
    fig, ax = plt.subplots()
    fig.set_tight_layout(True)
    cf = ax.contourf(space, space, field, levels=11)
    cbar = fig.colorbar(cf)
    cbar.ax.set_ylabel("Utility of Alternative")
    for obs in [1, 2]:
        for (ch, mo), gg in data2.query(f"obs=={obs}").groupby(["chosen", "mode"]):
            marker = "o" if ch else "x"
            color = "r" if mo == "bus" else "b"
            ax.scatter(gg.time, gg.cost, label=(ch, mo), marker=marker, color=color)
            ax.annotate(
                mo,
                (gg.time, gg.cost),
                textcoords="offset points",
                xytext=(0, 10),
                ha="center",
                color="w",
            )
            ax.annotate(
                ch,
                (gg.time, gg.cost),
                textcoords="offset points",
                xytext=(0, -15),
                ha="center",
                color="w",
            )
        ax.set_xlabel("Time")
        ax.set_ylabel("Cost")
        ax.set_ylim(8, 22)
        ax.set_xlim(8, 22)
    ax.arrow(11.5, 18.5, 7, -7, head_width=0.5, color="k")
    ax.arrow(19.75, 14.1, -6, 1.6, head_width=0.5, color="k")
    ax.set_title(fr"$\beta_{{time}}$ = {beta_time},  $\beta_{{cost}}$ = {beta_cost}")
    return xmle.Show(fig)


def figure_differences_on_field(df, beta_time=-0.5, beta_cost=-0.8):
    space = np.linspace(-11, 11)
    grid = np.meshgrid(space, space)
    field = grid[0] * -beta_time + grid[1] * -beta_cost
    fig, ax = plt.subplots()
    cf = ax.contourf(space, space, field, levels=11, cmap="RdBu")
    cbar = fig.colorbar(cf)
    cbar.ax.set_ylabel("Net Utility of Car")
    for ch, gg in df.groupby(["choice"]):
        marker = "o" if ch == "bus" else "s"
        color = "r" if ch == "bus" else "b"
        ax.scatter(
            gg.timediff,
            gg.costdiff,
            label=ch,
            marker=marker,
            color=color,
            edgecolor="w",
            s=50,
        )
    ax.set_xlabel("Car Time Advantage")
    ax.set_ylabel("Car Cost Advantage")
    ax.legend(title="Chosen")
    ax.set_title(fr"$\beta_{{time}}$ = {beta_time},  $\beta_{{cost}}$ = {beta_cost}")
    return xmle.Show(fig)


def interactive_differences_on_field(data, beta_time=-0.5, beta_cost=-0.8):
    from plotly import graph_objects as go
    from ipywidgets import FloatSlider, HBox, Layout

    choose_car = data.query("choice == 'car'")
    choose_bus = data.query("choice == 'bus'")
    space = np.linspace(-11, 11)
    grid = np.meshgrid(space, space)
    b_cost = FloatSlider(
        value=beta_cost,
        max=1.0,
        min=-1.0,
        step=0.05,
        orientation="vertical",
        description=r"$\beta$ Cost",
    )
    b_time = FloatSlider(
        value=beta_time,
        max=1.0,
        min=-1.0,
        step=0.05,
        orientation="vertical",
        description=r"$\beta$ Time",
    )
    field = grid[0] * -b_time.value + grid[1] * -b_cost.value
    fig = go.FigureWidget(
        [
            go.Contour(
                name="Net Utility of Car",
                z=field,
                x=space,
                y=space,
                colorbar=dict(
                    thickness=25,
                    thicknessmode="pixels",
                    len=0.65,
                    lenmode="fraction",
                    outlinewidth=0,
                    yanchor="bottom",
                    y=0,
                    title="Net Utility of Car",
                    titleside="right",
                ),
                colorscale="rdbu",
            ),
            go.Scatter(
                x=choose_bus.timediff,
                y=choose_bus.costdiff,
                mode="markers",
                name="bus",
                marker_line_width=2,
                marker_line_color="white",
                marker_size=10,
                marker_color="red",
            ),
            go.Scatter(
                x=choose_car.timediff,
                y=choose_car.costdiff,
                mode="markers",
                name="car",
                marker_line_width=2,
                marker_line_color="white",
                marker_size=10,
                marker_symbol="square",
                marker_color="blue",
            ),
        ]
    )
    fig.update_xaxes(
        range=[-11, 11], showline=True,
    )
    fig.update_yaxes(
        range=[-11, 11], showline=True,
    )
    fig.layout.margin = {"b": 5, "t": 5, "l": 5, "r": 5}
    fig.layout.width = 450
    fig.layout.height = 250
    fig.update_layout(
        xaxis_title="Car Time Advantage",
        yaxis_title="Car Cost Advantage",
        legend_title="Chosen",
        font=dict(size=11,),
    )

    def refield(*args):
        field = grid[0] * -b_time.value + grid[1] * -b_cost.value
        fig.data[0].z = field

    b_cost.observe(refield)
    b_time.observe(refield)
    return HBox(
        [fig, b_cost, b_time], layout=Layout(display="flex", align_items="center")
    )


def interactive_differences_with_probability(
    data, beta_time=-0.5, beta_cost=-0.8, likelihood=False, loglikelihood=False, correct=False, beta_bus=None,
):
    from plotly import graph_objects as go
    from ipywidgets import FloatSlider, HBox, Layout

    likelihood |= bool(loglikelihood)
    choose_car = data.query("choice == 'car'")
    choose_bus = data.query("choice == 'bus'")
    space = np.linspace(-11, 11)
    grid = np.meshgrid(space, space)
    b_cost = FloatSlider(
        value=beta_cost,
        max=2.5,
        min=-2.5,
        step=0.01,
        orientation="vertical",
        description=r"$\beta$ Cost",
    )
    b_time = FloatSlider(
        value=beta_time,
        max=2.5,
        min=-2.5,
        step=0.01,
        orientation="vertical",
        description=r"$\beta$ Time",
    )
    b_bus = FloatSlider(
        value=beta_bus or 0,
        max=2.5,
        min=-2.5,
        step=0.01,
        orientation="vertical",
        description=r"$\beta$ Bus",
    )

    field = 1 / (1 + np.exp(grid[0] * b_time.value + grid[1] * b_cost.value + b_bus.value))
    fig = go.FigureWidget(
        [
            go.Contour(
                name="Probability of Car",
                z=field,
                x=space,
                y=space,
                colorbar=dict(
                    thickness=25,
                    thicknessmode="pixels",
                    len=0.65,
                    lenmode="fraction",
                    outlinewidth=0,
                    yanchor="bottom",
                    y=0,
                    title="Probability of Car",
                    titleside="right",
                ),
                colorscale="bluered_r",
                contours=dict(start=0, end=1.0, size=0.1,),
            ),
            go.Scatter(
                x=choose_bus.timediff,
                y=choose_bus.costdiff,
                mode="markers",
                name="bus",
                marker_line_width=2,
                marker_line_color="white",
                marker_size=10,
                marker_color="red",
            ),
            go.Scatter(
                x=choose_car.timediff,
                y=choose_car.costdiff,
                mode="markers",
                name="car",
                marker_line_width=2,
                marker_line_color="white",
                marker_size=10,
                marker_symbol="square",
                marker_color="blue",
            ),
        ]
    )
    fig.update_xaxes(
        range=[-11, 11], showline=True,
    )
    fig.update_yaxes(
        range=[-11, 11], showline=True,
    )
    fig.layout.margin = {"b": 5, "t": 5, "l": 5, "r": 5}
    fig.layout.width = 450
    fig.layout.height = 250
    fig.update_layout(
        xaxis_title="Car Time Advantage",
        yaxis_title="Car Cost Advantage",
        legend_title="Chosen",
        font=dict(size=11,),
    )
    if likelihood:
        fig.update_layout(
            title=dict(
                text="Likelihood = ",
                y=0.98,
                x=0.5,
                xref="paper",
                xanchor="center",
                yanchor="top",
                font_size=11,
            ),
            margin={"b": 5, "t": 20, "l": 5, "r": 5},
        )

    def refield(*args):
        with fig.batch_update():
            field = 1 / (1 + np.exp(grid[0] * b_time.value + grid[1] * b_cost.value + b_bus.value))
            fig.data[0].z = field
            if correct or likelihood:
                likely2 = 1 / (
                    1
                    + np.exp(
                        fig.data[2].x * b_time.value + fig.data[2].y * b_cost.value + b_bus.value
                    )
                )
                likely1 = 1 - (
                    1
                    / (
                        1
                        + np.exp(
                            fig.data[1].x * b_time.value + fig.data[1].y * b_cost.value + b_bus.value
                        )
                    )
                )
                if correct:
                    fig.data[2].marker.symbol = np.where(
                        likely2 > 0.5,
                        np.where(likely2 > 0.95, "square-dot", "square"),
                        "x",
                    )
                    fig.data[1].marker.symbol = np.where(
                        likely1 > 0.5,
                        np.where(likely1 > 0.95, "circle-dot", "circle"),
                        "x",
                    )
                if likelihood:
                    fig.data[2].marker.size = np.clip(15 * likely2, 3, 15)
                    fig.data[1].marker.size = np.clip(15 * likely1, 3, 15)
                    if loglikelihood:
                        fig.update_layout(
                            title_text=f"Log Likelihood = {np.log(likely1).sum()+np.log(likely2).sum():.4g}",
                        )
                    else:
                        fig.update_layout(
                            title_text=f"Likelihood = {likely1.prod()*likely2.prod():.4g}",
                        )

    refield()
    b_cost.observe(refield)
    b_time.observe(refield)
    b_bus.observe(refield)
    if beta_bus is None:
        parts = [fig, b_cost, b_time]
    else:
        parts = [fig, b_cost, b_time, b_bus]
    return HBox(
        parts, layout=Layout(display="flex", align_items="center")
    )


def figure_log_likelihood(likely, trajectory=None):
    if trajectory is not None:
        trajectory = pd.DataFrame(trajectory, columns=['c', 't'])
        c_space = np.linspace(trajectory['c'].min() - 0.05, trajectory['c'].max() + 0.05)
        t_space = np.linspace(trajectory['t'].min() - 0.05, trajectory['t'].max() + 0.05)
    else:
        c_space = t_space = np.linspace(-0.5, 0.5)
    beta_grid = np.meshgrid(c_space, t_space)
    beta_LL = np.vectorize(lambda a, b: likely([a, b]))(*beta_grid)
    fig, ax = plt.subplots()
    cf = ax.contourf(c_space, t_space, beta_LL, levels=15)
    cbar = fig.colorbar(cf)
    if trajectory is not None:
        trajectory.plot(
            x='c', y='t', ax=ax,
            color='r',
            label='optimization trajectory',
            marker=".",
            lw=1,
        )
    ax.set_xlabel(r'$\beta_{time}$')
    ax.set_ylabel(r'$\beta_{cost}$')
    cbar.ax.set_ylabel('Log Likelihood')
    return xmle.Show(fig)


def figure_log_likelihood_3d(likely, trajectory):
    _t, _c, _z = trajectory[-1]
    trajectory = pd.DataFrame(trajectory, columns=['t', 'c', 'z'])
    c_space = np.linspace(trajectory['c'].min() - 0.15, trajectory['c'].max() + 0.15)
    t_space = np.linspace(trajectory['t'].min() - 0.15, trajectory['t'].max() + 0.15)
    z_space = np.linspace(trajectory['z'].min() - 0.15, trajectory['z'].max() + 0.15)
    # beta_grid = np.meshgrid(c_space, t_space, z_space)
    # beta_LL = np.vectorize(lambda a, b, c: likely([a, b, c]))(*beta_grid)
    fig, axs = plt.subplots(1,3, figsize=(6, 2))
    # constant t
    ax = axs[0]
    beta_grid = np.meshgrid(c_space, z_space)
    beta_LL = np.vectorize(lambda a, b, c: likely([a, b, c]))(_c, beta_grid[0], beta_grid[1])
    if np.min(beta_LL) > 0: beta_LL = -beta_LL
    cf = ax.contourf(c_space, z_space, beta_LL, levels=15)
    if trajectory is not None:
        trajectory.plot(
            x='c', y='z', ax=ax,
            color='r',
            label='optimization trajectory',
            marker=".",
            lw=1,
            legend=False,
        )
    ax.set_xlabel(r'$\beta_{cost}$')
    ax.set_ylabel(r'$\beta_{bus}$')
    ax.set_title(r'At converged $\beta_{time}$', fontsize=8)

    # constant c
    ax = axs[1]
    beta_grid = np.meshgrid(t_space, z_space)
    beta_LL = np.vectorize(lambda a, b, c: likely([a, b, c]))(beta_grid[0], _c, beta_grid[1])
    if np.min(beta_LL) > 0: beta_LL = -beta_LL
    cf = ax.contourf(t_space, z_space, beta_LL, levels=15)
    if trajectory is not None:
        trajectory.plot(
            x='t', y='z', ax=ax,
            color='r',
            label='optimization trajectory',
            marker=".",
            lw=1,
            legend=False,
        )
    ax.set_xlabel(r'$\beta_{time}$')
    ax.yaxis.set_ticklabels([])
    ax.set_title(r'At converged $\beta_{cost}$', fontsize=8)

    # constant z
    ax = axs[2]
    beta_grid = np.meshgrid(c_space, t_space)
    beta_LL = np.vectorize(lambda a, b, c: likely([a, b, c]))(beta_grid[0], beta_grid[1], _z)
    if np.min(beta_LL) > 0: beta_LL = -beta_LL
    cf = ax.contourf(c_space, t_space, beta_LL, levels=15)
    if trajectory is not None:
        trajectory.plot(
            x='c', y='t', ax=ax,
            color='r',
            label='optimization trajectory',
            marker=".",
            lw=1,
            legend=False,
        )
    ax.set_xlabel(r'$\beta_{cost}$')
    ax.set_ylabel(r'$\beta_{time}$')
    ax.set_title(r'At converged $\beta_{bus}$', fontsize=8)
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    # cbar = fig.colorbar(cf)
    # cbar.ax.set_ylabel('Log Likelihood')
    return xmle.Show(fig)


def figure_gumbel_draws(draws, gumbel_r=None):
    fig, axs = plt.subplots(3, 2, figsize=(7,7))
    fig.set_tight_layout(True)
    for d, ax in zip(draws, axs.reshape(-1)):
        ax.set_title(f"Samples of Size {d.shape[0]:,}")
        dmax = d.max(axis=0)
        ax.hist(dmax, bins=30, density=True) # plot the distribution
        if gumbel_r is not None:
            m, v = (dmax.mean(), dmax.var())
            x = np.linspace(dmax.min(),dmax.max(),100)
            s = (v/1.645)**0.5
            mu = m - s*0.577
            ax.plot(x, gumbel_r.pdf(x,mu,s), label='Gumbel', lw=3)
    return xmle.Show(fig)


def figure_gumbel_vs_normal():
    from scipy.stats import gumbel_r, norm

    fig, axs = plt.subplots(1, 2, figsize=(7, 3), squeeze=True)

    x = np.linspace(-3, 5, 100)
    axs[0].plot(x, gumbel_r.pdf(x), label='Gumbel')
    axs[0].plot(x, norm.pdf(x, 0.577, 1.282), label='Normal')
    axs[0].set_title("Probability Density Functions\n(same mean and variance)")
    axs[0].legend()

    axs[1].plot(x, gumbel_r.cdf(x), label='Gumbel')
    axs[1].plot(x, norm.cdf(x, 0.577, 1.282), label='Normal')
    axs[1].set_title("Cumulative Density Functions\n(same mean and variance)")
    axs[1].legend()
    return xmle.Show(fig)

def figure_logistic_vs_normal():
    from scipy.stats import logistic, norm

    fig, axs = plt.subplots(1, 2, figsize=(7, 3), squeeze=True)

    x = np.linspace(-5, 5, 100)
    axs[0].plot(x, logistic.pdf(x), label='Logistic')
    axs[0].plot(x, norm.pdf(x, 0, 1.8138), label='Normal')
    axs[0].set_title("Probability Density Functions\n(same mean and variance)")
    axs[0].legend()

    axs[1].plot(x, logistic.cdf(x), label='Logistic')
    axs[1].plot(x, norm.cdf(x, 0, 1.8138), label='Normal')
    axs[1].set_title("Cumulative Density Functions\n(same mean and variance)")
    axs[1].legend()
    return xmle.Show(fig)

def figure_distribution_vs_normal(other):
    from scipy.stats import  norm
    mean_, var_ = other.stats(moments='mv')
    try:
        other_name = other.name.title()
    except AttributeError:
        other_name = other.dist.name.title()

    fig, axs = plt.subplots(1, 2, figsize=(7, 3), squeeze=True)

    x = np.linspace(other.ppf(0.005), other.isf(0.005), 100)
    axs[0].plot(x, other.pdf(x), label=other_name)
    axs[0].plot(x, norm(mean_, np.sqrt(var_)).pdf(x), label='Normal')
    axs[0].set_title("Probability Density Functions\n(same mean and variance)")
    axs[0].legend()

    axs[1].plot(x, other.cdf(x), label=other_name)
    axs[1].plot(x, norm(mean_, np.sqrt(var_)).cdf(x), label='Normal')
    axs[1].set_title("Cumulative Density Functions\n(same mean and variance)")
    axs[1].legend()
    return xmle.Show(fig)


def figure_gumbel_translate(*gumbels):

    fig, ax = plt.subplots(1, 1, figsize=(6, 3), squeeze=True)

    x = np.linspace(-3, 11, 100)
    for g in gumbels:
        ax.plot(x, g.pdf(x), label=f'Gumbel{g.args}')
    ax.set_title("Gumbel Translation")
    ax.legend()

    return xmle.Show(fig)


def figure_gumbel_scale(*gumbels):

    fig, ax = plt.subplots(1, 1, figsize=(6, 3), squeeze=True)

    x = np.linspace(-3, 11, 100)
    for g in gumbels:
        ax.plot(x, g.pdf(x), label=f'Gumbel{g.args}')
    ax.set_title("Gumbel Scales")
    ax.legend()

    return xmle.Show(fig)
