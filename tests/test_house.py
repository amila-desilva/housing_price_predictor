import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from classes.House import House

def test_update_houses_by_id():
    house = House(id=1, neighborhood='Downtown', house_style='Ranch', overall_condition='Good', 
                  year_built=1990, roof_type='Gable', roof_material='Asphalt', 
                  foundation_material='Concrete', heating='Gas', central_air='Yes', 
                  electrical='Standard', fireplace_num=1, garage_area=500, 
                  date_sold='2024-08-14')

    updated_fields = {'house_style': 'Colonial', 'year_built': 1995}
    house.update_houses_by_id(1, updated_fields)

    assert house.house_style == 'Colonial'
    assert house.year_built == 1995

def test_delete_house_by_id():
    house = House(id=1, neighborhood='Downtown', house_style='Ranch', overall_condition='Good', 
                  year_built=1990, roof_type='Gable', roof_material='Asphalt', 
                  foundation_material='Concrete', heating='Gas', central_air='Yes', 
                  electrical='Standard', fireplace_num=1, garage_area=500, 
                  date_sold='2024-08-14')

    result = house.delete_house_by_id(1)
    assert result is True

    result = house.delete_house_by_id(2)
    assert result is False

def test_get_houses_by_filters():
    house = House(id=1, neighborhood='Downtown', house_style='Ranch', overall_condition='Good', 
                  year_built=1990, roof_type='Gable', roof_material='Asphalt', 
                  foundation_material='Concrete', heating='Gas', central_air='Yes', 
                  electrical='Standard', fireplace_num=1, garage_area=500, 
                  date_sold='2024-08-14')

    filters = {'neighborhood': 'Downtown', 'house_style': 'Ranch'}
    result = house.get_houses_by_filters(filters)
    assert result is True

    filters = {'neighborhood': 'Downtown', 'house_style': 'Colonial'}
    result = house.get_houses_by_filters(filters)
    assert result is False
