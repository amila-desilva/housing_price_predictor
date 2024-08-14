from src.classes.house import House
import pandas as pd
import pprint

def read_from_file(file_name: str) -> list:
    housing_df = pd.read_csv('housing_data.csv')
    housing_list = []
    housing_dict = {}
    for index, row in housing_df.iterrows():
        new_house:House = House(row['Id'], row['Neighborhood'], row['HouseStyle'], row['OverallCond'],
                                row['YearBuilt'], row['RoofStyle'], row['RoofMatl'], row['Foundation'],
                                row['Heating'], row['CentralAir'], row['Electrical'], row['Fireplaces'],
                                row['GarageArea'], row['MoSold'], row['YrSold']
                            )
        housing_list.append(new_house)
        housing_dict[new_house.id] = new_house
    return housing_list, housing_dict

def write_to_file(housing_list: list, housing_dict: dict, file_name: str) -> None:
    output_file = open(file_name, 'w')
    output_file.write("housing_list = " + pprint.pformat(housing_list) + '\n')
    output_file.write("housing_dict = " + pprint.pformat(housing_dict) + '\n')

