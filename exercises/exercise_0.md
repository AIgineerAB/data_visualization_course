# Exercise 0 - Matplotlib fundamentals

In this exercise, you get to familiarize yourself with matplotlib to make simple graphings such as line and bar charts.

> [!NOTE]
> For each chart that you draw, make sure to have appropriate titles, xlabel, ylabel and other annotations that might be needed

## 0. Car sales in Norway - emissions and trends

From lecture 02 with car sales in Norway, we worked with one dataset, however there were some more that you downloaded from kaggle. In this exercise, work with this dataset `norway_new_car_sales_by_month.csv`

&nbsp; a) Do some EDA with info, find out column names, shape of dataset, describe method to get summary descriptive statistics.

&nbsp; b) Draw a line chart of quantity for each year. Is there a year that should be skipped?

&nbsp; c) Draw a line chart of average CO2 emissions for same years that as in b)

&nbsp; d) Draw a line chart of all years and months for import

&nbsp; e) Draw a line chart of all years and months for average CO2 emissions

&nbsp; f) Draw a line chart of all years and months for electric cars import

&nbsp; g) Draw a line chart of average diesel share per year

&nbsp; h) Discuss some findings with a friend based on this dataset, and do plot more graphs

## 1. Recreate graphs

The following graphs below are created from [this dataset](https://data.world/makeovermonday/2025w3-steam-top-100-played-games). Try to recreate them as close as possible

&nbsp; a) Here we use subplots to get two axes in one figure

<img src="https://github.com/kokchun/assets/blob/main/data_visualization/popular_games.png?raw=true" alt="bar chart and line chart" width="300">

&nbsp; b) This one will require some data processing to be able to come to this point.

Hint: df.explode() and df.join()

<img src="https://github.com/kokchun/assets/blob/main/data_visualization/top5_genre_tags.png?raw=true" alt="bar chart and line chart" width="300">

&nbsp; c) A df has a hist() method for creating histogram

<img src="https://github.com/kokchun/assets/blob/main/data_visualization/histogram_tags.png?raw=true" alt="bar chart and line chart" width="300">

## 2. Theory questions

&nbsp; a) When can you make line charts and when can't you make line charts?

&nbsp; b) Whats wrong with this chart?

<img src="https://github.com/kokchun/assets/blob/main/data_visualization/bar_no_zero.png?raw=true" alt="bar chart and line chart" width="300">

&nbsp; c) Whats wrong with this chart?

<img src="https://github.com/kokchun/assets/blob/main/data_visualization/line_categorical.png?raw=true" alt="bar chart and line chart" width="300">

&nbsp; d) What is the difference between OOP approach and plt approach in drawing graphs.

&nbsp; e) How do you draw an arrow in matplotlib?

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology | explanation |
| ----------- | ----------- |
| artist      |             |
| containers  |             |
| spine       |             |
| axes        |             |
| figure      |             |
| subplot     |             |
| patch       |             |
| annotation  |             |
| arrowprops  |             |
| marker      |             |
| ticks       |             |
| ticklabels  |             |
| layout      |             |
| grid        |             |
| legend      |             |
