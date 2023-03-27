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
print(air_quality.head())
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882

print(air_quality.head())

air_quality["ratio_paris_antwerp"] = (
    air_quality["station_paris"] / air_quality["station_antwerp"]
)

print(air_quality.head())

air_quality_renamed = air_quality.rename(
    columns={
    "station_antwerp": "BETR801", 
    "station_paris": "FR0414",
    "station_london":"London Westminster",
    }
)

print(air_quality_renamed.head())

air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
print(air_quality_renamed.head())

titanic = pd.read_csv("data/titanic.csv")
print(titanic.head())

print(titanic["Age"].mean())

print(titanic[["Age", "Fare"]].median())


print(titanic[["Age", "Fare"]].describe())

print(titanic.describe())


print(titanic.agg(
    {
    "Age":["min","max","median","skew"],
    "Fare":["min","max","median","mean"],
    }
))

print(titanic[["Sex", "Age"]].groupby("Sex").mean())

print(titanic.groupby("Sex").mean(numeric_only=True))

print(titanic.groupby("Sex")["Age"].mean())

print(titanic.groupby(["Sex", "Pclass"])["Fare"].mean())

print(titanic["Pclass"].value_counts())

print(titanic.groupby("Pclass")["Pclass"].count())

titanic = pd.read_csv("data/titanic.csv")
print(titanic.head())

air_quality = pd.read_csv("data/air_quality_long.csv", index_col="date.utc", parse_dates=True)

print(air_quality.head())

print(titanic.sort_values(by="Age".head()))