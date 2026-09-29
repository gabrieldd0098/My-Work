import csv
import pandas

# with open (file="weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temps = []
#     for row in data:
#         if row[1] != "temp":
#             temps.append(int(row[1]))
#     print(temps)

data = pandas.read_csv(filepath_or_buffer="weather_data.csv", sep=",")

data_dict = data.to_dict()
temp_list = data["temp"].tolist()

print(f"AVG = {data["temp"].mean().round(2)}")
print(f"MAX = {data["temp"].max()}")
print(f"MIN = {data["temp"].min()}")
print(f"{data[data.day == 'Monday']}")
print(f"DAY MAX = {data[data.temp == data.temp.max()]}")

d_dict = {
    "students": ["Amelia", "Jon", "Horace"],
    "scores": [650, 766, 899]
}

n_data = pandas.DataFrame(data=d_dict)
n_data.to_csv(path_or_buf="new_data.csv")

print("=================================================================")

squirrel_data = pandas.read_csv(filepath_or_buffer="2018_Central_Park_Squirrel_Data.csv")

gray_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
print(f"{gray_squirrels_count} Gray Squirrels")

cin_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
print(f"{cin_squirrels_count} Cinnamon Squirrels")

black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
print(f"{black_squirrels_count} Black Squirrels")

squirrel_data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count" : gray_squirrels_count, cin_squirrels_count: black_squirrels_count,
}

sdf = pandas.DataFrame(data=squirrel_data_dict)
sdf.to_csv(path_or_buf="new_squirrel_data.csv")
