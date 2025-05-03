import plotly.express as px


def create_municipality_bar(df, **options):

    df["Ansökta_label"] = df["Ansökta utbildningar"].apply(
        lambda row: " " * 2 + f"{row}" + " " * 2
    )

    fig = px.bar(
        df,
        y="Kommun",
        x="Ansökta utbildningar",
        text="Ansökta_label",
    )
    fig.update_layout(
        plot_bgcolor="white",
        margin=dict(t=0, l=40, r=30, b=50),
        yaxis=dict(
            autorange="reversed",
            ticklabelposition="outside left",
            showline=True,
            linecolor="lightgray",
            title=dict(text=f"<b>{options.get('ylabel')}</b>"),
        ),
        xaxis=dict(
            linecolor="lightgray",
            showticklabels=False,
            title=f"<b>{options.get('xlabel')}</b>",
        ),
    )

    fig.update_traces(
        textposition="outside",
        hovertemplate="<b>%{y}</b><br>Ansökta utbildningar: %{x}",
    )

    return fig
