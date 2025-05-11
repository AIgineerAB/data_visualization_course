import taipy.gui.builder as tgb
from backend.data_processing import df


with tgb.Page() as data_page:
    with tgb.part(class_name="container card stack-large"):
        tgb.navbar()

        tgb.text("## Rådata", mode="md")
        tgb.table("{df}")

