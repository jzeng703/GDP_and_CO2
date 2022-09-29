import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)

mortality = data["Mortality rate, infant (per 1,000 live births)"]
gdppercap = data["GDP per capita (constant 2010 US$)"]
country_name = data["Country Name"]

# 1. Create a scatter plot of GDP per capita vs. infant mortality rate
plt.(mortality, gdppercap, marker="o", linestyle="None")
plt.xlabel("Mortality rate, infant (per 1,000 live births)")