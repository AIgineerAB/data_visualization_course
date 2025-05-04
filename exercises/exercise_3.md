# Exercise 3 - Taipy for creating web apps

In this exercise, you learn how to create interactive web applications including dashboards using Taipy

> [!NOTE]
> all data for the exercises is found in this repo under exercises/data

## 0. Palindrome game

A palindrome is a set of characters that is read the same backwards as forwards. Example of palindromes (case-insensitive and ignoring spaces):

- Anna
- racecar
- Ni talar bra latin

Your task is to create a palindrome game in Taipy, where the user can input a string and a button to submit the input. The written string should also be displayed in a text instantaneously. After clicking the submit button, the game displays this GPT4o-generated cat image if it is a palindrome.

<img src="https://github.com/kokchun/assets/blob/main/data_visualization/fake_cat.png?raw=true" alt="fake cat" width="200">

If it is not a palindrome, then this GPT4o-generated sad bunny is shown

<img src="https://github.com/kokchun/assets/blob/main/data_visualization/fake_sad_rabbit.png?raw=true" alt="fake sad rabbit" width="100">

Also keep track of points, give one star for each correct answer and deduct one star for each incorrect answer. You can choose an appropriate icon/emoji/image for negative scores.

Something else you want your palindrome game to have - go ahead and try implement it?

## 1. Simulate dices

Try to recreate this app here for simulating dices.

Tips:

- `rebuild = True` for tgb.table
- adjust `page_size` for table

<img src="https://github.com/kokchun/assets/blob/main/data_visualization/dices_simulation.png?raw=true" alt="dices app" width="500">

## 2. Gapminder dashboard

Use the gapminder dataset from plotly.express and create a dashboard. Do explorative data analysis, pick out graphs and metrics you are interested in displaying, then draw a wireframe by hand or a simple tool such as paint, powerpoint or figma or something else. Use this wireframe to guide your design of your dashboard.

## 3. Theory questions

&nbsp; a) What are some differences between streamlit and taipy?

&nbsp; b) What is the state variable used for?

&nbsp; c) How do you style taipy apps?

&nbsp; d) What is a KPI?

&nbsp; e) How do you integrate plotly graphs into taipy?

&nbsp; f) What is the difference between python-syntax and markdown syntax in taipy?

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology | explanation |
| ----------- | ----------- |
| on_action   |             |
| on_change   |             |
| state       |             |
| KPI         |             |
|             |             |
|             |             |
