from src.classes.house import House
import pandas as pd


housing_list = []
housing_dict = {}


def read_from_file(file_name: str) -> list:
    # initialize datastructures
    housing_df = pd.read_csv(file_name)
    
    # for each row in the dataset, make a House object
    for index, row in housing_df.iterrows():
        new_house:House = House(row['Id'], row['Neighborhood'], row['HouseStyle'], row['OverallCond'],
                                row['YearBuilt'], row['RoofStyle'], row['RoofMatl'], row['Foundation'],
                                row['Heating'], row['CentralAir'], row['Electrical'], row['Fireplaces'],
                                row['GarageArea'], row['MoSold'], row['YrSold']
                            )
        
        # add new_house to housing_list and housing_dict
        housing_list.append(new_house)
        housing_dict[new_house.id] = new_house
    return housing_list, housing_dict


def write_to_file(file_name:str, housing_list: list=housing_list, housing_dict: dict=housing_dict) -> None:
    # open a file in write mode ('w') and write the House objects to that file
    output_file = open(file_name, 'w')
    
    labels: str = ("Id,Neighborhood,HouseStyle,OverallCond,YearBuilt,RoofStyle," + 
        "RoofMatl,Foundation,Heating,CentralAir,Electrical,Fireplaces,GarageArea," + 
        "MoSold,YrSold").replace('\n', '')
    
    print(labels)

    output_file.write(labels + '\n')
    for house in housing_list:
        print(house.__repr__())
        output_file.write(house.__repr__())


def update_house_by_id(house_id, updated_fields: dict, housing_dict: dict=housing_dict) -> None:
    for key in updated_fields.keys():
       pass 
    

def delete_house_by_id(house_id: int, housing_dict: dict=housing_dict, housing_list: list=housing_list) -> None:
    """
    Removes the house with the given house_id from the housing_dict dictionary and housing_list list.
    """
    housing_list.remove(housing_dict[house_id])
    housing_dict.pop(house_id)
    

def get_houses_by_filter(filters: list) -> list:
    pass


