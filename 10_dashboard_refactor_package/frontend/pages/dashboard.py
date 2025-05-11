import taipy.gui.builder as tgb
from frontend.charts import create_municipality_bar
from backend.data_processing import filter_df_municipality, df
from backend.updates import filter_data

df_municipality = filter_df_municipality(df)

municipality_chart = create_municipality_bar(
    df_municipality.head(), ylabel="KOMMUN", xlabel="# ANSÖKTA UTBILDNINGAR"
)

number_municipalities = 5
municipalities_title = number_municipalities

selected_educational_area = "Data/IT"
educational_area_title = selected_educational_area

with tgb.Page() as dashboard_page:
    with tgb.part(class_name="container card stack-large"):
        tgb.navbar()
        with tgb.part(class_name="card"):
            tgb.text("# MYH dashboard 2024", mode="md")
            tgb.text(
                "En dashboard för att visa statistik och information om ansökningsomgång 2024",
                mode="md",
            )

        with tgb.layout(columns="2 1"):
            with tgb.part(class_name="card"):
                tgb.text(
                    "## Antalet ansökta YH utbildningar per kommun (topp {municipalities_title}) för {educational_area_title}",
                    class_name="title-chart",
                    mode="md",
                )
                tgb.chart(figure="{municipality_chart}")

            with tgb.part(class_name="card"):
                tgb.text("## Filtrera data", mode="md")
                tgb.text("Filtrera antalet kommuner", mode="md")

                tgb.slider(
                    value="{number_municipalities}",
                    min=5,
                    max=len(df_municipality),
                    continuous=False,
                )
                # tgb.text("{number_municipalities} kommuner valda")

                tgb.text("Välj utbildningsområde", mode="md")
                tgb.selector(
                    value="{selected_educational_area}",
                    lov=df["Utbildningsområde"].unique(),
                    dropdown=True,
                )

                tgb.button("FILTRERA DATA", on_action=filter_data, class_name="plain")
