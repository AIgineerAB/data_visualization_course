from backend.data_processing import filter_df_municipality
from frontend.charts import create_municipality_bar

def filter_data(state):

    df_municipality = filter_df_municipality(
        state.df, educational_area=state.selected_educational_area
    )
    state.municipality_chart = create_municipality_bar(
        df_municipality.head(state.number_municipalities),
        ylabel="KOMMUN",
        xlabel="# ANSÖKTA UTBILDNINGAR",
    )

    state.municipalities_title = state.number_municipalities
    state.educational_area_title = state.selected_educational_area

