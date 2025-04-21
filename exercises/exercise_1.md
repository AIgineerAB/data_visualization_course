# Exercise 1 - Data storytelling

In this exercise, you get to use matplotlib and combine with data storytelling to make visuals that are targeted towards telling a suitable story for your target audience.

> [!NOTE]
> For each explanatory chart that you draw, make sure to use data storytelling principles to make your visualizations truly explanatory and not exploratory

## 0. Tell a story from immigration

This visualization comes from [03_matplotlib_annotations](https://github.com/AIgineerAB/data_visualization_course/tree/main/03_matplotlib_annotations).

<img src="https://github.com/kokchun/assets/blob/main/data_visualization/annotate_arrow.png?raw=true" alt="bar chart and line chart" width="300">

Lets improve upon this visualization.

&nbsp; a) Remove clutter from this visualization such as top spine and right spine. Also change the unit to thousands with a prefix K.

&nbsp; b) Left align the xlabel, top align the ylabel and left align the title

&nbsp; c) Use contrast to focus the attention to what you want the audience to see

&nbsp; d) Choose a story to tell and change the labels and title accordingly

&nbsp; e) You can choose several different stories to tell and depending on which one you choose, the visualization might look differently in terms of what parts are annotated, what parts are highlighted etc.

## 1. Makeover

The given code

```py
import pandas as pd
import duckdb

df = pd.read_csv("data/norway_new_car_sales_by_month.csv")
df = duckdb.query(
    """
    SELECT avg_CO2, import,quantity, year, month
    FROM df

"""
).df()

df["date"] = pd.to_datetime(
    df["Year"].astype(str) + "-" + df["Month"].astype(str).str.zfill(2), format="%Y-%m"
)

df = df.set_index("date")

ax = df["Avg_CO2"].plot()
```

creates a graph that looks like this

<img src="https://github.com/kokchun/assets/blob/main/data_visualization/avg_co2.png?raw=true" alt="bar chart and line chart" width="300">

<br/>

Your task is to do a `data storytelling makeover` of this visual.


## 2. CO2 data storytelling

Based on the dataset `co2_annmean_mlo.csv` create this visualization as closely as you can 

<img src="https://github.com/kokchun/assets/blob/main/data_visualization/CO2_emissions_annual_mean.png?raw=true" alt="bar chart and line chart" width="300">



## 3. Exploring and explaining happiness

In the data happiness.xlsx from [here](https://data.world/makeovermonday/2025-week-4-world-happiness-report-2024) you can find happiness scores as well as a visualization of all the countries happiness along with different variables to explain the happiness to various levels. Do exploratory data analysis on this dataset, then pick out a few visualizations that you turn into explanatory data analysis using the principles of data storytelling. 

## 4. Theory questions

&nbsp; a) Why is it good to use the proximity principle when designing visuals? 

&nbsp; b) What is clutter and why is it undesirable?

&nbsp; c) Why should you spend time on data storytelling when there is a lot of things that needs to be explored and cleaned in the data? 

&nbsp; d) Data storytelling is very subjective in terms of which story to tell. How could you or your team craft a compelling story to tell? 


## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology               | explanation |
| ------------------------- | ----------- |
| exploratory data analysis |             |
| explanatory data analysis |             |
| clutter                   |             |
| proximity principle       |             |
| attention                 |             |
| contrast                  |             |
| colors sparingly          |             |
| data storytelling         |             |
| grid                      |             |
| axis                      |             |
| insight                   |             |
| context                   |             |
| call to action            |             |
| annotation                |             |
| KPI                       |             |
| story arc                 |             |
| data literacy             |             |
| dashboard fatigue         |             |
