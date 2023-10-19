import altair as alt
import pandas as pd
from vega_datasets import data


def plot_wells(well_data):
    df = pd.DataFrame(data, columns=["latitude", "longitude", "depth", "gradient"])
    counties = alt.topo_feature(data.us_10m.url, 'counties')

    map_ = (
        alt.Chart(counties)
        .mark_geoshape(fill="lightgray", stroke="white")
        .project(type="albersUsa")
    )

    wells = (
        alt.Chart(df)
        .mark_circle()
        .encode(
            latitude="latitude",
            longitude="longitude",
            tooltip=[
                alt.Tooltip("depth", title="Depth (m)", format="d"),
                alt.Tooltip("gradient", title="Gradient (deg C/m)", format="0.2f")
            ],
            color=alt.Color("gradient", scale=alt.Scale(scheme="inferno"))
        )
    )

    return (map_ + wells)
