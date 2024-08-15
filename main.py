import pandas as pd
from src.classes.house import House
from src.utils.read_write import *

INPUT_FILE: str = "housing_data.csv"
OUTPUT_FILE: str = "housing_predictor_out.csv"

house_list, house_dict = read_from_file(INPUT_FILE)

write_to_file(OUTPUT_FILE)

house_id = 1493

delete_house_by_id(house_id)

house_list, house_dict = read_from_file(OUTPUT_FILE)

print("yay")
