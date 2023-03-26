import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

print(df)

print(df["Age"])

print(df.describe())

titanic = pd.read_csv("data/titanic.csv")
print(titanic)

print(titanic.head(8))

print(titanic.tail(8))

print(titanic.dtypes)
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")
print(titanic)

print(titanic.shape)

print(titanic[["Age", "Sex"]])

print(type(titanic[["Age", "Sex"]]))

print(titanic[titanic["Age"] > 35])

print(titanic["Age"] > 35)

print(titanic[titanic["Pclass"].isin([2, 3])])

print(titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)])

age_no_na = titanic[titanic["Age"].notna()]

print(age_no_na.head())

print(age_no_na.shape)

adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
print(adult_names.head())

print(titanic.iloc[9:25, 2:5])
titanic.iloc[0:3, 3] = "anonymous"
print(titanic.head())

air_quality = pd.read_csv('data/air_quality_no2.csv', index_col=0, parse_dates=True)

print(air_quality)

# print(air_quality.plot())
# plt.show()
# air_quality["station_paris"].plot()
# plt.show()

# air_quality.plot.box()
# plt.show()

# axs = air_quality.plot.area(figsize=(15, 10), subplots=True)
# plt.show()

# fig, axs = plt.subplots(figsize=(12, 4))

# air_quality.plot.area(ax=axs)

# axs.set_ylabel('NO$_2$ concentration')

# fig.savefig("no2_concentrations.png")

# plt.show()

air_quality = pd.read_csv("data/air_quality_no2.csv", index_col = 0, parse_dates=True)