import weather
csv_path = "tests/data/example_one.csv"

test_list = weather.load_data_from_csv(csv_path)
print(test_list)

