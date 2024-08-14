
class House:
    def __init__(self, id: int, neighborhood: str, house_style: str, overall_condition: int,
                 year_built: int, roof_type: str, roof_material: str, foundation_material: str,
                 heating: str, central_air: chr, electrical: str, fireplace_num: int, garage_area: int,
                 month: int, year: int):
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
        self.date_sold = f"{month}/{year}"

    def __repr__(self) -> str:
        # TODO: Make representation more verbosef
        return f"House #{self.id}:\n"

    @classmethod
    def update_house_by_id(house_id, updated_fields: dict) -> None:
        pass

    @classmethod
    def delete_house_by_id(house_id: int) -> None:
        """
        Removes the house with the given house_id from the housing_dict dictionary.
        """
        housing_dict.pop(house_id)

    @classmethod
    def get_houses_by_filter(filters: list) -> list:
        pass

