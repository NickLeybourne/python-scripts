import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# ==============================================================
# Radioactive Decay Curve Plotter
# Nicholas Leybourne - Medical Physics
# ==============================================================
# Plots N(t) = N0 * exp(-lambda * t) for one or more isotopes.
# Half-lives sourced from standard nuclear data tables.
# ==============================================================

ISOTOPES = {
    "F-18":   {"half_life_hours": 1.8295,  "color": "#E63946", "initial_activity_MBq": 370},
    "Tc-99m": {"half_life_hours": 6.0072,  "color": "#457B9D", "initial_activity_MBq": 740},
    "Ga-68":  {"half_life_hours": 1.1302,  "color": "#2A9D8F", "initial_activity_MBq": 185},
    "Co-57":  {"half_life_hours": 6528.0,  "color": "#E9C46A", "initial_activity_MBq": 100},
}


def decay_activity(A0, half_life_hours, time_hours):
    """Calculate activity at time t using A(t) = A0 * exp(-lambda * t)."""
    lam = np.log(2) / half_life_hours
    return A0 * np.exp(-lam * time_hours)


def plot_decay(isotopes, duration_hours=24, num_points=500):
    time = np.linspace(0, duration_hours, num_points)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("Radioactive Decay Curves", fontsize=16, fontweight="bold", y=1.01)

    for name, props in isotopes.items():
        A0 = props["initial_activity_MBq"]
        t_half = props["half_life_hours"]
        color = props["color"]
        activity = decay_activity(A0, t_half, time)
        label = f"{name}  (T½ = {t_half:.4g} h)"

        # Linear scale
        axes[0].plot(time, activity, label=label, color=color, linewidth=2)
        # Log scale
        axes[1].semilogy(time, activity, label=label, color=color, linewidth=2)

    for ax, scale in zip(axes, ["Linear", "Logarithmic"]):
        ax.set_xlabel("Time (hours)", fontsize=12)
        ax.set_ylabel("Activity (MBq)", fontsize=12)
        ax.set_title(f"{scale} Scale", fontsize=13)
        ax.legend(fontsize=9, loc="upper right")
        ax.grid(True, linestyle="--", alpha=0.5)
        ax.set_xlim(0, duration_hours)

    axes[0].yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x:.0f}"))
    axes[0].set_ylim(bottom=0)

    plt.tight_layout()
    output_file = "decay_curves.png"
    plt.savefig(output_file, dpi=150, bbox_inches="tight")
    print(f"Plot saved to {output_file}")
    plt.show()


if __name__ == "__main__":
    plot_decay(ISOTOPES, duration_hours=24)
