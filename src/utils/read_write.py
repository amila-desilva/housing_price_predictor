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
    
    # make a string of all the attributes of a house
    labels: str = ("Id,Neighborhood,HouseStyle,OverallCond,YearBuilt,RoofStyle," + 
        "RoofMatl,Foundation,Heating,CentralAir,Electrical,Fireplaces,GarageArea," + 
        "MoSold,YrSold").replace('\n', '')

    output_file.write(labels + '\n')  # write the labels to a write file and end that line

    # for each house in the housing_list, print its attributes to the write file
    for house in housing_list:
        output_file.write(house.__repr__())


def update_house_by_id(house_id, updated_fields: dict, housing_dict: dict=housing_dict) -> None:
    house = housing_dict[house_id]                      # get the relevant house from the dictionary
    for key in updated_fields.keys():                   # for each field we want to update
        house.properties[key] = updated_fields[key]     # update that field using the house.properties dict
    

def delete_house_by_id(house_id: int, housing_dict: dict=housing_dict, housing_list: list=housing_list) -> None:
    """
    Removes the house with the given house_id from the housing_dict dictionary and housing_list list.
    """
    housing_list.remove(housing_dict[house_id])  # remove house from list of houses
    housing_dict.pop(house_id)                   # remove house from dictionary of houses
    

def get_houses_by_filter(filters: dict) -> list:
    filtered_list = []          # create an empty list
    for house in house_list:    
        flag == True            # flag to notify us if an event occured
        for key in filters.keys():
            if filter[key] != house.properties[key]:  # if the house does not match the filter_list
                flag = False                          # set flag to False
                break                                 # break the loop, and check next house
        if flag == True:               # if the flag is still True
            filter_list.append(house)  # add it to filtered_list

    return filter_list



