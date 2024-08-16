from utils.read_from_file import read_from_file
from utils.write_to_file import write_to_file
from classes.House import House

import pandas as pd
from datetime import datetime
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

    houses = []
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
        houses.append(house)
    print(f"Total houses: {len(houses)}")

    # Example 1: Filtering houses in a specific neighborhood
    filters = {'neighborhood': 'Gilbert'}
    matching_houses = [house for house in houses if house.get_houses_by_filters(filters)]
    print(f"Houses in {filters['neighborhood']}: {len(matching_houses)}")

    # Example 2: Updating a house's details
    house_id_to_update = 1
    updated_fields = {'house_style': 'Colonial', 'year_built': 1995}
    for house in houses:
        if house.id == house_id_to_update:
            house.update_houses_by_id(house_id=house_id_to_update, updated_fields=updated_fields)
            print(f"Updated house with ID {house_id_to_update}: {house}")

    # Example 3: Deleting a house by ID
    house_id_to_delete = 1
    initial_count = len(houses)
    houses = [house for house in houses if house.id != house_id_to_delete]
    deleted_count = initial_count - len(houses)

    
    updated_df = df[df['id'] != house_id_to_delete] # Update the DataFrame by filtering out the deleted records

    # Save the updated DataFrame back to the file
    write_to_file(updated_df, file_path)
    
    # After deletion
    print(f"Deleted {deleted_count} house(s) with ID {house_id_to_delete}")
    print(f"Remaining houses: {len(houses)}")
  
    

if __name__ == "__main__":
    main()
