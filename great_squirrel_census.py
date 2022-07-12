import pandas
"""
data = pandas.read_csv("weather_data.csv")
print(data["temp"].mean())
print(data["temp"].max())
print(data["condition"])
print(data.condition)
print(data[data["day"] == "Monday"])

print(data[data["temp"] == data.temp.max()])

data_dict = {
    "students": ["Amy","James","Abdul","DaQuarius","Chang"],
    "scores": [84,95,91,56,100]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

"""

df = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(df.columns)
fur = df["Primary Fur Color"].value_counts()
print(fur)