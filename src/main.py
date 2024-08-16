from utils.read_from_file import read_from_file
from utils.write_to_file import write_to_file
from classes.House import House

import pandas as pd
import os

def main():
    """
    Main function of the Housing Price Predictor.

    This function loads the dataset, processes the data, and runs predictions.

    Returns:
        None (for now)
    """
    # Loading dataset
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '..', 'housing_price_predictor', 'dataset', 'data.xlsx')

    df = read_from_file(file_path)

    # Checking if the DataFrame is loaded correctly
    print(df.head())
    print(df.columns)

    houses_dict = {}    # Creating a dictionary to store House instances with 'id' as the key
    for _, row in df.iterrows():
        house = House(
            id=row['id'],
            neighborhood=row['neighborhood'],
            house_style=row['house_style'],
            overall_condition=row['overall_condition'],
            year_built=row['year_built'],
            roof_type=row['roof_type'],
            roof_material=row['roof_material'],
            foundation_material=row['foundation_material'],
            heating=row['heating'],
            central_air=row['central_air'],
            electrical=row['electrical'],
            fireplace_num=row['fireplace_num'],
            garage_area=row['garage_area'],
            date_sold=row['date_sold']
        )
        houses_dict[house.id] = house 
    print(f"Total houses: {len(houses_dict)}")

     # Example 1: Filtering houses in a specific neighborhood
    filters = {'neighborhood': 'Gilbert'}
    matching_houses = {house_id: house for house_id, house in houses_dict.items() if house.get_houses_by_filters(filters)}
    print(f"Houses in {filters['neighborhood']}: {len(matching_houses)}")

   # Example 2: Updating a house's details
    house_id_to_update = 1  # This id will not be found on record in purpose so no record is updated
    updated_fields = {'house_style': '2Story', 'year_built': 1995}
    if house_id_to_update in houses_dict:
        houses_dict[house_id_to_update].update_houses_by_id(house_id=house_id_to_update, updated_fields=updated_fields)
        print(f"Updated house with ID {house_id_to_update}: {houses_dict[house_id_to_update]}")

    # Example 3: Deleting a house by ID using the delete_house_by_id method
    house_id_to_delete = 1  # This id will not be found on record in purpose so no record is deleted
    initial_count = len(houses_dict)

    # Checking if the house exists
    if house_id_to_delete in houses_dict and houses_dict[house_id_to_delete].delete_house_by_id(house_id_to_delete):
        del houses_dict[house_id_to_delete]
    
    deleted_count = initial_count - len(houses_dict)


    # Converting the remaining houses back to a DataFrame - Saving to file after all pertinent modifications
    remaining_data = {
        'id': [],
        'neighborhood': [],
        'house_style': [],
        'overall_condition': [],
        'year_built': [],
        'roof_type': [],
        'roof_material': [],
        'foundation_material': [],
        'heating': [],
        'central_air': [],
        'electrical': [],
        'fireplace_num': [],
        'garage_area': [],
        'date_sold': []
    }

    for house in houses_dict.values():
        remaining_data['id'].append(house.id)
        remaining_data['neighborhood'].append(house.neighborhood)
        remaining_data['house_style'].append(house.house_style)
        remaining_data['overall_condition'].append(house.overall_condition)
        remaining_data['year_built'].append(house.year_built)
        remaining_data['roof_type'].append(house.roof_type)
        remaining_data['roof_material'].append(house.roof_material)
        remaining_data['foundation_material'].append(house.foundation_material)
        remaining_data['heating'].append(house.heating)
        remaining_data['central_air'].append(house.central_air)
        remaining_data['electrical'].append(house.electrical)
        remaining_data['fireplace_num'].append(house.fireplace_num)
        remaining_data['garage_area'].append(house.garage_area)
        remaining_data['date_sold'].append(house.date_sold)

    updated_df = pd.DataFrame(remaining_data)

    # Save the updated DataFrame back to the file
    write_to_file(updated_df, file_path)
    
    # After deletion
    print(f"Deleted {deleted_count} house(s) with ID {house_id_to_delete}")
    print(f"Remaining houses: {len(houses_dict)}")

 

if __name__ == "__main__":
    main()
