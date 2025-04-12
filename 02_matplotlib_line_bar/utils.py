import matplotlib.pyplot as plt
import duckdb 
import pandas as pd
from pathlib import Path

data_path = Path(__file__).parent / "data"

df = pd.read_csv(data_path / "norway_new_car_sales_by_make.csv")


df_quantity_make = duckdb.query(
    """
             SELECT make, SUM(quantity) as Quantity 
             FROM df 
             GROUP BY make 
             ORDER BY quantity DESC"""
).df()

def top_ten_bar():
    df_quantity_make_top_10 = df_quantity_make.iloc[:10]

    fig, ax = plt.subplots(figsize=(12, 6))


    ax.bar(
        x=df_quantity_make_top_10["Make"],
        height=df_quantity_make_top_10["Quantity"],
        width=0.6,
    )

    ax.set(
        title="Number of cars from top 10 most sold brands in Norway 2007-2017",
        xlabel="Car brand",
        ylabel="Number of cars",
    )

    return fig, ax