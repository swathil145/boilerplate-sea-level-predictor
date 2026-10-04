import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read the data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    ax = df.plot(
        kind="scatter",
        x="Year",
        y="CSIRO Adjusted Sea Level"
    )

    # -----------------------------
    # Line of best fit - all data
    # -----------------------------

    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Years from the first year to 2050
    years = range(df["Year"].min(), 2051)

    # Predicted sea levels
    predicted = slope * years + intercept

    # Plot line
    ax.plot(years, predicted)


    # --------------------------------
    # Line of best fit - from year 2000
    # --------------------------------

    df_recent = df[df["Year"] >= 2000]

    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    # Years from 2000 to 2050
    years2 = range(2000, 2051)

    # Predicted sea levels
    predicted2 = slope2 * years2 + intercept2

    # Plot second line
    ax.plot(years2, predicted2)


    # -----------------------------
    # Labels and title
    # -----------------------------

    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")


    # Save and return
    fig = ax.get_figure()
    fig.savefig("sea_level_plot.png")
    return ax