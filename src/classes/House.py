class House():
    def __init__(self, id, neighborhood, house_style, overall_condition, year_built, roof_type, 
                 roof_material, foundation_material, heating, central_air, electrical, 
                 fireplace_num, garage_area, date_sold):
        self.id = id
        self.neighborhood = neighborhood
        self.house_style = house_style
        self.overall_condition = overall_condition
        self.year_built = year_built
        self.roof_type = roof_type
        self.roof_material = roof_material
        self.foundation_material = foundation_material
        self.heating = heating
        self.central_air = central_air
        self.electrical = electrical
        self.fireplace_num = fireplace_num
        self.garage_area = garage_area
        self.date_sold = date_sold


    def update_houses_by_id(self, house_id: int, updated_fields: dict) -> None:
        """
        Update the fields of a house by its ID.
        
        Args:
            house_id (int): The ID of the house to update.
            updated_fields (dict): A dictionary of fields to update with their new values.
        """
        if self.id == house_id:
            for key, value in updated_fields.items():
                if hasattr(self, key):
                    setattr(self, key, value)
                else:
                    print(f"Warning: {key} is not a valid attribute.")
        else:
            print("House ID not found.")


    def get_houses_by_filters(self, filters: dict) -> bool:
        """
        Check if the house matches the given filters.
        
        Args:
            filters (dict): A dictionary of filters where the key is the field and the value is the expected value.
        
        Returns:
            bool: True if the house matches all the filters, False otherwise.
        """
        for key, value in filters.items():
            if hasattr(self, key):
                if getattr(self, key) != value:
                    return False
            else:
                print(f"Warning: {key} is not a valid attribute.")
                return False
        return True
    

    def delete_house_by_id(self, house_id: int) -> bool:
        """
        Checks if the house matches the given ID and marks it for deletion.

        Args:
            house_id (int): The ID of the house to delete.

        Returns:
            bool: True if the house matches the ID, False otherwise.
        """
        if self.id == house_id:
            print(f"House with ID {house_id} marked for deletion.")
            return True  # True to indicate this house should be deleted
        return False  # False if the house does not match the ID
