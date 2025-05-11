import taipy.gui.builder as tgb


with tgb.Page() as home_page:
    with tgb.part(class_name="container card stack-large"):
        tgb.navbar()

        with tgb.part(class_name="max-text-width"):
            tgb.text("# Välkommen till YH dashboard 2024", mode="md")
            tgb.text(
                """
            YH Dashboard 2024 är ett interaktivt verktyg som visualiserar
            statistik och information kring ansökningsomgången för Yrkeshögskoleutbildningar (YH) under året 2024. Syftet med dashboarden är att ge en tydlig överblick över antalet ansökta utbildningar per kommun och utbildningsområde, med möjlighet att filtrera och analysera data utifrån användarens intresse.
            """
            )
