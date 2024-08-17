import re

def print_month(month):
    month = month.strip('/')
    return "".join(["0", month]) if (int(month) < 9) else month

class House:
    def __init__(self, id: int, neighborhood: str, house_style: str, overall_condition: int,
                 year_built: int, roof_type: str, roof_material: str, foundation_material: str,
                 heating: str, central_air: chr, electrical: str, fireplace_num: int, garage_area: int,
                 month: int, year: int):

        self.properties: dict ={
                "id" : id,
                "neighborhood" : neighborhood,
                "house_style" : house_style,
                "overall_condition" : overall_condition,
                "year_built" : year_built,
                "roof_type" : roof_type,
                "roof_material" : roof_material,
                "foundation_material" : foundation_material,
                "heating" : heating,
                "central_air" : central_air,
                "electrical" : electrical,
                "fireplace_num" : fireplace_num,
                "garage_area" : garage_area,
                "date_sold" : f"{month}/{year}"
        }
        
        self.id = self.properties["id"]
        self.neighborhood = self.properties["neighborhood"]
        self.house_style = self.properties["house_style"]
        self.overall_condition = self.properties["overall_condition"]
        self.year_built = self.properties["year_built"]
        self.roof_type = self.properties["roof_type"]
        self.roof_material = self.properties["roof_material"]
        self.foundation_material = self.properties["foundation_material"]
        self.heating = self.properties["heating"]
        self.central_air = self.properties["central_air"]
        self.electrical = self.properties["electrical"]
        self.fireplace_num = self.properties["fireplace_num"]
        self.garage_area = self.properties["garage_area"]
        self.date_sold = self.properties["date_sold"]



    def __repr__(self):
        return f"{self.id},{self.neighborhood},{self.house_style},{self.overall_condition},{self.year_built},{self.roof_type},{self.roof_material},{self.foundation_material},{self.heating},{self.central_air},{self.electrical},{self.fireplace_num},{self.garage_area},{print_month(self.date_sold[:2])},{self.date_sold[-4:]}\n"

